
import os
import time
import numpy as np
import base64
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration, WebRtcMode

# Try to import dlib and dependencies - may not be available on cloud
try:
    import dlib
    import cv2
    from imutils import face_utils
    from scipy.spatial import distance
    DLIB_AVAILABLE = True
except ImportError:
    DLIB_AVAILABLE = False
    import cv2

# =============================================================================
# CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="DrowseGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

try:
    load_css("assets/style.css")
except FileNotFoundError:
    st.warning("CSS file not found. Please ensure assets/style.css exists.")

# Load Audio
@st.cache_data
def load_alert_sound():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(script_dir, "music.wav")
    if os.path.exists(sound_path):
        with open(sound_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

alert_sound_b64 = load_alert_sound()

# Constants
MODEL_PATH = "models/shape_predictor_68_face_landmarks.dat"

# Auto-download model if not present (for cloud deployment)
@st.cache_resource
def ensure_model_exists():
    """Download facial landmark model if not present"""
    import urllib.request
    
    if not DLIB_AVAILABLE:
        return None
        
    if not os.path.exists(MODEL_PATH):
        os.makedirs("models", exist_ok=True)
        
        with st.spinner("📥 Downloading facial landmark model (one-time, ~95MB)..."):
            try:
                url = "https://github.com/italojs/facial-landmarks-recognition/raw/master/shape_predictor_68_face_landmarks.dat"
                urllib.request.urlretrieve(url, MODEL_PATH)
                st.success("✅ Model downloaded successfully!")
            except Exception as e:
                st.error(f"❌ Failed to download model: {e}")
                st.info("💡 Please manually download shape_predictor_68_face_landmarks.dat and place in models/ folder")
                return None
    return MODEL_PATH

# Ensure model exists before proceeding
if DLIB_AVAILABLE:
    ensure_model_exists()

# =============================================================================
# CORE LOGIC
# =============================================================================

def calculate_ear(eye):
    if not DLIB_AVAILABLE:
        return 0.3
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

class DrowsinessProcessor(VideoProcessorBase):
    def __init__(self):
        self.frame_count = 0
        self.alert_status = False
        self.ear_value = 0.0
        self.ear_threshold = 0.25
        self.frame_check = 20
        
        if DLIB_AVAILABLE:
            try:
                self.detector = dlib.get_frontal_face_detector()
                if os.path.exists(MODEL_PATH):
                    self.predictor = dlib.shape_predictor(MODEL_PATH)
                else:
                    self.predictor = None
                self.lStart, self.lEnd = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
                self.rStart, self.rEnd = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
            except Exception:
                self.predictor = None
        else:
            self.predictor = None
            
    def update_settings(self, threshold, frames):
        self.ear_threshold = threshold
        self.frame_check = frames

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        # If dlib not available, just return the frame with a message
        if not DLIB_AVAILABLE or self.predictor is None:
            cv2.putText(img, "Face detection unavailable (dlib not installed)", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
            cv2.putText(img, "Running in demo mode - UI functional", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
            return frame.from_ndarray(img, format="bgr24")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = self.detector(gray, 0)
        
        current_alert = False
        
        for rect in rects:
            shape = self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[self.lStart:self.lEnd]
            rightEye = shape[self.rStart:self.rEnd]
            leftEAR = calculate_ear(leftEye)
            rightEAR = calculate_ear(rightEye)

            ear = (leftEAR + rightEAR) / 2.0
            self.ear_value = ear

            # Visuals
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(img, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(img, [rightEyeHull], -1, (0, 255, 0), 1)

            if ear < self.ear_threshold:
                self.frame_count += 1
                if self.frame_count >= self.frame_check:
                    current_alert = True
                    cv2.putText(img, "DROWSINESS ALERT!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                self.frame_count = 0
        
        self.alert_status = current_alert
        return frame.from_ndarray(img, format="bgr24")

# =============================================================================
# UI COMPONENTS
# =============================================================================

def render_brand_header():
    st.markdown("""
    <div class="brand-header">
        <div class="brand-logo">🛡️</div>
        <div class="brand-text">
            <h1>DrowseGuard</h1>
            <p>Driver Fatigue Monitoring System</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    render_brand_header()
    
    # Show warning if dlib not available
    if not DLIB_AVAILABLE:
        st.warning("⚠️ **Demo Mode**: Face detection libraries (dlib) are not available in this deployment. The UI is fully functional, but drowsiness detection is disabled. For full functionality, run locally or use Docker deployment.")
    
    # Layout: Left video (2/3), Right stats (1/3)
    col_video, col_stats = st.columns([2, 1], gap="medium")
    
    with col_video:
        st.markdown("""
        <div class="video-container">
            <div class="video-header">
                <div class="live-indicator">● Live Feed</div>
                <span style="color:rgba(255,255,255,0.4); font-size:0.8rem;">Camera 0</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        ctx = webrtc_streamer(
            key="drowsiness-detection",
            mode=WebRtcMode.SENDRECV,
            rtc_configuration=RTCConfiguration(
                {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
            ),
            video_processor_factory=DrowsinessProcessor,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )

    with col_stats:
        # 1. Status Card (Big)
        status_placeholder = st.empty()
        
        # Audio Placeholder (Hidden)
        audio_placeholder = st.empty()
        
        # 2. Metrics Row
        m_col1, m_col2 = st.columns(2)
        with m_col1:
             ear_placeholder = st.empty()
             ear_placeholder.markdown("""
                <div class="metric-box">
                    <div class="metric-label">Eye Aspect Ratio</div>
                    <div class="metric-value">--</div>
                </div>
             """, unsafe_allow_html=True)
        with m_col2:
             alert_count_placeholder = st.empty()
             alert_count_placeholder.markdown("""
                <div class="metric-box">
                    <div class="metric-label">Total Alerts</div>
                    <div class="metric-value">0</div>
                </div>
             """, unsafe_allow_html=True)

        # 3. Session Time
        session_placeholder = st.empty()
        session_placeholder.markdown("""
            <div class="metric-box">
                <div class="metric-label">Session Time</div>
                <div class="metric-value" style="color:white;">00:00:00</div>
            </div>
        """, unsafe_allow_html=True)

        # 4. Settings (Expander at bottom)
        with st.expander("⚙️ Configuration", expanded=True):
            threshold = st.slider("EAR Sensitivity", 0.15, 0.35, 0.25, 0.01)
            frames = st.slider("Alert Delay (frames)", 5, 50, 20)
            
            if ctx.video_processor:
                ctx.video_processor.update_settings(threshold, frames)

        # Logic Loop
        if ctx.state.playing:
            start_time = time.time() if 'start_time' not in st.session_state else st.session_state.start_time
            if 'start_time' not in st.session_state:
                st.session_state.start_time = start_time
                st.session_state.total_alerts = 0

            while ctx.state.playing:
                if ctx.video_processor:
                    # Update EAR
                    ear_val = ctx.video_processor.ear_value
                    ear_placeholder.markdown(f"""
                        <div class="metric-box">
                            <div class="metric-label">Eye Aspect Ratio</div>
                            <div class="metric-value">{ear_val:.3f}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Check Alert Status
                    if ctx.video_processor.alert_status:
                        status_placeholder.markdown("""
                            <div class="css-card" style="text-align:center; border-color: #ff4757;">
                                <div class="status-big-icon" style="color:#ff4757;">💤</div>
                                <div class="status-text-large" style="color:#ff4757;">DROWSINESS!</div>
                                <div style="color:rgba(255,255,255,0.5); font-size:0.9rem; margin-top:0.5rem;">Wake Up!</div>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Audio
                        if alert_sound_b64:
                            unique_id = f"audio_{int(time.time() * 10)}"
                            audio_placeholder.markdown(
                                f'<div id="{unique_id}"><audio autoplay><source src="data:audio/wav;base64,{alert_sound_b64}"></audio></div>',
                                unsafe_allow_html=True
                            )
                        
                    else:
                        status_placeholder.markdown("""
                            <div class="css-card" style="text-align:center;">
                                <div class="status-big-icon">👁️</div>
                                <div class="status-text-large">ACTIVE</div>
                                <div style="color:rgba(255,255,255,0.5); font-size:0.9rem; margin-top:0.5rem;">Monitoring Driver</div>
                            </div>
                        """, unsafe_allow_html=True)
                        audio_placeholder.empty()

                    # Update Timer
                    elapsed = int(time.time() - st.session_state.start_time)
                    mins, secs = divmod(elapsed, 60)
                    hrs, mins = divmod(mins, 60)
                    session_placeholder.markdown(f"""
                        <div class="metric-box">
                            <div class="metric-label">Session Time</div>
                            <div class="metric-value" style="color:white;">{hrs:02d}:{mins:02d}:{secs:02d}</div>
                        </div>
                    """, unsafe_allow_html=True)

                time.sleep(0.1)
        else:
            # Standby State
            if 'start_time' in st.session_state:
                del st.session_state.start_time
            
            status_placeholder.markdown("""
                <div class="css-card" style="text-align:center;">
                    <div class="status-big-icon" style="opacity:0.5;">📷</div>
                    <div class="status-text-large" style="opacity:0.5;">STANDBY</div>
                    <div style="color:rgba(255,255,255,0.3); font-size:0.9rem; margin-top:0.5rem;">Ready to monitor</div>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

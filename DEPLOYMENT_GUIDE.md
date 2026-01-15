# 🚀 Hugging Face Spaces Deployment Guide
## DrowseGuard - Complete Beginner's Tutorial

This guide will walk you through deploying DrowseGuard to Hugging Face Spaces step-by-step, assuming you know nothing about hosting or deployment.

---

## 📋 What You'll Need

- ✅ Your DrowseGuard project files (you already have these!)
- ✅ A web browser
- ✅ Internet connection
- ✅ 30 minutes of time

**No coding knowledge, Git experience, or server setup required!**

---

## 🎯 Step 1: Create a Hugging Face Account

### 1.1 Go to Hugging Face
1. Open your web browser
2. Go to: **https://huggingface.co/join**
3. You'll see a signup page

### 1.2 Sign Up
Choose one of these options:

**Option A: Sign up with Google/GitHub**
- Click "Continue with Google" or "Continue with GitHub"
- Follow the popup instructions
- ✅ Done!

**Option B: Sign up with Email**
- Enter your email address
- Create a username (lowercase, no spaces, e.g., "john_smith")
- Create a password
- Click "Create Account"
- Check your email for verification link
- Click the verification link
- ✅ Done!

### 1.3 Complete Your Profile (Optional)
- Add a profile picture
- Add a short bio (e.g., "ML enthusiast working on drowsiness detection")
- Click "Save"

---

## 🎯 Step 2: Create a New Space

### 2.1 Navigate to Spaces
1. After logging in, click your **profile picture** (top right)
2. Click **"New Space"** from the dropdown
   - Or go directly to: **https://huggingface.co/new-space**

### 2.2 Configure Your Space

Fill out the form:

#### **Space Name** (Required)
- Enter: `drowseguard` (or any name you like)
- ⚠️ Must be lowercase, can use hyphens/underscores
- ✅ Good examples: `drowseguard`, `driver-alert`, `fatigue_detector`
- ❌ Bad examples: `DrowseGuard`, `My App`, `drowse guard`

#### **License** (Required)
- Select: **MIT** (recommended - most permissive)
- Or choose any other license you prefer

#### **Select the Space SDK** (Required)
- Select: **Streamlit** ⭐ (Very important!)
- Don't select Gradio, Docker, or Static

#### **Space Hardware** (Optional)
- Keep default: **CPU basic - Free** ✅
- Don't change unless you need more power

#### **Visibility** (Required)
- Select: **Public** (Free - anyone can use it)
- Or select **Private** (Only you can access it)

### 2.3 Create the Space
1. Review your settings
2. Click **"Create Space"** button (bottom of page)
3. Wait a few seconds...
4. ✅ Your Space is created!

You'll be taken to your Space's page.

---

## 🎯 Step 3: Upload Your Project Files

You now have an empty Space. Let's add your files!

### 3.1 Understanding the Upload Interface

You'll see:
- **Files** tab (you're here)
- An area that says "Drag and drop files or click to browse"
- Some example files might be shown

### 3.2 Two Methods to Upload

---

### **Method A: Web Upload** (Easiest - Recommended for Beginners)

#### Step 1: Prepare Your Files
1. Open File Explorer on your computer
2. Navigate to: `d:\ML_projects\Driver Drowsiness Detection`
3. You should see these files:
   - `main.py`
   - `requirements.txt`
   - `README.md` (newly created)
   - `music.wav`
   - `assets` folder
   - `models` folder

#### Step 2: Upload Files One by One

**Upload main.py:**
1. On the Hugging Face Space page, click **"Add file"** → **"Upload files"**
2. Click "Choose files" or drag `main.py` into the upload area
3. In the commit message box at bottom, type: `Add main application file`
4. Click **"Commit changes to main"** button
5. Wait for upload to complete (you'll see a success message)

**Upload requirements.txt:**
1. Click **"Add file"** → **"Upload files"** again
2. Select `requirements.txt`
3. Commit message: `Add Python dependencies`
4. Click **"Commit changes to main"**

**Upload README.md:**
1. Click **"Add file"** → **"Upload files"**
2. Select `README.md`
3. Commit message: `Add documentation`
4. Click **"Commit changes to main"**

**Upload music.wav:**
1. Click **"Add file"** → **"Upload files"**
2. Select `music.wav`
3. Commit message: `Add alert sound`
4. Click **"Commit changes to main"**

#### Step 3: Upload the Assets Folder

**⚠️ Important: You need to recreate the folder structure**

1. Click **"Add file"** → **"Create a new file"**
2. In the filename box, type: `assets/style.css`
   - ⚠️ Note the `/` - this creates a folder!
3. Open your local `assets/style.css` file in Notepad
4. Copy ALL the contents
5. Paste into the Hugging Face editor
6. Commit message: `Add CSS styling`
7. Click **"Commit changes to main"**

Repeat for other asset files:
- `assets/eye1.jpg` - Upload as file (not text)
- `assets/eye2.png` - Upload as file
- `assets/eye3.jpg` - Upload as file

#### Step 4: Upload the Models Folder

**⚠️ CRITICAL: This is the most important file (95 MB)**

The model file is too large for the regular upload. Here's how to handle it:

**Option 1: Use Git LFS (Recommended but Advanced)**
- Skip for now, we'll use Option 2

**Option 2: Download During App Startup (Easier)**
- We'll modify the code to download the model automatically
- Skip uploading the models folder for now
- I'll provide the code modification below

**Option 3: Split Upload (Temporary Solution)**
- The model file might upload via the web interface
- Try: Click **"Add file"** → **"Upload files"**
- Navigate to `models/shape_predictor_68_face_landmarks.dat`
- Try to upload
- If it fails (file too large), use Option 2

---

### **Method B: Git/Command Line** (Advanced - Skip if Unfamiliar)

If you're comfortable with Git:

```bash
# 1. Install Git if not already installed
# 2. Clone your Space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/drowseguard
cd drowseguard

# 3. Copy your project files
copy "d:\ML_projects\Driver Drowsiness Detection\*" .

# 4. For the large model file, use Git LFS
git lfs install
git lfs track "models/shape_predictor_68_face_landmarks.dat"
git add .gitattributes

# 5. Add all files
git add .

# 6. Commit
git commit -m "Initial deployment"

# 7. Push to Hugging Face
git push

# 8. Wait for build
```

---

## 🎯 Step 4: Handle the Large Model File

Since the model file is 95 MB, we have a special solution.

### Option A: Let Hugging Face Handle It

1. Try uploading via web interface
2. If successful, you're done! ✅
3. If it fails, proceed to Option B

### Option B: Auto-Download on Startup (Recommended)

We'll modify `main.py` to download the model automatically.

**Don't worry - I'll give you the exact code to add!**

#### Manual Code Edit via Hugging Face:

1. On your Space page, click on **`main.py`**
2. Click the **"Edit"** button (pencil icon, top right)
3. Find this line near the top (around line 47):
   ```python
   MODEL_PATH = "models/shape_predictor_68_face_landmarks.dat"
   ```

4. **REPLACE** that entire section with:
   ```python
   MODEL_PATH = "models/shape_predictor_68_face_landmarks.dat"
   
   # Auto-download model if not present
   @st.cache_resource
   def ensure_model_exists():
       import urllib.request
       import bz2
       import os
       
       if not os.path.exists(MODEL_PATH):
           os.makedirs("models", exist_ok=True)
           st.info("📥 Downloading facial landmark model (one-time, ~95MB)...")
           
           url = "https://github.com/italojs/facial-landmarks-recognition/raw/master/shape_predictor_68_face_landmarks.dat"
           
           try:
               urllib.request.urlretrieve(url, MODEL_PATH)
               st.success("✅ Model downloaded successfully!")
           except Exception as e:
               st.error(f"Failed to download model: {e}")
               st.stop()
       return MODEL_PATH
   
   # Ensure model exists before proceeding
   ensure_model_exists()
   ```

5. Scroll down to the bottom
6. Commit message: `Add automatic model download`
7. Click **"Commit changes to main"**

✅ Done! The model will now download automatically on first run.

---

## 🎯 Step 5: Wait for Build & Deployment

### 5.1 Building Process

After uploading files, Hugging Face will automatically:
1. **Install dependencies** from `requirements.txt`
2. **Build the environment** (Python + libraries)
3. **Start your app**

This takes **3-10 minutes** the first time.

### 5.2 Monitor the Build

1. On your Space page, look for **"Building"** status (top)
2. Click **"Logs"** to see real-time progress
3. You'll see output like:
   ```
   Installing streamlit...
   Installing opencv-python-headless...
   Installing dlib... (this takes a while!)
   ```

### 5.3 Build Success!

When complete, you'll see:
- ✅ Status changes to **"Running"**
- Your app interface appears in the preview
- URL is active: `https://huggingface.co/spaces/YOUR_USERNAME/drowseguard`

### 5.4 Build Failed?

If you see **"Build Failed"** or **"Runtime Error"**:

**Check the logs for errors:**
1. Click **"Logs"** tab
2. Look for red error messages
3. Common issues:

**Error: "dlib installation failed"**
- Solution: This is common. Hugging Face might need special dlib configuration
- Add to `requirements.txt`: `dlib==19.24.2`
- Or use: `cmake` package first

**Error: "No module named 'cv2'"**
- Solution: Verify `requirements.txt` has `opencv-python-headless`

**Error: "ModuleNotFoundError"**
- Solution: Missing package in `requirements.txt`
- Add the missing package

---

## 🎯 Step 6: Test Your Deployed App!

### 6.1 Access Your Space

1. Go to your Space URL:
   - `https://huggingface.co/spaces/YOUR_USERNAME/drowseguard`
2. You should see the DrowseGuard interface! 🎉

### 6.2 Test Functionality

**Test the Video Feed:**
1. Click the **"START"** button in the video section
2. Your browser will ask: **"Allow drowseguard to use your camera?"**
3. Click **"Allow"** ✅
4. Your webcam feed should appear!

**Test Detection:**
1. Position your face in front of the camera
2. You should see:
   - Green contours around your eyes
   - Eye Aspect Ratio value updating
   - Status showing "ACTIVE"
3. Close your eyes for a few seconds
4. You should see:
   - Status changes to "DROWSINESS!"
   - Alert sound plays
   - Red text on video

**Test Settings:**
1. Expand the **"⚙️ Configuration"** section
2. Move the sliders
3. Values should update in real-time

### 6.3 Troubleshooting

**Camera Not Working?**
- Ensure you clicked "Allow" for camera permissions
- Try a different browser (Chrome recommended)
- Check if HTTPS is enabled (Hugging Face enables by default)
- Some browsers block webcam on embedded frames

**App Crashes When Starting Video?**
- Check logs for errors
- Model file might not be loaded
- dlib might have installation issues

**Alert Sound Not Playing?**
- Browser autoplay policies vary
- Try clicking on the page first (some browsers require user interaction)
- Check if `music.wav` was uploaded successfully

---

## 🎯 Step 7: Share Your Space!

### 7.1 Get Your Shareable Link

Your Space is now live at:
```
https://huggingface.co/spaces/YOUR_USERNAME/drowseguard
```

Share this link with anyone!

### 7.2 Embed Your Space

You can even embed it in websites:

```html
<iframe
  src="https://huggingface.co/spaces/YOUR_USERNAME/drowseguard"
  width="100%"
  height="800px"
></iframe>
```

### 7.3 Add to Your Portfolio

- Add the link to your resume
- Share on LinkedIn
- Include in GitHub profile README
- Showcase in project presentations

---

## 📊 Understanding Your Space Dashboard

### Metrics You Can See:
- **👥 Visits** - How many people viewed your Space
- **🔄 Runs** - How many times the app was used
- **❤️ Likes** - Users can "like" your Space

### Available Tabs:
- **App** - The running application (default view)
- **Files** - Edit/view your code and files
- **Community** - Discussions and feedback
- **Settings** - Configure Space settings

---

## 🔧 Advanced: Updating Your Space

### To Make Changes:

**Method 1: Edit Directly on HF**
1. Go to **"Files"** tab
2. Click the file you want to edit
3. Click **"Edit"** (pencil icon)
4. Make changes
5. Add commit message
6. Click **"Commit changes"**
7. Space rebuilds automatically!

**Method 2: Re-upload**
1. Go to **"Files"** tab
2. Click **"Add file"** → **"Upload files"**
3. Upload the new version
4. It will overwrite the old file

### To Delete Your Space:
1. Go to **"Settings"** tab
2. Scroll to **"Delete this Space"**
3. Type your Space name to confirm
4. Click **"Delete Space"**

---

## 🐛 Common Issues & Solutions

### Issue: "Application startup failed"
**Solution:**
- Check logs for specific error
- Verify all files uploaded correctly
- Ensure `requirements.txt` is valid

### Issue: "Import Error: No module named 'dlib'"
**Solution:**
- dlib can be tricky to install
- Try adding `cmake` to `requirements.txt`:
  ```txt
  cmake
  dlib==19.24.2
  ```

### Issue: "Model file not found"
**Solution:**
- Ensure model auto-download code is added
- Or manually upload the model file
- Check `models/` folder exists

### Issue: "WebRTC connection failed"
**Solution:**
- This is often browser-specific
- Try Chrome or Edge
- Check browser console for errors
- Some corporate networks block WebRTC

### Issue: "Space is always building"
**Solution:**
- A package installation might be stuck (often dlib)
- Restart the Space: Settings → "Factory Reboot"

---

## 💰 Cost & Limits

### Free Tier Includes:
- ✅ **Unlimited** public Spaces
- ✅ **CPU basic** hardware (free)
- ✅ **No time limits**
- ✅ **Decent storage** for code/files

### Limitations:
- ⚠️ **Shared CPU** - May be slow during high traffic
- ⚠️ **No GPU** on free tier (don't need it for this project)
- ⚠️ **Sleep mode** - Space may sleep after inactivity (wakes up when visited)

### Upgrades (Optional - NOT Required):
- Pro subscription for faster hardware
- GPU for machine learning models
- Private Spaces features

**For DrowseGuard: FREE tier is perfectly fine!** ✅

---

## ✅ Deployment Checklist

Before you start, make sure you have:

- [ ] Created Hugging Face account
- [ ] Created new Space with Streamlit SDK
- [ ] Uploaded `main.py`
- [ ] Uploaded `requirements.txt`
- [ ] Uploaded `README.md`
- [ ] Uploaded `music.wav`
- [ ] Uploaded `assets/style.css`
- [ ] Uploaded asset images (or created empty folder)
- [ ] Handled model file (upload or auto-download code)
- [ ] Waited for build to complete (3-10 min)
- [ ] Tested camera access
- [ ] Tested drowsiness detection
- [ ] Tested alert sound
- [ ] Shared your Space URL!

---

## 🎉 Congratulations!

You've successfully deployed DrowseGuard to the cloud! 🚀

Your app is now:
- ✅ **Live on the internet**
- ✅ **Accessible from any device**
- ✅ **Free to use and share**
- ✅ **Automatically updated** when you push changes

### What's Next?

- Share with friends and family
- Add to your portfolio
- Collect feedback via Community tab
- Improve based on user suggestions
- Deploy other projects!

---

## 📞 Need Help?

- **Hugging Face Docs**: https://huggingface.co/docs/hub/spaces
- **Streamlit Docs**: https://docs.streamlit.io
- **Community Forum**: https://discuss.huggingface.co

---

## 📝 Quick Reference

**Your Space URL Format:**
```
https://huggingface.co/spaces/YOUR_USERNAME/drowseguard
```

**Edit Files:**
Files tab → Click file → Edit button → Make changes → Commit

**View Logs:**
App tab → Click "Logs" button (top right)

**Restart Space:**
Settings tab → Factory Reboot

---

**Made with ❤️ for beginners. Happy deploying!** 🚀

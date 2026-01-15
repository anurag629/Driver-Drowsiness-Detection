# Use buildpack-deps for better build dependencies (slightly larger but more reliable)
FROM python:3.10-bullseye

WORKDIR /app

# Install system dependencies (these are already included in bullseye but we ensure they're present)
RUN apt-get update && apt-get install -y \
    cmake \
    wget \
    curl \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libglib2.0-0 \
    ffmpeg \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies in optimized order
# Install build dependencies first
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install numpy and scipy (needed by other packages)
RUN pip install --no-cache-dir numpy==1.24.3 scipy==1.11.4

# Install dlib separately with extended timeout
RUN pip install --no-cache-dir --timeout 2000 dlib==19.24.2

# Install remaining packages
RUN pip install --no-cache-dir \
    streamlit==1.36.0 \
    streamlit-webrtc==0.47.7 \
    opencv-python-headless==4.8.1.78 \
    imutils==0.5.4 \
    aiortc==1.9.0 \
    aioice==0.9.0 \
    av==12.3.0 \
    attrs==23.2.0

# Copy all application files
COPY . .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

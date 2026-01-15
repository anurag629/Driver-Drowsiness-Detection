# 🐳 Docker Deployment Guide - Full Functionality
## Complete Step-by-Step Process for Beginners

This guide will help you deploy DrowseGuard with **100% face detection functionality** using Docker on Hugging Face.

---

## 📋 What You Need

- ✅ Your Hugging Face account (already created)
- ✅ Your Space (already created: broootech/drowseguard)
- ✅ The new files I created (Dockerfile, updated requirements.txt)
- ✅ 15-20 minutes

---

## 🎯 STEP 1: Upload Dockerfile to Hugging Face

### What is Dockerfile?
A Dockerfile is like a recipe that tells the computer exactly how to set up your app, including installing dlib and all dependencies.

### Upload Steps:

1. Go to your Space: **https://huggingface.co/spaces/broootech/drowseguard**
2. Click **"Files"** tab
3. Click **"+ Add file"** → **"Create a new file"**
4. In the filename box, type: `Dockerfile` (exactly, no .txt extension)
5. Now paste this content:

```dockerfile
# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (required for dlib, opencv, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopencv-dev \
    libavcodec-dev \
    libavformat-dev \
    libavutil-dev \
    libswscale-dev \
    libavdevice-dev \
    libavfilter-dev \
    libswresample-dev \
    pkg-config \
    ffmpeg \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run the application
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

6. Commit message: `Add Dockerfile for full functionality`
7. Click **"Commit new file"**
8. ✅ Done!

---

## 🎯 STEP 2: Update requirements.txt

### Why Update?
The Docker requirements.txt includes dlib and all dependencies that couldn't install before.

### Update Steps:

1. Still on the **"Files"** tab
2. Click on **`requirements.txt`** (the existing file)
3. Click **"Edit"** button (pencil icon)
4. **Delete everything** in the file
5. Paste this:

```txt
streamlit==1.36.0
streamlit-webrtc==0.47.7
opencv-python-headless==4.8.1.78
dlib==19.24.2
imutils==0.5.4
scipy==1.11.4
numpy==1.24.3
aiortc==1.9.0
aioice==0.9.0
av==12.3.0
attrs==23.2.0
```

6. Commit message: `Update requirements for Docker`
7. Click **"Commit changes"**
8. ✅ Done!

---

## 🎯 STEP 3: Delete packages.txt (If It Exists)

Docker doesn't need packages.txt (we use Dockerfile instead).

1. On the **"Files"** tab, look for **`packages.txt`**
2. If you see it, click on it
3. Click the **trash/delete icon**
4. Confirm deletion
5. If you don't see it, skip this step ✅

---

## 🎯 STEP 4: Change Space SDK to Docker ⚠️ CRITICAL

This is the **most important step** - telling Hugging Face to use Docker instead of Streamlit SDK.

### Steps:

1. Click on **`README.md`** file (in Files tab)
2. Click **"Edit"**
3. At the very top between `---` marks, find this line:
   ```yaml
   sdk: streamlit
   ```
4. **Change it to**:
   ```yaml
   sdk: docker
   ```
5. The top section should now look like:
   ```yaml
   ---
   title: DrowseGuard - Driver Drowsiness Detection
   emoji: 🛡️
   colorFrom: blue
   colorTo: blue
   sdk: docker
   sdk_version: "1.36.0"
   app_file: main.py
   pinned: false
   license: mit
   ---
   ```

6. Commit message: `Switch to Docker SDK for full functionality`
7. Click **"Commit changes"**
8. ✅ Done!

---

## 🎯 STEP 5: Wait for Docker Build

### What Happens Now:

Hugging Face will:
1. Detect the Dockerfile
2. Start building a Docker container
3. Install ALL system dependencies (cmake, ffmpeg, etc.)
4. Install dlib (this takes longest - 10-15 minutes!)
5. Install all Python packages
6. Start your app

### Monitor the Build:

1. Click **"App"** tab
2. You'll see **"Building..."** status
3. Click **"Logs"** button (top right)
4. You'll see Docker build output

### What You'll See in Logs:

```
Step 1/10 : FROM python:3.11-slim
Step 2/10 : WORKDIR /app
Step 3/10 : RUN apt-get update...
Step 4/10 : COPY requirements.txt .
Step 5/10 : RUN pip install...
  Installing dlib... (THIS TAKES LONG - BE PATIENT!)
  Installing streamlit...
  Installing opencv-python-headless...
Step 6/10 : COPY . .
...
Successfully built!
```

### ⏱️ Build Time: 15-20 minutes

**This is NORMAL!** Docker needs to:
- Download base image
- Install system packages
- Compile dlib from source (slowest part)
- Install Python packages

☕ **Go get coffee, watch a video, take a break!**

---

## 🎯 STEP 6: Verify It's Working

### When Build Completes:

1. Status changes from "Building..." to **"Running"** ✅
2. Your app loads in the App tab
3. You should see:
   - **DrowseGuard dashboard**
   - **NO warning about demo mode!**
   - **Video feed with START button**

### Test Face Detection:

1. Click **"START"** button
2. Grant camera permission
3. Position your face in front of camera
4. You should see:
   - ✅ **Green contours around your eyes!** (this means dlib is working!)
   - ✅ Eye Aspect Ratio value updates
   - ✅ Status shows "ACTIVE"

5. **Close your eyes** for 5-10 seconds
6. You should see:
   - ✅ **"DROWSINESS ALERT!"** message
   - ✅ Alert sound plays
   - ✅ Red overlay on video

### ✅ SUCCESS CRITERIA:

If you see green eye contours and drowsiness detection works, **you have 100% functionality!**

---

## 🐛 Troubleshooting

### Issue: Build Fails with Error

**Check the logs for:**
- Red error messages
- "Failed to build" messages

**Common fixes:**
- Make sure Dockerfile is exactly as provided
- Verify SDK is set to `docker` in README.md
- Try "Factory Reboot" (Settings tab)

### Issue: Build Takes Forever (>30 min)

**Solution:**
- This sometimes happens with dlib compilation
- Go to **Settings** tab
- Click **"Factory reboot"**
- Wait for rebuild

### Issue: App Loads But No Face Detection

**Solution:**
- Check logs for errors
- Look for "import dlib" errors
- Verify requirements.txt has `dlib==19.24.2`

### Issue: "Application Error" on Page

**Solution:**
- Click **"Logs"** to see specific error
- Often a missing file or syntax error
- Verify all files uploaded correctly

---

## 📊 Files You Should Have

After completing all steps, your Space should have:

- ✅ `Dockerfile` (NEW - Docker configuration)
- ✅ `requirements.txt` (UPDATED - with dlib)
- ✅ `README.md` (UPDATED - sdk: docker)
- ✅ `main.py` (your application code)
- ✅ `music.wav` (alert sound)
- ✅ `assets/style.css` (UI styling)
- ❌ `packages.txt` (DELETED - not needed with Docker)

---

## ✅ Success Checklist

You're done when:

- [ ] Dockerfile uploaded
- [ ] requirements.txt updated with dlib
- [ ] README.md changed to `sdk: docker`
- [ ] packages.txt deleted (if it existed)
- [ ] Docker build completed (15-20 min)
- [ ] App loads without errors
- [ ] Camera permission granted
- [ ] **Green contours appear around eyes** ⭐
- [ ] Drowsiness detection works
- [ ] Alert sound plays when eyes closed

---

## 🎉 What You Get

After successful Docker deployment:

- ✅ **100% face detection** (dlib working!)
- ✅ **Real-time eye tracking**
- ✅ **Drowsiness alerts**
- ✅ **Audio warnings**
- ✅ **All features functional**
- ✅ **Professional demo**
- ✅ **Portfolio-ready**

---

## 🚀 Your App URL

Once working:
```
https://huggingface.co/spaces/broootech/drowseguard
```

Share it with friends, recruiters, on LinkedIn!

---

## ⚡ Quick Reference

**Files to Upload:**
1. `Dockerfile` - Docker build instructions
2. Update `requirements.txt` - Add dlib

**Key Changes:**
1. README.md: `sdk: streamlit` → `sdk: docker`
2. Delete `packages.txt` if exists

**Build Time:** 15-20 minutes (dlib compilation is slow)

**Test:** Look for green eye contours when camera active

---

## 📞 If You Get Stuck

1. Check **Logs** for specific errors
2. Verify `sdk: docker` in README.md
3. Try **Factory Reboot** (Settings tab)
4. Rebuild can take 15-20 min - be patient!

---

**Ready? Start with STEP 1: Upload Dockerfile!** 🐳🚀

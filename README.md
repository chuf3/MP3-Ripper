# MP3-Ripper

# Lisa's MP3 Ripper

A local web application for extracting audio from YouTube videos, managing MP3 files, and trimming audio using a browser-based interface.

Designed for **personal use** and tested for **Raspberry Pi** environments.

---

## Features

- 🎵 Extract audio from YouTube URLs (MP3)
- 📂 View all downloaded files in a web interface
- ▶️ Play audio directly in the browser
- ✂️ Trim audio using start/end sliders
- 💾 Save edits (overwrites original file)
- ⬇️ Download MP3 files
- 🗑 Delete files

Webpage title: **Lisa's MP3 Ripper**

---

## Tech Stack

- Python 3
- Flask
- yt-dlp
- FFmpeg
- HTML5 Audio + JavaScript sliders

---

## Project Structure

```text
lisas-mp3-ripper/
├── app.py
├── downloads/
├── templates/
│   ├── index.html
│   └── edit.html
├── static/
│   └── editor.js
└── README.md
```

---

## Installation (Raspberry Pi / Linux)

### 1. System Dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-pip ffmpeg
```

Verify FFmpeg:
```bash
ffmpeg -version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/lisas-mp3-ripper.git
cd lisas-mp3-ripper
```

---

### 3. Python Dependencies

```bash
pip3 install flask yt-dlp
```

---

## Running the App

```bash
python3 app.py
```

Open your browser and navigate to:

```
http://<raspberry-pi-ip>:5000
```

(or `http://127.0.0.1:5000` if local)

---

## Audio Editing Notes

- Audio trimming uses FFmpeg under the hood
- Start and end sliders allow precise cutting
- Saving edits **overwrites the original MP3 file**
- Playback is available before saving

---

## Legal Notice

This application is intended for **personal use only**.
Ensure you have the rights to download and edit any audio content.

---

## Next Enhancements (Optional)

- Playlist support
- Drag-and-drop uploads
- Waveform visualization
- Authentication / access control

---

Enjoy 🎧

**Lisa's MP3 Ripper**

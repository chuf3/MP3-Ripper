import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import yt_dlp

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]

                ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "quiet": True,
            "js_runtimes": {
                "deno": {}
            },
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return redirect(url_for("index"))

    files = sorted(f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".mp3"))
    return render_template("index.html", files=files)


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)


@app.route("/delete/<filename>")
def delete(filename):
    os.remove(os.path.join(DOWNLOAD_DIR, filename))
    return redirect(url_for("index"))


@app.route("/edit/<filename>")
def edit(filename):
    return render_template("edit.html", filename=filename)


@app.route("/trim", methods=["POST"])
def trim():
    filename = request.form["filename"]
    start = request.form["start"]
    end = request.form["end"]

    src = os.path.join(DOWNLOAD_DIR, filename)
    tmp = os.path.join(DOWNLOAD_DIR, "tmp_" + filename)

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            src,
            "-ss",
            start,
            "-to",
            end,
            "-c",
            "copy",
            tmp,
        ],
        check=True,
    )

    os.replace(tmp, src)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

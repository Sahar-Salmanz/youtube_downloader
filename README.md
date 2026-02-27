<img src='./images/banner.png'>


# YouTube Downloader
A clean, object-oriented YouTube downloader built with Python and `yt-dlp`.  
This project provides a powerful and flexible command-line interface (CLI) to download YouTube videos in selected quality or extract audio-only (MP3), with progress tracking and a modular architecture.  


## Features
* 📥 Download videos from YouTube via URL
* 🎥 Select video quality (best, worst, 720p, etc.)
* 🎵 Audio-only download (MP3 extraction)
* 📂 Custom output directory
* 📊 Real-time progress display
* 🧱 Clean OOP architecture
* 🖥️ Professional CLI interface
* 📦 Installable as a command-line tool 


## Project Structure
```
youtube_downloader/
│
├── src/
│   ├── downloader.py      # Core YouTubeDownloader class
│   └── cli.py             # CLI interface
│   └── main.py            # Entry point 
│
├── requirements.txt
└── README.md
```


## Installation
1. __Clone the Repository__
```
git clone https://github.com/Sahar-Salmanz/youtube_downloader.git
cd youtube_downloader
```

2. __Create & Activate Environment__
```
conda create --name ytdl python=3.10
conda activate ytdl
```

3. __Install Dependencies__
```
pip install -r requirements.txt
```

4. __Install FFmpeg (Required for Audio Extraction)__
On macOS:
```
brew install ffmpeg
```

## Usage
__Add src to the path__
```
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

__Basic Download__
```
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"
```
Downloads best available quality to current directory.  

__Download to Specific Folder__
```
python main.py URL -o downloads
```

__Select Quality__
```
python main.py URL -q "best[height<=720]"
```
Other examples:
* best
* worst
* bestvideo+bestaudio


__Download Audio Only (MP3)__
```
python main.py URL -a
```


## How It Works
The project is structured with separation of concerns:
* `cli.py` → Handles user input via `argparse`
* `downloader.py` → Contains `YouTubeDownloader` class
* `yt-dlp` → Handles video extraction and downloading


## Dependencies
* Python 3.10+
* yt-dlp
* ffmpeg (for audio extraction)


## Future Improvements
* Playlist support
* Metadata extraction (title, duration, thumbnails)
* Logging system
* Unit tests
* GUI version (Streamlit / Tkinter)
* Docker support
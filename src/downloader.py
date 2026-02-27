import os
import yt_dlp


class YouTubeDownloader:
    def __init__(self, url: str, output_dir: str = None, quality: str = 'best', audio_only: bool = False):
        """
        Downloader for YouTube videos using yt-dlp.

        :param url: YouTube video URL
        :param output_dir: Output directory path, defaults to None (current working directory)
        :param quality: Video quality, defaults to 'best'
        :param audio_only: Whether to download only audio, defaults to False
        """
        self.url = url
        self.output_dir = output_dir or os.getcwd()
        self.quality = quality
        self.audio_only = audio_only

    def validate_url(self):
        """
        Validates the provided YouTube URL.

        :raises ValueError: If URL is invalid or not a YouTube link
        """
        if not self.url.startswith(('http://', 'https://')):
            raise ValueError('Invalid URL: Must start with http:// or https://')
        if 'youtube.com' not in self.url and 'youtu.be' not in self.url:
            raise ValueError('Invalid URL: Must be a YouTube link')
        
    def validate_output_dir(self):
        """
        Validates the output directory.

        :raises ValueError: If output directory does not exist or is not a directory
        """
        if not os.path.exists(self.output_dir):
            raise ValueError(f'Output directory does not exist: {self.output_dir}')
        if not os.path.isdir(self.output_dir):
            raise ValueError(f'Output path is not a directory: {self.output_dir}')
        
    def _progress_hook(self, d: dict):
        """
        Progress hook for yt-dlp to display download progress.

        :param d: Dictionary containing download status and progress information
        """
        if d['status'] == 'downloading':
            print(f"Downloading: {d['_percent_str']} at {d['_speed_str']} ETA {d['_eta_str']}")
        elif d['status'] == 'finished':
            print('Download completed, Processing...')

    def download(self):
        """
        Downloads the YouTube video with progress tracking.

        :raises ValueError: If URL or output directory is invalid
        """
        self.validate_url()
        self.validate_output_dir()
        ydl_opts = {
            'format': self.quality,
            'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }
        if self.audio_only:
            ydl_opts['format'] = 'bestaudio/best'
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
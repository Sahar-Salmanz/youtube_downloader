import argparse
from src.downloader import YouTubeDownloader


def main():
    """
    Main function to parse command-line arguments and initiate the YouTube download process.
    """
    parser = argparse.ArgumentParser(description='YouTube Video Downloader')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('--output', '-o', help='Output directory (default: current directory)')
    parser.add_argument('--quality', '-q', default='best', help='Video quality (default: best)')
    parser.add_argument('--audio-only', '-a', action='store_true', help='Download audio only')
    
    args = parser.parse_args()
    
    # Create a YouTubeDownloader instance with the provided arguments
    downloader = YouTubeDownloader(
        url=args.url,
        output_dir=args.output,
        quality=args.quality,
        audio_only=args.audio_only
    )
    
    downloader.download()

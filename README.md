# hollowlake-pytube
A video downloader using the Python PyTube library

In order to use this script, make sure you have PyTube installed: https://pypi.org/project/pytube/

This script will do 4 things. 

1. Ask for the YouTube URL
2. Ask for a new name for the video
- This is so videos are easy to find as some YouTube videos have crazy names
3. Ask if the video is video only
- I use this for MagicMirror, in which I don't want audio. If Video Only is answered "y", it downloads the highest stream available without audio. 
- If the user says "n" it will download the highest available with audio. This is usually somewhere between 360p and 720p due to YouTube limitations. 
4. Download video to specified directory
- Replace hold text with your own directory. 

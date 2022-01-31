from pytube.cli import on_progress
from pytube import YouTube

while True:
    
    url = input("Paste Youtube URL: ")
    yt = YouTube(url, on_progress_callback=on_progress)
    
    print(f"Located: {yt.title}") 

    choice = input("Is this a 'Video Only' download? (Y/N): ")

    if choice[0] == 'y':
        try:
            print(f"Downloading as video only...")
            
            yt.streams.filter(adaptive=True).first().download('D:\Videos\VideoOnly')
                
            print(f'\n{yt.title} has finished downloading as Video Only.')
        
        except EOFError as err:
            print("An error occured, try again.")
    
    else:
        try:
            print(f"Downloading complete video...")

            yt.streams.get_highest_resolution().download('D:\Videos')    
                
            print(f'\n{yt.title} has finished downloading.')
                
        except EOFError as err:
            print("An error occured, try again.")
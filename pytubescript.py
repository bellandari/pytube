from pytube.cli import on_progress
from pytube import YouTube

while True:
    
    url = input("Paste Youtube URL: ")
    yt = YouTube(url, on_progress_callback=on_progress)
    
    print(f"{yt.title} found...") 

    name = input("Enter new file name: ")
    choice = input("Is this 'Video Only'? (Y/N): ")

    if choice[0] == 'y':
        try:
            print(f"Downloading {yt.title}...")
            
            yt.streams.filter(adaptive=True).first().download('C:\directoryhere', filename=name)   
                
            print(f'\n{yt.title} has finished downloading as Video Only.')
        
        except EOFError as err:
            print("An error occured, try again.")
    
    else:
        try:
            print(f"Downloading {yt.title}...")

            yt.streams.get_highest_resolution().download('C:\directoryhere', filename=name)    
                
            print(f'\n{yt.title} has finished downloading as Video/Audio.')
                
        except EOFError as err:
            print("An error occured, try again.")
            
# This is a sample Python script.
import sys
from pytube import YouTube
from termcolor import colored


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def youtube_dwnld(link):
    print(colored('Welcome to vortex_tube :) -_-', 'green'))
    for i in range(80):
        print("#", end="")
    print()
    print(colored('Hang on we getting the file size :) -_-', 'blue'))
    yt = YouTube(link)
    yt.register_on_progress_callback(show_progress_bar)
    file_size = yt.streams.get_highest_resolution().filesize
    print("Video File Size: " + '{0:.2f}'.format(file_size / 10000))
    print("Download in progress...")
    for i in range(80):
        print("#", end="")
    print()
    # get highest resolution
    stream = yt.streams.get_highest_resolution()
    # download video at highest resolution
    # current = ((stream.filesize - bytes_remaining) / stream.filesize)
    stream.download()
    for i in range(80):
        print("#", end="")
    print()
    print(colored("******* Download Complete *******", 'green'))
    for i in range(80):
        print("#", end="")
    print()
    print(colored('Thanks for using vortex_tube :) ^_-', 'yellow'))


def show_progress_bar(stream, _chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining) / stream.filesize)
    percent = '{0:.1f}'.format(current * 100)
    progress = int(50 * current)
    # status = '█' * progress + '-' * (50 - progress)
    status = '#' * progress + '-' * (50 - progress)
    # sys.stdout.write(f' ↳ {status} {percent}%', end="\r")

    # for i in tqdm(range(0, 100), initial=int(current), colour="#00fda0", ncols=100, desc="Progress: "):
    #     sleep(.1)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))


# print(' ↳ |bar={status}| percent={percent}%'.format(status, percent))
    sys.stdout.flush()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        youtube_dwnld('https://www.youtube.com/watch?v=WSW6Xc2Pq-Y')
    except:
        print('Retrying...')
        youtube_dwnld('https://www.youtube.com/watch?v=WSW6Xc2Pq-Y')

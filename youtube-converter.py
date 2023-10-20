from pytube import YouTube
import os
import datetime

download_path = os.getcwd() + '/download'

def Download():
    try:
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        
        mp3Links = GetLinks('mp3.txt')
        mp4Links = GetLinks('mp4.txt')
        for link in mp3Links:
            DownloadAudio(link)
        for link in mp4Links:
            DownloadVideo(link)
            
    except Exception as exc:
        with open('error.txt', 'a+') as file:
            file.write(str(datetime.datetime.now()) + ': ' + str(exc) + '\r\n')
    
def GetLinks(fileName):
    links = []
    if(os.path.isfile(fileName)):
        with open(fileName, 'r') as file:
            for line in file:
                links.append(str(line))
    return links
    
def DownloadAudio(link):
    youtubeObject = YouTube(link)
    youtubeObject.streams.filter()
    stream = youtubeObject.streams.get_audio_only()
    stream.download(output_path = download_path, filename = MakeNameWindowsAcceptable(stream.title) + '.mp3')

def DownloadVideo(link):
    youtubeObject = YouTube(link)
    youtubeObject.streams.filter()
    stream = youtubeObject.streams.get_highest_resolution()
    stream.download(output_path = download_path, filename = MakeNameWindowsAcceptable(stream.title) + '.mp4')
    
def MakeNameWindowsAcceptable(name):
    return name.replace('<', '').replace('>', '').replace(':', '').replace('"', '').replace('/', '').replace('\\', '').replace('|', '').replace('?', '').replace('*', '')
    
if __name__ == '__main__':
    Download()
import sys
from pytube import YouTube

args = sys.argv

# print(type(args[1]))

#yt = YouTube('https://youtu.be/-sUXMzkh-jI')
yt = YouTube('https://www.youtube.com/watch?v=PMivT7MJ41M')

# https://youtu.be/-PMivT7MJ41M

#yt = YouTube(args[1])
stream = yt.streams.first()
finished = stream.download()

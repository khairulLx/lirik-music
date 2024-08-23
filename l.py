import time
from threading import Thread
import sys

lyrics = [
    ("This song has started now", 0.08),
    ("And you're just finding out", 0.08),
    ("Now isn't that a laugh?", 0.08),
    ("A major sacrifice", 0.08),
    ("But clueless at the time", 0.08),
    ("Enter, Caroline", 0.08),
    ("'Just trust me, you'll be fine'", 0.09),
    ("And when I'm back in Chicago, I feel it", 0.09),
    ("Another version of me, I was in it", 0.08),
    ("I wave goodbye to the end of beginning", 0.1)
]

delays = [0, 3.0, 7.0, 10.5, 14.0, 18.0, 21.0, 26.0, 31.0, 35.0]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyrics(text, delay, speed):
    time.sleep(delay)
    animate_text(text, speed)

def sing_song():
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyrics, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    sing_song()

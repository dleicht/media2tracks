<img height="250" alt="Media2Tracks" src="https://github.com/user-attachments/assets/40e520ef-deed-4335-a445-4c263d7763f4" />

## Why?
Let's say you found a media file that contains separate audio parts you are interested in and you want these parts as individual MP3 files. Imagine doing all the cutting and joining manually on multiple files. Tiresome, yeah.
Write a super simple CSV tracklist file instead and let the magic happen automatically. Many sources provide tracklists anyway.

## How?
Media2Tracks is a wrapper for riad-azz' [audio-extract](https://github.com/riad-azz/audio-extract) to make it iterate over the tracklist. It supports a multitude of audio and video formats.

- Install audio-extract: `pip install audio-extract`
- Clone the repo: `git clone https://github.com/dleicht/media2tracks.git media2tracks`
- Use it: `python3 media2tracks.py <media file> <tracklist file>`

The tracklist is a very simple comma separated .csv or .txt file with the following information:
  - Title of the track
  - Start time in HH:MM:SS format

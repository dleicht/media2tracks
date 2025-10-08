from audio_extract import extract_audio, utils
from math import floor
from mutagen import MutagenError
from sys import argv
from csv import reader

if len(argv) != 3:
    print("\nMedia2Tracks v1.0\nExtract separate tracks from a media file, based on a given tracklist file.\n\nUsage: media2tracks.py <media file> <tracklist file>\n\n<media file>:\tAudio (WAV, OGG, MP3, AAC, FLAC, M4A, OGA, OPUS)\n\t\tVideo (MP4, MKV, WEBM, FLV, AVI, MOV, WMV, M4V)\n<tracklist file>: CSV or TXT with '<title>,<start>(HH:MM:SS)'\n\nPlease make sure to use matching media and tracklist files.")
else:
    audio_file = str(argv[1])
    trackinfo_file = str(argv[2])
    try:
        if trackinfo_file.endswith((".csv",".txt")):    
            with open(trackinfo_file, newline='') as f:
                r = reader(f, delimiter=',')
                trackinfo_data = list(r)
                start_list = list(i[1] for i in trackinfo_data)
                file_duration = floor(utils.media_duration(audio_file))
                start_list.append(utils.seconds_to_hms(file_duration))
                duration_list = list()

                if floor(utils.hms_to_seconds(start_list[-2])) > file_duration:
                    print("Tracktiming mismatch! Tracktime (",start_list[-2],") in the tracklist file doesn't match the duration of the media file (",utils.seconds_to_hms(file_duration),")!")
                else:
                    print("\nMedia2Tracks v1.0\nParsing the tracklist:\n")
                    for index, item in enumerate(start_list[:-1]):
                        duration = floor(utils.hms_to_seconds(start_list[index+1]) - utils.hms_to_seconds(start_list[index]))
                        print(index+1,"-",trackinfo_data[index][0],"-",start_list[index],"-",start_list[index+1],"-",duration,"sec")
                        duration_list.append(duration)
                    
                    for index, item in enumerate(trackinfo_data):
                        print(f"Writing track: {str(index+1)}-{item[0]}")
                        extract_audio(
                            input_path = audio_file,
                            output_path = f"./{index+1}-{item[0]}",
                            start_time = f"{item[1]}",
                            duration = duration_list[index],
                            overwrite = True
                            )
        else:
            print('Second file must be CSV or TXT!')

    
    except MutagenError as err:
         print(f"{type(err)} with file {err}.")
    except FileNotFoundError as err:
        print(f"{type(err)} with file {err}.")
    except KeyError as err:
        print(f"{type(err)} with key {err}. Looks like your tracklist file is missing information.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
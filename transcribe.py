import whisper
import time
import os
import moviepy.editor as mp


def transcribe_video(trim):
    directory = 'videos'

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        file_path = os.path.join(directory, file)
        audio_file_path = os.path.join(directory + '/audio', file.replace('.mp4', '.mp3'))
        if os.path.exists(audio_file_path) :
            print('Found ', audio_file_path, '. No need to transcribe.')
        else :
            clip = mp.VideoFileClip(file_path) 
            duration = clip.duration
            
            # First 10 minutes plus 20% of remainder
            if trim and duration > 10*60 :
                clip = clip.subclip(0, 10*60 + 0.20*duration) 
    
            # getting audio from the clip 
            audioclip = clip.audio 

            audio = clip.audio
            audio.write_audiofile(audio_file_path, codec='mp3')
            clip.close()
            audioclip.close()

            print('Transcribed ', audio_file_path)

    whisper_model = "base"

    model = whisper.load_model(whisper_model)
    whisper.DecodingOptions.fp16 = False

    # Specify the directory path
    directory = 'videos/audio'

    transcript_directory = 'transcripts/' + whisper_model

    if not os.path.exists(transcript_directory):
        os.makedirs(transcript_directory)

    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Print the list of files
    print("Files in directory:")
    print(files)
    # Access each file using os.path.join()
    for file in files:
        file_path = os.path.join(directory, file)

        # Now you can use file_path to access each file
        print("Accessing file:", file_path)
        for i in range(1) :
            # Record the starting time
            start_time = time.time()
            result = model.transcribe(file_path.replace(".mp4", ".mp3"))

            with open(os.path.join(transcript_directory, file.replace(".mp3", ".txt")), 'w') as f:
                # Write the text from the variable to the file
                f.write(result['text'])

            # Record the ending time
            end_time = time.time()

            # Calculate the elapsed time
            elapsed_time = end_time - start_time

            print("Elapsed time:", elapsed_time, "seconds, For file: ", file, 'Run: ', i)

if __name__ == "__main__":
    input_value = input("Would you like to trim the video content? Y/N: ")

    if input_value == 'Y': 
        trim = True
        transcribe_video(trim)
    elif input_value == 'N':
        trim = False
        transcribe_video(trim)
    else :
        print("Invalid input. Please enter 'Y' or 'N'.")

    
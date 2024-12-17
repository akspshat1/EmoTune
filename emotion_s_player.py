import os
import pygame
import random

def play_random_song(emotion):
    # Define the folders containing songs for each emotion
    emotion_folders = {
        "Angry": "songs\calm",
        "Happy": "songs\happy",
        "Surprise": "songs\surprise",
        "Fear": "songs\sad",
        "Sad": "songs\sad",
        "Neutral": "songs\calm",
        "Disgust": "songs\sad"

       
        # Add more emotions and corresponding folders as needed
    }
    
    # Check if the input emotion is in the defined emotions
    if emotion in emotion_folders:
        folder_path = emotion_folders[emotion]
        # Get a list of all song files in the folder
        song_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]
        if song_files:
            # Choose a random song from the folder
            song_name = random.choice(song_files)
            # Play the randomly selected song
            play_song(folder_path, song_name)
        else:
            print("No songs found for the specified emotion.")
    else:
        print("Emotion not supported.")

def play_song(folder_path, song_name):
    # Initialize pygame
    pygame.init()
    
    # Get the full path of the song
    song_path = os.path.join(folder_path, song_name)
    
    try:
        # Initialize the mixer module
        pygame.mixer.init()
        
        # Load the song
        sound = pygame.mixer.Sound(song_path)
        
        # Play the song
        sound.play()
        
        # Wait until the song finishes playing
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
        
        # Quit pygame
        pygame.quit()
        
    except pygame.error:
        print("Could not load or play the song.")

# Example usage
# emotion = "Sad"  # Replace this with the desired emotion
# play_random_song(emotion)

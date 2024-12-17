import os
import pygame

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
folder_path = r"C:\Users\rhyth\Downloads\CSL2050_CourseProject-main (1)"
song_name = "joy.mp3"
play_song(folder_path, song_name)

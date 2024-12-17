from rmn import RMN
import streamlit as st
import numpy as np
import cv2
from PIL import Image
from collections import Counter
import random
import os
import threading




model = RMN()


emotion_folders = {
    "angry": r"songs\calm",
    "happy": r"songs\happy",
    "surprise": r"songs\surprise",
    "sad": r"songs\sad",
    "calm": r"songs\calm",
}

emotion_css_files = {
        "happy": "happy.css",
        "sad": "sad.css",
        "calm":"calm.css",
        "angry":"angry.css",
        "surprise":"surprise.css"

}





def process_image(image):
    image = np.array(image)
    emotion = model.detect_emotion_for_single_frame(image)
    return emotion

def capture_face():
    capture_duration = 1  # Capture images for 5 seconds
    cap = cv2.VideoCapture(0)  # Open the camera (0 for default camera)

    images = []
    start_time = cv2.getTickCount()

    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            break

        # Convert the frame to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        images.append(Image.fromarray(rgb_frame))
        #st.image(rgb_frame, channels="RGB", use_column_width=True, caption="Camera Capture")
        # Check if capture duration is reached
        elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
        if elapsed_time >= capture_duration:
            break

    cap.release()  # Release the camera
    
    emotions = []
    for image in images:
        emotions.append(process_image(image))
    emotion_counts = Counter(emotions)
    most_common_emotion = emotion_counts.most_common(1)[0][0]
    
    return most_common_emotion



def main():
    st.title("EmoTune")
    # st.markdown("Tune Your Experience")
    st.markdown("Capture your emotion and enjoy music tailored to your mood.")
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

   
    curr_emo = None
    
    if st.button("Play"):
        with st.spinner("Detecting emotion..."):
            curr_emo = capture_face()
            
        st.write("Your Current emotion is:", curr_emo)
        if curr_emo in emotion_css_files:
            css_file = emotion_css_files[curr_emo]
            with open(css_file) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)      
        # Define path to your songs folder based on current emotion
        songs_emo = emotion_folders.get(curr_emo)  # Get the path based on current emotion
        if songs_emo is not None:
            random_num = np.random.randint(1, 3)
            song_filename = f"{random_num}.mp3"  # Assuming your songs are named like "song1.mp3", "song2.mp3", etc.
            song_path = os.path.join(songs_emo, song_filename)  # Joining the folder path with the random song filename
            st.audio(song_path, format="audio/mp3", loop=True)



if __name__ == "__main__":
    main()




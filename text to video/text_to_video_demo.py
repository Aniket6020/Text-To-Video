from gtts import gTTS
from moviepy.editor import *
from PIL import Image, ImageDraw

# Function to convert text to speech
def text_to_speech(text, output_audio_file):
    tts = gTTS(text)
    tts.save(output_audio_file)

# Function to create a simple avatar animation
def create_avatar_animation(output_image_file, duration=5):
    width, height = 720, 480
    frames = []
    
    # Create frames for the animation
    for i in range(duration * 10):  # 10 frames per second
        img = Image.new('RGB', (width, height), color=(73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10, 10), "Hello, I am your avatar!", fill=(255, 255, 0))
        frames.append(img)
    
    # Save frames as a GIF
    frames[0].save(output_image_file, save_all=True, append_images=frames[1:], duration=100, loop=0)

# Function to combine speech with avatar animation
def create_video_with_audio(text, output_video_file):
    # Convert text to speech
    output_audio_file = "output.mp3"
    text_to_speech(text, output_audio_file)
    
    # Create avatar animation
    output_image_file = "avatar.gif"
    create_avatar_animation(output_image_file)
    
    # Load audio and image
    audio = AudioFileClip(output_audio_file)
    video = VideoFileClip(output_image_file)
    
    # Set the duration of the video to match the audio
    video = video.set_duration(audio.duration)
    
    # Combine audio and video
    final_video = video.set_audio(audio)
    final_video.write_videofile(output_video_file, fps=10)

if __name__ == "__main__":
    text = "Welcome to the demo of text to video conversion with an avatar!"
    output_video_file = "output_video.mp4"
    create_video_with_audio(text, output_video_file)
    print(f"Video saved as {output_video_file}") 

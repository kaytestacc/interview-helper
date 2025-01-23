'''
import whisper

def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result["text"]
'''



import whisper
import os

def transcribe_audio(audio_file_path):
    """
    Transcribes the audio file to text using Whisper.

    :param audio_file_path: Path to the audio file to transcribe.
    :return: Transcribed text.
    """
    try:
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"File not found: {audio_file_path}")

        # Load the Whisper model
        model = whisper.load_model("base")

        # Transcribe the audio file
        result = model.transcribe(audio_file_path)

        # Return the text part of the transcription
        return result.get("text", "")
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    sample_audio_path = "sample_audio.wav"  # Replace with your audio file path
    transcription = transcribe_audio(sample_audio_path)
    print("Transcribed Text:", transcription)

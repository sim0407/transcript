import whisper

def main():
    #tiny, base, small, medium, largeの5つのモデルが用意されている
    model = whisper.load_model("medium")
    result = model.transcribe(r"audio_file.mp3")
    print(result["text"])


main()
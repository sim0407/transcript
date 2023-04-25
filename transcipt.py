import whisper

#TODO (必要であれば)入力ファイルの形式に合わせて変換を噛ませる
#TODO GPUを使用するようにする
#TODO printでなくtxtファイルとして出力する
#TODO 出力ファイルを、元ファイルの名前に応じたものにする
#TODO (未定)GUI化する

def main():
    audio_file_name = input('ファイル名を入力してください').replace('\"', '')
    #tiny, base, small, medium, largeの5つのモデルが用意されている
    model = whisper.load_model("large")
    result = model.transcribe(audio_file_name)
    print(result["text"])
    

main()
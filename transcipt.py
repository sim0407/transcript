import whisper

#TODO (必要であれば)入力ファイルの形式に合わせて変換を噛ませる
#TODO GPUを使用するようにする
#TODO printでなくtxtファイルとして出力する
#TODO 出力ファイルを、元ファイルの名前に応じたものにする
#TODO ファイル名をコード内でなく、プロンプトとして受け取る
#TODO (未定)GUI化する

def main():

    #tiny, base, small, medium, largeの5つのモデルが用意されている
    model = whisper.load_model("medium")
    result = model.transcribe(r"output.wav")
    print(result["text"])


main()
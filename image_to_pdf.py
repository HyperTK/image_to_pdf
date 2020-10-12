import img2pdf
from pathlib import Path

# 単処理


def ImageToPdf(outputpath, imagepath):
    '''
    outputpath: pathlib.Path()
    imagepath: pathlib.Path()
    '''
    lists = list(imagepath.glob("**/*"))  # 単フォルダ内を検索
    # pdfを作成
    with open(outputpath, "wb") as f:
        # jpg,pngファイルだけpdfに結合
        # Pathlib.WindowsPath()をstring型に変換しないとエラー
        f.write(img2pdf.convert(
            [str(i) for i in lists if i.match("*.jpg") or i.match("*.png")]))
    print(outputpath.name + " :Done")

# 複数フォルダをループ処理する


def main():
    # 入力フォルダ入力待ち
    in_folder = input('画像フォルダを指定してください: ')
    # 出力フォルダ入力待ち
    # out_folder = input('出力フォルダを指定してください: ')
    # 作業フォルダ
    base_path = in_folder
    # 作業フォルダ内のディレクトリだけを抽出する
    glob = Path(base_path).glob("*")
    imagelist = list([item for item in list(glob) if item])
    print(imagelist)
    # outputpathに指定ディレクトリと同名を指定する
    outputpathlist = list([item.with_suffix(".pdf")
                           for item in imagelist])
    print(outputpathlist)
    # ループ処理を行う
    for outputpath, imagepath in zip(outputpathlist, imagelist):
        try:
            ImageToPdf(outputpath, imagepath)
        except:
            pass


if __name__ == "__main__":
    main()

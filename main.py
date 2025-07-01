from PyPDF2 import PdfReader, PdfWriter

# 元のPDFファイル名
input_file = "【報告資料】松田ｽﾏｰﾄﾌｧｸﾄﾘｰ構想.pdf"   # 処理したいPDFファイルに置き換える

# 出力先ファイル名
output_file = "【報告資料】松田ｽﾏｰﾄﾌｧｸﾄﾘｰ構想_protected.pdf"

# 設定するパスワード
password = "XYZ"

# PDFを読み込む
reader = PdfReader(input_file)
writer = PdfWriter()

# 全ページをコピー
for page in reader.pages:
    writer.add_page(page)

# パスワードを設定
writer.encrypt(password)

# 出力
with open(output_file, "wb") as f:
    writer.write(f)

print("パスワード付きPDFを作成しました！")
print(f"出力ファイル: {output_file}")
print(f"パスワード: {password}")

#!/usr/bin/env python3
"""
セキュアなローカル版 PDF パスワード設定ツール
機密ファイルの処理にはこちらをご使用ください
"""

import os
import sys
import getpass
from PyPDF2 import PdfReader, PdfWriter

def secure_process_pdf():
    """セキュアなPDF処理（ローカル実行専用）"""
    
    print("🔒 PDF パスワード設定ツール (セキュア版)")
    print("=" * 50)
    
    # 入力ファイルの指定
    while True:
        input_file = input("処理するPDFファイルのパスを入力してください: ").strip()
        if os.path.exists(input_file) and input_file.lower().endswith('.pdf'):
            break
        print("❌ ファイルが見つからないか、PDFファイルではありません。")
    
    # パスワードの入力（非表示）
    password = getpass.getpass("設定するパスワードを入力してください（入力は非表示）: ")
    
    if not password:
        print("❌ パスワードが入力されていません。")
        return False
    
    # 出力ファイル名の生成
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_protected.pdf"
    
    try:
        print("📄 PDF処理中...")
        
        # PDFを読み込み
        with open(input_file, 'rb') as file:
            reader = PdfReader(file)
            writer = PdfWriter()
            
            # 全ページをコピー
            total_pages = len(reader.pages)
            for i, page in enumerate(reader.pages):
                writer.add_page(page)
                print(f"進捗: {i+1}/{total_pages} ページ")
            
            # パスワードを設定
            writer.encrypt(password)
            
            # 出力
            with open(output_file, 'wb') as output:
                writer.write(output)
        
        print("✅ 処理完了！")
        print(f"📁 出力ファイル: {output_file}")
        print("🔒 パスワードが設定されました。")
        
        # セキュリティ: 変数をクリア
        password = None
        del reader, writer
        
        return True
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {str(e)}")
        return False
    
    finally:
        # メモリクリーンアップ
        if 'password' in locals():
            password = None

def main():
    """メイン関数"""
    try:
        success = secure_process_pdf()
        if success:
            input("\n✨ 処理が完了しました。Enterキーを押して終了してください。")
        else:
            input("\n❌ 処理に失敗しました。Enterキーを押して終了してください。")
    except KeyboardInterrupt:
        print("\n\n⚠️  処理が中断されました。")
    except Exception as e:
        print(f"\n❌ 予期しないエラー: {str(e)}")

if __name__ == "__main__":
    main()

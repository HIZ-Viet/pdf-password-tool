import streamlit as st
import io
from PyPDF2 import PdfReader, PdfWriter
import os

def main():
    st.set_page_config(
        page_title="PDF パスワード設定アプリ",
        page_icon="🔒",
        layout="centered"
    )
    
    st.title("🔒 PDF パスワード設定アプリ")
    st.markdown("---")
    
    # サイドバーに説明
    with st.sidebar:
        st.header("📖 使い方")
        st.markdown("""
        1. PDFファイルをアップロード
        2. パスワードを入力
        3. 「パスワード付きPDFを作成」ボタンをクリック
        4. 作成されたPDFをダウンロード
        """)
        
        st.header("⚠️ 注意事項")
        st.markdown("""
        - アップロードされたファイルは処理後に自動削除されます
        - 強力なパスワードを設定することをお勧めします
        - 大きなファイルの処理には時間がかかる場合があります
        """)
    
    # メインエリア
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # ファイルアップロード
        uploaded_file = st.file_uploader(
            "PDFファイルを選択してください",
            type=['pdf'],
            help="処理したいPDFファイルをドラッグ&ドロップまたはクリックして選択"
        )
        
        # パスワード入力
        password = st.text_input(
            "設定するパスワード",
            type="password",
            help="PDFに設定するパスワードを入力してください"
        )
        
        # パスワード強度チェック
        if password:
            strength = check_password_strength(password)
            if strength == "弱い":
                st.warning("⚠️ パスワードが弱いです。より複雑なパスワードをお勧めします。")
            elif strength == "普通":
                st.info("💡 パスワード強度は普通です。")
            else:
                st.success("✅ 強力なパスワードです！")
    
    with col2:
        if uploaded_file and password:
            st.info("📋 ファイル情報")
            st.write(f"**ファイル名:** {uploaded_file.name}")
            st.write(f"**サイズ:** {uploaded_file.size:,} bytes")
    
    # 処理ボタン
    if st.button("🔒 パスワード付きPDFを作成", type="primary", use_container_width=True):
        if uploaded_file is None:
            st.error("❌ PDFファイルを選択してください")
        elif not password:
            st.error("❌ パスワードを入力してください")
        else:
            with st.spinner("📄 PDFを処理中..."):
                try:
                    # PDFを処理
                    result_pdf = process_pdf(uploaded_file, password)
                    
                    if result_pdf:
                        st.success("✅ パスワード付きPDFの作成が完了しました！")
                        
                        # ダウンロードボタン
                        original_name = os.path.splitext(uploaded_file.name)[0]
                        download_name = f"{original_name}_protected.pdf"
                        
                        st.download_button(
                            label="📥 パスワード付きPDFをダウンロード",
                            data=result_pdf,
                            file_name=download_name,
                            mime="application/pdf",
                            use_container_width=True
                        )
                        
                        st.balloons()  # お祝いアニメーション
                    else:
                        st.error("❌ PDF処理中にエラーが発生しました")
                        
                except Exception as e:
                    st.error(f"❌ エラーが発生しました: {str(e)}")

def process_pdf(uploaded_file, password):
    """PDFにパスワードを設定する処理"""
    try:
        # アップロードされたファイルを読み込み
        reader = PdfReader(uploaded_file)
        writer = PdfWriter()
        
        # プログレスバー
        progress_bar = st.progress(0)
        total_pages = len(reader.pages)
        
        # 全ページをコピー
        for i, page in enumerate(reader.pages):
            writer.add_page(page)
            progress_bar.progress((i + 1) / total_pages)
        
        # パスワードを設定
        writer.encrypt(password)
        
        # バイナリデータとして出力
        output_buffer = io.BytesIO()
        writer.write(output_buffer)
        output_buffer.seek(0)
        
        return output_buffer.getvalue()
        
    except Exception as e:
        st.error(f"PDF処理エラー: {str(e)}")
        return None

def check_password_strength(password):
    """パスワード強度をチェック"""
    if len(password) < 6:
        return "弱い"
    elif len(password) < 10:
        return "普通"
    else:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        if sum([has_upper, has_lower, has_digit, has_special]) >= 3:
            return "強い"
        else:
            return "普通"

if __name__ == "__main__":
    main()

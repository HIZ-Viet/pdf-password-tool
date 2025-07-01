# 🔒 PDF Password Tool

PDFファイルにパスワードを設定するシンプルなWebアプリケーションです。

## 🌟 特徴

- 📱 **使いやすいWebインターフェース** - Streamlitを使用した直感的なUI
- 🔒 **安全なパスワード設定** - PDFファイルに強力な暗号化を適用
- 💻 **ブラウザで動作** - インストール不要、どこからでもアクセス可能
- 🚀 **高速処理** - 効率的なPDF処理エンジン
- 📊 **パスワード強度チェック** - セキュリティレベルの可視化

## 🚀 ライブデモ

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)

## 📦 インストール

### 必要な環境
- Python 3.7以上
- pip

### ローカルでの実行

1. このリポジトリをクローン
```bash
git clone https://github.com/yourusername/pdf-password-tool.git
cd pdf-password-tool
```

2. 依存関係をインストール
```bash
pip install -r requirements.txt
```

3. アプリを起動
```bash
streamlit run app.py
```

4. ブラウザで `http://localhost:8501` にアクセス

## 🎯 使い方

1. **PDFファイルをアップロード** - 処理したいPDFファイルを選択
2. **パスワードを入力** - 設定したいパスワードを入力
3. **処理実行** - 「パスワード付きPDFを作成」ボタンをクリック
4. **ダウンロード** - 作成されたPDFファイルをダウンロード

## 📸 スクリーンショット

![アプリのスクリーンショット](docs/screenshots/app_screenshot.png)

## 🛠️ 技術スタック

- **Frontend**: Streamlit
- **Backend**: Python
- **PDF処理**: PyPDF2
- **デプロイ**: Streamlit Cloud

## 📁 プロジェクト構造

```
pdf-password-tool/
├── app.py                 # メインのStreamlitアプリ
├── main.py               # 元のCLIバージョン
├── requirements.txt      # 依存関係
├── README.md            # プロジェクト説明
├── .gitignore           # Git除外ファイル
└── docs/               # ドキュメント
    └── screenshots/    # スクリーンショット
```

## 🚀 Streamlit Cloudでのデプロイ

1. GitHubにプロジェクトをプッシュ
2. [Streamlit Cloud](https://streamlit.io/cloud)にアクセス
3. GitHubリポジトリを連携
4. `app.py`を指定してデプロイ

## 🤝 コントリビューション

プルリクエストやイシューの報告を歓迎します！

1. このリポジトリをフォーク
2. フィーチャーブランチを作成 (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット (`git commit -m 'Add some AmazingFeature'`)
4. ブランチにプッシュ (`git push origin feature/AmazingFeature`)
5. プルリクエストを開く

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご覧ください。

## 🙏 謝辞

- [Streamlit](https://streamlit.io/) - 素晴らしいWebアプリフレームワーク
- [PyPDF2](https://pypdf2.readthedocs.io/) - PDF処理ライブラリ

## 📞 お問い合わせ

プロジェクトについて質問がある場合は、イシューを作成してください。

---

⭐ このプロジェクトが役に立った場合は、スターをつけていただけると嬉しいです！

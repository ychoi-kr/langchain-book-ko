# LangChain Book
このリポジトリは書籍「[LangChain完全入門　生成AIアプリケーション開発がはかどる大規模言語モデルの操り方](https://book.impress.co.jp/books/1123101047)」で作成するソースコードです。


## 04_memoryのサンプルコードが正常に動作しない問題について
4章で使用しているチャット画面を作成するライブラリであるchainlitの破壊的アップデートの影響でサンプルコードが正常に動作しない問題が発生しています。

以下コマンドを実行することで、執筆時点のバージョンに下げて正常に動作せることができます。

```
python3 -m pip install chainlit==0.5.1
```

# rag-sample-practice


\[ ja / [en](./README_en.md) \]

本リポジトリは，Retrieval-Augmented Generation（RAG）の勉強・技術検証を目的としております．  
RAG に使用している [rules.json](./data/rules.json) の中身はフィクションであり，実在の企業・団体・人物とは一切関係ありません．

## 動作確認環境
* macOS
* Python 3.12
* CPU

## 使用モデル
* [Phi-3-mini-4k-instruct-q4.gguf](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf) by Microsoft  
    License: MIT
* [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)  
    License: Apache-2.0

## 使い方
### Linux/macOS
1. リポジトリ clone
    ```bash
    $ git clone git@github.com:k2-gc/rag-sample-practice.git
    $ cd rag-sample-practice
    ```
1. ライブラリインストール
    ```bash
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -U pip
    $ pip install -r requirements.txt
    ```
1. モデルダウンロード  
   `Phi-3-mini-4k-instruct-q4.gguf` をダウンロードし，[models](./models/) に格納する
1. ベクターデータベース作成
    ```bash
    $ python build_index.py
    ```

1. 質問  
    [query.py](./query.py#L34) あたりで質問の内容を変更して下記実行
    ```bash
    $ python query.py
    ```
    RAG あり/なし の結果が出力される

### Windows
1. リポジトリ clone
    ```cmd
    git clone git@github.com:k2-gc/rag-sample-practice.git
    cd rag-sample-practice
    ```
1. ライブラリインストール
    ```cmd
    python -m venv .venv
    .venv\Scripts\activate
    pip install -U pip
    pip install -r requirements.txt
    ```
1. モデルダウンロード  
   `Phi-3-mini-4k-instruct-q4.gguf` をダウンロードし，[models](./models/) に格納する

1. ベクターデータベース作成
    ```cmd
    python build_index.py
    ```

1. 質問  
    [query.py](./query.py#L34) あたりで質問の内容を変更して下記実行
    ```cmd
    python query.py
    ```
    RAG あり/なし の結果が出力される

## デモ結果
* 質問内容：社内規則に関して，朝の挨拶のルールを教えてください
* 回答:
    1. RAG なし
        ```text
        [INFO] [RAG なし] answer
        社内ルールに基づいて、朝の挨拶に関しては、以下のポリシーを掲示しています。

        - 朝の挨拶は、同僚との協調性を持って行ってください。
        - 尊敬を表する挨拶を優先し、プラットフォームやSNSでは適用されません。
        - 個々の文化や儀式に従い、挨拶に関しては尊重することを心がけてください。

        具体的な挨拶例は社内ルールの公式な文書に記載されている場合がありますので、そのリソースに確認してください。
        ```
    2. RAG あり
        ```text
        [INFO] [RAG あり] answer
        社内規則において、朝の挨拶に関するルールは次のとおりです。出社時には、3回のお辞儀をしてから席につくことです。
        ```

---

※ 本リポジトリは個人の学習・検証目的で作成されたものであり，Microsoft やその他の関係企業とは無関係です．
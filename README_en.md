# rag-sample-practice


\[ [ja](./README.md) / en \]

This repository is for practicing and experimenting with Retrieval-Augmented Generation (RAG).

The file [rules.json](./data/rules.json) contains fictional content. It has no relation to any real-world organizations, companies, or individuals.

## Verified Environment

* macOS
* Python 3.12
* CPU

## Models Used

* [Phi-3-mini-4k-instruct-q4.gguf](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf) by Microsoft  
  License: MIT
* [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)  
  License: Apache-2.0

## Usage
### Linux/macOS

1. Clone the repository
    ```bash
    $ git clone git@github.com:k2-gc/rag-sample-practice.git
    $ cd rag-sample-practice
    ```
1. Install libraries
    ```bash
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -U pip
    $ pip install -r requirements.txt
    ```
1. Download the model  
   Download `Phi-3-mini-4k-instruct-q4.gguf` and place it in the [models](./models/) directory.
1. Create the vector database
    ```bash
    $ python build_index.py
    ```

1. Run a query  
    Edit the query text around [query.py](./query.py#L34), then run:
    ```bash
    $ python query.py
    ```
    The output will be printed in Japanese.

### Windows

1. Clone the repository
    ```cmd
    git clone git@github.com:k2-gc/rag-sample-practice.git
    cd rag-sample-practice
    ```
1. Install libraries
    ```cmd
    python -m venv .venv
    .venv\bin\activate
    pip install -U pip
    pip install -r requirements.txt
    ```
1. Download the model  
   Download `Phi-3-mini-4k-instruct-q4.gguf` and place it in the [models](./models/) directory.
1. Create the vector database
    ```cmd
    python build_index.py
    ```

1. Run a query  
    Edit the query text around [query.py](./query.py#L34), then run:
    ```cmd
    python query.py
    ```
    The output will be printed in Japanese.

---

※ This repository is intended solely for personal learning and experimentation.  
It is not affiliated with Microsoft or any other organization.
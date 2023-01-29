FROM rust:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN pip3 install --upgrade \
    openai \
    openai[datalib] \
    transformers \
    tiktoken \
    python-dotenv \
    nltk

ENTRYPOINT []
import os
import openai
import pandas as pd
from transformers import GPT2TokenizerFast
from nltk.tokenize import sent_tokenize

from dotenv import load_dotenv
load_dotenv()
import nltk
nltk.download('punkt')

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
OPEN_API_KEY = os.environ.get("OPEN_API_KEY")

def get_embedding(text, model="text-embedding-ada-002"):
    openai.api_key = OPEN_API_KEY
    return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']


def count_tokens(text: str) -> int:
    """count the number of tokens in a string"""
    return len(tokenizer.encode(text))


def reduce_long(
    long_text: str, long_text_tokens: bool = False, max_len: int = 8191
) -> str:
    """
    Reduce a long text to a maximum of `max_len` tokens by potentially cutting at a sentence end
    """
    if not long_text_tokens:
        long_text_tokens = count_tokens(long_text)
    if long_text_tokens > max_len:
        sentences = sent_tokenize(long_text.replace("\n", " "))
        ntokens = 0
        for i, sentence in enumerate(sentences):
            ntokens += 1 + count_tokens(sentence)
            if ntokens > max_len:
                return ". ".join(sentences[:i][:-1]) + "."

    return long_text


def extract():
    # specify the file path
    file_path = 'data.csv'

    # read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Reduce content for any sections that are too long
    df['content'] = df.apply(lambda row: reduce_long(row.content), axis=1)

    # Add tokens column
    df['tokens'] = df.content.apply(lambda row: count_tokens(row))

    # Get embedding vector
    df['ada_embedding'] = df.content.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))


    # Save the output to a CSV and pickle
    df.to_csv('./out.csv', index=False)
    df.to_pickle('/out.pkl')


extract()

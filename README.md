# Embedding Machine 📠

Easily get the embedding vectors for text in a csv file 

 [OpenAI Embedding API Docs](https://beta.openai.com/docs/api-reference/embeddings)

## How to Use

1. Open the dev container
2. Replace `data.csv` with the your data

    **NOTE** column named *content* will be used to create embedding vector

3. Add your OpenAI API key to .env
4. `python3 main.py`

## Output

`tokens` - number of tokens in content cell (API limit = 8191 per request)

`ada_embedding` - embedding vector

### Notes

Some dependencies require Rust, so the dev container is based on `rust:latest`
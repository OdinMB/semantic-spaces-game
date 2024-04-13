# Semantic Spaces

Compare your semantic intuition to that of a modern AI language model.

Play online at https://semantics.fun.

## Screenshots

### Puzzle and options

![Puzzle and options](img/screen1.png)

### Results

![Results](img/screen2.png)

## Getting started

### Prerequisite

- Python 3.6 or newer

### Installation

Clone the repo

    git clone https://github.com/OdinMB/semantic-spaces-game.git

Navigate to the game's directory:

    cd semantic-spaces-game

Install the required Python packages:

    pip install -r requirements.txt

Launch the game

    streamlit run Game.py

## Creating new riddles

### Convention

Riddles are stored in the `riddles.json` file. For semantic pathway riddles, provide three terms as `keywords`.

"**Japan** is to **Germany** as **sushi** is to **\_\_\_\_\_**" is stored like this:

    "keywords": ["Japan", "Germany", "sushi"]

For semantic distance riddles, provide just one term for `keywords`.

"**Lame vacation** is closest to **\_\_\_\_\_**" is stored like this:

    "keywords": ["lame vacation"]

### Process

**Set up creation mode** (once)

1. Create an account at OpenAI (API access, not ChatGPT).
2. Create a `.env` file with this entry: `OPENAI_API_KEY=your-api-key`.
3. Create a `riddles_wip.json` file.

**Activate creation mode**

If the `riddles_wip.json` file exists and has at least one riddle defined, you have entered riddle creation mode. The game will now use this file over the default `riddles.json` file.

**Add a new riddle**

4. Enter a riddle into the `riddles_wip.json` file using the JSON structure from the `riddles.json` file.
5. Run the game to test your riddle (embeddings are created automatically).
6. Once you're happy with the result, copy the new riddle from `riddles_wip.json` to `riddles.json`.

**Wrap-up creation mode**

7. Delete all keywords, options, and tags from the `riddles_wip.json` file (or delete the file).
8. Run `python create_embeddings_openai.py` to update the embeddings database `riddles.npy` with the newly added riddles. Alternatively, you can answer one of the new riddles in game mode. (At that point, the missing embeddings are created automatically.)

## Deployment

Streamlit needs to be deployed in headless mode. Do one of these:

- Set environment variable `STREAMLIT_SERVER_HEADLESS=true`
- Use a parameter in the start command `streamlit run Game.py --server.headless true`

If you want the page to include HTML meta tags (description, OpenGraph and Twitter information), run the following command before starting the app: `python modify_index_html.py`. Depending on your hosting environment, you might have to combine this with the start command. `python modify_index_html.py && streamlit run Game.py --server.headless true`.

## License

"Semantic Spaces" by Odin Mühlenbein is published under a CC-BY 4.0 license.

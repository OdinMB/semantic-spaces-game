# Semantic Spaces

Dive into the depths of semantic pathways as perceived by cutting-edge AI.

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

Riddles are stored in the `riddles.txt` file, with one riddle in each line. For semantic pathway riddles, the first three terms of each line are the ones showing up in the riddle statement. The six following ones are the options that the player can choose from. Terms are separated by ';'.

"**Japan** is to **Germany** as **sushi** is to **\_\_\_\_\_**" is stored like this:

    Japan;Germany;sushi;bratwurst;schnitzel;beer;pretzel;marzipan;autobahn

For semantic distance riddles, leave the first two terms empty.

"**Lame vacation** is semantically closest to **\_\_\_\_\_**" is stored like this:

    ;;lame vacation;guided bus tour;cruise ship vacation;etc.

### Process

**Set up creation mode** (once)

1. Create a `.env` file with this entry: `OPENAI_API_KEY=your-api-key`.
2. Create a `riddles_wip.txt` file.

**Activate creation mode**

If the `riddles_wip.txt` file exists and is not empty, you have entered riddle creation mode. The game will now use this file over the default `riddles.txt` file.

**Add a new riddle**

3. Enter a riddle into the `riddles_wip.txt` file using the structure summarized above.
4. Run the game to test your riddle (embeddings are created automatically).
5. Once you're happy with the result, copy the new riddle from `riddles_wip.txt` to `riddles.txt`.

**Wrap-up creation mode**

8. Delete all content from the `riddles_wip.txt` file (or delete the file).
9. Run `python create_embeddings_openai.py` to update the embeddings database `riddles.npy` with the newly added riddles. Alternatively, you can answer one of the new riddles in game mode. (At that point, the missing embeddings are created automatically.)

## Deployment

Streamlit needs to be deployed in headless mode. Do one of these:

- Set environment variable `STREAMLIT_SERVER_HEADLESS=true`
- Use a parameter in the start command `streamlit run Game.py --server.headless true`

If you want the page to include HTML meta tags (description, OpenGraph and Twitter information), run the following command before starting the app:

    python modify_index_html.py

## License

"Semantic Spaces" by Odin Mühlenbein is published under a CC-BY 4.0 license.

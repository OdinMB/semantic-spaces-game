# Semantic Spaces

Online available at https://semantic-spaces.onrender.com/.
(Please allow for 50 seconds loading time. I'm using a free hosting service.)

Journey through the semantic world as it's mapped by AI language models. This interactive game challenges you to explore the nuanced connections between words, diving into the depths of semantic distance and direction as perceived by cutting-edge AI.

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

    cd semantic-puzzle-game

Install the required Python packages:

    pip install -r requirements.txt

Launch the game

    streamlit run app.py

### Deployment

Streamlit needs to be deployed in headless mode. Do one of these:

- Set environment variable `STREAMLIT_SERVER_HEADLESS=true`
- Use a parameter in the start command `streamlit run app.py --server.headless true`

## License

"Semantic Spaces" by Odin Mühlenbein is published under a CC-BY 4.0 license.

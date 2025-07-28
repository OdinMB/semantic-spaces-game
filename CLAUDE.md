# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Semantic Spaces is a Streamlit-based game that compares human semantic intuition to AI language model embeddings. Players solve riddles about semantic relationships and distances between words.

## Common Commands

### Running the Application
```bash
streamlit run Game.py
```

For deployment (headless mode):
```bash
streamlit run Game.py --server.headless true
```

### Setting up Riddle Creation Mode
1. Create `.env` file with `OPENAI_API_KEY=your-api-key`
2. Create `riddles_wip.json` file with at least one riddle
3. Run the game to test riddles (embeddings generated automatically)

### Generate/Update Embeddings
```bash
python create_embeddings_openai.py
```

### Prepare for Deployment with Meta Tags
```bash
python modify_index_html.py
```

Combined deployment command:
```bash
python modify_index_html.py && streamlit run Game.py --server.headless true
```

## Architecture Overview

### Core Game Flow
- **Game.py**: Main entry point, handles riddle selection, user interaction, and scoring
- **config.py**: Determines whether to use production (`riddles.json`) or development (`riddles_wip.json`) riddles

### Data Management
- **riddles.json**: Production riddle database
- **riddles_wip.json**: Development/testing riddles (activates creation mode when present)
- **riddles.npy**: Cached OpenAI embeddings for all riddle terms
- **groups.py**: Defines riddle groups (e.g., gender-jobs, race, religion) for sequential presentation
- **tags.py**: Tag definitions for riddle categorization and filtering

### Embedding System
- **create_embeddings_openai.py**: Generates text-embedding-ada-002 embeddings via OpenAI API
- **Game.py::get_embedding()**: Retrieves embeddings, auto-generates missing ones
- Uses cosine distance for semantic similarity calculations

### UI Components
- **visualization.py**: Creates interactive charts showing semantic distances
- **template.py**: Page layout and styling utilities
- **pages/**: Additional Streamlit pages for instructions and AI information

### Riddle Types
1. **Semantic Pathway**: "A is to B as C is to ____" (3 keywords)
2. **Semantic Distance**: "X is closest to ____" (1 keyword)

### State Management
Streamlit session state tracks:
- Current riddle and user choices
- Attempted riddles history
- Active group and sequence position
- Filter preferences (weird, bias, satirical tags)
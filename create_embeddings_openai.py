import json
import numpy as np
from langchain_openai import OpenAIEmbeddings
from tqdm import tqdm
import os
from dotenv import load_dotenv

load_dotenv()

embed_model = "text-embedding-ada-002"
embeddings_model = OpenAIEmbeddings(model=embed_model)

def get_embedding(text):
    """Obtain an embedding from GPT-3 Ada."""
    response = embeddings_model.embed_query(text.strip())
    return response

def generate_npy(file_name="riddles"):
    """Generate and update numpy embeddings file from JSON structured riddles, removing unneeded embeddings."""
    # Load or initialize the riddles embeddings dictionary
    try:
        embeddings_dict = np.load(f"{file_name}.npy", allow_pickle=True).item()
    except FileNotFoundError:
        embeddings_dict = {}

    # Load the riddles from JSON
    with open(f"{file_name}.json", "r") as file:
        riddles_data = json.load(file)["riddles"]

    # Collect all unique terms from keywords and options
    all_terms = set()
    for riddle in riddles_data:
        all_terms.update(riddle["keywords"])
        all_terms.update(riddle["options"])

    # Generate embeddings for terms not already in the dictionary
    for term in tqdm(all_terms, desc="Checking and generating embeddings"):
        if term not in embeddings_dict:
            embeddings_dict[term] = get_embedding(term)

    # Filter the embeddings_dict to keep only the embeddings needed
    embeddings_to_keep = {term: embeddings_dict[term] for term in all_terms if term in embeddings_dict}

    # Update the numpy file with filtered embeddings
    np.save(f"{file_name}.npy", embeddings_to_keep)

if __name__ == "__main__":
    generate_npy()

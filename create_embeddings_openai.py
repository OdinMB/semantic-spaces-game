import numpy as np
from langchain_openai import OpenAIEmbeddings
from tqdm import tqdm
from config import file_name

import os
from dotenv import load_dotenv
load_dotenv()

embed_model = "text-embedding-ada-002"
embeddings_model = OpenAIEmbeddings(model=embed_model)


# Function to obtain an embedding from GPT-3 Ada
def get_embedding(text):
    response = embeddings_model.embed_query(text.strip())
    return response

# Load or initialize the riddles embeddings dictionary
try:
    embeddings_dict = np.load(f"{file_name}.npy", allow_pickle=True).item()
except FileNotFoundError:
    embeddings_dict = {}

# Read the riddles and options, and split by ";"
with open(f"{file_name}.txt", "r") as file:
    lines = [line.strip().split(';') for line in file.read().strip().split('\n') if line]

# Flatten the list of terms and remove duplicates
all_terms = set(term.strip() for line in lines for term in line)

# Generate embeddings for terms not already in the dictionary
for term in tqdm(all_terms, desc="Checking and generating embeddings"):
    if term not in embeddings_dict:
        embeddings_dict[term] = get_embedding(term)

# Update the riddles.npy with new embeddings
np.save(f"{file_name}.npy", embeddings_dict)

# Identify the terms that are needed (used in the riddles)
needed_terms = set(term.strip() for line in lines for term in line)

# Remove any embeddings that are no longer needed
embeddings_to_keep = {term: embeddings_dict[term] for term in needed_terms}
np.save(f"{file_name}.npy", embeddings_to_keep)

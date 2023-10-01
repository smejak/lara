import faiss 
from typing import List
import numpy as np


class DBStore:
    
    def __init__(self, user_name) -> None:
        self.user_name = user_name
        self.index = self.build_index()
        

    def build_index(self, dimensionality:int = 1536):
        index = faiss.IndexFlatL2(dimensionality)   # build the index
        return index
    
    def add_embeddings_to_index(self, embeddings_matrix: np.ndarray):
        # here we assume xb contains a n-by-d numpy matrix of type float32
        self.index.add(embeddings_matrix) 
        
    def querry_index(self, query_vector: np.ndarray, k:int = 5):
        # xq is a n2-by-d matrix with query vectors
        D, I = self.index.search(query_vector, k)     # actual search
        return D, I

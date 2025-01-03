import pandas as pd
import numpy as np
from scipy.sparse import csc_matrix, lil_matrix

# The pagerank is a measeure of the probability to visit a web page by following random links indefinitly.
# We calculate it by creating a transition matrix (sparse matrix to ease the size of it) of the probabilities of going from one page to another.
# Then we multiply this matrix (100 times in our case) by a vector of the initial probabilities of visiting each page (which is 1/N for each page in our case).

# Load the data
edges = pd.read_csv('wikidata/edges.csv')
names = pd.read_csv('wikidata/names.csv')

def create_pagerank(edges : pd.DataFrame, names : pd.DataFrame, n_iter=100, s_c=1e-15):
    n_pages = names.shape[0] # Number of pages
    transition_matrix = lil_matrix((n_pages, n_pages)) # Create a sparse matrix of dimension n_pages x n_pages
    pagerank = np.ones(n_pages) / n_pages # Initial probabilities of visiting each page

    edge_counts = edges['FromNode'].value_counts().reindex(range(n_pages), fill_value=0) # Count the number of edges for each origin nodes

    for _, edge in edges.iterrows():
        originNode = edge.iloc[0] - 1 # Gets the origin node of the edge (column FromNode)
        targetNode = edge.iloc[1] - 1 # Gets the target node of the edge (column ToNode)

        if edge_counts[originNode] != 0:
            transition_matrix[originNode, targetNode] = 1 / edge_counts[originNode]

    transition_matrix = transition_matrix.tocsc()  # Convert to csc_matrix for efficiency

    for i in range(n_iter):
        pagerank = pagerank * transition_matrix
        if np.any(pagerank <= s_c):
            print(f"Stopping early at iteration {i+1} due to convergence criterion.")
            break

    return pagerank

pagerank = create_pagerank(edges, names)

top_10_indices = np.argsort(pagerank)[-10:][::-1]
top_10_probabilities = pagerank[top_10_indices]
top_10_names = names.iloc[top_10_indices, 0]

for i in range(10):
    print(f"Page: {top_10_names.iloc[i]}, Probability: {top_10_probabilities[i]:.6f}")

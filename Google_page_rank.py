import pandas as pd
from scipy.sparse import coo_matrix, csr_matrix
import numpy as np
import time

 # 1) construct the transition matric X  (= T)
 # 2) calculate p->(k+1) = Tp(k)
 # 3) for k sufficiently large => p->(inf) = p->(k)
 
begin_time = time.time()
edges = pd.read_csv('wikidata/edges.csv')
names = pd.read_csv('wikidata/names.csv')

print("milliseconds to read csv : ", time.time() - begin_time)

def google_page_rank(edges: pd.DataFrame, names: pd.DataFrame, iterations=100, s_c=1e-15):
    num_nodes = names.shape[0]
    
    # Adjust indices to 0-based
    from_nodes = edges['FromNode'].to_numpy() - 1
    to_nodes = edges['ToNode'].to_numpy() - 1
    
    # Calculate out-degrees using numpy
    out_degrees = np.bincount(from_nodes, minlength=num_nodes)
    
    # Create weights array (1/out_degree for each edge)
    weights = np.divide(1, out_degrees[from_nodes], where=out_degrees[from_nodes]!=0)
    
    # Create transition matrix directly
    T = csr_matrix((weights, (from_nodes, to_nodes)), shape=(num_nodes, num_nodes))
    
    # Power iteration
    p = np.ones(num_nodes) / num_nodes
    for i in range(iterations):
        p = p @ T
        if np.any((p > 0) & (p <= s_c)):
            print(f"Stopping early at iteration {i+1} due to convergence criterion.")
            break
    
    top_10_indices = np.argsort(p)[-10:][::-1]
    return pd.DataFrame({
        'Page': names.iloc[top_10_indices, 0],
        'Probability': p[top_10_indices]
    })

print(google_page_rank(edges, names).head(10))  # Display the top 10 pages
print("milliseconds to execute algorithm : ", time.time() - begin_time)
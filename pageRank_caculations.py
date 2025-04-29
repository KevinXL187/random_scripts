import numpy as np
import networkx as nx

def pageRank():
    # Define the stochastic matrix M
    M = np.array([
    [0, 0.5, 0.5, 1],   # A receives from B, C, D
    [1, 0, 0, 0],        # B receives from A
    [0, 0.5, 0, 0],      # C receives from B
    [0, 0, 0.5, 0]       # D receives from C
]) 
     
    # Initialize the rank vector r0
    r = np.array([1, 1, 1, 1])

    # Set the convergence threshold
    threshold = 1e-3

    # Initialize iteration counter
    iterations = 0

    # Iterative process
    while True:
        r_next = M @ r  # Matrix multiplication: r_next = M * r
        iterations += 1

        print(f"Iteration {iterations}: r = {r_next}")

        # Check for convergence
        if np.linalg.norm(r_next - r) < threshold:
            break

        # Update r for the next iteration
        r = r_next

    # Print the results
    print(f"Converged in {iterations} iterations.")
    print(f"Final rank vector: {r}")
    
def pageRank2():
    # Define the stochastic matrix M
    M = np.array([
    [0, 0.5, 0.5, 1],   # A receives from B, C, D
    [1, 0, 0, 0],        # B receives from A
    [0, 0.5, 0, 0],      # C receives from B
    [0, 0, 0.5, 0]       # D receives from C
]) 
    assert np.allclose(M.sum(axis=0), 1.0), "Transition matrix must be column-stochastic!"
    # Initialize the rank vector r0
    r = np.array([1, 1, 1, 1])
    r = r / r.sum()
    # Set the convergence threshold
    threshold = 1e-3

    # Initialize iteration counter
    iterations = 0

    # Iterative process
    while True:
        r_prev = r.copy()
        r = M @ r  # Matrix multiplication: r = M * r
        r = r / r.sum()  # Normalize to prevent overflow
        iterations += 1

        # Optional: Print intermediate results
        print(f"Iteration {iterations}: r = {r}")

        # Check for convergence
        if np.linalg.norm(r - r_prev) < threshold:
            break

    # Print the results
    print(f"Converged in {iterations} iterations.")
    print(f"Final rank vector: {r}")

def dampedPageRank():
    # Define the stochastic matrix M
    M = np.array([
        [0, 0, 1, 0],
        [1/2, 0, 0, 0],
        [1/2, 1, 0, 1],
        [0, 0, 0, 0]]) 
    # Define the constant vector c
    c = np.array([0.1, 0.1, 0.1, 0.1])

    # Initialize the rank vector r0
    r = np.array([1, 1, 1, 1])

    # Set the convergence threshold
    threshold = 1e-3

    # Initialize iteration counter
    iterations = 0

    # Iterative process
    while True:
        r_next = 0.9 * (M @ r) + c  # Update formula: r = 0.9 * M * r + c
        iterations += 1

        # Print the current iteration and rank vector
        print(f"Iteration {iterations}: r = {r_next}")

        # Check for convergence
        if np.linalg.norm(r_next - r) < threshold:
            break

        # Update r for the next iteration
        r = r_next

    # Print the final results
    print(f"\nConverged in {iterations} iterations.")
    print(f"Final rank vector: {r}")

def hits_algorithm():
    # Define the web pages and their links
    #pages = ["A", "B", "C", "D"]
    links = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "A"), ("D", "C")]

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes (web pages)
    #G.add_nodes_from(pages)

    # Add edges (links between pages)
    G.add_edges_from(links)

    # Compute hub and authority scores using the HITS algorithm
    hub_scores, authority_scores = nx.hits(G, normalized = True)

    # Print the results
    print("Hub Scores:")
    for page, score in hub_scores.items():
        print(f"{page}: {score:.4f}")
    print("\nAuthority Scores:")
    for page, score in authority_scores.items():
        print(f"{page}: {score:.4f}")

if __name__ == "__main__":
    pageRank()
    pageRank2()
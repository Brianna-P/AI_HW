# Problem: Implement the Breadth-First Search (BFS), Depth-First Search (DFS) 
# and Greedy Best-First Search (GBFS) algorithms on the graph from Figure 1 in hw1.pdf.


# Instructions:
# 1. Represent the graph from Figure 1 in any format (e.g. adjacency matrix, adjacency list).
# 2. Each function should take in the starting node as a string. Assume the search is being performed on
#    the graph from Figure 1.
#    It should return a list of all node labels (strings) that were expanded in the order they where expanded.
#    If there is a tie for which node is expanded next, expand the one that comes first in the alphabet.
# 3. You should only modify the graph representation and the function body below where indicated.
# 4. Do not modify the function signature or provided test cases. You may add helper functions. 
# 5. Upload the completed homework to Gradescope, it must be named 'hw1.py'.

# Examples:
#     The test cases below call each search function on node 'S' and node 'A'
# -----------------------------

adj_list = {"A": ["B", "E"], "B": ["A", "C", "F"], "C": ["B", "H", "S"], "D": ["L", "S"], "E": ["A", "F", "I"],
    "F": ["B", "E", "J", "K"], "G": ["M", "N", "Q"], "H": ["C", "K", "L"], "I": ["E", "J", "M"], "J": ["F", "I", "K", "N"],
    "K": ["F", "H", "J", "L", "P"], "L": ["D", "Q", "H", "K"], "M": ["G", "I"], "N": ["J", "G", "P"], "P": ["K", "N"], 
    "Q": ["L", "G"], "S": ["C", "D"]}

h = {"S": 17, "A": 10, "B": 9, "C": 16, "D":21, "E":13, "F": 9, "G": 0, "H": 12, "I": 9, "J":5, "K": 8, "L": 18, "M": 3, "N": 4, "P": 6, "Q": 9}

def BFS(start: str) -> list:
    visited = []
    queue = [start]
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            visited.append(curr)
            if curr == "G":
                print(visited)
                return visited
            curr_neighbors = sorted(adj_list[curr])
            for neighbor in curr_neighbors:
                if neighbor not in visited and neighbor not in queue:
                    #print(neighbor)
                    queue.append(neighbor)
                    if neighbor == 'G':
                        visited.append("G")
                        return visited
    print(visited)
    return visited
    # END: Your code here


def DFS(start: str) -> list:
    # START: Your code here
    visited = []
    stack = [start]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            curr_neighbors = adj_list[curr]
            sorted_curr_neighbors = sorted(curr_neighbors, reverse=True)
            for neighbor in sorted_curr_neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    if neighbor == 'G':
                        visited.append("G")
                        return visited
    return visited
    # END: Your code here


def GBFS(start: str) -> list:
    visited = []
    priority_queue = [(h[start], start)]
    while priority_queue:
        priority_queue.sort()
        curr = priority_queue.pop(0)[1]
        if curr not in visited:
            visited.append(curr)
            curr_neighbors = adj_list[curr]
            for neighbor in curr_neighbors:
                if neighbor not in visited:
                    priority_queue.append((h[neighbor], neighbor))
                    if neighbor == 'G':
                        visited.append("G")
                        return visited
    return visited
    # END: Your code here



# test cases - DO NOT MODIFY THESE
def run_tests():
    # Test case 1: BFS starting from node 'A'
    assert BFS('A') == ['A', 'B', 'E', 'C', 'F', 'I', 'H', 'S', 'J', 'K', 'M', 'G'], "Test case 1 failed"
    
    # Test case 2: BFS starting from node 'S'
    assert BFS('S') == ['S', 'C', 'D', 'B', 'H', 'L', 'A', 'F', 'K', 'Q', 'G'], "Test case 2 failed"

    # Test case 3: DFS starting from node 'A'
    assert DFS('A') == ['A', 'B', 'C', 'H', 'K', 'F', 'E', 'I', 'J', 'N', 'G'], "Test case 3 failed"
    
    # Test case 4: DFS starting from node 'S'
    assert DFS('S') == ['S', 'C', 'B', 'A', 'E', 'F', 'J', 'I', 'M', 'G'], "Test case 4 failed"

    # Test case 5: GBFS starting from node 'A'
    assert GBFS('A') == ['A', 'B', 'F', 'J', 'N', 'G'], "Test case 5 failed"
    
    # Test case 6: GBFS starting from node 'S'
    assert GBFS('S') == ['S', 'C', 'B', 'F', 'J', 'N', 'G'], "Test case 6 failed"

    
    
    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()

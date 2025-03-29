# **Depth-First Search (DFS) Explained in Detail**

## **1. What is Depth-First Search (DFS)?**
DFS (**Depth-First Search**) is a **graph traversal algorithm** used to explore nodes and edges **deeply** before backtracking. It is widely used in **trees** and **graphs** to solve various problems such as **pathfinding, connected components, and cycle detection**.

### **Key Characteristics of DFS**
- **Goes deep first**: It explores a branch of a tree or graph completely before backtracking.
- **Uses recursion or a stack** to remember nodes that need to be processed.
- **Time Complexity**: **O(V + E)** (where `V` = vertices, `E` = edges).
- **Space Complexity**:
  - **O(H)** in a tree (where `H` is the height).
  - **O(V)** in a graph (in worst case, if all nodes are visited).

---

## **2. How DFS Works?**
### **Step-by-Step DFS Traversal**
1. **Start from the root (or any starting node).**
2. **Visit the node** and mark it as **visited**.
3. **Move to the next unvisited adjacent node** (go left in a tree).
4. **Repeat until no more unvisited nodes exist**.
5. **Backtrack** and explore other unvisited nodes.

---

## **3. DFS Variants**
DFS can be implemented in two ways:
1. **Recursive (Using function calls)**
2. **Iterative (Using an explicit stack)**

---

## **4. DFS Example in a Binary Tree**
### **Binary Tree**
```
        1
       / \
      2   3
     / \   \
    4   5   6
```

### **DFS Traversal Orders**
1. **Preorder (Root → Left → Right)**  
   - **Output:** `[1, 2, 4, 5, 3, 6]`
2. **Inorder (Left → Root → Right)**  
   - **Output:** `[4, 2, 5, 1, 3, 6]`
3. **Postorder (Left → Right → Root)**  
   - **Output:** `[4, 5, 2, 6, 3, 1]`

---

## **5. Recursive DFS Implementation**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_recursive(root):
    if not root:
        return
    
    print(root.val, end=" ")  # Process the node (Preorder)
    dfs_recursive(root.left)  # Visit left subtree
    dfs_recursive(root.right) # Visit right subtree

# Example Tree
root = TreeNode(1, 
                TreeNode(2, TreeNode(4), TreeNode(5)), 
                TreeNode(3, None, TreeNode(6)))

dfs_recursive(root)  # Output: 1 2 4 5 3 6
```

### **Explanation**
1. Start at **root (1)** → Print `1`
2. Move to **left child (2)** → Print `2`
3. Move to **left child (4)** → Print `4`
4. **Backtrack to 2**, move to **right child (5)** → Print `5`
5. **Backtrack to 1**, move to **right child (3)** → Print `3`
6. Move to **right child (6)** → Print `6`
7. **DFS traversal completed**

---

## **6. Iterative DFS using a Stack**
Instead of recursion, we use a **stack** to keep track of nodes.

```python
def dfs_iterative(root):
    if not root:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")  # Process node

        # Push right child first so that left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Example Tree
dfs_iterative(root)  # Output: 1 2 4 5 3 6
```

### **Why Push Right Child First?**
- **Stacks are LIFO (Last-In, First-Out)**.
- By pushing the **right child first**, the **left child is processed first**, maintaining **preorder traversal**.

---

## **7. DFS in Graphs**
DFS can also be used in graphs. Unlike trees, graphs may have **cycles**, so we need a **visited set** to avoid infinite loops.

### **Example Graph**
```
    1
   / \
  2   3
 / \
4   5
```

### **Adjacency List Representation**
```python
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}
```

### **Recursive DFS for Graph**
```python
def dfs_graph(node, graph, visited):
    if node in visited:
        return
    
    print(node, end=" ")  # Process node
    visited.add(node)  # Mark as visited
    
    for neighbor in graph[node]:
        dfs_graph(neighbor, graph, visited)

visited = set()
dfs_graph(1, graph, visited)  # Output: 1 2 4 5 3
```

### **Iterative DFS for Graph**
```python
def dfs_graph_iterative(start, graph):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process node
            visited.add(node)
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

dfs_graph_iterative(1, graph)  # Output: 1 2 4 5 3
```

---

## **8. Applications of DFS**
1. **Tree Traversals** (Preorder, Inorder, Postorder)
2. **Pathfinding** (Maze solving, Google Maps)
3. **Detecting Cycles** in a Graph
4. **Connected Components** in a Graph
5. **Topological Sorting** in DAG (Directed Acyclic Graph)
6. **Solving Puzzles** (Sudoku, Word Search)

---

## **9. DFS vs BFS**
| Feature          | DFS                              | BFS                              |
|-----------------|---------------------------------|---------------------------------|
| Traversal Style | Deep-first (Explore a path)    | Breadth-first (Level by Level) |
| Data Structure  | Stack (Recursion or Explicit)  | Queue                           |
| Memory Usage    | O(H) (Tree), O(V) (Graph)      | O(V) (Can be larger)           |
| Best for       | Solving mazes, backtracking    | Shortest Path (Dijkstra, A*)   |

---

## **10. Summary**
✅ DFS explores **deep before backtracking**  
✅ It can be **recursive (implicit stack)** or **iterative (explicit stack)**  
✅ Used in **trees, graphs, puzzles, and pathfinding**  
✅ Works in **O(V + E) time complexity**  
✅ DFS is different from BFS, which explores **level by level**  

---

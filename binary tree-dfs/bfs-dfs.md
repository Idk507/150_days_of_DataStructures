### **Understanding Binary Tree DFS Through Example Problems (LeetCode)**  

Instead of just focusing on code, let’s **deeply understand the logic** behind how DFS is applied to binary tree problems. I will break down problems step by step so that you can grasp **how DFS works conceptually**.

---

## **Example 1: Maximum Depth of Binary Tree (LeetCode 104)**  
### **Problem Statement**  
Given a binary tree, find its **maximum depth**.  
- The maximum depth is the number of nodes along the **longest path** from the root to a leaf.

### **Example Input**
```
        3
       / \
      9   20
         /  \
        15   7
```
### **Expected Output**  
```
Max Depth: 3
```

---

### **Understanding the Problem**
DFS helps us traverse **deep into the tree** before backtracking.  
To find the **maximum depth**, we need to explore **both left and right subtrees** and return the **maximum depth of either subtree** + 1 (for the root).

---

### **Step-by-Step Thought Process**
1. Start at the root (`3`).
2. Go **left** to `9`. It has no children, so its depth is `1`.
3. Go **right** to `20`.
   - Go **left** to `15` (Depth = 1).
   - Go **right** to `7` (Depth = 1).
   - Since both subtrees of `20` have depth `1`, the depth of `20` is `1 + max(1,1) = 2`.
4. Finally, for root `3`: `1 + max(1, 2) = 3`.

---

### **Logical Formula**
For any node:
\[
\text{Depth} = 1 + \max(\text{Depth of Left Subtree}, \text{Depth of Right Subtree})
\]

---

### **Final Depth Calculation**
```
Depth(9)  = 1
Depth(15) = 1
Depth(7)  = 1
Depth(20) = 1 + max(1, 1) = 2
Depth(3)  = 1 + max(1, 2) = 3
```
**Final Answer: `3`**

---

## **Example 2: Path Sum (LeetCode 112)**  
### **Problem Statement**  
Given a binary tree and a sum `targetSum`, determine if the tree **has a root-to-leaf path** such that adding up all values along the path equals `targetSum`.

### **Example Input**
```
        5
       / \
      4   8
     /   / \
    11  13  4
   /  \
  7    2
```
Target Sum = `22`

### **Expected Output**  
```
True (Path: 5 → 4 → 11 → 2)
```

---

### **Understanding the Problem**
- We need to **find a path from root to leaf** where the sum of node values equals `22`.
- We use **DFS** to explore **each path down to the leaf**.
- As we traverse, we subtract the node value from `targetSum`.
- If we reach a **leaf node** and the remaining sum is `0`, we return `True`.

---

### **Step-by-Step Thought Process**
1. Start at `5` → Remaining sum = `22 - 5 = 17`.
2. Go **left** to `4` → Remaining sum = `17 - 4 = 13`.
3. Go **left** to `11` → Remaining sum = `13 - 11 = 2`.
4. Go **left** to `7` → Remaining sum = `2 - 7 = -5` (**not a valid path**).
5. Backtrack and go **right** to `2` → Remaining sum = `2 - 2 = 0` (**Valid path found!**).

---

### **Logical Formula**
For each node:
- **Remaining sum = targetSum - node value**.
- If we reach a **leaf node** and `remainingSum == 0`, return `True`.

---

### **Final Answer**
```
Path Found: 5 → 4 → 11 → 2 (Sum = 22)
Return: True
```

---

## **Example 3: Lowest Common Ancestor (LCA) of a Binary Tree (LeetCode 236)**  
### **Problem Statement**  
Given a binary tree and two nodes, **find the lowest common ancestor (LCA)**.  
The **LCA** is the **lowest** node in the tree that has both nodes as descendants.

### **Example Input**
```
        3
       / \
      5   1
     / \  / \
    6   2 0  8
       / \
      7   4
```
Find **LCA of `5` and `1`**.

### **Expected Output**  
```
LCA = 3
```

---

### **Understanding the Problem**
- **LCA of two nodes** is the deepest node that **has both nodes in its left or right subtree**.
- If a node **itself** is one of the targets, it could be an LCA.
- DFS helps in searching both **left and right** subtrees to find the **first node** where both nodes are present.

---

### **Step-by-Step Thought Process**
1. Start at `3`.  
   - `5` is in the **left** subtree.
   - `1` is in the **right** subtree.
   - Since they are in different subtrees, `3` is the **LCA**.
   
2. If the nodes were **both on the left or right**, we would continue searching.

---

### **Logical Formula**
- If **both nodes** are found in **left and right** subtrees, the current node is **LCA**.
- If **one node is found** (but not both), return that node.

---

### **Final Answer**
```
LCA(5,1) = 3
```

---

## **Key Takeaways**
| Problem               | Goal                                  | DFS Role |
|----------------------|--------------------------------|----------|
| **Max Depth (104)** | Find the longest path to a leaf | Go deep and return max depth |
| **Path Sum (112)** | Check if any root-to-leaf path matches a sum | Explore paths, backtrack when needed |
| **LCA (236)** | Find the lowest common ancestor of two nodes | Search left and right subtrees |

---

## **Final Thoughts**
- **DFS is essential** when dealing with tree problems that require exploring paths or deep relationships.
- **Understanding recursion** and **backtracking** is key to solving DFS-based tree problems.
- **Always break problems down** into **small recursive steps**.


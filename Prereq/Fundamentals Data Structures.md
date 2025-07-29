Absolutely! Let’s now explore **Stack vs Heap memory** and **Time & Space Complexity** in the **context of Data Structures**, with examples:

---

## 📌 1. Stack vs Heap Memory in Data Structures

### 🔷 Stack Memory

* **Used for**: Storing **function calls**, **local variables**, and **temporary data structures**.
* **Data Structures typically using Stack memory**:

  * **Primitive variables** inside functions (`int`, `float`, etc.)
  * **Recursive function calls** (each call gets its own frame on the stack)
  * **Explicit Stack Data Structure** (e.g., for DFS traversal)

#### 📌 Example:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

* Each call to `factorial()` creates a new **stack frame**.
* Too deep recursion → **Stack Overflow**.

---

### 🔷 Heap Memory

* **Used for**: Dynamic memory allocation — objects, lists, trees, graphs, etc.
* **Data Structures typically using Heap memory**:

  * **Linked Lists** – each node is dynamically created
  * **Trees** – nodes are allocated on heap
  * **Graphs** – nodes and adjacency lists stored in heap
  * **Dynamic Arrays / Lists** (e.g., Python’s `list`, Java’s `ArrayList`)
  * **Priority Queue (Heap data structure)**

#### 📌 Example:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)  # Heap allocated
```

* `Node` objects live in **heap memory**.

---

## 📌 2. Time and Space Complexity in Data Structures

### 🔹 Arrays / Lists

| Operation           | Time Complexity | Space Complexity |
| ------------------- | --------------- | ---------------- |
| Access              | O(1)            | O(n)             |
| Search (unsorted)   | O(n)            | O(1)             |
| Insert/Delete (end) | O(1)            | O(n)             |
| Insert/Delete (mid) | O(n)            | O(n)             |

### 🔹 Stack (LIFO)

| Operation  | Time | Space |
| ---------- | ---- | ----- |
| Push / Pop | O(1) | O(n)  |
| Peek / Top | O(1) | O(n)  |

* Uses stack memory when implemented via recursion.

### 🔹 Queue (FIFO)

| Operation         | Time | Space |
| ----------------- | ---- | ----- |
| Enqueue / Dequeue | O(1) | O(n)  |

### 🔹 Linked List

| Operation     | Time                     | Space |
| ------------- | ------------------------ | ----- |
| Insert/Delete | O(1) (head) / O(n) (pos) | O(n)  |
| Search        | O(n)                     | O(n)  |

* Each node is **heap-allocated**, with pointer/reference.

### 🔹 Binary Tree / BST

| Operation (avg)      | Time     | Space |
| -------------------- | -------- | ----- |
| Search/Insert/Delete | O(log n) | O(n)  |
| Worst-case (skewed)  | O(n)     | O(n)  |

* Recursive traversal uses **stack memory**.
* Tree structure is in **heap**.

### 🔹 Hash Table / Dict

| Operation     | Time (avg) | Time (worst) | Space |
| ------------- | ---------- | ------------ | ----- |
| Insert/Search | O(1)       | O(n)         | O(n)  |

* Collisions may cause linear time in worst case (with chaining).

### 🔹 Heap (as a DS)

| Operation       | Time     | Space |
| --------------- | -------- | ----- |
| Insert          | O(log n) | O(n)  |
| Extract-Min/Max | O(log n) | O(n)  |

* Binary Heap uses **array representation** (backed by heap memory).
* Useful for Priority Queues.

---

## 📌 Summary Table: Stack vs Heap in DS Terms

| Concept       | Stack                           | Heap                       |
| ------------- | ------------------------------- | -------------------------- |
| Lifetime      | Tied to function scope          | Manual or GC managed       |
| DS Examples   | Stack, recursion                | Linked List, Trees, Graphs |
| Speed         | Very fast (LIFO)                | Slower (more flexible)     |
| Overflow Risk | Stack Overflow (deep recursion) | Memory Leak (if not freed) |

---

<img width="1453" height="767" alt="image" src="https://github.com/user-attachments/assets/fafb77ad-2c2b-42ca-b410-cac658a89612" />

<img width="1154" height="652" alt="image" src="https://github.com/user-attachments/assets/f69f33b0-84c9-46ca-beb4-aa449cfe0d77" />
<img width="841" height="605" alt="image" src="https://github.com/user-attachments/assets/e7ff549d-3ecb-4f82-ba0b-bf2d7829e3a8" />


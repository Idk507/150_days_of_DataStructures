

---

### 🧠 **What is the Brute Force Approach?**

A **brute force algorithm** solves a problem by:
- Generating all possible candidates for the solution.
- Checking whether each candidate satisfies the problem’s conditions.
- Returning the first valid solution (or the best one, depending on the task).

---

### 💡 **Key Characteristics**
- ✅ Simple and easy to implement.
- ❌ Not efficient for large input sizes (time complexity can be exponential or factorial).
- 🛠️ Often used as a **baseline** or for small input cases.

---

### 📌 **Example 1: Linear Search**
Let’s say you want to find if a number `x` exists in an array.

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```

This checks **each element** in the array — that's brute force.

---

### 📌 **Example 2: String Matching**
To check if a pattern `P` exists in a string `S`:

- Try matching `P` starting at every position in `S`.
- Compare characters one by one.

This has a time complexity of O(n * m), where `n` is the length of `S` and `m` is the length of `P`.

---

### 📌 **Example 3: Combinations / Permutations**
If you want to find all permutations of a string:

```python
from itertools import permutations

s = "abc"
perm = list(permutations(s))
print(perm)
```

It generates **all possible permutations**, checks for the desired one — that's brute force.

---

### 🧮 **Time Complexity**
- Usually **very high** — often **O(n!)**, **O(2ⁿ)**, or **O(n²)**.
- Acceptable only for small inputs or when no better approach is known.

---

### ✅ **When to Use Brute Force**
- Input size is small.
- You’re trying to get a working solution first before optimizing.
- You’re verifying the correctness of an optimized solution.
- Problem guarantees allow brute force within time limits.



### 📚 What is a Permutation?

A **permutation** is an **arrangement of all elements** of a set in **every possible order**.

Example:
- For a set `{1, 2, 3}`, the permutations are:  
  `[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]`

- For `n` unique elements, the number of permutations = `n!` (n factorial)

---

### 🛠️ Use Cases in DSA
1. **Generate all permutations of a string/array**
2. **Backtracking problems** (e.g., N-Queens, Sudoku)
3. **Traveling Salesman Problem (TSP)**
4. **Solving puzzles** (like 8-puzzle, Rubik's cube logic)
5. **Password generation / brute force attack simulation**
6. **Finding next lexicographical permutation**

---

## ✅ 1. **Using Built-in Library – Python’s `itertools.permutations`**
```python
from itertools import permutations

arr = [1, 2, 3]
perms = list(permutations(arr))
print(perms)
```

- Easy and efficient for quick tasks.
- Returns all `n!` permutations as tuples.

---

## ✅ 2. **Recursive Approach (DFS Style)**
```python
def permute(arr):
    result = []
    
    def dfs(path, used):
        if len(path) == len(arr):
            result.append(path[:])
            return
        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                dfs(path + [arr[i]], used)
                used[i] = False
    
    dfs([], [False]*len(arr))
    return result

print(permute([1, 2, 3]))
```

- Good for understanding recursion and backtracking.
- Space: O(n), Time: O(n!)

---

## ✅ 3. **Backtracking Approach**
```python
def backtrack(start, arr, res):
    if start == len(arr):
        res.append(arr[:])
    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        backtrack(start + 1, arr, res)
        arr[start], arr[i] = arr[i], arr[start]

res = []
arr = [1, 2, 3]
backtrack(0, arr, res)
print(res)
```

- In-place swap technique
- Efficient for generating permutations without extra space

---

## 🔄 Next Lexicographical Permutation
Used in problems like **Leetcode 31: Next Permutation**
```python
def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = reversed(nums[i+1:])
    return nums
```

---

## 🔥 DSA Problems That Use Permutations

| Problem | Platform | Concept |
|--------|----------|--------|
| [Permutations](https://leetcode.com/problems/permutations/) | Leetcode | Basic recursion/backtracking |
| [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) | Leetcode | k-th permutation using factorials |
| [Next Permutation](https://leetcode.com/problems/next-permutation/) | Leetcode | Lexicographical next |
| [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) | Leetcode | BFS + backtracking with permutation generation |
| [N-Queens](https://leetcode.com/problems/n-queens/) | Leetcode | Classic backtracking (position permutations) |
| Traveling Salesman Problem | Custom | Brute force on all permutations of cities |

---

Absolutely! Let's go step by step to understand this permutation-generating code using **DFS (Depth-First Search)** and **backtracking**:

---

### 🔍 **Function Breakdown**
```python
def permute(arr):
    result = []
    ...
    return result
```

This function takes a list `arr` (e.g., `[1, 2, 3]`) and returns all **possible permutations** of it.

---

### 🧠 Step 1: Initialize Helper Function
```python
def dfs(path, used):
```

- `path`: current partial permutation being built.
- `used`: boolean list tracking which elements in `arr` are already used in `path`.

Example for `[1, 2, 3]`:
- Initially: `path = []`, `used = [False, False, False]`

---

### 🧠 Step 2: Base Condition
```python
if len(path) == len(arr):
    result.append(path[:])
    return
```

When the current `path` is the same length as `arr`, we’ve built a full permutation.  
So we copy and append it to `result`.

---

### 🔁 Step 3: DFS Traversal
```python
for i in range(len(arr)):
    if not used[i]:
        used[i] = True
        dfs(path + [arr[i]], used)
        used[i] = False
```

- For each element in `arr`, if it hasn't been used:
  1. Mark it as used.
  2. Add it to the path.
  3. Recur with updated path and used.
  4. Backtrack: mark it unused again (to allow other permutations).

---

### 🚀 Full Example Walkthrough: `permute([1, 2, 3])`

#### Level 0:
- path = `[]`
- used = `[False, False, False]`

Loop over `arr`:
- Pick `1` → path = `[1]`, used = `[True, False, False]`

#### Level 1:
- path = `[1]`
- Loop: pick `2` → path = `[1,2]`, used = `[True, True, False]`

#### Level 2:
- path = `[1,2]`
- Loop: pick `3` → path = `[1,2,3]`, used = `[True, True, True]`
- ✅ Base condition met → store `[1,2,3]`

**Backtrack**: used = `[True, True, False]`

#### Level 2: Try other options → pick `3` earlier → `[1,3,2]`
...
This continues until **all 6 permutations** are generated:

```python
[[1, 2, 3],
 [1, 3, 2],
 [2, 1, 3],
 [2, 3, 1],
 [3, 1, 2],
 [3, 2, 1]]
```

---

### 🔁 Backtracking Magic

Backtracking happens with:
```python
used[i] = False
```
This "unlocks" the element to be used in different positions.

---

### ✅ Final Output:
```python
print(permute([1, 2, 3]))
# Output: All 6 permutations
```

---

Would you like me to show the **visual tree/recursion stack** of this DFS call? It's super helpful for intuition.

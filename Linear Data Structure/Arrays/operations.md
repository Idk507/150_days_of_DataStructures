Here’s a **comprehensive list of all common array operations and shortcuts**, including code examples and time complexity — useful for interviews, coding, and data science tasks.

We’ll use **Python** for illustration, but most of these apply across languages.

---

## 🔷 1. **Creation & Initialization**

### ➤ Static initialization

```python
arr = [1, 2, 3, 4]
```

### ➤ Dynamic creation

```python
arr = list(range(5))         # [0, 1, 2, 3, 4]
arr = [0] * 5                # [0, 0, 0, 0, 0]
```

---

## 🔷 2. **Access & Indexing**

```python
arr = [10, 20, 30]
print(arr[0])    # 10
print(arr[-1])   # 30 (last element)
```

### ➤ Access 2D

```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3
```

---

## 🔷 3. **Update/Modify Elements**

```python
arr[2] = 99    # arr = [10, 20, 99]
```

---

## 🔷 4. **Insertion**

### ➤ Append at end

```python
arr.append(5)  # O(1) amortized
```

### ➤ Insert at index

```python
arr.insert(1, 100)   # O(n)
```

---

## 🔷 5. **Deletion**

### ➤ Delete by index

```python
del arr[1]     # O(n)
```

### ➤ Remove by value

```python
arr.remove(99)  # O(n)
```

### ➤ Pop last (or at index)

```python
arr.pop()       # O(1)
arr.pop(1)      # O(n)
```

---

## 🔷 6. **Searching**

### ➤ Linear Search

```python
x in arr      # True / False
arr.index(x)  # Returns index of first occurrence
```

### ➤ Binary Search (sorted array)

```python
import bisect
bisect.bisect_left(arr, x)
```

---

## 🔷 7. **Slicing / Subarrays**

```python
arr[1:3]     # from index 1 to 2
arr[:2]      # first two
arr[::2]     # every second element
arr[::-1]    # reversed array
```

---

## 🔷 8. **Iteration / Traversal**

### ➤ 1D

```python
for x in arr:
    print(x)
```

### ➤ 2D

```python
for row in matrix:
    for val in row:
        print(val)
```

---

## 🔷 9. **Sorting**

```python
arr.sort()              # In-place ascending
arr.sort(reverse=True)  # Descending
sorted_arr = sorted(arr)  # Returns new sorted list
```

---

## 🔷 10. **Reversing**

```python
arr.reverse()         # In-place
rev = arr[::-1]       # Returns new list
```

---

## 🔷 11. **Aggregation / Math Ops**

```python
sum(arr)
min(arr)
max(arr)
len(arr)
```

---

## 🔷 12. **List Comprehension (Python shortcut)**

```python
squares = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]
evens = [x for x in arr if x % 2 == 0]
```

---

## 🔷 13. **Flattening a 2D List**

```python
flat = [item for row in matrix for item in row]
```

---

## 🔷 14. **Zipping Multiple Arrays**

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

---

## 🔷 15. **Unzipping**

```python
x, y = zip(*zipped)  # x = (1,2,3), y = ('a','b','c')
```

---

## 🔷 16. **Copying Arrays**

```python
b = arr[:]         # deep copy
b = arr.copy()     # deep copy
b = arr            # shallow copy (same reference)
```

---

## 🔷 17. **Multidimensional Initialization Pitfall**

❌ Incorrect:

```python
matrix = [[0]*3]*3  # All rows point to same list
```

✅ Correct:

```python
matrix = [[0 for _ in range(3)] for _ in range(3)]
```

---

## 🔷 18. **Matrix Transpose**

```python
transpose = list(map(list, zip(*matrix)))
```

---

## 🔷 19. **Matrix Rotation (90° Clockwise)**

```python
rotated = [list(reversed(col)) for col in zip(*matrix)]
```

---

## 🔷 20. **Filtering Elements**

```python
arr = [x for x in arr if x > 5]   # Keep values > 5
```

---

## 🔷 21. **Using NumPy (for nD arrays)**

```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
a.T           # transpose
a.flatten()   # flatten array
np.sum(a)     # total sum
```

---

## ✅ Summary Table

| Operation            | Shortcut Example              | Time Complexity |
| -------------------- | ----------------------------- | --------------- |
| Create list          | `[0]*5`, `list(range(n))`     | O(n)            |
| Access/update        | `arr[i]`, `arr[i] = x`        | O(1)            |
| Append/Insert/Delete | `arr.append(x)`, `del arr[i]` | O(1)-O(n)       |
| Search               | `x in arr`, `arr.index(x)`    | O(n)            |
| Sort/Reverse         | `arr.sort()`, `arr[::-1]`     | O(n log n)      |
| Slice/Subarray       | `arr[i:j]`, `arr[::-1]`       | O(k)            |
| List comprehension   | `[x for x in arr]`            | O(n)            |
| Matrix ops           | `zip(*matrix)`                | O(n²)           |

---



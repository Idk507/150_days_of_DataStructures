
---

## 🔷 1. What is an Array?

An **array** is a **linear data structure** that stores **elements of the same type** in a **contiguous memory block**.

### 🔑 Key Characteristics:

* Fixed order (index-based access)
* Elements stored in contiguous memory
* Efficient access (`O(1)` for index-based read)

---

## 🔷 2. Types of Arrays

### 📘 A. Static Array

* **Size is fixed at creation time**
* Memory is allocated on the **stack**
* No resizing
* Languages: C, C++ arrays (e.g., `int arr[10]`)

#### Example:

```c
int arr[5] = {1, 2, 3, 4, 5};
```

### 📘 B. Dynamic Array

* **Resizable** (grows/shrinks as needed)
* Memory is allocated on the **heap**
* Backed by static array internally
* Languages: Python (`list`), Java (`ArrayList`), C++ (`vector`)

#### Example:

```python
arr = [1, 2, 3]  # Python list (dynamic array)
arr.append(4)
```

---

## 🔷 3. Array Operations and Time Complexity

| **Operation**   | **Static Array** | **Dynamic Array** | **Time Complexity** |
| --------------- | ---------------- | ----------------- | ------------------- |
| Access (index)  | ✅ Allowed        | ✅ Allowed         | `O(1)`              |
| Update (index)  | ✅ Allowed        | ✅ Allowed         | `O(1)`              |
| Insert at end   | ❌ Not allowed    | ✅ `append()`      | `O(1)*` (amortized) |
| Insert at index | ❌ ❗ (shift reqd) | ✅ (but costly)    | `O(n)`              |
| Delete at end   | ❌                | ✅ `pop()`         | `O(1)`              |
| Delete at index | ❌ ❗ (shift reqd) | ✅ `del arr[i]`    | `O(n)`              |
| Search (linear) | ✅ Allowed        | ✅ Allowed         | `O(n)`              |
| Search (binary) | ✅ Sorted only    | ✅ Sorted only     | `O(log n)`          |
| Resize          | ❌ Fixed size     | ✅ Auto-managed    | `O(n)` (on grow)    |

> \* Amortized `O(1)`: Dynamic arrays double in size when full, but that costly copy operation is infrequent.

---

## 🔷 4. Internal Working of Dynamic Arrays

| **Property**         | **Explanation**                                        |
| -------------------- | ------------------------------------------------------ |
| **Initial Capacity** | Starts with small size (e.g., 4)                       |
| **Resize Mechanism** | When full, a new array is created with **2x capacity** |
| **Copy Overhead**    | All old elements copied → `O(n)`                       |
| **Amortized Insert** | Most inserts are `O(1)`, but some rare ones `O(n)`     |

#### 📌 Example in Python

```python
import sys

arr = []
for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}, Memory: {sys.getsizeof(arr)} bytes")
```

Shows how memory grows with size (due to resizing).

---

## 🔷 5. Memory Allocation (Stack vs Heap)

| **Array Type** | **Memory Location** | **Reason**                 |
| -------------- | ------------------- | -------------------------- |
| Static Array   | Stack               | Known size at compile time |
| Dynamic Array  | Heap                | Size changes at runtime    |

> **C/C++**:

```c
int arr[100];          // Static → stack
int* arr = malloc(100 * sizeof(int)); // Dynamic → heap
```

---

## 🔷 6. Use Cases of Arrays

| Use Case                     | Array Type                         |
| ---------------------------- | ---------------------------------- |
| Machine learning features    | NumPy arrays (dynamic, contiguous) |
| Image processing (pixels)    | 2D arrays / matrices               |
| Real-time sensor data buffer | Circular array (fixed size)        |
| Sorting/search algorithms    | Input as static or dynamic array   |

---

## 🔷 7. Special Concepts in Arrays

### ✅ Multidimensional Arrays

* Arrays of arrays (e.g., 2D matrix, 3D tensor)
* `matrix[row][col]` access

### ✅ Slicing (in Python-like languages)

```python
arr = [10, 20, 30, 40]
sub = arr[1:3]  # [20, 30]
```

### ✅ Shallow vs Deep Copy

```python
a = [1, 2, 3]
b = a           # shallow (same object)
c = a[:]        # deep copy (new array)
```

### ✅ Circular Arrays

* Used in **queues**, buffer management
* Wraps around when end is reached

---

## 🔷 8. Limitations

| Static Arrays                 | Dynamic Arrays                      |
| ----------------------------- | ----------------------------------- |
| Can't resize                  | Copy overhead when resizing         |
| Stack overflow for large size | Slower than static for tight memory |

---

## ✅ Summary Table

| Feature             | Static Array | Dynamic Array                |
| ------------------- | ------------ | ---------------------------- |
| Size change allowed | ❌            | ✅                            |
| Access time         | O(1)         | O(1)                         |
| Insert/delete mid   | ❌ (`O(n)`)   | ✅ (`O(n)`)                   |
| Memory location     | Stack        | Heap                         |
| Language examples   | C arrays     | Python lists, Java ArrayList |

---



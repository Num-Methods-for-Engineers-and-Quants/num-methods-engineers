# Python File Handling

## 1. Overview

Python provides built-in functions and methods for interacting with
files. File handling allows programs to store, retrieve, and modify
information outside of program memory.

The general file handling process consists of:

1. Opening a file.
2. Performing a file operation.
3. Closing the file.

File handling is particularly important in scientific computing,
where programs frequently read input datasets, record experimental
observations, and export computational results.

---

## 2. Opening a File — `open()`

The `open()` function opens a file and returns a file object that
can be used to perform file operations.

### Syntax

```python
file = open(filename, mode, encoding)
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `filename` | Name or path of the file |
| `mode` | Specifies how the file will be accessed |
| `encoding` | Character encoding used for text files |

### Example

```python
file = open("data.txt", "r", encoding="utf-8")
```

### File Access Modes

| Mode | Description |
|------|-------------|
| `r` | Read an existing file |
| `w` | Write to a file, overwriting existing contents |
| `a` | Append information to the end of a file |
| `x` | Exclusively create a new file |
| `r+` | Read and write an existing file |
| `w+` | Read and write, overwriting existing contents |
| `a+` | Read and append to a file |
| `x+` | Exclusively create a file for reading and writing |

The default access mode is `r`.

### File Type Modifiers

| Modifier | Description |
|----------|-------------|
| `t` | Text mode (default) |
| `b` | Binary mode |

Examples:

```python
file = open("data.txt", "rt")
file = open("image.png", "rb")
file = open("output.bin", "wb")
```

Text mode operates on strings (`str`), while binary mode operates
on bytes (`bytes`).

The `encoding` parameter applies only to text mode.

---

## 3. Closing a File — `close()`

The `close()` method closes an open file and releases the
associated operating system resources.

Closing a file also flushes buffered output under normal
operating conditions.

### Syntax

```python
file.close()
```

### Example

```python
file = open("data.txt", "r", encoding="utf-8")
file.close()
```

Once a file has been closed, subsequent read or write operations
on that file object will raise a `ValueError`.

### Checking File Status

The `closed` attribute indicates whether a file is closed.

```python
file = open("data.txt", "r", encoding="utf-8")

print(file.closed)  # False

file.close()

print(file.closed)  # True
```

---

## 4. Reading a File

Python provides several methods for reading information from
an open file.

### 4.1 Reading File Contents — `read()`

The `read()` method retrieves information from an open file.

#### Syntax

```python
file.read(size)
```

The optional `size` parameter specifies the maximum number of
characters to read in text mode or bytes in binary mode.

If omitted, Python reads the remaining contents of the file.

#### Reading the Entire File

```python
file = open("data.txt", "r", encoding="utf-8")

contents = file.read()

print(contents)

file.close()
```

#### Reading a Specified Number of Characters

```python
with open("data.txt", "r", encoding="utf-8") as file:
    contents = file.read(10)

print(contents)
```

### 4.2 Reading a Single Line — `readline()`

The `readline()` method reads a single line from the current
file position.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()

print(first_line)
print(second_line)
```

The newline character is retained when present.

### 4.3 Reading Multiple Lines — `readlines()`

The `readlines()` method reads the remaining lines of a file
and returns them as a list.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
print(type(lines))
```

### 4.4 Iterating Through a File

A file object can be iterated over directly.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))
```

Iterating through a file is generally more memory-efficient
than loading the entire file into memory.

This is particularly useful when processing large scientific
datasets.

### 4.5 Reading Method Comparison

| Method | Return Type | Description |
|--------|-------------|-------------|
| `read()` | `str` | Reads remaining text |
| `read(n)` | `str` | Reads up to n characters |
| `readline()` | `str` | Reads one line |
| `readlines()` | `list` | Reads remaining lines |
| `for line in file` | `str` per iteration | Iterates through lines |

The return types shown above assume text mode.

---

## 5. Writing to a File — `write()`

The `write()` method writes information to an open file.

The file must be opened using an access mode that permits
writing.

Opening a file in `w` mode:

- Creates the file if it does not exist.
- Immediately truncates the file if it already exists.
- Begins writing at the start of the file.

### Syntax

```python
file.write(string)
```

### Example

```python
file = open("data.txt", "w", encoding="utf-8")

file.write("Groundwater Drawdown Analysis\n")
file.write("Pumping Rate: 500 gpm\n")

file.close()
```

### Newline Characters

The `write()` method does not automatically insert newline
characters.

```python
file.write("First line\n")
file.write("Second line\n")
```

Without the newline characters, the strings would be written
consecutively on the same line.

### Return Value

In text mode, `write()` returns the number of characters
written.

```python
with open("data.txt", "w", encoding="utf-8") as file:
    count = file.write("Hello")

print(count)  # 5
```

### Writing Numerical Values

Numerical values must be converted to strings before being
written to a text file.

```python
drawdown = 12.45678

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(f"Drawdown: {drawdown:.2f} ft\n")
```

### Writing Multiple Strings — `writelines()`

The `writelines()` method writes an iterable of strings
to a file.

```python
lines = [
    "Groundwater Drawdown Analysis\n",
    "Pumping Rate: 500 gpm\n",
    "Drawdown: 12.45 ft\n",
]

with open("data.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

Like `write()`, the `writelines()` method does not automatically
insert newline characters.

---

## 6. Appending to a File

Append mode allows additional information to be written to
the end of a file without overwriting its previous contents.

Opening a file in `a` mode:

- Creates the file if it does not exist.
- Preserves existing file contents.
- Directs new write operations to the end of the file.

### Example

```python
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Additional simulation results\n")
```

Python does not provide a separate `append()` method for
file objects.

Appending is accomplished using `write()` or `writelines()`
after opening the file in append mode.

### Writing Versus Appending

| Characteristic | Write (`w`) | Append (`a`) |
|----------------|-------------|--------------|
| Creates missing file | Yes | Yes |
| Preserves existing contents | No | Yes |
| Truncates existing file | Yes | No |
| Initial write location | Beginning | End |
| Supports reading | No | No |

### Scientific Applications

Append mode is particularly useful for:

- Recording simulation results.
- Maintaining research logs.
- Recording experimental observations.
- Recording successive numerical calculations.
- Preserving computational history.
- Recording numerical convergence histories.

---

## 7. Context Managers — `with`

The recommended approach to file handling is to use a
context manager through the `with` statement.

A context manager automatically closes the file when
execution leaves the associated code block, including
when an exception occurs.

### Syntax

```python
with open(filename, mode, encoding) as file:
    # Perform file operations
    pass
```

### Reading

```python
with open("data.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

### Writing

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Simulation results\n")
```

### Appending

```python
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Additional results\n")
```

An explicit call to `close()` is not required when using
a context manager.

### Traditional Versus Context Manager Approach

Traditional approach:

```python
file = open("data.txt", "r", encoding="utf-8")

contents = file.read()

file.close()
```

Context manager approach:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

The context manager approach is generally preferred because
it provides automatic resource management.

---

## 8. File Position

Python maintains an internal file position that determines
where the next read or write operation occurs.

### 8.1 Current File Position — `tell()`

The `tell()` method returns the current file position.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    print(file.tell())

    contents = file.read(5)

    print(file.tell())
```

In binary mode, the position represents a byte offset.

In text mode, the returned value is an opaque position
indicator and should not necessarily be interpreted as
a character or byte count.

### 8.2 Changing File Position — `seek()`

The `seek()` method changes the current file position.

### Syntax

```python
file.seek(offset, whence)
```

| Parameter | Description |
|-----------|-------------|
| `offset` | Position or offset |
| `whence` | Reference position |

### Reference Positions

| Value | Reference |
|-------|-----------|
| `0` | Beginning of file |
| `1` | Current file position |
| `2` | End of file |

Arbitrary relative offsets are generally supported in binary
mode. Text mode imposes additional restrictions on valid
offsets.

### Returning to the Beginning

```python
with open("data.txt", "r", encoding="utf-8") as file:
    contents = file.read()

    file.seek(0)

    contents = file.read()
```

### Reading and Appending

When using `a+` mode, the file position may initially be
at the end of the file.

```python
with open("data.txt", "a+", encoding="utf-8") as file:
    file.write("Additional results\n")

    file.seek(0)

    contents = file.read()

print(contents)
```

Append-mode writes are directed to the end of the file,
even when `seek()` changes the current read position.

---

## 9. File Buffering — `flush()`

Python may temporarily store written information in a
buffer before transferring it to the underlying file.

The `flush()` method transfers buffered output to the
underlying stream without closing the file.

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Simulation started\n")
    file.flush()
```

This may be useful during long-running numerical simulations
where intermediate results need to become available before
the program finishes.

Flushing Python's buffer does not necessarily guarantee that
the operating system has physically persisted the data to
the storage device.

---

## 10. File Paths

Files may be accessed using either relative or absolute paths.

### Relative Path

```python
with open("data/results.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

Relative paths are interpreted relative to the current
working directory.

### Absolute Path

```python
with open("/home/user/research/results.txt", "r",
          encoding="utf-8") as file:
    contents = file.read()
```

### Using pathlib

The `pathlib` module provides an object-oriented approach
to working with filesystem paths.

```python
from pathlib import Path

path = Path("data") / "results.txt"

with path.open("r", encoding="utf-8") as file:
    contents = file.read()
```

### Checking Whether a File Exists

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
print(path.is_file())
```

### Current Working Directory

```python
from pathlib import Path

print(Path.cwd())
```

This is particularly important when working in Spyder,
where the current working directory may differ from the
directory containing the Python script.

---

## 11. File Handling Exceptions

File operations may generate exceptions when the requested
operation cannot be completed.

| Exception | Description |
|-----------|-------------|
| `FileNotFoundError` | Requested file does not exist |
| `FileExistsError` | File already exists in exclusive creation mode |
| `PermissionError` | Insufficient filesystem permissions |
| `IsADirectoryError` | Specified path refers to a directory |
| `UnicodeDecodeError` | File cannot be decoded using the selected encoding |
| `UnicodeEncodeError` | Text cannot be encoded using the selected encoding |
| `ValueError` | Invalid mode or operation on a closed file |
| `io.UnsupportedOperation` | Operation is unsupported by the selected mode |
| `OSError` | General operating system or filesystem error |

### Exception Handling Example

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        contents = file.read()

except FileNotFoundError:
    print("The requested file does not exist.")

except PermissionError:
    print("Permission to access the file was denied.")
```

---

## 12. File Access Mode Summary

| Mode | Read | Write | Create | Truncate | Append |
|------|------|-------|--------|----------|--------|
| `r` | Yes | No | No | No | No |
| `w` | No | Yes | Yes | Yes | No |
| `a` | No | Yes | Yes | No | Yes |
| `x` | No | Yes | Yes* | No | No |
| `r+` | Yes | Yes | No | No | No |
| `w+` | Yes | Yes | Yes | Yes | No |
| `a+` | Yes | Yes | Yes | No | Yes |
| `x+` | Yes | Yes | Yes* | No | No |

*Exclusive creation raises an exception if the file
already exists.*

---

## 13. File Method Summary

| Method | Purpose |
|--------|---------|
| `open()` | Opens a file |
| `close()` | Closes a file |
| `read()` | Reads file contents |
| `readline()` | Reads a single line |
| `readlines()` | Reads lines into a list |
| `write()` | Writes information |
| `writelines()` | Writes an iterable of strings |
| `seek()` | Changes the file position |
| `tell()` | Returns the current file position |
| `flush()` | Flushes buffered output |
| `truncate()` | Resizes the file |
| `readable()` | Determines whether reading is supported |
| `writable()` | Determines whether writing is supported |
| `seekable()` | Determines whether seeking is supported |

---

## 14. Applied Example — Groundwater Research Log

The following example demonstrates writing, appending,
and reading groundwater simulation results.

```python
# =============================================================================
# Groundwater Research Log
# =============================================================================

filename = "groundwater_results.txt"

# Write initial simulation results.

with open(filename, "w", encoding="utf-8") as file:
    file.write("Groundwater Drawdown Analysis\n")
    file.write("=" * 40 + "\n")
    file.write("Pumping Rate: 500 gpm\n")
    file.write("Elapsed Time: 24 hours\n")
    file.write("Drawdown: 12.45 ft\n")

# Append additional simulation results.

with open(filename, "a", encoding="utf-8") as file:
    file.write("\nAdditional Simulation\n")
    file.write("Pumping Rate: 750 gpm\n")
    file.write("Elapsed Time: 24 hours\n")
    file.write("Drawdown: 18.68 ft\n")

# Read and display the complete file.

with open(filename, "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)
```

### Expected Output

```text
Groundwater Drawdown Analysis
========================================
Pumping Rate: 500 gpm
Elapsed Time: 24 hours
Drawdown: 12.45 ft

Additional Simulation
Pumping Rate: 750 gpm
Elapsed Time: 24 hours
Drawdown: 18.68 ft
```

The numerical values are illustrative and are not calculated
groundwater drawdown results.

---

## 15. Engineering and Scientific Computing Applications

File handling provides the foundation for numerous scientific
computing activities.

| Application | Description |
|-------------|-------------|
| Model inputs | Reading simulation parameters |
| Experimental data | Importing measured observations |
| Simulation results | Exporting calculated quantities |
| Research logs | Recording scientific observations |
| Convergence histories | Recording iterative solver performance |
| Verification | Preserving benchmark results |
| Parameter studies | Recording successive model configurations |
| Computational research | Maintaining reproducible investigations |

More advanced scientific data handling may involve specialized
file formats and libraries.

| Format | Python Library |
|--------|----------------|
| Plain text | Built-in file handling |
| CSV | `csv`, pandas, NumPy |
| JSON | `json` |
| Excel | pandas, openpyxl |
| NumPy arrays | NumPy |
| HDF5 | h5py |
| NetCDF | netCDF4, xarray |
| Parquet | pandas, PyArrow |

---

## 16. Recommended Practices

- Use context managers for file operations.
- Explicitly specify character encoding for text files.
- Use descriptive filenames.
- Preserve original experimental datasets.
- Avoid unintentionally overwriting existing results.
- Use pathlib for filesystem path management.
- Maintain appropriate numerical precision when exporting data.
- Document units associated with numerical quantities.
- Separate input data from generated simulation results.
- Use exception handling where appropriate.
- Verify the current working directory when using relative paths.
- Use append mode when maintaining sequential research logs.

---

## 17. Learning Exercises

### Exercise 1 — Basic File Operations

Create a text file containing several lines of information.
Read the file and display its contents.

### Exercise 2 — File Access Modes

Investigate the behavior of the following modes:

- `r`
- `w`
- `a`
- `x`
- `r+`
- `w+`
- `a+`

Observe how each mode affects existing file contents.

### Exercise 3 — Reading Methods

Compare the behavior and return types of:

- `read()`
- `readline()`
- `readlines()`
- File iteration

### Exercise 4 — File Position

Investigate the behavior of `seek()` and `tell()` in both
text and binary modes.

### Exercise 5 — Scientific Data Export

Develop a Python script that writes the following quantities
to a text file:

- Pumping rate
- Transmissivity
- Storativity
- Radial distance
- Elapsed pumping time
- Calculated drawdown

Include appropriate units and numerical formatting.

### Exercise 6 — Numerical Iteration Log

Develop a script that records the iteration number and
calculated value for a simple iterative numerical process.

Use append mode to preserve successive results.

---

## 18. References

- Kiusalaas, J. *Numerical Methods in Engineering with Python 3*.
  Third Edition. Cambridge University Press, 2013.

- Python Documentation — Reading and Writing Files:
  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

- Python Documentation — Built-in Functions:
  https://docs.python.org/3/library/functions.html#open

- Python Documentation — I/O Tools:
  https://docs.python.org/3/library/io.html

- Python Documentation — pathlib:
  https://docs.python.org/3/library/pathlib.html

---

**Subject:** Python Programming Fundamentals

**Category:** Input and Output

**Application:** Numerical Methods and Scientific Computing

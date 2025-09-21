📖 Reading

1.https://www.w3schools.com/python/python_lists.asp Python Lists – W3Schools → quick intro (creation, indexing, slicing).

2. https://www.programiz.com/python-programming/list Programiz – Python Lists → clear explanation + diagrams.

3. https://www.geeksforgeeks.org/python-list/ GeeksforGeeks – List Methods → covers all important methods (append, extend, insert, pop, remove, etc.).

4. https://realpython.com/list-comprehension-python/ → detailed guide on Pythonic one-liners.


🎥 Videos

1. List, Tuples, Dictionaires Playlist: https://youtube.com/playlist?list=PLBlnK6fEyqRhJ_qiFbz9KZB1CO1HXBDHb&si=QoufWyNavrfi4Ojz

📊 Python Data Structures Comparison
| Feature                                      | List                                      | Tuple                                             | Set                                                             | Dictionary                                                       |
|----------------------------------------------|-------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
| **Syntax**                                   | `[1, 2, 3]`                               | `(1, 2, 3)`                                       | `{1, 2, 3}`                                                     | `{"a": 1, "b": 2}`                                               |
| **Order**                                    | ✅ Ordered (keeps insertion order)         | ✅ Ordered (Python 3.7+)                          | ❌ Unordered                                                     | ✅ Ordered (Python 3.7+)                                          |
| **Duplicates**                               | ✅ Allowed                                 | ✅ Allowed                                        | ❌ Not allowed (only unique items)                               | ❌ Keys must be unique (values can repeat)                        |
| **Mutable**                                  | ✅ Yes (can add, remove, change)           | ❌ No (immutable)                                 | ✅ Yes (can add/remove, but elements must be immutable)          | ✅ Yes (can add, remove, update key-value pairs)                  |
| **Indexing**                                 | ✅ Supports indexing/slicing               | ✅ Supports indexing/slicing                      | ❌ No indexing (unordered)                                       | ❌ No direct indexing (access by key instead)                     |
| **Typical Use Case**                         | Collections that may change, dynamic list | Fixed collections, read-only data (e.g., coords) | Membership tests, uniqueness, set ops (union, intersection)     | Key → Value mappings (like JSON, configs, lookup tables)          |
| **Performance**                              | Fast lookup O(1) by index, O(n) search    | Same as list, but faster to read (immutable)      | Very fast membership check (O(1) average)                       | Very fast key lookup (O(1) average)                              |
| **Memory**                                   | More memory than tuple                    | More compact (since immutable)                    | Efficient for unique items                                      | Higher overhead (stores hash map)                                |
| **Hashable? (Can be used as a key in dict)** | ❌ No                                      | ✅ Yes (if elements inside are immutable)         | ❌ No                                                            | Keys must be hashable (int, str, tuple)                          |

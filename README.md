# kiruthick-python

A small collection of Python examples and exercises organized by concept and package. This repository groups learning material and code for Python basics, string operations, lists, tuples and dictionaries.

## Package Index

This index lists the learning packages and example files in this repository. Each package focuses on a core Python concept and contains small example scripts, exercises, and an explanatory README.

- python_basic/
  - Description: Core fundamentals — variables, data types, control flow (if/else), loops (for/while), functions, basic I/O.
  - Example files: hello.py, control_flow.py, functions_example.py
- strings/
  - Description: String creation, formatting, methods, slicing, encoding, and common patterns (parsing, templating).
  - Example files: formatting.py, slicing_and_indexing.py, parse_key_values.py
- lists/
  - Description: Building and manipulating lists, comprehensions, nested lists, common algorithms, mutability.
  - Example files: comprehension_examples.py, list_methods.py, flatten_nested.py
- tuples/
  - Description: Immutable sequences, packing/unpacking, when to use tuples vs lists, using tuples as dict keys.
  - Example files: pack_unpack.py, tuple_use_cases.py
- dictionaries/
  - Description: Mapping types, creation patterns, dictionary methods, nested structures, iteration, common use-cases.
  - Example files: dict_methods.py, invert_dict.py, merge_dicts.py

## Quick links

- Packages:
  - python_basic/ - basic Python concepts and examples
  - strings/ - string operations and examples
  - lists/ - list operations and examples
  - tuples/ - tuple usage examples
  - dictionaries/ - dictionary examples and patterns

## Concept flow

Below is a mermaid sequence diagram that represents how a learner might progress through the core concepts in this repository (Python Basic -> String -> List -> Tuple -> Dictionary).

```mermaid
sequenceDiagram
    participant Learner as Learner
    participant Basic as Python Basic
    participant String as String
    participant List as List
    participant Tuple as Tuple
    participant Dict as Dictionary

    Learner->>Basic: Start with fundamentals (variables, types, control flow)
    Basic->>String: Learn string creation and manipulation
    String->>List: Convert and split strings into lists; learn indexing
    List->>Tuple: Understand immutability and when to use tuples
    Tuple->>Dict: Use tuples as keys and migrate to mappings (dicts)
    List->>Dict: Build dictionaries from list of pairs
    String->>Dict: Parse key:value strings into dictionaries

    note over Learner,Dict: Iterate, practice exercises, and refer to package readmes
```

## How to use

1. Browse the package folders and open the README or example scripts.
2. Run example scripts locally using Python 3.x: `python3 path/to/example.py`.
3. Each package contains focused explanations and sample code.
4. Try small edits and rerun to learn by experimentation.

## Contributing

Contributions welcome — open issues and PRs to add examples, fixes or explanations.

## Next ideas / TODOs

- Add focused READMEs inside each package with short exercises and expected outputs.
- Add unit tests for examples (pytest) and a CI workflow to run them.
- Add more intermediate/advanced packages (file handling, modules, OOP, exceptions).

# kiruthick-python

A small collection of Python examples and exercises organized by concept and package. This repository groups learning material and code for Python basics, string operations, lists, tuples and dictionaries.

See the full package index in [index.md](index.md).

## Quick links

- Index: [index.md](index.md)
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

1. Open the `index.md` to see the list of packages and example files.
2. Browse the package folders and run example scripts locally using Python 3.x.
3. Each package contains a README with focused explanations and sample code.

## Contributing

Contributions welcome — open issues and PRs to add examples, fixes or explanations.

## Fundamentals



- Create Dictionaries `<dictionary>[<key>:<value>, <key>:<value>...]`
- Access Elements: Ref: [Access Elements](2.access-elements.py)
- Multiple ways to creating dictionaries using Constructors: Ref: [Create - Multiple ways](1.create.py)
- [Characteristics of a Dictionary](#Characteristics)

### Characteristics:
| S.No | Characteristics    | Details                                                 |
|------|--------------------|---------------------------------------------------------|
| 1    | Unordered Set      | No index associated in Dictionary                       |
| 2    | Not a Sequence     | Its Unordered Set of elements                           |
| 3    | Indexed by Keys    | Its Indexed by KEYS and Immutable                       |
| 4    | Keys are unique    | Key can't be duplicate, Values can be duplicated        |
| 5    | Values are Mutable | Modify values `<dictionary>[<key>] = <value>`           |
| 6    | Stored as mappings | Stored internally using `Hash`, linking called Mappings |

#### Adding Elements to Dictionaries:
- Add new elements (key:value) using assignment as per syntax.
- Key being added must not exist in dictionary and must unique.

<span style="margin-left:40px">Ex: `<dictionary>[<key>] = <value>` </span>
Ex: Ref: [Add Elements](4.add-elements.py)

#### Nesting Dictionaries
- Storing a dictionary inside another dictionary is called nesting of Dictionary.
- Ref: [Nesting](5.nesting-dictionary.py)

#### Update/Modify existing Elements
- If Key already exists, the new value will be changed for the existing key.
<span style="margin-left:40px">Ex: `<dictionary>[<existing key>] = <value>` </span>
Ex: Ref: [Add Elements](4.add-elements.py)

#### Deleting Elements from a Dictionary

| S.No | Options            | Details                                                                                      |
|------|--------------------|----------------------------------------------------------------------------------------------|
| 1    | del()              | It will not return any values <br/> `del <dict>` <br/> `del <dict>[<key>]`                   |
| 2    | pop()              | It will return removed value <br/> `<dict>.pop(key, <value>)` <br/>`<value>` - Return values |
| 3    | popitem()          | Remove and return last inserted element <br/> `<dict>.popitem(key, <value>)`                 |
| 4    | clear()            | Remove all items from Dictionary <br/>`<dict>.clear()`                                       |

Ex: Ref: [Delete items](6.delete.py)


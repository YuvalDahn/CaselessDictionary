# Caseless Dictionary
> **forked from:** [babakness/caselessDictionary.py](https://gist.github.com/3901174.git) (on gist)

Dictionary that enables case insensitive searching while preserving case sensitivity 
when keys are listed, ie, via keys() or items() methods. 
Works by storing a lowercase version of the key as the new key and stores the original key-value 
pair as the key's value (values become dictionaries).

## Example of how it stores it in the background:
```python
>>> d = CaselessDictionary()
>>> d['Aa'] = 'Bb'
>>> print(d)
{'Aa': 'Bb'}
```
but in the background it will be stored as:
```python
{'aa': {'key': 'Aa', 'val': 'Bb'}}
```

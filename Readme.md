# Pastebin.com as a python file object

A small python library with little dependencies to use [pastebin.com](pastebin.com) as file like objects
Don't take it serious it's just a project to have some fun

## TODO

* Add support for none buffered files
* Split huge files to multiple pastes
* Add encoding options
* Add os function support (move, cpy, list)
* Add async operations
* Add missing tests

## install locally

> pip install .

## uninstall

> pip uninstall pastebinfs

## Example

```python
user_key = pastebinfs.sync.pastebin_auth(api_key, username, password)

with pastebinfs.sync.pastebin_open("test.txt", "w", api_key, user_key) as f:
    f.write("hello pastebin this is a test")

with pastebinfs.sync.pastebin_open("test.txt", "r", api_key, user_key) as f:
    print(f.read()) # yields "hello pastebin this is a test"
```
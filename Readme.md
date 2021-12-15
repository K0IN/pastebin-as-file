# Pastebin.com as a python file object

A small python library with little dependencies to use [pastebin.com](pastebin.com) as file like objects
Don't take it serious it's just a project to have some fun

## install

### git

> pip install .

### pypi

> pip install pastebinfs

## Example

```python
# user key can be saved / cached
user_key = pastebinfs.sync.pastebin_auth(api_key, username, password)

with pastebinfs.sync.pastebin_open("test.txt", "w", api_key, user_key) as f:
    # f implements all file methodes - just like open
    f.write("hello pastebin this is a test")

with pastebinfs.sync.pastebin_open("test.txt", "r", api_key, user_key) as f:
    print(f.read()) # yields "hello pastebin this is a test"

print(pastebinfs.os.stat("test.txt", api_key, user_key))
# st_updatetime == 1297953260   # last update time
# st_key == '0b42rwhf'          # paste key (this changes on every write)
# st_mode == 1                  # paste visibility mode (unlisted)
# st_size == 29                 # paste size (note in binary mode the size will be len(base64(input)))

pastebinfs.os.move("test.txt", "old_test.txt", api_key, user_key) # also works with copy

pastebinfs.os.remove("old_test.txt", api_key, user_key)
```

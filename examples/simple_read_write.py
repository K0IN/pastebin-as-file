import pastebinfs.sync
import pastebinfs.os

api_key = input("apikey > ")
username = input("username > ")
password = input("password > ")

# user key can be cached - see pastebin api for more details (https://pastebin.com/doc_api#9)
user_key = pastebinfs.sync.pastebin_auth(api_key, username, password)

print(user_key)

with pastebinfs.sync.pastebin_open("test.txt", "w", api_key, user_key) as file:
    file.write("hello pastebin this is a test")


with pastebinfs.sync.pastebin_open("test.txt", "r", api_key, user_key) as file:
    print(file.read())


print(pastebinfs.os.stat("test.txt", api_key, user_key))
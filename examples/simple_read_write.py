import pastebinfs.sync

api_key = input("apikey > ")
username = input("username > ")
password = input("password > ")

user_key = pastebinfs.sync.pastebin_auth(api_key, username, password)

print(user_key)

with pastebinfs.sync.pastebin_open("test.txt", "w", api_key, user_key) as file:
    file.write("hello pastebin this is a test")


with pastebinfs.sync.pastebin_open("test.txt", "r", api_key, user_key) as file:
    print(file.read())

# try: something that might cause an exception

# except: do this if there was an exception

# else: do this if there were no exceptions

# finally: do this no matter what happens

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:               # we can have multiple exceptions
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print(f"File was closed.")
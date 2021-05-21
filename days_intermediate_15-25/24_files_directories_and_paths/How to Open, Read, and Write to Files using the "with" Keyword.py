# with open("my_file.txt") as f:
#     content = f.read()
#     print(content)


with open("new_file.txt", mode="w") as f:        #mode: w-write, a-append, r-read.
    f.write("\nFelicidades again.")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 220. Understand Relative and Absolute File Paths
# Writing to a file
f = open("example.txt", "w")
f.write("Hello, this is a test.\n Writing another line.\n")
f.close()

# Reading from a file
f = open("example.txt", "r")
content = f.read()
print(content)
f.close()

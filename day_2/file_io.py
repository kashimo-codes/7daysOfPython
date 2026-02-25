# File I/O
# Used to read/write data to and from
# files on disk
# Built-in func open() used to open a file
# After which you can read from and write to
#  using methods like read() and write()
f = open("90DaysOfDevOps.txt", "r")
print(f.read())
f.close()
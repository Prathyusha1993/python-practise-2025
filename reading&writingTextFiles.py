# Why encoding?
# Text files are bytes on disk; encoding="utf-8" tells Python how to convert bytes ↔ text (portable, reliable).
# Text (r/w/a): human-readable content (CSV, JSON, logs). Always specify encoding="utf-8" for portability.
# Binary (rb/wb/ab): media files, pickles, compressed archives; anything not plain text.


# over writes file if it exists
with open('notes.txt', 'w', encoding='utf-8') as f:
    f.write('Hello\n')
    f.writelines(['Line 2\n', 'Line 3\n'])

# Read whole File
with open('notes.txt', 'r', encoding='utf-8') as f:
    data = f.read()

# read line by line memory efficient:
with open('notes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())

# read fixed size chunk
with open('notes.txt', 'r', encoding='utf-8') as f:
    chunk = f.read(100)


# with open as f(context manager)
# context manager that guarantees cleanup(closing the file) even if an exception happens
f = open('notes.txt', 'r', encoding='utf-8')
try:
    data = f.read()
finally:
    f.close()


# essential read write patterns:
text = f.read()   #read entire file carefully with huge files

# readline() -> one line including trailing /n
line = f.readline()

# readlines() ->list of lines (avoid for huge files)
lines = f.readlines()

# best for big files:
# for line in f:
    # process(line)

# writing pattersn:
f.write('one line\n')   # returns no of characters written
f.writelines(['a\n', 'b\n'])   #does not add new lines for you
f.flush()   #force buffer to OS


# file pointer, seek() & tell()
with open('notes.txt', 'r+', encoding='utf-8') as f:
    print(f.tell())   #current bte position
    f.seek(0)    #go to start
    first_10 = f.read(10)
    f.seek(0,2)
    f.write('\nAppended')


# robutsness: erros & safe patterns
from pathlib import Path

path = Path('data.txt')
try:
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            ...
except FileNotFoundError:
    print('File not found.')
except PermissionError:
    print('No permission to read this file.')


p = Path('notes.txt')
p.write_text('Hello\n', encoding='utf-8')
print(p.read_text(encoding='utf-8'))
p.write_bytes(b"\x00\x01")

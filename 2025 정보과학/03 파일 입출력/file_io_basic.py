with open('file1.txt', 'w') as f:
    f.writelines("hello")
    f.writelines("hello")
    f.writelines("hello")

with open('file1.txt', 'r') as f:
    print('1', f.read())
    f.seek(0)
    print('2', f.read())
    f.tell()
    print('2-1', f.read())

with open('file1.txt', 'r') as f:
    print('3', f.readline())

# def infinite_iterator():
#     i = 1
#     while True:
#         yield i
#         i += 1
#
#
# for num in infinite_iterator():
#     print(num)


class MyFile:
    def __init__(self, filename, mode, encoding="utf-8"):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with MyFile("test.txt", "w") as f:
    f.write("Hello")

with MyFile("test.txt", "r") as f:
    print(f.read())
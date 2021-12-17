# without context management

# file_descriptor = []
# for i in range(8180):
#     file_descriptor.append(open('test.txt', 'w'))
#
# print(len(file_descriptor))


# context management using functions

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('test.txt', 'w') as f:          # with keyword is used in python for context management
    f.write('Akrati')

print(f.closed)

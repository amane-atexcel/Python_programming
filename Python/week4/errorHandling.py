try:
    file = open("./Python/week4/js.pdf", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
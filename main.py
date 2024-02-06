with open(".env") as file:
    read = file.readline()[10:-1]
    print(read)
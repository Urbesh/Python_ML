'''''
File Not Found Exception:
Try to open a non-existent file and catch the FileNotFoundError
'''''
while True:
    file_name = input("Enter the file name you want to open: ")
    try:
        f = open(file_name)
        print("File opened successfully!")
        break
    except FileNotFoundError:
        print("File not found! Please check again.")
import shutil

file_name = input("Png filename: ")

input_file = open(file_name, 'rb')
destination_file = open('lab1zad1.png', 'wb')

shutil.copyfileobj(input_file, destination_file)

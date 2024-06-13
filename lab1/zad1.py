import shutil

file_name = input("File name: ")

intput_file = open(file_name, 'rb')

destination_file = open('lab1zad1.txt', 'wb')

shutil.copyfileobj(intput_file, destination_file)




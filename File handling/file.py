import os, shutil
# File handling-> open file, close file, read file, write and maintain file
path = r"/Users/pemaa/Documents/vs code/python/File handling/test.txt"

# my_file = open(path)
# print(my_file)
# print(my_file.read())
# print(my_file.writable()) # To check weather to write in file or not
# my_file.close()

# my_another_file = open(path,"r+")    #Read and Write
# print(my_another_file.readable())
# print(my_another_file.writable())
# print(my_another_file.read())
# my_another_file.write("Namaste \n")

"""my_another_file = open(path,"w+")
print(my_another_file.readable())
print(my_another_file.writable())
my_another_file.write("Namaste \n")
my_another_file.seek(0)
print(my_another_file.read())"""

my_next_file=open("next.txt","a+")
print(my_next_file.readable())
print(my_next_file.writable())
print(my_next_file.write("Hello \n World\n"))

my_next_file.seek(0)
print(my_next_file.read())
list=["Pema\n","Lhakpa\n","Pranil\n"]
print(my_next_file.writelines(list))
my_next_file.seek(0)

print(my_next_file.readline())
print(my_next_file.readlines())

# shutil.copy("next.txt","next1.txt")
# os.remove("next.txt")

shutil.move("test.txt","next2.txt")




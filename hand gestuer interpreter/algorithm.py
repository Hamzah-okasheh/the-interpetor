import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file = open("algorithm.txt")
# read the content of the file opened 
content = file.readlines() 
  
# read 10th line from the file 
print("tenth line") 
print(content[4]) 
  
# print first 3 lines of file 
print("first three lines") 
print(content[0:3]) 

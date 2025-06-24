# This is a placeholder for try_except.py

try: #try the code and test errors
      num = int(input("write your edge:"))
except: #handlingin errors if it is found
    print(" Bad,this is not integer")
else:
     print("Good, this is integer")
finally:
   print("print finally whatever happens")

#--------------------------------------------
# Example
#-------------------------------------------
try:
  #  print(10/0)
   # print(print(x))
    print(int("hello"))
except ZeroDivisionError:
    print("can not divide")
except NameError:
    print("variable is not defined")
except ValueError:
    print("error happens") 

#file_handling 
f = open("C:\Users\pc\Downloads\haidy_ML\Sprints-Python-Track\OOP\classes.py" ,"r")  # only read the file 
print(f.read())
f.close()                             # note: as there is no memory mangment you should close your file after each single operation 

f=open("C:\Users\pc\Downloads\haidy_ML\Sprints-Python-Track\OOP\classes.py","r")
all_lines = f.readline()    # to read line by line 
for line in all_lines:
    print(line)
    f.close()


f=open("C:\Users\pc\Downloads\haidy_ML\Sprints-Python-Track\OOP\classes.py","w") # if the file is not exist it will creat a file automaticly 
f.write("hello") # it overwrite the data in the file and write new data for every single time you use this method  
f.close() 
   

f=open("C:\Users\pc\Downloads\haidy_ML\Sprints-Python-Track\OOP\classes.py","a") # if the file is not exist it will creat a file automaticly 
for i in range (30):                                                             # append () is as the same way of write() but has small diff that append() does not overwrite it add the new data in file without overwrite 
    f.write("\n i love python") + str(i)
    f.close()    

# This is a placeholder for try_except.py

 #try: #try the code and test errors
  #    num = int(input("write your edge:"))
#except: #handlingin errors if it is found
 #   print(" Bad,this is not integer")
#else:
 #    print("Good, this is integer")
#finally:
 #    print("print finally whatever happens")

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
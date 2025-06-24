
#list_methodes_examples
#----------------------------
my_list = [1.0 ,2.0 ,3.0]
print(type(my_list))

rep = my_list*2
print(rep)

#mixed_data type 
my_data=['A string', 23 , 100.232 ,'o']
print(len(my_data))
my_data = my_data +['Ahmed']

#methodes
my_data.append(15)
my_data.insert(5,11)
my_data.extend(my_list)
my_data.remove(23)

#indexing and slicing
print(my_data[2])
print(my_data[:3])

my_data.pop()
my_data.clear()

#--------------------------
#tuples 
#--------------------------
t=(1,2,3)
print(len(t))

#mixed data type
tt = ("one",2)
print(tt[0])      # not: tuples are immutable -> no  append() ,insert(),extend(),or item assignment are allowed


#tuples with one element  
my_tuple1 = ("haidy",)
my_tuple2 = "haidy" ,    # not: you can write a tuple without parantheses ()
print(type(my_tuple1))
print(type(my_tuple2))
print(len(my_tuple1))
print(len(my_tuple2))

#Tuples_concatinitions
a =(1,2,3)
b = (4,5)
c = a + b
d = a + ('hamada',20,42) + b
print(d)
print(c)

#Tuples methodes
H =(1,3,7,8,2,6,5,8)
print(H.count(8))
print(f' the position of this element is {H.index(7)}')

#Tuples Destruct 
G = ('A','B',4,'C')
X,Y,_,Z =G
print(X)
print(Y)
print(Z)

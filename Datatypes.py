x=5
print(type(x))
y=7.5
print(type(y))
z=2+3j
print(type(z))
name="hello"
print(type(name))
name1='hello'
print(type(name1))
name2="""hello"""
print(type(name2))

print("Sequence Tags")

fruits=["apple","banana","cherry"] #list and mutable
print(type(fruits))

point=[10,20]  #tuple and immutable
print(type(point))
print("\n")
nums=range(5)  #range
print(type(nums))

print("\n")
print("\n")
colors={"red","green","blue"} #set and mutable and unordered
print(type(colors))
colors.add("red")
#frozen_colors=frozenset it is immutable and ordered
student={"name":"alice","age":20} #dict key_valuepairs and key should be unique and value can duplicate
print(type(student))

print("\n")
is_active=True
is_verified=False
print(type(is_verified))

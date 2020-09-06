#Day - 2 , Assignment - 1

#LIST
a=[142,"Himavanth",7.05,'s']
print(a)

a.append(25)
print(a)


b=a.copy()
b.append("Hi")
print(b)


a.extend([142,"Bye"])
print(a)


print(a.count(142))


print(a.index('s'))


a.insert(1,"LetsUpgrade")
print(a)


a.pop()
print(a)


a.pop(-2)
print(a)


a.remove("Himavanth")
print(a)


a.reverse()
print(a)


c=[4,2,7,5,8,12,2]
c.sort()
print(c)

c.clear()
print(c)
print("\n")





#DICT
d={
    "name":"Himavanth",
    "age":20,
    "gender":"Male",
    "college":"BEC"
    }
print(d)

e=d.copy()
print(e)

print(e.clear())

print(d.get("name"))


d.update({"age":19})
print(d)


print(d.values())


print(d.keys())


print(d.items())


d.popitem()
print(d)

d.pop("name")
print(d)


x=('key1','key2','key3')
y=1
mydict=dict.fromkeys(x,y)
print(mydict)

d.clear()
print(d)
print("\n")




#SETS
fruits={"apple","mango","banana","grapes"}
print(fruits)
fruits.add("papaya")
print(fruits)

s=fruits.copy()
print(s)

fruits.discard("banana")
print(fruits)

fruits.remove("papaya")
print(fruits)

z=s.difference(fruits)
print(z)

s.difference_update(fruits)
print(s)

s.add("apple")
print("The two sets are")
print(fruits)
print(s)
x=fruits.intersection(s)
print(x)


fruits.intersection_update(s)
print(fruits)

y=fruits.isdisjoint(s)
print(y)

xy=fruits.issubset(s)
print(xy)

xy=fruits.issuperset(s)
print(xy)

zz=fruits.symmetric_difference(s)
print(zz)

fruits.symmetric_difference_update(s)
print(fruits)

z=fruits.union(s)
print(z)
print("\n")



#TUPLE
color=("red","green","white","black","pink")
print(color)
x=list(color)
x.insert(1,"red");
color=tuple(x)
print(color)

print(len(x))

z=x.count("red")
print(z)

print(x.index("pink"))
print("\n")



#STRING
age=20
str="hey.. hello, my name is himavanth! my age is {}"
print(str.format(age))

str="hello... this is himavanth"
print(str.capitalize())

print(str.upper())

print(str.lower())

print(str.count("s"))

print(str.islower())

print(str.isupper())

print(str.index("."))

print(str.find("is"))

print(str.replace("himavanth","sai krishna"))

print(str.split(" "))

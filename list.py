fruits = ["apple", "banana", "cherry", "date"]

anewlist = [] 
bnewlist = []

for i in fruits:
  
  if "a" in i :
    anewlist.append(i)
  
  if "b" in i:
    bnewlist.append(i)

print(anewlist) 
print(bnewlist) 
## using comprehensive list , this is how to create list from list if the condition is true 

fruits = ["apple", "banana", "cherry", "date"]

anewlist = [i for i in fruits if "a" in i]
bnewlist = [i for i in fruits if "b" in i]

print(anewlist)
print(bnewlist)

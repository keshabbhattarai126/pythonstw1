# # append
# a = [0,1,2,3,4]
# a.append(1)
# print(a)

# # insert
# a = [1,2,3,4]
# a.insert(1,'ram')
# print(a)

# # extend is valid
# a= [1,2,3,4]
# a.extend('1')
# print(a)

# # extend is invalid because integrer 1 is non- iterable object
# a= [1,2,3,4]
# a.extend(1)
# print(a)

# #remove using element directly
# a=[1,2,3,4]
# a.remove(4)
# print(a)

# #remove using indexing
# a=[1,2,3,4]
# a.remove(a[3])
# print(a)

# # pop method. It takes argument as index
# a= [1,2,3,4] 
# a.pop(1)
# print(a)

# # if non argument given then it will remove the last item
# a = [1,2,3,4]
# a.pop()
# print(a)

# #clear removes all
# a =[1,2,3,4]
# a.clear()
# print(a)

# # copy method copies value from one var to another
# a =[1,2,3,4]
# b = a.copy()
# print(b)

# # set operation. if there is no item in set then remove returns error
# a ={1,2,3,4}
# a.remove(5)
# print(a)

# # set operation. if there is no item in set then discard returns the orignial set
# a ={1,2,3,4}
# a.discard(5)
# print(a)

# #union
# a ={1,2,3,4}
# b ={3,4,5,6}
# c= a.union(b)
# print(c)

# # union using bitwise operator |
# a ={1,2,3,4}
# b ={3,4,5,6}
# c= a | b
# print(c)

# # #intersection
# a ={1,2,3,4}
# b ={3,4,5,6}
# c= a.intersection(b)
# print(c)

# #intersection using bitwise &
# a ={1,2,3,4}
# b ={3,4,5,6}
# c= a & b
# print(c)

# # isdisjoint. if var doesn't have in another set then true else false
# a ={1,2,3,4}
# b ={3,4,5,6}
# c= a.isdisjoint(b)
# print(c)

# # dictionary operations
# a = {'ram':1,'shyam':2}
# a['hari'] = 4
# print(a)

# # dict update operation
# a = {'ram':1,'shyam':2,'hari':4}
# b = {1:2,3:4}
# a.update(b)
# print(a)

# # dict pop operation. pop(key). pass the key to pop
# a = {'ram':1,'shyam':2,'hari':4}
# a.pop('shyam')
# print(a)

# # dict pop operation. popitem(value). pass the value to pop
# a = {'ram':1,'shyam':2,'hari':4}
# c= a.popitem()
# print(type(c))


# #get method is used to access value if key is provided. if vlaue not available returns None
# a = {'ram':1,'shyam':2,'hari':4}
# b=a.get('shyam')
# print(b)

# a = {'ram':1,'shyam':2,'hari':4}
# b=a.get('shyaam','value not available')
# print(b)


# a = {'ram':1,'shyam':2,'hari':4}
# for i in a:
#     print(i)

# a = {'ram':1,'shyam':2,'hari':4}
# for i,j in a.items():
#     print(i, j)
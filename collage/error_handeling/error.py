# Accessing invalid index
lst = [1, 2, 3]
print(lst[5])
# Assertion fails
x = 5
assert x > 10,"Error"
# Attribute does not exist
num = 10
num.append(5)
# Importing non-existing module
#import non_existing_module
# Accessing missing key
data = {"a": 1, "b": 2}
print(data["c"])
# Using undefined variable
#print(value)  
# Trying to allocate huge memory
a = [1] * (10**10)   # May crash system / raise MemoryError
# Wrong type operation
result = "10" + 5 
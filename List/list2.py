laptops=["mac","del","sony","hp"]

laptops.append("lenovo")
print(laptops)

laptops.insert(2,"lenovo")
print(laptops)

print(laptops.count("lenovo"))

laptops.remove("lenovo")
print(laptops)

laptops.pop(4)
print(laptops)

removed_element = laptops.pop(2)
print(removed_element)
print(laptops)

a=[1,2,3,4,5]
laptops.extend(a)
print(laptops)

laptops.insert(3,"microsoft")
print(laptops)

laptops.reverse()
print(laptops)

print(laptops.count("microsoft"))
print(laptops.count("hp"))
print(a)

a.clear()
print(a)
copy_list = laptops.copy()
print("This is the original list:",laptops)
print("This  is the copied list:",copy_list)
copy_list.clear()
print(copy_list)

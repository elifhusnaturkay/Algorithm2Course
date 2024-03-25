#Q5
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#a
print("*************")
for i in xs:
  print(i)

#b
print("*************")
for i in xs:
  print(i, i**2)

#c
print("*************")
total = 0
for i in xs:
  total = total + i
print(total)

#d
print("*************")
product = 1
for i in xs:
  product = product * i
print(product)

#ex1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#ex2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#ex3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#ex4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#ex5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#ex6
tuple1 = ("abc", 34, True, 40, "male")

#ex7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#ex8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#ex9
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#ex10
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#ex11
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#ex12
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#ex13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#ex14
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#ex15
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#ex16
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#ex17
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#ex18
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#ex19
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#ex20
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


#ex21
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#ex22
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#ex23
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#ex24
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#ex25
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#ex26
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#ex27
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#ex28
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
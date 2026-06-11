# Write your code here 👇
for pain in range(1, 101):
  if pain % 3 == 0 and pain % 5 == 0 :
    pain = "FizzBuzz"
    print(pain)
  elif pain % 3 == 0:
    pain = "Fizz"
    print(pain)
  elif pain % 5 == 0:
    pain = "Buzz"
    print(pain)
  else :
    print(pain)

  
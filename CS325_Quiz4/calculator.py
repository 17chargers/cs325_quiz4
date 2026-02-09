def multiply(a, b):
  return float(a) * float(b)

def divide(a, b):
  return float(a) / float(b)

def add(a, b):
  return float(a) + float(b)

def subtract(a, b):
  return float(a) - float(b)

nums = input("Enter a command followed by two numbers: ")
command, num1, num2 = nums.split()

if (command == "add"):
  result = add(num1, num2)
  print(f"{num1} plus {num2} equals {result}"
elif (command == "sub"):
  result = subtract(num1, num2)
  print(f"{num1} minus {num2} equals {result}")
elif (command == "mul"):
  result = multiply(num1, num2)
  print(f"{num1} times {num2} equals {result}")
elif (command == "div"):
  result = divide(num1, num2)
  print(f"{num1} divided by {num2} equals {result}")
else:
  print("Unknown command. Use 'add', 'sub', 'mul', or 'div'.")
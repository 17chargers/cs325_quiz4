def multiply(a, b):
  return float(a) * float(b)

def divide(a, b):
  return float(a) / float(b)

nums = input("Enter two numbers: ")
num1, num2 = nums.split()

result1 = multiply(num1, num2)
result2 = divide(num1, num2)

print(f"{num1} times {num2} equals {result1}")
print(f"{num1} divided by {num2} equals {result2}")

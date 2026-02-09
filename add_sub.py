# Get input from the user
user_input = input("Enter a command (add/sub followed by two integers): ")

#Split the input into parts
parts = user_input.split()

#Extract command and numbers
command = parts[0]
num1 = int(parts[1])
num2 = int(parts[2])

# Perform the operation
if command == "add":
    result = num1 + num2
    print(result)
elif command == "sub":
    result = num1 - num2
    print(result)
else:
    print("Unknown command. Use 'add' or 'sub'.")

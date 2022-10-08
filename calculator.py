x = input("What is x? ")
y = input("What is y? ")

z = int(x) + int(y)

print(z)

# We can do it this other way
x = int(input("What is x? "))
y = int(input("What is y? "))

print(x + y)

# For float
x = float(input("What is x? "))
y = float(input("What is y? "))

print(x + y)

# To round up to the nearest interger
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

print(z)

# OR
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

print(f"{z:,}")

# To round up to two decimal places
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x / y, 2)

print(z)


# OR
x = float(input("What is x? "))
y = float(input("What is y? "))

z = x / y

print(f"{z:.2f}")


def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))
    
    
def square(n):
    return n * n


main()

def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))
    
    
def square(n):
    return pow(n, 2)


main()

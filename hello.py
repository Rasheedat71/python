# Ask user for their name
name = input("What is your name?")

# Say hello to user
print("Hello, "  + name)

# We can also write it this way 
print("Hello,", name)


# Remove whitespace from str
name = name.strip()

# Capitalize user's name
name = name.capitalize()

# To capitalize each word
name = name.title()

# Remove whitespace from str and capitalize each word
name = name.strip().title()

# We can also write our code this way to avoid using too mucg lines
name = input("what's your name? ").strip().title()


print(f"Hello, {name}")

# To add a quote inside a quote
print('Hello, "friend"') #OR
print("Hello, \"friend\"")

# A method is a function that's built in to a type of value,
# like these functions are.
# Or on F strings 

# split user's name into first name and last name
first, last = name.split(" ")
print(f"hello, {first}")

# To define a function and say hello to the user
def hello(to):
    print("hello,", to)
    
    
name = input("What's your name? ")
hello(name)

# To say hello to the world and the user
def hello(to="world"):
    print("hello,", to)
    

hello()
name = input("What's your name? ")
hello(name)

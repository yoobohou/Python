while True:
    name = input("Enter your name: ")
    a = len(name)
    if a < 5:
        print("Hello Mr.", name)
        break
    else:
        print("Please enter a valid name (less than 5 characters).")

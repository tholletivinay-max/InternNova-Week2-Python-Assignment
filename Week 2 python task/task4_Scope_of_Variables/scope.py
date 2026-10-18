# Global variable
message = "I am a global variable"


def display_message():
    # Local variable
    name = "Python Student"

    print("Inside the function:")
    print("Global variable:", message)
    print("Local variable:", name)


# Call the function
display_message()

# Access the global variable outside the function
print("\nOutside the function:")
print("Global variable:", message)
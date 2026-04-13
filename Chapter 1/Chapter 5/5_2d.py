"""
In scripts that include the definition of several cooperating functions, it is often useful to define a special function
named main that serves as the entry point for the script. 
"""

def square(x):
    return x * x

def main():
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

# The entry point for program execution.
# Must be called at the end of the script

if __name__ == "__main__":  # if running as a standalone program
#Always before we call main() to ensure that main() is only called when the script is run directly, and not when it is imported as a module in another script.
     main()


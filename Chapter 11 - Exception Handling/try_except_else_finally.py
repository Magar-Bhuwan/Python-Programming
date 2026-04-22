# try-except-else-finally
# try:    # block of code to be tested
# except: # block of code to be executed if an error occurs
# else:  # block of code to be executed if no error occurs. or it will executed if try block will executed without any error.
# finally: # block of code to be executed regardless of an error occurs. it will always executed.

# Example 1: Using the try-except-else-finally block
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:                               # executed if ZeroDivisionError occurs
    print("Cannot divide by zero")
except ValueError:                                      # executed if ValueError occurs
    print("Invalid input")
except Exception as e:                                  # executed if any other exception occurs
    print(e)
else:                                           # executed if try block executed successfully
    print("No error occurred")
finally:                                        # executed always
    print("Execution completed")


# finally block specially use in function file handling

# Example 2: Using the try-except-else-finally block in function

def main():
    try: 
        a = int(input("Enter a number: "))
        print(a)
        return
    except ValueError as e:
        print(e)
        return
    finally:
        print("Execution completed")

main()

# Here we can check the finally block uses
# if we think finally block always runs, then we can write print statement without finally block
# but it will run after the return statement
# just run the program and check the output results.

def main():
    try: 
        a = int(input("Enter a number: "))
        print(a)
        return
    except ValueError as e:
        print(e)
        return
    
    print("Execution completed")

main()

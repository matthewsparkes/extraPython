# exception = An event that interrupts the normal flow of a program
#             e.g ZeroDivisionError, TypeError, ValueError
#             1. try, 2.except, 3.finally


# Any code that could be considered dangerous, we place in a 'try' block (e.g user input)
try:
    number = int(input("Enter a number: "))
    print(1 / number)


except ZeroDivisionError:
    print("You can't divide by 0 you donut!")
except ValueError:
    print("Enter only numbers you donut!")
except Exception:
   print("Something went wrong!")      # covers all exceptions but is bad practice (doesn't tell the user specific reason why it didn't work)


# finally block will always execute, regardless if theres an exception or not.
finally:
    print("Do some cleanup here!")
# OPTION1: Simpler and shorter way to handle exceptions with similar message
# try:
#     a = int(input("Enter the numarator: "))
#     b = int(input("Enter the denominator: "))
#     c = a/b
#     print("result :" , c)
# except Exception as e:
#     print("An Error Occurred : ", e)


#OPTION2: More specific way to handle exceptions with different messages
try:
    a = int(input("Enter the numarator: "))
    b = int(input("Enter the denominator: "))
    c = a/b
    print("result :" , c)
except ZeroDivisionError as zde:
    print("An Error Occurred : Division by zero is not allowed ", zde)
except ValueError as ve:
    print("An Error Occurred : Invalid input. Please enter a valid integer ", ve)#we can skip using and asigning the ve or zde to the exception variable if we don't want to use it in the print statement.
except Exception as e:
    print("An Error Occurred : ", e)

finally:
    print("RESOURCED closed")#finally block will always execute whether there is an exception or not.

print("end of program")
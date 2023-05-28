# In this example we are using camelCase, PascalCase, and snake_case naming convension.
import traceback
import argparse

name_convension = {
    '1' : 'Pascal Case',
    '2' : 'Snake Case',
    '3' : 'Camel Case'
}
# PascalCase
def ExceptionHandlingExample():
    if int2 == 0:
        print("It will return raise statement, this statement will not executed any code after raise")
        raise ZeroDivisionError("cannot divide by zero")
        print("This line will not be excuted")
    return int1/int2


# snake_case
def exception_handling_example():
    try:
        num1 = int(input("Enter a number:"))
        num2 = int(input("Enter another number:"))
        result = num1/num2
    except ValueError:
        print("Invalid input. Please Enter a valid integer.")
    except ZeroDivisionError:
        print("cannot divide by zero")
    except Exception as e:
        print(traceback.format_exe())
    else:
        print("The division result is :",round(result,2))
    finally:
        print("Thanks for using this calculator")

# camelCase
def exceptionHandlingExample():
    # here we know more about data types in python
    # mainly we have two types of data
    # primitive: int, float, bool, str, None
    try:
        student_name = input("Please enter a your name: ") # input function will take string type
        age = int(input("How old you are: ")) # here we need only whole number
        married = bool(input("Are you married: ")) # here we only except True or False
        weight = float(input("please Enter your weight: ")) #here we can enter int or float number
        approval = None
    except Exception:
        print(traceback.format_exc())
    else:
        print(f"Student Name : {student_name}. \nAge : {age}. \nMarrid Status : {married}.\nWeight : {weight}.\nApproval: {approval}.")
    finally:
        print("Thanks for showing interest..")

    #Non primitive data types: list, tuple, set, dictionary
    try:
        list_number = [1,2,3,4,6]
        print(list_number,type(list_number))
        print(isinstance(list_number,list))
        tuple_number = (1,2,3,4,6)
        print(tuple_number, type(tuple_number))
        print(isinstance(tuple_number,tuple))
        set_number = {1,2,3,4,4,5,6}
        print(set_number, type(set_number))
        print(isinstance(set_number,set))
        dict_data = {}
        print(isinstance(dict_data, dict))
        print(dict_data,type(dict_data))
    except Exception:
        print(traceback.format_exc())

if __name__ == '__main__':
    # we are use argparse module for command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-mode', type=str, default='1', help='select name convension functions')
    args = parser.parse_args()

    # Here we are defining cases and get method of dictionary
    if args.mode == '1':
        int1 = int(input("Please enter a number: "))
        int2 = int(input("Please another number: "))
        print("You are selected {} naming conventions".format(name_convension.get(args.mode, '')))
        try:
            # here are define variable inside main function it has global scope
            # Pascal case name conventions used to define the function name
            result = ExceptionHandlingExample()
        except ZeroDivisionError as e:
            print(str(e))
        except Exception as e:
            print(traceback.format_exc())
        else:
            print("Division of two number is : ", round(result))
        finally:
            print("Thanks for using the calculator")

    elif args.mode == '2':
        print("You are selected {} naming convensions".format(name_convension.get(args.mode,'')))
        # Snake case name conventions used to define the function name
        exception_handling_example()

    elif args.mode == '3':
        print("You are selected {} naming convensions".format(name_convension.get(args.mode, '')))
        # Camel case name conventions used to define the function name
        exceptionHandlingExample()

    else:
        print("Please enter valid mode")
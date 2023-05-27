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
    pass

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
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-mode', type=str, default='1', help='select name convension functions')
    args = parser.parse_args()
    if args.mode == '1':
        print("You are selected {} naming convensions", name_convension.get(args.mode, ''))
    elif args.mode == '2':
        import pdb;pdb.set_trace()
        print("You are selected {} naming convensions",name_convension.get(args.mode,''))
        exception_handling_example()
    elif args.mode =='3':
        print("You are selected {} naming convensions", name_convension.get(args.mode, ''))


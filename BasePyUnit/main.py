import Conversions

def DecToBinCheck(x):  # Built in converting, used to check if the number was correct
    return bin(x)


def BinToDecCheck(x):  # Built in converting, used to check if the number was correct
    return int(x, 2)


if __name__ == '__main__':
    DTB = Conversions.ConvertDecToBin
    BTD = Conversions.ConvertBinToDec
    conversion = "na"  # No input at the start, needed for the while loop.
    while conversion.upper() != "X":  # Exits the program if input is X
        conversion = input("What would you like to convert from? \n D - Decimal to Binary \n B - Binary to Decimal "
                           "\n X - Exit\n")  # First part of the menu, asking for
        if conversion.upper() == "D":  # Decimal to Binary
            number = (input("Type your decimal number to convert to binary\n")) # Asking user for input
            if number.isdigit(): # Checks if the number is a valid integer
                if int(number) > 10000000000000000000000:  # Tells user not to input too high of an number
                    print("Please enter a number less than 10000000000000000000000.")  # Ints are used to store the num
                else:
                    x = int(number)
                    convert = DTB.DecToBin(x) # Converts the number
                    print("Your converted number is: %s" % convert)  # Displays answer
                    # Built in converting, used to check if the number was correct
                    print("The built in converter converts it to: %s" % DecToBinCheck(int(number)))
            else:  # Number is not valid
                print("Please enter a valid number.")
        elif conversion.upper() == "B":  # Binary to Decimal
            number = (input("Type your binary number to convert to decimal\n"))  # Asking user for input
            if number.isdigit():  # Checks if the number is valid
                if int(number) > 10000000000000000000000:  # Tells user not to input too high of an number
                    print("Please enter a number less than 10000000000000000000000.")  # Ints are used to store the num
                else:
                    x = int(number)
                    convert = BTD.BinToDec(x)  # Converts the number
                    if convert == -1: # Number was not binary
                        pass
                    else:  # Number is binary
                        print("Your converted number is: %s" % convert)  # Prints output
                        # Built in converting, used to check if the number was correct
                        print("The built in converter converts it to: %s" % BinToDecCheck(number))
            else:  # Number was not a valid number
                print("Please enter a valid number.")
        elif conversion.upper() == "X":  # Exiting the program
            exit(0)
        else:  # Argument not valid for the menu
            print("Please input a valid argument.")
    exit(0)  # Exiting program incase for whatever reason the exit button does not work
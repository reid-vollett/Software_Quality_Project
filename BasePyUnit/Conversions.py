
class ConvertDecToBin:

    def DecToBin(x):  # Decimal to Binary conversion
        k = []  # Initialing the list used in the conversions
        if x == 0:  # Checks if the inputted number is 0, it's a special case for the program
            k.append(0)  # If the input is 0, the output will be 0
        while (x > 0):  # Loops until x is 0
            a = int((x % 2))  # Checking if the binary is 1 or 0
            k.append(a)  # Adding the number to a list to take out later
            x = (x - a) / 2  # Moving to the next number
        out = ""  # Defining the out variable
        for j in k[::-1]:  # For loop for the list k, taking all the binary numbers that was converted
            out = out + str(j)  # Adding them to "out"
        out = int(out)
        return out  # giving back the new binary number.


class ConvertBinToDec:

    def BinToDec(x):  # Binary to Decimal conversion
        out = 0  # Setting out to 0, special case incase of user inputting 0 to convert.
        j = 1  # Binary conversions start at 1
        while (x >= 1):  # While loop, keeps looping until no more numbers
            a = (x % 10)  # Divides by 10 and gets the remainder ( 1 or 0 )
            if a == 1:  # Checking if the binary digit is one
                out = out + j  # Adds the current place to the output
            elif a == 0:  # Checks if the binary digit is 0, does nothing
                out = out
            else:  # If it's anything else, it is not a binary number.
                print("Please input a valid binary number ( only 1's or 0's. )")
                out = -1
                return out
            j = j + j  # Goes to the next place in the binary conversions
            x = int(x / 10)  # Gets rid of another number
        return out  # Returns the converted number
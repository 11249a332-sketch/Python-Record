def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str)
        return decimal
    except ValueError:
        return "invalid binary number!"

def octal_to_hexadecimal(octal_str):
    try:
        decimal=int(octal_str,8)
        hexa=hexa(decimal).upper().replce("ox","")
        return hexa
    except ValueError:
     return "invalid octal number!"

print(")number system conversion")
print("1.binary to decimal")
print("2.octal to hexadecimal")
choice=input("enter your choice(1or2):")
if choice=="1":
    binary=input("enter a binary number:")
    print("decimal value:"binary_to_decimal(binary))
elif choice=="2":


    octal=input("enter your octal number:")
    print("hexadecimal value:"octal_to_hexadecimal(octal))

else:
    print("invalid choice!please enter 1or2")
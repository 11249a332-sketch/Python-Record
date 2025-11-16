def convert_temp(temp,unit):
    if unit=='C' or unit=='C':
        #convert celsius to fahrenheit
        fahrenheit =(temp*9/5)+32
        return f"{fahrenheit:.2f}°f"
    elif unit=='f' or unit=='f':
         #convert fahrenheit to celsius
         celsius=(temp-32)*5/9
         return f"{celsius:.2f}°C"
    else:
      return"Invalid unit! please enter 'C' for celsius or 'f' for fahrenheit."
#Example usage
print(convert_temp(37,'C'))
print(convert_temp(98.6,'f'))
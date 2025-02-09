#Multiplication Calculator (Only Integers)
def multiply():
    x=int(input('What is the first number you would like to multiply?'))
    y=int(input('What is the second number you would like to multiply?'))
    multiplied=x*y
    return multiplied

result=multiply()
print(result)
#Payment Calculator (with Overtime Pay, Regular Pay, and Total Pay)
def hours():
    try:
        x=float(input('Enter Hours:'))
        h=x
        return h
    except:
        print('Error, please enter a valid numeric value for Hours')
        quit()
time=hours()

def rate():
    try:
        y=float(input('Enter Rate:'))
        r=y
        return r
    except:
        print('Error, please enter a valid numeric value for Rate')
        quit()
dollars=rate()
print(time)
print(dollars)
regpay=time*dollars
print('Regular Pay:',regpay)

otorno=input('Did you do any overtime this week?(Yes or No):')
try:
    yesorno=str(otorno)
except:
    print('Please answer Yes or No (Case Sensitive)')
    quit()

def otpay():
    a=float(input('Enter OT Hours:'))
    b=dollars*1.5
    otpayment=a*b
    return otpayment

if yesorno=='Yes':
    overtimepay = otpay()
    print('Overtime Pay:', overtimepay)
    totalpayment = overtimepay + regpay
    print('Total Pay:', totalpayment)
if yesorno=='No':
    print('Total Pay:',regpay)
else:
    print('Please answer Yes or No')
    quit()




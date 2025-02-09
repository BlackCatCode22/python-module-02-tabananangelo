#Payment Calculator (with Overtime Pay, Regular Pay, and Total Pay)
def hours():
    x=float(input('Enter Hours:'))
    h=x
    return h

time=hours()
print(time)

def rate():
    y=float(input('Enter Rate:'))
    r=y
    return r

dollars=rate()
print(dollars)
regpay=time*dollars
print('Regular Pay:',regpay)

otorno=input('Did you do any overtime this week?(Yes-1 or No-2):')
yesorno=int(otorno)

def otpay():
    a=float(input('Enter OT Hours:'))
    b=dollars*1.5
    otpayment=a*b
    return otpayment

if yesorno==1:
    overtimepay = otpay()
    print('Overtime Pay:', overtimepay)
    totalpayment = overtimepay + regpay
    print('Total Pay:', totalpayment)
else:
    print('Total Pay:',regpay)





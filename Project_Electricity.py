def data(a, b, c, d, e, f, g):
    print('Name : ', a)
    print('Area : ', b)
    print('Address : ', c)
    print('Meter Number : ', d)
    print('Units Consumed : ', e)
    print('Email ID : ', f)
    print('Mobile Number : ', g)
    return 'Generating Bill'


def urban(u):
    if 0 <= u <= 30:
        amount = units_consumed * 3.25  # RS 3.25 per unit
        return f'Your Bill is : {amount}'
    elif 31 <= u <= 100:
        amount = units_consumed * 4.70  # RS 4.70 per unit
        return f'Your Bill is : {amount}'
    elif 101 <= u <= 200:
        amount = units_consumed * 6.25  # RS 6.25 per unit
        return f'Your Bill is : {amount}'
    else:
        amount = units_consumed * 7.30  # RS 7.30 per unit
        return f'Your Bill is : {amount}'


def rural(r):
    amount = 1
    if 0 <= r <= 30:
        amount = units_consumed * 3.15  # RS 3.15 per unit
        return f'Your Bill is : {amount}'
    elif 31 <= r <= 100:
        amount = units_consumed * 4.40  # RS 4.40 per unit
        return f'Your Bill is : {amount}'
    elif 101 <= r <= 200:
        amount = units_consumed * 5.95  # RS 5.95 per unit
        return f'Your Bill is : {amount}'
    else:
        amount = units_consumed * 6.80  # RS 6.80 per unit
        return f'Your Bill is : {amount}'


Name = input('Enter your Name : ')
Area = input('Enter your Area (Urban/Rural) : ')
Address = input('Enter your address : ')
Meter_Number = input('Enter your Meter Number : ')
units_consumed = int(input('Enter the total units consumed : '))
Email_ID = input('Enter your Email ID : ')
Mobile_no = input('Enter your Mobile Number : ')

print('********* ELECTRICITY BILL *********')
print(data(Name, Area, Address, Meter_Number, units_consumed, Email_ID, Mobile_no))
if Area == 'Urban' or Area == 'urban':
    print(urban(units_consumed))
elif Area == 'Rural' or Area == 'rural':
    print(rural(units_consumed))

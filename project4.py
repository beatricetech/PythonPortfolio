def computepay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = 40 * rate
        pay = overtime_pay + regular_pay
    else:
        pay = hours * rate
    return pay
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
pay = computepay(hours, rate)
print("Pay:",pay)

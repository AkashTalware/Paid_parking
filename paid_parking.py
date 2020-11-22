from datetime import timedelta

def verification(**args):
    sum_of_code = 0
    discount = 0
    isweekday = None
    entrance_time_final = 0
    exit_time_Final = 0
    if args['input_day'].lower() in args['days']['weekdays'] or args['input_day'].lower() in args['days']['weekend']:
        print(f"The Day {args['input_day']} is available!!")
        if args['input_day'].lower() in args['days']['weekdays']:
            isweekday = True
        elif args['input_day'].lower() in args['days']['weekend']:
            isweekday = False
    else:
        print("Invalid Day You have Entered, my loyal subject!!")
        isweekday = None

    if float(args['entry_time'].split(".")[0]) >= 8.00:
        if int(args['entry_time'].split(".")[1]) <= 59:
            print("Valid Entrance Time")
            entrance_time_final = timedelta(hours = int(args['entry_time'].split(".")[0]), 
                                            minutes = int(args['entry_time'].split(".")[1]))
            print("entrance_time_final", entrance_time_final)
        else:
            print("Invalid Minutes in Entry Time")
    else:
        print("We open at 8.00 AM")

    if float(args['exit_time'].split(".")[0]) <= 22.00:
        if int(args['exit_time'].split(".")[1]) <= 59:
            print("Valid Exit Time")
            exit_time_Final = timedelta(hours = int(args['exit_time'].split(".")[0]), 
                                            minutes = int(args['exit_time'].split(".")[1]))
            print("exit_time_Final", exit_time_Final)
        else:
            print("Invalid Minutes in Exit Time")
    else:
        print("We close at 22.00 PM")

    for digit in args['code']:
        sum_of_code += int(digit)
    if len(args['code']) == 6 and sum_of_code % 2 == 0:
        print("Coupen code Accepted!")
        print("Entered Coupen Code: ", args['code'])
        discount = 2
    else:
        print("Coupen Code Unacceptable")  

    return discount, isweekday, entrance_time_final, exit_time_Final

def calculate_bill(args):
    charge_rate = 0
    total_time_parked = str(args[3] - args[2])
    print("total_time_parked: ", total_time_parked)
    total_hours = int(total_time_parked.split(":")[0]) + (int(total_time_parked.split(":")[1]) / 60)

    if args[1]:
        charge_rate = 4
    else:
        charge_rate = 10

    total_bill = round((total_hours * charge_rate) - args[0])
    return total_bill



days = {'weekdays': ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'], 'weekend': ['saturday', 'sunday'] }

input_day = input("Enter the day: ")
entry_time = input("Entry time (in the format \'hh.mm\' and in 24hrs format): ")
exit_time = input("Exit time (in the format \'hh.mm\' and in 24hrs format): ")
code = input("Enter six digit Coupen code, if you have any: ")

coupen_code = 0

# input_day = 'satUrDaY'
# entry_time = '9.56'
# exit_time = '20.10'
# code = '223223'

print("Total Bill is: Rs.", calculate_bill(verification(input_day = input_day, days = days, entry_time = entry_time, exit_time = exit_time, code = code)))

    
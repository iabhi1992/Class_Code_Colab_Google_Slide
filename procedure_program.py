base_sal = int(input('Enter Base Salary: '))
extra_hours = int(input('Enter the Extra hours: '))
hourly_rate = int(input('Enter hourly rate: '))

def calculate_Wage(base_sal, extra_hours, hourly_rate):
	return base_sal + (extra_hours * hourly_rate)

print(calculate_Wage(base_sal, extra_hours, hourly_rate))

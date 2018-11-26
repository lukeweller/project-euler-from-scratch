# i7-4870HQ 4 cores, 8 threads, 2.5 GHz -> 3.7 GHz

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def first_sundays(first_day, month_dict):

	sunday_counter = 0

	if first_day == 0:
		sunday_counter += 1

	for month in range(1,13):
		first_day = (first_day + month_dict[month]) % 7
		if first_day == 0:
			sunday_counter += 1

	return sunday_counter, first_day

if __name__ == '__main__':

	month_dict = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
	leap_month_dict = { 1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

	days_counter = 0
	first_day = 2 # January 1 1901 was a Tuesday (We're using 0 for Sunday)

	for year in range(1901, 2001):
		print(first_day, days_counter)
		if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
			sundays, first_day = first_sundays(first_day, leap_month_dict)
		else:
			sundays, first_day = first_sundays(first_day, month_dict)
		days_counter += sundays

	print(days_counter)
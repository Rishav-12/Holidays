'''
This script uses the https://calendarific.com/ api
'''
import requests
from datetime import date

with open('api_key.txt', 'r') as key: # <-- use your own api key here
	api_key = key.read().strip()

country = 'IN' # <-- you can also change the country... just look up the iso code from the docs

now = date.today()
day = str(now.day)
month = str(now.month)
year = str(now.year)

url = f'https://calendarific.com/api/v2/holidays?&api_key={api_key}&country={country}&day={day}&month={month}&year={year}'

try:
	r = requests.get(url)
	data = r.json()

	holidays = data['response']['holidays']

except Exception:
	holidays = None

if holidays is None:
	print("Could not fetch data. Terminating")

elif len(holidays) == 0:
	print("No holidays today...")

else:
	print("\nToday's holidays :")
	print("*************************")

	for holiday in holidays:
		print("\n")
		print(holiday['name'])
		print(holiday['description'])

input()

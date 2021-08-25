'''
This script uses the https://calendarific.com/ api
'''
import requests
from datetime import date
import smtplib

SENDER = "" # make sure less secure app access is turned on
RECEIVER = ""
PASSWORD = "" # sender's gmail password

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

response = ""

if holidays is None:
	response += "Could not fetch data. Terminating"

elif len(holidays) == 0:
	response += "No holidays today..."

else:
	response += "\nToday's holidays :\n"
	response += "*************************\n"

	for holiday in holidays:
		response += "\n"
		response += holiday['name'] + "\n"
		response += holiday['description']+ "\n"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER, PASSWORD)
server.sendmail(SENDER, RECEIVER, response)

import webbrowser  
import time
import datetime

def roombooking():
	today = datetime.date.today()
	thismonday = today - datetime.timedelta(days=today.weekday())
	thissunday = thismonday + datetime.timedelta(days=6)
	tomorrow = today + datetime.timedelta(days=1)
	nextmonday = thismonday + datetime.timedelta(days=7)
	nextsunday = thissunday + datetime.timedelta(days=7)

	date = input('Choose now, today, tomorrow, this week or next week: ', ) or ""
	attendees = input('Number of attendees (leave blank for any): ',) or ""
	length = input('Number of minutes (leave blank for any): ',) or ""

	startdate=today
	enddate=today
	mystery=1

	if date.lower()=="now":
		startdate=0
	elif date.lower()=="today":
		startdate=today
		mystery=3
	elif date.lower()=="tomorrow":
		startdate=tomorrow
		mystery=3
	elif date.lower()=="this week":
		startdate=thismonday
		mystery=3
	elif date.lower()=="next week":
		startdate=nextmonday
		mystery=3
	else:
		startdate=0

	if date.lower()=="now":
		enddate=0
	elif date.lower()=="today":
		enddate=today
		mystery=3
	elif date.lower()=="tomorrow":
		enddate=tomorrow
		mystery=3
	elif date.lower()=="this week":
		enddate=thissunday
		mystery=3
	elif date.lower()=="next week":
		enddate=nextsunday
		mystery=3
	else:
		enddate=0

	if date.lower() in ["today","tomorrow","this week","next week"]:
		start = datetime.datetime(startdate.year, startdate.month, startdate.day,0,0,0,0)
		start_time = int(time.mktime(start.timetuple()))*1000
		end = datetime.datetime(enddate.year, enddate.month, enddate.day,23,59,59,999)
		end_time = int(time.mktime(end.timetuple()))*1000
	else:
		start_time=0
		end_time=0

	webbrowser.open("https://app.matrixbooking.com/ui/#/find/rooms/results/{s}/{e}/{l}/{a}/718321/{m}/0/0".format(s=start_time, e=end_time, a=attendees, l =length, m=mystery), new=2, autoraise=True)

	message = "Your search will open in a new window"

	return message
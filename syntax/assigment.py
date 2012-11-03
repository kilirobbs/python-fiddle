from datetime import datetime
class calendar:
	year = None
	weeknumber = None
	weekday = None
	def __init__(self):
		self.year = None
		self.weeknumber = None
		self.weekday = None	
now=calendar()
now.year,now.weeknumber,now.weekday=datetime.now().isocalendar()
print now.year,now.weeknumber,now.weekday

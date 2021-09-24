import datetime,time
def iplcountdown():
	total=1
	while(total>0):
	# taking difference in dates 
		current_date = datetime.datetime.now()
		till_date = datetime.datetime(2022,1,25,0,0,0,0)
		difference = till_date - current_date
		total = difference.total_seconds()
		# countdwon code
		if(total<=0):
			print("You're Going to Disney World!")
		else:
			# days
			days = difference.days
			# hours
			hours,rest = divmod(difference.seconds,60*60)
			# minutes,seconds
			minutes,seconds = divmod(rest,60)
			countdown='WDW in {:02d} Days : {:02d} Hours : {:02d} Mins : {:02d} Secs'.format(
				days,hours,minutes,seconds)
			print(countdown,end="\r")
			time.sleep(1)
iplcountdown(countdown)
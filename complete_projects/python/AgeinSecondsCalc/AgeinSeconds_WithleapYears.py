
#AgeInSeconds


#1 year = 365 days = 8,760 hours = 525,600 minutes = 31,536,000 seconds
#1 * 365 * 24 * 60 * 60

ageYear = int(input())

ageSeconds = ageYear * 31,536,000

leapDays = int(ageYear/4)
# *24 hours * 60 minutes * 60 secs = 86400
leapSeconds = leapDays * 86,400

totalSeconds = ageSeconds + leapSeconds

print("This is your age in seconds (with leap years)",totalSeconds,"seconds")
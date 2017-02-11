#PROGRAM TO ENTER VALUEIN DAYS AND CONVERT N FORMS OF YEARS, MONTHS AND DAYS(ASSUMING ALL MONTHS HAS 30 DAYS AND YEAR IS OF 360).
days=int(input("ENTER THE DAYS:"))
year=int(days/360)
month=int((days/30)-(12*year))
days=days%30
print(year,"YEARS:",month,"MONTHS:",days,"DAYS:")

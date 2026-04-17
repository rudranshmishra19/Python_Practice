def leap(year):
     if year%400==0 or (year%4==0 and year %100!=0):
          return True
     return False
year=(int(input("Enter a year:")))
leap_year=leap(year)
if leap_year is True:
     print("it is a leap year")
else:
     print("it is not a leap year")     

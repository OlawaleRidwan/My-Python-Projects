import datetime


def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """

    
    first_of_given_month = datetime.date(year, month, 1)
    first_of_next_month = datetime.date(year, month+1, 1)
    days_interval = first_of_next_month - first_of_given_month
    
    return days_interval.days

print(days_in_month(2011,2))


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if( ( datetime.MINYEAR <= year <= datetime.MAXYEAR) and ( 0 < month <= 12) and ( 1 <= day <= (days_in_month(year,month)) )):
        return True
    else:
         return False



print(is_valid_date(2011,40,40))

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """

    if (is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2) and (datetime.date(year1,month1,day1) < datetime.date(year2,month2,day2))):
        second_date = datetime.date(year2,month2,day2)
        first_date = datetime.date(year1,month1,day1)
        diff = second_date - first_date
        no_of_days = diff.days
        return no_of_days
    else:
        return 0


print(days_between(1994,6,12,2022,6,12))

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    today = datetime.date.today()
    age = days_between(year,month,day,today.year,today.month,today.day)
    return age

print(age_in_days(1994,6,12))

  #  if(is_valid_date(year,month,day) and (datetime.date(year,month,day) < datetime.date.today() ) ):
   #     today = datetime.date.today()
    #    days_between(year, month, day,today.year, today.month, today.day)
    
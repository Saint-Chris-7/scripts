from datetime import date, datetime,timedelta


date_of_birth= str(input("Enter your date of birth-dd/mm/yyyy: "))

def calcAge(dob:str):
    """Take in date string and calculate the age"""
    format_dob= dob.split(sep="/")
    month,day,year= format_dob[0],format_dob[1],format_dob[2]
    date_of_birth_object= datetime.strptime(format_dob,"%d%m%Y")
    today_day= date.today().day
    today_month= date.today().month
    today_year= date.today().year
    age = timedelta()
    return age

calcAge(date_of_birth)
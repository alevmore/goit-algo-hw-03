import datetime as dt

def get_days_from_today(date = str) -> str:
     
# Calculating the number of days between dates
    date_delta = dt.datetime.now ().date().toordinal() - dt.datetime.strptime (date, '%Y-%m-%d').toordinal()
    return (date_delta)

while True:    
    try: 
        input_data = input ('Enter the date in YYYY-MM-DD format: ')
        your_date = get_days_from_today(input_data)
        print (f'The number of days between the given date and the current date is {your_date}')
        break
    except ValueError: 
        print ("Enter the date in the correct format YYYY-MM-DD:  ")
        
     
       




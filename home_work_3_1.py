import datetime as dt

def get_days_from_today(date = str) -> str:
     
# Обрахунок кількості днів між датами
    date_delta = dt.datetime.now ().date().toordinal() - dt.datetime.strptime (date, '%Y-%m-%d').toordinal()
    return (date_delta)

while True:    
    try: # Перевірка помилки введення
        input_data = input ('Введіть дату у форматі РРРР-ММ-ДД: ')
        your_date = get_days_from_today(input_data)
        print (f'Кількість днів між заданою датою і поточною датою складає {your_date}')
        break
    except ValueError: 
        print ("Введіть дату у вірному форматі РРРР-ММ-ДД:  ")
        
     
       




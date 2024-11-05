import datetime as dt

users = [{"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}]

def get_upcoming_birthdays(users=None):
    tdate=dt.datetime.today().date() 
    tdate.toordinal() 
    birthdays=[] 
    for user in users: 
        bdate=user["birthday"] 
        bdate=str(tdate.year)+bdate[4:] 
        bdate=dt.datetime.strptime(bdate, "%Y.%m.%d").date() 
        week_day=bdate.isoweekday() 
        bdo=bdate.toordinal() 
        days_between=bdo-tdate.toordinal() 
        if 0<=days_between<7: 
            if week_day<6: 
                birthdays.append({'name':user['name'], 'birthday':bdate.isoformat().replace('-','.')[:10]}) 
                
            else:
                if dt.datetime.fromordinal(bdo+1).weekday()==0:
                    birthdays.append({'name':user['name'], 'birthday':dt.datetime.fromordinal(bdo+1).isoformat().replace('-','.')[:10]})
                    
                elif dt.datetime.fromordinal(bdo+2).weekday()==0: 
                    birthdays.append({'name':user['name'], 'birthday':dt.datetime.fromordinal(bdo+2).isoformat().replace('-','.')[:10]})
                   
    return birthdays

    #return {"name":name, "congratulation_date":cdate}

print(get_upcoming_birthdays(users))




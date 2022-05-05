import time
time_val = time.time()


def timeCalc (val):
    years = int((val//3600)//24//365)
    years_sec = years*365*24*3600
    months = int((val - years_sec)//3600//24//30)
    months_sec = months*30*24*3600
    days = int((val - years_sec - months_sec)//3600//24)
    days_sec = days*24*3600
    hours = int((val - years_sec - months_sec - days_sec)//3600)
    hours_sec = hours*3600
    minutes = int((val - years_sec - months_sec - days_sec - hours_sec)//60)
    minutes_sec = minutes*60
    seconds = int(val - years_sec - months_sec - days_sec - hours_sec - minutes_sec)
    print(years,' years, ',months,' months, ',days, ' days, ',hours,' hours, ',minutes,' minutes, ',seconds, ' seconds ')

timeCalc(time_val)    
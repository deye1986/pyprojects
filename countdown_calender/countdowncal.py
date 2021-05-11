# Countdown calender TKinter GUI . dave ikin
# VSC wont show the tkinter window if you dont explicitly call mainloop().
# The reason you don't need to call mainloop in IDLE is because 
# IDLE does that for you automatically. In all other cases you must call mainloop() usually at the bottom. 
# A solid Tkinter program should always explicitly create a root window before creating any other widgets.

from tkinter import Tk, Canvas 
from datetime import date, datetime

def runcc():
    '''display a TKinter window with dates read and counting down from the events.txt'''
    def get_events():
        list_events = []
        with open('events.txt') as file:
            for line in file:
                line = line.rstrip('\n')
                current_event = line.split(',')
                event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
                current_event[1] = event_date
                list_events.append(current_event)
        return list_events


    def days_between_dates(date1, date2):
        time_between = str(date1 - date2)
        number_of_days = time_between.split(' ')
        return number_of_days[0]

    
    root = Tk()
    root.title("Countdown calender for Dave.")

    c = Canvas(root, width=700, height=470, bg='blue')
    c.pack()
    c.create_text(100, 50, anchor='w', fill='white', font='Arial 28 bold underline', text='My Countdown Calender')

    events = get_events()
    today = date.today()

    vertical_space = 100

    for event in events:
        event_name = event[0]
        days_until = days_between_dates(event[1], today)
        display = 'It is %s days until %s' % (days_until, event_name)
        c.create_text(100, vertical_space, anchor='w', fill='light blue', font='Arial 28 bold', text=display)

        vertical_space = vertical_space + 130
    
    root.mainloop()

runcc()
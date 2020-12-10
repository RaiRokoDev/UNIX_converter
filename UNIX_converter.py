from tkinter import *
import datetime
import time


def tc_convert(arg):
    global r_var, text1, text2, utc_field
    var = r_var.get()
    if var == 0:
        text = str(text1.get(1.0, END))
        utc = int(utc_field.get()[:3])
        output = datetime.datetime.fromtimestamp(int(text)-(3*3600)+((utc+3)*3600)).strftime('%d-%m-%Y %H:%M:%S')
        text2.delete(1.0, END)
        text2.insert(1.0, output)
    if var == 1:
        text = str(text2.get(1.0, END))
        utc = int(utc_field.get()[:3])

        day = int(text[0:2])
        month = int(text[3:5])
        year = int(text[6:10])
        hour = int(text[11:13])
        minute = int(text[14:16])
        second = int(text[17:19])
        start = datetime.datetime(1970, 1, 1, 0, 0, 0)
        stop = datetime.datetime(year, month, day, hour, minute, second)
        delta = stop-start
        output = str(delta.total_seconds()-10800+((utc+3)*3600))[:str(delta.total_seconds()).index('.')]
        text1.delete(1.0, END)
        text1.insert(1.0, output)

def main_window():
    window = Tk()
    window.title('UNIX time converter')
    window.geometry('210x130')
    window.resizable(width=False, height=False)
    window['bg'] = 'grey13'

    hat1 = Label(text='TC')
    hat1['bg'] = 'grey13'
    hat1['fg'] = 'white'
    hat1.place(x=0, y=40)

    hat2 = Label(text='Time')
    hat2['bg'] = 'grey13'
    hat2['fg'] = 'white'
    hat2.place(x=0, y=100)

    global r_var
    r_var = IntVar()
    r_var.set(0)
    r0 = Radiobutton(text='', variable = r_var, value = 0)
    r1 = Radiobutton(text='', variable = r_var, value = 1)

    r0['bg'] = 'grey13'
    r1['bg'] = 'grey13'

    r0.place(x=60, y=70)
    r1.place(x=150, y=70)

    r0text = Label(text='⬇')
    r1text = Label(text='⬆')
    r0text['bg'] = 'grey13'
    r0text['fg'] = 'white'
    r1text['bg'] = 'grey13'
    r1text['fg'] = 'white'
    r0text.place(x=40, y=70)
    r1text.place(x=190, y=70)

    global text1
    text1 = Text(width=20, height=1)
    text1.place(x=40, y=40)
    text1['bg'] = 'white'

    global text2
    text2 = Text(width=20, height=1)
    text2.place(x=40, y=100)
    text2['bg'] = 'white'

    global utc_field
    time_zone = Label(text='Time\nZone')
    time_zone.place(x=0, y=-5)
    time_zone['bg'] = 'grey13'
    time_zone['fg'] = 'white'

    utc_field = StringVar(window)
    utc_field.set('+00:00')

    utc_list = OptionMenu(window, utc_field, '+12:00',
                                             '+11:00',
                                             '+10:00',
                                             '+09:00',
                                             '+08:00',
                                             '+07:00',
                                             '+06:00',
                                             '+05:00',
                                             '+04:00',
                                             '+03:00',
                                             '+02:00',
                                             '+01:00',
                                             '+00:00',
                                             '-01:00',
                                             '-02:00',
                                             '-03:00',
                                             '-04:00',
                                             '-05:00',
                                             '-06:00',
                                             '-07:00',
                                             '-08:00',
                                             '-09:00',
                                             '-10:00',
                                             '-11:00',
                                             '-12:00')
    utc_list['bg'] = 'grey13'
    utc_list['fg'] = 'white'
    utc_list.place(x=40, y=0)

    convert = Button(text='Convert', width=5, highlightthickness = 2)
    convert.bind('<Button-1>', tc_convert)
    convert['bg'] = 'grey13'
    convert['fg'] = 'white'
    convert.place(x=136, y=0)

    window.mainloop()

main_window()

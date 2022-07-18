import tkinter as tk
from tkinter import *
from  tkinter import ttk
from PIL import ImageTk
import second_filmScript
import tkinter.font as tkFont
import pandas as pd
import time
from pandastable import Table, TableModel


#Создание окна и насстройка его
window = tk.Tk()
window.geometry("625x800")
mainColorBG = "#FFDBB9"
window.configure(bg=mainColorBG)
photo = ImageTk.PhotoImage(file="pixelVirtual.png")
mainColor = "#DCAC80"
Font_lbl = tkFont.Font(family="Share",size=15)
Font_btn = tkFont.Font(family="Share",size=10)
window.title("GUIFilm")
id = 1
#Создание фрейма для таблицы
frame_table = Frame(window,width=560,height=531)
frame_table.propagate(0)
frame_table.place(x=37,y=234)
#Скроллбар
scroll_table = Scrollbar(frame_table)
scroll_table.pack(side=RIGHT, fill=Y)

scroll_table1 = Scrollbar(frame_table,orient='horizontal')
scroll_table1.pack(side= BOTTOM,fill=X)

my_table = ttk.Treeview(frame_table,yscrollcommand=scroll_table.set, xscrollcommand =scroll_table1.set)
my_table.place(x=0,y=0,width=543,height=515)

scroll_table.config(command=my_table.yview)
scroll_table1.config(command=my_table.xview)



#Поиск фильма через обращение к другому файла
def find_film():
    clear_info()
    global answer
    answer = second_filmScript.find_film(Entry_find_title.get())
    print(len(answer))
    df_test = []
    for i in range(len(answer)):
        df_test.append(answer[i])
    df_check=pd.DataFrame(df_test)
    global pt
    #Добавление данных в таблицу в окне приложения
    for i in range(len(answer)):
        table = pt = Table(frame_table, dataframe= df_check,showtoolbar=True, showstatusbar=True)
        time.sleep(0.100)
    pt.show()

#Очистка таблицы
def clear_info():
    for i in my_table.get_children(): my_table.delete(i)

#Сохранение в таблицу excel
def save_on_base():
    #считывает все выбранные строки
    list_test =str(pt.getSelectedRows())
    #сплит через след строку
    list_test = list_test.split("\n")
    list_answer = []
    for i in range(1,len(list_test)):
        time_per = list_test[i].split()
        try:
            list_answer.append(time_per[0])
        except IndexError:
            pass

    for i in range(len(list_answer)):
        second_filmScript.save_on_base(answer[int(list_answer[i])])
    print("end")

#Создание и расположение элементов
button_find = tk.Button(
    text="Найти\n фильм",
    image=photo,
    width=137,
    height=60,
    compound="c",
    bg=mainColor,
    command=find_film,
    font= Font_btn
)

button_clear_text = tk.Button(
    text="Очистить\n информацию",
    image=photo,
    width=137,
    height=60,
    compound="c",
    bg=mainColor,
    command=clear_info,
    font= Font_btn
)

button_save_on_base = tk.Button(
    text="Добавить информацию\n в базу",
    image=photo,
    width=137,
    height=60,
    compound="c",
    bg=mainColor,
    command=save_on_base,
    font= Font_btn
)

Entry_find_title = tk.Entry(
    bg=mainColor,
    font= Font_lbl
)


lbl_title=tk.Label(text="поиск по названию",font= Font_lbl,bg=mainColorBG)


button_find.place(x=37, y=119)
button_save_on_base.place(x=250, y=119)
button_clear_text.place(x=450, y=119)

Entry_find_title.place(x=37, y=67, width=560)

lbl_title.place(x=225,y=37)

window.mainloop()
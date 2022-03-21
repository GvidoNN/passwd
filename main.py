from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Сохранения паролей')
root.geometry('320x200+625+300')

def test_txt(file_name='Школьные истории.txt'):
    with open(file_name,'a',encoding="utf-8") as f:
        name1=name.get()
        login1=login.get()
        password1=password.get()
        if password1!='' and login1!='':
            f.write(f'Название:{name.get()}\n')
            f.write(f'логин:{login.get()}\n')
            f.write(f'пароль:{password.get()}\n\n')
        else:
            messagebox.showerror('ERROR','''Ничего не ввёл в пароль или логин,
Мне за тебя это вводить или что?''')

def spravka():
    messagebox.showinfo('Справка','''Великій Государь, Царь и Великій Князь Ходосок Александр Викторович, всея Великія и Малыя и Бѣлыя Россіи Самодержецъ, Московскій, Кіевскій, Владимірскій, Новгородскій,
Царь Казанскій, Царь Астраханскій, Царь Сибирскій, Государь Псковскій и Великій Князь Тверскій, Югорскій, Пермскій, Вятскій, Болгарскій и иныхъ, Государь и Великій Князь Новагорода Низовскія земли, Черниговскій,
Рязанскій, Ростовскій, Ярославскій, Бѣлоозерскій, Удорскій, Обдорскій, Кондинскій и всея Сѣверныя страны Повелитель, и Государь Иверскія земли, Карталинскихъ и Грузинскихъ Царей и Кабардинскія земли,
Черкасскихъ и Горскихъ Князей и инымъ многимъ Государствамъ и Землямъ Восточнымъ и Западнымъ, и Сѣвернымъ Отчичъ и Дѣдичъ, и Наслѣдникъ, и Государь и Обладатель''')

def instruction():
    messagebox.showinfo('Инструкция','''    1. После того, как вписываете всю информацию, нажимаете кнопку 'Запись'
    2. После этого, в корневой папке появляется файл 'Школьные истории.txt'
    3. Для удобства можно создать ярлык на рабочем столе
    ''')

label_input_app=Label(text='Введите название приложения')
label_input_login=Label(text='Введите логин')
label_input_password=Label(text='Введите пароль')
label_input_app.grid(row=1, column=0, sticky='w')
label_input_login.grid(row=2, column=0, sticky="w")
label_input_password.grid(row=3, column=0, sticky="w")

name = StringVar()
name_entry = Entry(textvariable=name)
name_entry.grid(row=1,column=1, padx=5, pady=5)
login = StringVar()
login_entry = Entry(textvariable=login)
login_entry.grid(row=2,column=1, padx=5, pady=5)
password = StringVar()
password_entry = Entry(textvariable=password)
password_entry.grid(row=3,column=1, padx=5, pady=5)

message_button = Button(text="Запись", command=test_txt)
message_button.place(relx=.5, rely=.7, anchor="c")

menu=Menu()
file_menu=Menu(tearoff=0)
menu.add_cascade(label='Файл',menu=file_menu)
file_menu.add_command(label='Выход', command=root.quit)
menu.add_cascade(label='Справка', command=spravka)
menu.add_cascade(label='Инструкция', command=instruction)



root.config(menu=menu)
root.mainloop()
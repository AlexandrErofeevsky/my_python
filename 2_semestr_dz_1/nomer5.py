# Задание 5
import tkinter
import tkinter.messagebox

class MyGUI5:

    def __init__(self):


        self.main_window = tkinter.Tk()
        
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.medium_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        
        self.radio_var = tkinter.IntVar()
        
        self.radio_var.set(1)

        
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Дневное время(6:00-17:59)',
                                       variable=self.radio_var,
                                       value=10)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вечернее время(18:00-23:59)',
                                       variable=self.radio_var,
                                       value=12)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Непиковый период(00:00-5:59)',
                                       variable=self.radio_var,
                                       value=5)
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        
        self.label = tkinter.Label(self.medium_frame,

                    text='Введите количество минут: ')

        self.entry = tkinter.Entry(self.medium_frame,

                                        width=10)
        
        
        self.label.pack(side='left')

        self.entry.pack(side='left')
        

        
        self.inf_button = tkinter.Button(self.bottom_frame,
                                          text='Показать стоимость',
                                          command=self.show)

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                    command=self.main_window.destroy)




        self.inf_button.pack(side='left')

        self.quit_button.pack(side='left')



        self.top_frame.pack()
        self.medium_frame.pack()
        self.bottom_frame.pack()
        

        # Войти в главный цикл tkinter.

        tkinter.mainloop()

        
    def show(self):
        #min=float(self.entry.get())
        
        
        tkinter.messagebox.showinfo('Общая стоимость', 'Ваши затраты = $' + str(float(self.entry.get())*self.radio_var.get()/100))


# Создать экземпляр класса MyGUI.

my_gui5 = MyGUI5()

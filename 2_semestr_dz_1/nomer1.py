# Задание 1
import tkinter

class MyGUI:

    def __init__(self):


        self.main_window = tkinter.Tk()
        

        self.fi_frame = tkinter.Frame()

        self.se_frame = tkinter.Frame()

        self.inf = tkinter.StringVar() 
        self.inf_label = tkinter.Label(self.fi_frame,
                   textvariable=self.inf)
        self.inf_label.pack(side='left') 
        
        

        self.inf_button = tkinter.Button(self.se_frame,
                                          text='Показать инфо',
                                          command=self.show)

        self.quit_button = tkinter.Button(self.se_frame,

                                          text='Выйти',

                                    command=self.main_window.destroy)




        self.inf_button.pack(side='left')

        self.quit_button.pack(side='left')



        self.fi_frame.pack()

        self.se_frame.pack()

        

        # Войти в главный цикл tkinter.

        tkinter.mainloop()

        
    def show(self):
        self.inf.set('Стивен Маркус\n274 Бейли\nУэйнзвилль, Северная Каролина 27999')
        

# Создать экземпляр класса MyGUI.

my_gui = MyGUI()

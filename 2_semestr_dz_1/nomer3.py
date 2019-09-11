# Задание 3
import tkinter

class MyGUI3:

    def __init__(self):


        self.main_window = tkinter.Tk()
        
        
        self.fi_frame = tkinter.Frame()

        self.se_frame = tkinter.Frame()
        
        self.th_frame = tkinter.Frame()

        self.fo_frame = tkinter.Frame()

        
        self.G_label = tkinter.Label(self.fi_frame,

                    text='Введите количество галонов: ')

        self.G_entry = tkinter.Entry(self.fi_frame,

                                        width=10)
        
        
        self.G_label.pack(side='left')

        self.G_entry.pack(side='left')
        
        
        self.M_label = tkinter.Label(self.se_frame,

                    text='Введите количество миль: ')

        self.M_entry = tkinter.Entry(self.se_frame,

                                        width=10)
        
        self.M_label.pack(side='left')

        self.M_entry.pack(side='left')
        
        
        self.P_label = tkinter.Label(self.th_frame,

                   text='Мили на галлон = ')
        
        
        self.inf = tkinter.StringVar() 
        self.inf_label = tkinter.Label(self.th_frame,
                   textvariable=self.inf)
        
        self.P_label.pack(side='left') 
        self.inf_label.pack(side='left') 
        
        

        self.inf_button = tkinter.Button(self.fo_frame,
                                          text='Вычислить MPG',
                                          command=self.show)

        self.quit_button = tkinter.Button(self.fo_frame,

                                          text='Выйти',

                                    command=self.main_window.destroy)




        self.inf_button.pack(side='left')

        self.quit_button.pack(side='left')



        self.fi_frame.pack()

        self.se_frame.pack()
        self.th_frame.pack()
        self.fo_frame.pack()

        

        # Войти в главный цикл tkinter.

        tkinter.mainloop()

        
    def show(self):
        gal = float(self.G_entry.get())
        miles = float(self.M_entry.get())
        MPG=miles/gal
        self.inf.set(MPG)
        

# Создать экземпляр класса MyGUI.

my_gui3 = MyGUI3()

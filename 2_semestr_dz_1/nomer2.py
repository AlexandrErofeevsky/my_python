# Задание 2
import tkinter

class MyGUI2:

    def __init__(self):


        self.main_window = tkinter.Tk()
        

        self.fi_frame = tkinter.Frame()

        self.se_frame = tkinter.Frame()

        self.inf = tkinter.StringVar() 
        self.inf_label = tkinter.Label(self.fi_frame,
                   textvariable=self.inf)
        self.inf_label.pack(side='left') 
        
        

        self.sin_button = tkinter.Button(self.se_frame,
                                          text='sinister',
                                          command=self.funsin)

        self.dexter_button = tkinter.Button(self.se_frame,
                                          text='dexter',
                                          command=self.fundex)
                                            
        self.med_button = tkinter.Button(self.se_frame,
                                          text='medium',
                                          command=self.funmed)




        self.sin_button.pack(side='left')

        self.dexter_button.pack(side='left')
                
        self.med_button.pack(side='left')



        self.fi_frame.pack()

        self.se_frame.pack()

        

        # Войти в главный цикл tkinter.

        tkinter.mainloop()

        
    def funsin(self):
        self.inf.set('левый')
                                         
    def fundex(self):
        self.inf.set('правый')
                                         
    def funmed(self):
        self.inf.set('центральный')
        

# Создать экземпляр класса MyGUI2.

my_gui2 = MyGUI2()

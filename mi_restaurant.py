from tkinter import *

#iniciar ventana tkinter
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

#evitar maximizar
aplicacion.resizable(False, False)

#titulo de la ventana
aplicacion.title("Mi restaurante - sistema de facturacion")

#color de fondo de la ventana
aplicacion.config(bg='burlywood')




#evitar que la pantalla se cierre
aplicacion.mainloop()



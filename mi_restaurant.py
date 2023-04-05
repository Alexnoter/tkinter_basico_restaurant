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

######################################################################
#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4', font=('Dosis', 48),
                        bg='burlywood', width=27)

etiqueta_titulo.grid(row=0, column=0)


#########################################################################

#panel menu del lado izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

####

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#panel comida
panel_comida = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='azure4')
panel_comida.pack(side=LEFT)

#panel bebidas
panel_bebida = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='azure4')
panel_bebida.pack(side=LEFT)

#panel Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)
##################################################################################

#panel del lado Derecho
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)


#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()



############################################

#listas de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merlusa', 'kebad', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua1', 'soda', 'vino1', 'vino2', 'vino3', 'vino4', 'vino5', 'vino6']
lista_postres = ['helado', 'frutas', 'flan', 'gelatina', 'mush', 'pastel1', 'pastel2', 'pastel3']

#generar item comida
variables_comida = []
contador = 0

for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comida, text=comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)
    contador += 1

#generar item comida
variables_bebida = []
contador = 0

for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebida, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)
    contador += 1

#generar item postre
variables_postre = []
contador = 0

for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)
    contador += 1




#evitar que la pantalla se cierre
aplicacion.mainloop()



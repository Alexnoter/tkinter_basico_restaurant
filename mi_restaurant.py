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
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=40)
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

cuadros_comida = []
texto_comida = []

contador = 0

for comida in lista_comidas:

    #crear los checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comida,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)


    #crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comida,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)


    contador += 1

#generar item bebida
variables_bebida = []
contador = 0
cuadros_bebida = []
texto_bebida = []

for bebida in lista_bebidas:

    # crear los checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebida,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador])
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebida,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1



#generar item postre
variables_postre = []
contador = 0
cuadros_postre = []
texto_postre = []

for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador])
    postre.grid(row=contador,
                column=0,
                sticky=W)



    # crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    contador += 1



#################################################################

#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()


#etiquetas de costos comida y campos de entradas
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0, column=0)


texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly', #esto dice que solo se podra leer
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41) #ese pad es el pading


#etiquetas de costos bebida y campos de entradas
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_bebida.grid(row=1, column=0)


texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly', #esto dice que solo se podra leer
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)


#etiquetas de costos postre y campos de entradas
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo postre',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_postre.grid(row=2, column=0)


texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly', #esto dice que solo se podra leer
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1, padx=41)


#etiquetas de subtotal y campos de entradas
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_subtotal.grid(row=0, column=2)


texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly', #esto dice que solo se podra leer
                           textvariable=var_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)


#etiquetas de impuesto y campos de entradas
etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_impuestos.grid(row=1, column=2)


texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly', #esto dice que solo se podra leer
                           textvariable=var_impuestos)

texto_impuestos.grid(row=1, column=3, padx=41)



#etiquetas de total y campos de entradas
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_total.grid(row=2, column=2)


texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly', #esto dice que solo se podra leer
                           textvariable=var_total)

texto_total.grid(row=2, column=3, padx=41)


####################################################################

#evitar que la pantalla se cierre
aplicacion.mainloop()



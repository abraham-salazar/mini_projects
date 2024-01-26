#importo la libreria tk para hacer las ventanas
from tkinter import *
import tkinter as tk
from tkinter import messagebox


#inicio las ventanas para poder hacer uso de ellas en las funciones
raiz =  Tk()
raiz.title("Raiz")
raiz.geometry("300x300")
raiz.resizable(False, False)
#inicio todas las ventanas necesarias y las oculto para que no haya problema
lb_suma = tk.Toplevel(raiz)
lb_suma.withdraw()
lb_resta = tk.Toplevel(raiz)
lb_resta.withdraw()
lb_division = tk.Toplevel(raiz)
lb_division.withdraw()
lb_division.geometry("300x300")
lb_division.resizable(False, False)
lb_multi = tk.Toplevel(raiz)
lb_multi.withdraw()
lb_multi.geometry("300x300")
lb_multi.resizable(False, False)
#inicio las variables numeros como globales
global num1
global num2

#Funcion para cerrar todo el programa
def Cerrar_todo():
    raiz.destroy()

#Funcion para regresar al menu principal
def volver():
    lb_suma.withdraw()
    lb_resta.withdraw()
    lb_multi.withdraw()
    lb_division.withdraw()
    raiz.deiconify()
    

        
#Funcion para abrir la ventana de suma
def Suma():
    global num1  # Indicar que se usará la variable global num1
    global num2
    lb_suma.deiconify()
    lb_suma.title("Suma")
    lb_suma.geometry("300x300")
    lb_suma.resizable(False, False)    
    raiz.withdraw()

    #Iniciamos las varibales num1 y num2 para hacer la suma
    num1 = tk.Variable()
    entry_num1 = tk.Entry(lb_suma, textvariable=num1)
    entry_num1.pack(pady=70)
    num2 = tk.Variable()
    entry_num2 = tk.Entry(lb_suma, textvariable=num2)
    entry_num2.place(x = 50, y = 100)
    #llamamos a la funcion obtener variable para hacer la suma 
    btn_obtener_valor = tk.Button(lb_suma, text="Obtener valor", command=lambda: obtener_valor_suma(num1.get(), num2.get()))
    btn_obtener_valor.place(x=10, y=150)
    
    btn_volver_suma = tk.Button(lb_suma, text="Volver", command=volver)
    btn_volver_suma.place(x=10, y=10)
    
    btncerrar_suma = tk.Button(lb_suma, text="Salir del programa", command=Cerrar_todo)
    btncerrar_suma.place(x=40, y=40)
    
    lb_suma.mainloop()
    
    
def obtener_valor_division(valor1, valor2):
    try:
        # Intenta convertir los valores a números flotantes
        num1 = float(valor1)
        num2 = float(valor2)

    
        #Realiza la division
        if num1 == 0 and num2 == 0:
            tk.messagebox.showwarning(title = "Advertencia", message = "No se puede dividir entre 0")
        else:
            div = num1 / num2

        # Muestra el resultado en la interfaz gráfica

        lb_resul_div = tk.Label(lb_division, text = f"El resultado de la division es: {div}").place(x=10, y=200)
   
    #Si el usuario ingresa letras, nos salta un aviso de que tienen que ser numeros
    except ValueError:
        tk.messagebox.showwarning(title="Advertencia", message="Ingrese un numero para hacer la operacion")
        
def obtener_valor_suma(valor1, valor2):
    try:
        # Intenta convertir los valores a números flotantes
        num1 = float(valor1)
        num2 = float(valor2)

    
        #Realiza la suma
        sum = num1 + num2
        
        # Muestra el resultado en la interfaz gráfica

        lb_resul_sum = tk.Label(lb_suma, text = f"El resultado de la suma es: {sum}").place(x=10, y=200)
   
    #Si el usuario ingresa letras, nos salta un aviso de que tienen que ser numeros
    except ValueError:
        tk.messagebox.showwarning(title="Advertencia", message="Ingrese un numero para hacer la operacion")
                
def obtener_valor_resta(valor1, valor2):
    try:
        # Intenta convertir los valores a números flotantes
        num1 = float(valor1)
        num2 = float(valor2)

    
        #Realiza la resta
        resta = num1 - num2
        
        # Muestra el resultado en la interfaz gráfica

        lb_resul_resta = tk.Label(lb_resta, text = f"El resultado de la suma es: {resta}").place(x=10, y=200)
   
    #Si el usuario ingresa letras, nos salta un aviso de que tienen que ser numeros
    except ValueError:
        tk.messagebox.showwarning(title="Advertencia", message="Ingrese un numero para hacer la operacion")
                  
def obtener_valor_multi(valor1, valor2):
    try:
        # Intenta convertir los valores a números flotantes
        num1 = float(valor1)
        num2 = float(valor2)

    
        #Realiza la suma
        multi = num1 * num2
        
        # Muestra el resultado en la interfaz gráfica

        lb_resul_multi = tk.Label(lb_multi, text = f"El resultado de la multiplicacion es: {multi}").place(x=10, y=200)
   
    #Si el usuario ingresa letras, nos salta un aviso de que tienen que ser numeros
    except ValueError:
        tk.messagebox.showwarning(title="Advertencia", message="Ingrese un numero para hacer la operacion")
              
#Funcion para abrir la ventana de resta 
def Resta():
    global num1  # Indicar que se usará la variable global num1
    global num2
    lb_resta.deiconify()
    lb_resta.title("RESTA")
    lb_resta.geometry("300x300")
    lb_resta.resizable(False, False)    
    raiz.withdraw()

    #Iniciamos las varibales num1 y num2 para hacer la resta
    num1 = tk.Variable()
    entry_num1 = tk.Entry(lb_resta, textvariable=num1)
    entry_num1.pack(pady=70)
    num2 = tk.Variable()
    entry_num2 = tk.Entry(lb_resta, textvariable=num2)
    entry_num2.place(x = 50, y = 100)
    #llamamos a la funcion obtener variable para hacer la suma 
    btn_obtener_valor = tk.Button(lb_resta, text="Obtener valor", command=lambda: obtener_valor_resta(num1.get(), num2.get()))
    btn_obtener_valor.place(x=10, y=150)
    
    btn_volver_resta = tk.Button(lb_resta, text="Volver", command=volver)
    btn_volver_resta.place(x=10, y=10)
    
    btncerrar_resta = tk.Button(lb_resta, text="Salir del programa", command=Cerrar_todo)
    btncerrar_resta.place(x=40, y=40)
    
    lb_resta.mainloop()
    
#Funcion para abrir la ventana de multiplicacion 
def Multiplicacion():
    global num1  # Indicar que se usará la variable global num1
    global num2
    lb_multi.deiconify()
    lb_multi.title("multi")
    lb_multi.geometry("300x300")
    lb_multi.resizable(False, False)    
    raiz.withdraw()

    #Iniciamos las varibales num1 y num2 para hacer la multi
    num1 = tk.Variable()
    entry_num1 = tk.Entry(lb_multi, textvariable=num1)
    entry_num1.pack(pady=70)
    num2 = tk.Variable()
    entry_num2 = tk.Entry(lb_multi, textvariable=num2)
    entry_num2.place(x = 50, y = 100)
    #llamamos a la funcion obtener variable para hacer la suma 
    btn_obtener_valor = tk.Button(lb_multi, text="Obtener valor", command=lambda: obtener_valor_multi(num1.get(), num2.get()))
    btn_obtener_valor.place(x=10, y=150)
    
    btn_volver_multi = tk.Button(lb_multi, text="Volver", command=volver)
    btn_volver_multi.place(x=10, y=10)
    
    btncerrar_multi = tk.Button(lb_multi, text="Salir del programa", command=Cerrar_todo)
    btncerrar_multi.place(x=40, y=40)
    
    lb_multi.mainloop()
    
   
#Funcion para abrir la ventana de divsion 
def divison():
    global num1  # Indicar que se usará la variable global num1
    global num2
    lb_division.deiconify()
    lb_division.title("RESTA")
    lb_division.geometry("300x300")
    lb_division.resizable(False, False)    
    raiz.withdraw()

    #Iniciamos las varibales num1 y num2 para hacer la division
    num1 = tk.Variable()
    entry_num1 = tk.Entry(lb_division, textvariable=num1)
    entry_num1.pack(pady=70)
    num2 = tk.Variable()
    entry_num2 = tk.Entry(lb_division, textvariable=num2)
    entry_num2.place(x = 50, y = 100)
    #llamamos a la funcion obtener variable para hacer la suma 
    btn_obtener_valor = tk.Button(lb_division, text="Obtener valor", command=lambda: obtener_valor_division(num1.get(), num2.get()))
    btn_obtener_valor.place(x=10, y=150)
    
    btn_volver_division = tk.Button(lb_division, text="Volver", command=volver)
    btn_volver_division.place(x=10, y=10)
    
    btncerrar_division = tk.Button(lb_division, text="Salir del programa", command=Cerrar_todo)
    btncerrar_division.place(x=40, y=40)
    
    lb_division.mainloop()
    
        
bt_suma = tk.Button(text = "SUMA", command = Suma)
bt_suma.place(x = 10, y = 10)
btn_resta = tk.Button(text = "RESTA", command = Resta)
btn_resta.place(x = 150, y = 10)
btn_div = tk.Button(text= "DIVISION",command = divison)
btn_div.place(x=10, y = 50)
btn_multi = tk.Button(text = "Multiplicacion", command = Multiplicacion)
btn_multi.place(x = 150, y = 50)
btn_cerrar = tk.Button(text = "CERRAR", command= Cerrar_todo)
btn_cerrar.place(x = 100, y = 200)
raiz.mainloop()

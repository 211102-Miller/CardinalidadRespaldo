import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

from markupsafe import re
import random

import AB1,BB1,BC1,BEyCE,CC1,CD1,DB1
#Ordenamiento
import EE1,EF1,FF1,FG1,FH1,FI1,GG1,GH,HF,HH
#Cardinalidad
import II1,IJ1,JJ,JK,JO,KK,KL,LL1, LM,LO,MM,MN,NL

class VentanaPrincipal:
    # la cinta 1 almacenara el universo donde se encuantran los elementos
    cinta2 = ['B','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','B']
        #cinta1 = ['0','1','2','3','4','5','6','7','8','9','B']
        # la cinta2 almacenara la expresion de union que el usuario ingreso 
    

        # la cinta 3 almacenara el resultado de la union de los conjuntos(aun no se an eliminado elementos repetidos)
    cinta3 = ['B']

    cinta4= ['0','1','2','3','4','5','6','7','8','9','B']

    cinta5 = ['B']

    cinta6 =['B']
    cinta1=[]
    cabezales = [0,0,0,0,0,0]
    def __init__(self, master):
        
        self.master = master
        master.title("Conjunto Cardinalidad")
        master.geometry('600x400')
        master['bg']='#BEBEBE'

        # Crear los botones
        style = ttk.Style()
        style.configure('my.TButton', font=('Arial', 12), foreground='black', background='black', padding=3)
        self.button1 = ttk.Button(master, text="Consulta", style='my.TButton', command=self.mostrar_vista1)
        self.button1.place(x=175, y=175)

        self.button2 = ttk.Button(master, text="Quiz",style='my.TButton', command=self.mostrar_vista2)
        self.button2.place(x=325, y=175)

    def mostrar_vista1(self):
        # Crear la vista 1
        vista1 = tk.Toplevel(self.master)
        vista1.title("calculadora de cardinalidad")
        vista1.geometry('400x100')
        vista1['bg']='#BEBEBE'
        entrada = tk.Entry(vista1)
        entrada.pack(pady=10)

        # Definir una función para mostrar el contenido del Entry en un Label
        def mostrar_contenido():
            contenido = entrada.get()
            for caracter in contenido:
                self.cinta1.append(caracter)
            self.cinta1.append("B")
            print(self.cinta1)
            self.maquina_Turing()
            
            
            if self.cinta6[1]=='B':
                 messagebox.showinfo("Resultado", f"Su cardinalidad es: {self.cinta6[0]}.")
                 self.cinta6 =['B']
                 self.cinta1=[]
                 self.cinta5=['B']
                 self.cabezales=[0,0,0,0,0,0]
                 self.cinta3 = ['B']

            else:
                 messagebox.showinfo("Resultado", f"Su cardinalidad es: {self.cinta6[0]}{self.cinta6[1]}.")
                 self.cinta6 =['B']
                 self.cinta1=[]
                 self.cinta5=['B']
                 self.cabezales=[0,0,0,0,0,0]
                 self.cinta3 = ['B']
           
            vista1.destroy()

        # Crear un botón para mostrar el contenido del Entry
        mi_Label = Label(vista1, text="Ingrese el conjunto")
        mi_Label.place(x=25, y=10)
        boton = tk.Button(vista1, text='Mostrar contenido', command=mostrar_contenido)
        boton.pack(pady=10)

        # Crear un Label para mostrar el contenido del Entry

    def mostrar_vista2(self):
        conjuntos = ['{t,p,h,t}', '{a,b,v}', '{i,x,w,w,e,f}', '{a,q,w,t,g,a,q}','{a,a,a,a}','{b}','{a,b,a,c,d,t,l,e,e}']
        for i in range(6):
            conjunto_Quiz=random.choice(conjuntos)
        for caracter in conjunto_Quiz:
                self.cinta1.append(caracter)
        print(conjunto_Quiz)
        # Crear la vista 2
        self.vista2 = tk.Toplevel(self.master)
        self.vista2.title("Conjunto Cardinalidad")
        self.vista2.geometry('400x100')
        self.vista2['bg']='#BEBEBE'

        self.pregunta = f"¿Cuál es la cardinalidad de {conjunto_Quiz}?"
        #self.cinta1[conjunto_Quiz]
        self.maquina_Turing()
        if self.cinta6[1]=='B':
            resultado=self.cinta6[0]
        else:
            resultado=self.cinta6[0],self.cinta6[1]
        print(self.cinta6[0],self.cinta6[1])
        self.respuesta_correcta =resultado
        print(f"El resultado es: {self.respuesta_correcta}")
        print(self.cinta6[0])
        
        self.label = tk.Label(self.vista2, text=self.pregunta)
        self.label.pack()
        
        self.entry = tk.Entry(self.vista2)
        self.entry.pack()
        
        self.button = tk.Button(self.vista2, text="Responder", command=self.comprobar_respuesta)
        self.button.pack()
        
        
    def comprobar_respuesta(self):
        respuesta_usuario = int(self.entry.get())
        print(respuesta_usuario)
        if str(respuesta_usuario) == str(self.respuesta_correcta):
            messagebox.showinfo("Respuesta Correcta", "¡Respuesta correcta!")
            self.cinta1=[]
            self.cabezales=[0,0,0,0,0,0]
            self.cinta5=['B']
            self.cinta3 = ['B']
            self.cinta6=['B']
        else:
            messagebox.showerror("Respuesta Incorrecta", f"La respuesta correcta es {self.respuesta_correcta}")
            self.cinta1=[]
            self.cabezales=[0,0,0,0,0,0]
            self.cinta5=['B']
            self.cinta3 = ['B']
            self.cinta6=['B']
        self.vista2.destroy()
    
    def maquina_Turing(self):
        

        #son los cabezales de cada cinta
       

        # estado final
        def B_final():
            
            self.cinta5.append("B")
            self.cinta6.append("B")

            if self.cabezales[0] != 0:
                self.cinta3.append("B")
                print("C3")
            elif self.cabezales[1] != 0:
                self.cinta5.append("B")
                print("C5")
            elif self.cabezales[2] != 0:
                self.cinta6.append("B")
                print("C6")






        #trancision = AB.trancicion + BB.trancicion + BC.transicion + BG.transicion + CC.transicion + CD.trasicion + DD.transicion + DE.transicion + DG.transicion + EE.transicion + EF.transicion + FD.transicion
        #trancision = trancicionAconB.trancicion + trancicionBconB.trancicion + trancicionBconC.trancicion + trancicionBconD.trancicion + trancicionBconF.trancicion + trancicionCconC.trancicion + trancicionCconD.trancicion + trancicionDconB.trancicicon + trancicionDconD.trancicion
        trancision = AB1.transicion + BB1.transicion + BC1.transicion + BEyCE.transicion + CC1.transicion + CD1.transicion +DB1.transicion + EE1.transicion + EF1.transicion + FF1.transicion +FG1.transicion + FH1.transiciones +FI1.transicion + GG1.transicion +GH.transicion + HF.transiciones + HH.transicion +II1.transicion + IJ1.transicion + JJ.transicion + JK.transicion +JO.transicion +KK.transicion +KL.transicion + LL1.transicion  +LM.transicion +LO.transicion +MM.transicion + MN.transicion +NL.transicion

        #mover cabezal
        def mover_derecha(cual):
            self.cabezales[cual] += 1
            print('cabezal:',cual,'  - D')

        #mover cabezal a la izquierda
        def mover_inquierda(cual):
            self.cabezales[cual] -= 1
            print('cabezal:',cual,'  - I')

        #identifica si el cabezal va a la derecha o a la izquierda
        def identificar_D_I_cabezal(e): #pasar el numero de trancision
        
            if trancision[e][1][7] == 'D':
                mover_derecha(0)
            elif trancision[e][1][7] == 'I':
                mover_inquierda(0)
            elif trancision[e][1][7] == 'S':
                print('no se mueve el cabezal1')

            if trancision[e][1][8] == 'D':
                mover_derecha(1)
            elif trancision[e][1][8] == 'I':
                mover_inquierda(1)
            elif trancision[e][1][8] == 'S':
                print('no se mueve el cabezal2')

            if trancision[e][1][9] == 'D':
                mover_derecha(2)
            elif trancision[e][1][9] == 'I':
                mover_inquierda(2)
            elif trancision[e][1][9] == 'S':
                print('no se mueve el cabezal3')

            if trancision[e][1][10] == 'D':
                mover_derecha(3)
            elif trancision[e][1][10] == 'I':
                mover_inquierda(3)
            elif trancision[e][1][10] == 'S':
                print('no se mueve el cabezal4')

            if trancision[e][1][11] == 'D':
                mover_derecha(4)
            elif trancision[e][1][11] == 'I':
                mover_inquierda(4)
            elif trancision[e][1][11] == 'S':
                print('no se mueve el cabezal5')

            if trancision[e][1][12] == 'D':
                mover_derecha(5)
            elif trancision[e][1][12] == 'I':
                mover_inquierda(5)
            elif trancision[e][1][12] == 'S':
                print('no se mueve el cabezal6')           


        #se genera la logica de la maquina de turing para
        #el error esta en que lo pongo en la posicion 0 por lo que pone primero { B depues a { B
        def rellenar_cinta3():
            estatado_actual = 'A'
            arreglo_auxiliar = []
            numero_elementos = 5000
            print(self.cinta3)
            numero_transiciones = len(trancision)
            for i in range(numero_elementos):
                arreglo_auxiliar.append(estatado_actual)
                arreglo_auxiliar.append(self.cinta1[self.cabezales[0]])
                arreglo_auxiliar.append(self.cinta2[self.cabezales[1]])
                arreglo_auxiliar.append(self.cinta3[self.cabezales[2]])
                arreglo_auxiliar.append(self.cinta4[self.cabezales[3]])
                arreglo_auxiliar.append(self.cinta5[self.cabezales[4]])
                arreglo_auxiliar.append(self.cinta6[self.cabezales[5]])


                for e in range(numero_transiciones):
                    if trancision[e][0] == arreglo_auxiliar:
                        print(trancision[e][0],' == ', arreglo_auxiliar)
                        print(trancision[e][1][0])
                        estatado_actual = trancision[e][1][0]
                        self.cinta1[self.cabezales[0]] =  trancision[e][1][1]
                        self.cinta2[self.cabezales[1]] =  trancision[e][1][2]
                        self.cinta3[self.cabezales[2]] =  trancision[e][1][3]
                        self.cinta4[self.cabezales[3]] =  trancision[e][1][4]
                        self.cinta5[self.cabezales[4]] =  trancision[e][1][5]
                        self.cinta6[self.cabezales[5]] =  trancision[e][1][6]
                        identificar_D_I_cabezal(e)
                        print(self.cabezales)

                        B_final()

                        arreglo_auxiliar = []

                        break
            
        
        def main():
            
            print(len(trancision))
            print(self.cabezales)
            rellenar_cinta3()
            print('cinta3: ', self.cinta3)
            print('cinta5: ',self.cinta5)
            print('cinta6: ',self.cinta6)
            
            
        main()          
                    
                    
                    





root = tk.Tk()
mi_ventana = VentanaPrincipal(root)
root.mainloop()
import AB1
import BB1
import BC1
import BEyCE
import CC1
import CD1
import DB1
#Ordenamiento
import EE1
import EF1
import FF1
import FG1
import FH1
import FI1
import GG1
import GH
import HF
import HH
#Cardinalidad
import II1
import IJ1
import JJ
import JK
import JO
import KK
import KL
import LL1
import LM
import LO
import MM
import MN
import NL



# la cinta 1 almacenara el universo donde se encuantran los elementos
cinta2 = ['B','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','B']
#cinta1 = ['0','1','2','3','4','5','6','7','8','9','B']
# la cinta2 almacenara la expresion de union que el usuario ingreso 
cinta1 = ['{','a','b','c','d','e','f','g','h','i','j','k','l','}']

# la cinta 3 almacenara el resultado de la union de los conjuntos(aun no se an eliminado elementos repetidos)
cinta3 = ['B']

cinta4= ['0','1','2','3','4','5','6','7','8','9','B']

cinta5 = ['B']

cinta6 =['B']

#son los cabezales de cada cinta 
cabezales = [0,0,0,0,0,0]

# estado final
def B_final():
    cinta5.append("B")
    cinta6.append("B")
    
    if cabezales[0] != 0:
        cinta3.append("B")
        print("C3")
    elif cabezales[1] != 0:
        cinta5.append("B")
        print("C5")
    elif cabezales[2] != 0:
        cinta6.append("B")
        print("C6")
    





#trancision = AB.trancicion + BB.trancicion + BC.transicion + BG.transicion + CC.transicion + CD.trasicion + DD.transicion + DE.transicion + DG.transicion + EE.transicion + EF.transicion + FD.transicion
#trancision = trancicionAconB.trancicion + trancicionBconB.trancicion + trancicionBconC.trancicion + trancicionBconD.trancicion + trancicionBconF.trancicion + trancicionCconC.trancicion + trancicionCconD.trancicion + trancicionDconB.trancicicon + trancicionDconD.trancicion
trancision = AB1.transicion + BB1.transicion + BC1.transicion + BEyCE.transicion + CC1.transicion + CD1.transicion +DB1.transicion + EE1.transicion + EF1.transicion + FF1.transicion +FG1.transicion + FH1.transiciones +FI1.transicion + GG1.transicion +GH.transicion + HF.transiciones + HH.transicion +II1.transicion + IJ1.transicion + JJ.transicion + JK.transicion +JO.transicion +KK.transicion +KL.transicion + LL1.transicion  +LM.transicion +LO.transicion +MM.transicion + MN.transicion +NL.transicion

#mover cabezal
def mover_derecha(cual):
    cabezales[cual] += 1
    print('cabezal:',cual,'  - D')

#mover cabezal a la izquierda
def mover_inquierda(cual):
    cabezales[cual] -= 1
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
    print(cinta3)
    numero_transiciones = len(trancision)
    for i in range(numero_elementos):
        arreglo_auxiliar.append(estatado_actual)
        arreglo_auxiliar.append(cinta1[cabezales[0]])
        arreglo_auxiliar.append(cinta2[cabezales[1]])
        arreglo_auxiliar.append(cinta3[cabezales[2]])
        arreglo_auxiliar.append(cinta4[cabezales[3]])
        arreglo_auxiliar.append(cinta5[cabezales[4]])
        arreglo_auxiliar.append(cinta6[cabezales[5]])


        for e in range(numero_transiciones):
            if trancision[e][0] == arreglo_auxiliar:
                print(trancision[e],' == ', arreglo_auxiliar)
                print(trancision[e][1][0])
                estatado_actual = trancision[e][1][0]
                cinta1[cabezales[0]] =  trancision[e][1][1]
                cinta2[cabezales[1]] =  trancision[e][1][2]
                cinta3[cabezales[2]] =  trancision[e][1][3]
                cinta4[cabezales[3]] =  trancision[e][1][4]
                cinta5[cabezales[4]] =  trancision[e][1][5]
                cinta6[cabezales[5]] =  trancision[e][1][6]
                identificar_D_I_cabezal(e)
                print(cabezales)

                B_final()

                arreglo_auxiliar = []
            
                break

    







def main():
    print(len(trancision))
    print(cabezales)
    rellenar_cinta3()
    print('cinta3: ', cinta3)
    print('cinta5: ',cinta5)
    print('cinta6:', cinta6)    
    


   


main()
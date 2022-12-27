# This Python file uses the following encoding: utf-8
import PySimpleGUI as sg # on importe les modules depuis PysimpleGui


def ConversionMachine(nb,mode):  # On définit toutes les convertions qu'on veut faire
    try: 
        if mode == "BIN2DEC" :   # ici pour passer de binaire à decimal 
            decimal= int(nb,2) # on doit d'abord convertir le "str" en "int"
            return (str(decimal)) # après cela on retourne le résultat en "str"

        elif mode == "DEC2BIN":  # ici pour passer de decimal à binaire
            decimal= int(nb)    # on le convertit d'abord en "int"
            binaire = (bin(decimal)) # ensuite on le tranforme en binaire en utilisant la fonction "bin() préexistante"
            return (str(binaire)) # après cela on retourne le résultat en "str"

        elif mode == "BIN2HEX": # ici pour passer de binaire à hexadécimale
            binaire = int(nb,2) # on le convertit en "int"
            hexa = (hex(binaire)) # on convertit  ce résultat en hexadécimal avec la fonction "hex()" préexistante
            return (str(hexa)) # après cela on retourne le résultat en "str"
        
        elif mode == "HEX2BIN":# ici pour passer de héxadécimale à binaire
            hexa = int(nb,16) # on le convertit en "int"
            binaire = (bin(hexa)) # ensuite on le tranforme en binaire en utilisant la fonction "bin() préexistante"
            return (str(binaire))# après cela on retourne le résultat en "str"

        elif mode == "DEC2HEX":# ici pour passer de decimal à hexadécimale
            decimal = int(nb,10) # on le convertit en "int"
            hexa = hex(decimal) #on convertit  ce résultat en hexadécimal avec la fonction "hex()" préexistante
            return (str(hexa))# après cela on retourne le résultat en "str"
        
        elif mode == "HEX2DEC":# ici pour passer de decimal à binaire
            hexa = int(nb,16) # on le convertit en "int"
            decimal= (int(hexa)) 
            return (str(hexa))# après cela on retourne le résultat en "str"
    except ValueError: # si il y'a une erreur causé par une valeur entré pas adéquate à la convertion choisie
        erreur = "Vous n'avez pas entrer la bonne valeur pour le mode choisi"
        return erreur

def addition(nb1,nb2): # fonction pour addtioner des valeurs binaires
    calcul = int(nb1,2) + int(nb2,2) # on transforme les deux valeurs binaire et int puis on les addtionne
    res = (bin(calcul)) # ensuite on le convertit au format binaire
    return((str(res))) # après cela on retourne le résultat en "str"

def multiplication(nb1,nb2): # fonction pour multiplier des valeurs binaires
    calcul = (int(nb1,2)) * (int(nb2,2))
    res = (bin(calcul))
    return((str(res)))

def soustraction(nb1,nb2): # fonction pour soustraire des valeurs binaires
    calcul = (int(nb1,2)) - (int(nb2,2))
    res = (bin(calcul))
    return((str(res)))

def interface3(): 
    while True:
        event, values = window3.read() 
        print(event, values)
        
        if event in  (None, 'Exit'):
            break
        
        if event == "ENTREZ": # lorsqu'in click sur "ENTREZ", la fenêtre se cache et la première interface s'ouvre
            window3.Hide()
            interface1()


def interface2():
    if interface2.open == True:
        window2.UnHide()
    interface2.open = True
    while True:
        event, values = window2.read()
        print(event, values)
        
        if event in  (None, 'Exit'):
            window.close() # lorqu'on click sur "Exit", les deux interfaces se ferment
            window2.close()
            break

        
        if event == 'ADDITION':
            res = addition(values['nb1'],values['nb2'])# on transforme les valeurs entrées avec la fonction défini avant
            res_dec = int(res,2)
            hexa = int(res,2)
            res_hex = (hex(hexa))
            window2['-OUTPUT-'].update(res) # on fait apparaître la clé 
            window2['OUTPUT2'].update(res_dec) # on fait apparaître la clé 
            window2['OUTPUT3'].update(res_hex)# on fait apparaître la clé 

        
        if event == 'MULTIPLICATION':
            res = multiplication(values['nb1'],values['nb2']) # on transforme les valeurs entrées avec la fonction défini avant
            res_dec = int(res,2)
            hexa = int(res,2)
            res_hex = (hex(hexa))
            window2['-OUTPUT-'].update(res)# on fait apparaître la clé 
            window2['OUTPUT2'].update(res_dec)# on fait apparaître la clé 
            window2['OUTPUT3'].update(res_hex)# on fait apparaître la clé 

        if event == 'SOUSTRACTION':
            res = soustraction(values['nb1'],values['nb2']) # on transforme les valeurs entrées avec la fonction défini avant
            res_dec = int(res,2)
            hexa = int(res,2)
            res_hex = (hex(hexa))
            window2['-OUTPUT-'].update(res)# on fait apparaître la clé 
            window2['OUTPUT2'].update(res_dec)# on fait apparaître la clé 
            window2['OUTPUT3'].update(res_hex)# on fait apparaître la clé 
            

        if event == "RETURN": # lorqu'on click sur return on cache l'interface 2 et on ouvre l'interface 1
            window2.Hide() 
            window.UnHide()
            interface1()

def interface1():
    while True:
        event, values = window.read()
        print(event, values)
        
        if event in (None, 'Exit'):
            window.close()
            window2.close()
            break
            
        
        if event == 'BIN2DEC':
            res = ConversionMachine(values['-IN-'],event)# on transforme la valeur entrer avec la fonction défini avant
            window['-OUTPUT-'].update(res)  # on fait apparaître la clé avec notre résultat
        
        if event == 'DEC2BIN':
            res = ConversionMachine(values['-IN-'],event)# on transforme la valeur entrer avec la fonction défini avant
            window['-OUTPUT-'].update(res) # on fait apparaître la clé avec notre résultat

        if event == 'BIN2HEX':
            res = ConversionMachine(values['-IN-'],event)# on transforme la valeur entrer avec la fonction défini avant
            window['-OUTPUT-'].update(res) # on fait apparaître la clé avec notre résultat

        if event == 'HEX2BIN':
            res = ConversionMachine(values['-IN-'],event) # on transforme la valeur entrer avec la fonction défini avant
            window['-OUTPUT-'].update(res)# on fait apparaître la clé avec notre résultat
        
        if event == 'DEC2HEX':
            res = ConversionMachine(values['-IN-'],event) # on transforme la valeur entrer avec la fonction défini avant
            window['-OUTPUT-'].update(res)# on fait apparaître la clé avec notre résultat

        if event == 'HEX2DEC':
            res = ConversionMachine(values['-IN-'],event) # on transforme la valeur entrer avec la fonction défini avant
            window['-OUTPUT-'].update(res) # on fait apparaître la clé avec notre résultat
        
        if event == 'DEC2HEX':
            res = ConversionMachine(values['-IN-'],event) # on transforme la valeur entrer avec la fonction défini avant
            window['-OUTPUT-'].update(res) # on fait apparaître la clé avec notre résultat



        if event == "CALCULS": # si on click sur “calcul“ on cache l'interface 1 et on ouvre l'interface 2
            window.Hide()
            interface2()


# Programme principal

import PySimpleGUI as sg
      
sg.theme('DarkPurple1') # le thème de couleur choisi
   
layout3= [[sg.Text('BIENVENUE SUR NSI WORLD', justification='center',size=(100,1), font=("Chalkboard"))],[sg.Text('Ces interfaces ont été crée dans le but de faciliter vos calcul en utilisant le sytème binaire ou héxadécimal.',justification='center',size=(100,1), font=("Chalkboard"))], [sg.Text(" Nous espérons que cela vous sera utile!",justification='center',size=(100,1), font=("Chalkboard"))],[ sg.Text(" Bonne Navigation!", justification='center',size=(100,1), font=("Chalkboard"))],  [sg.Button('ENTREZ', pad=(380, 0), font=("Chalkboard"))]]
# ici on a défini tous les boutons pour notre page d'accueil
  
window3 = sg.Window('ACCUEIL', layout3) # le nom en haut marge de l'interface

sg.theme('DarkPurple1')# le thème de couleur choisi

layout = [[sg.Button('BIN2DEC',font=("Chalkboard")), sg.Button('DEC2BIN',font=("Chalkboard")),
        sg.Button('DEC2HEX',font=("Chalkboard"))],
        [sg. Button('BIN2HEX',font=("Chalkboard")), sg.Button('HEX2BIN',font=("Chalkboard")),sg.Button('HEX2DEC',font=("Chalkboard"))],
        [sg.Text('Valeur à convertir',font=("Chalkboard"))],
        [sg.Input(key='-IN-')],
        [sg.Text('Résultat',font=("Chalkboard")),
		sg.Text(size=(50,2), key='-OUTPUT-')],
        [ sg.Button('Exit',font=("Chalkboard")), sg.Button('CALCULS',font=("Chalkboard"))]]
# ici on a défini tous les boutons et les clé qu'on va récuperer pour effectuer les convertions
window = sg.Window('Machine à Convertir', layout) # le nom en haut marge de l'interface

sg.theme('DarkPurple1') # le thème de couleur choisi
   
layout2 = [[sg.Button('ADDITION',font=("Chalkboard")),sg.Button('MULTIPLICATION',font=("Chalkboard")),sg.Button('SOUSTRACTION', font=("Chalkboard"))],
            [sg.Text('Entrez votre premier valeur en binaire:',font=("Chalkboard"))],
           [sg.Input(key='nb1')],
           [sg.Text('Entrez votre seconde valeur en binaire:',font=("Chalkboard"))],
          [sg.Input(key='nb2')],
          [sg.Text('Résultats:',font=("Chalkboard")),
           sg.Text(size=(15,1), key='-OUTPUT-')],[sg.Text('Décimal:',font=("Chalkboard")),
           sg.Text(size=(15,1), key='OUTPUT2')],[sg.Text('Héxadécimal:',font=("Chalkboard")),
           sg.Text(size=(15,1), key='OUTPUT3')],
           [sg.Button('Exit',font=("Chalkboard")),sg.Button('RETURN',font=("Chalkboard"))]]
# ici on a défini tous les boutons et les clé qu'on va récuperer pour effectuer les calculs
window2 = sg.Window('Calculatrice Binaire', layout2) # le nom en haut marge de l'interface



interface2.open = False
interface3()

window.close() #  on ferme les fenetres
window2.close()

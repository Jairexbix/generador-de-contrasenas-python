import random

def generador_contraseña (len,numeros,especiales):
    caracteres_simples = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM'
    num = '1234567890'
    esp = '@#$%&/?¿*'
    contraseña = ''
    
    if numeros == True and especiales == True:
        caracteres_selecionados = caracteres_simples + num + esp
    elif numeros == True and especiales == False:
        caracteres_selecionados = caracteres_simples + num
    elif numeros == False and especiales == True:
        caracteres_selecionados = caracteres_simples + esp
    else:
        caracteres_selecionados = caracteres_simples
    
    for _ in range(len):
        caracter = random.choice(caracteres_selecionados)
        contraseña += caracter
    
    return contraseña

def contraseña_con_numeros ():
    res = int(input('Escriba 1 si quiere que tenga numeros, 0 si no quiere que los tenga: '))
    if res == 1:
        return True
    else:
        return False

def contraseña_con_especiales ():
    res = int(input('Escriba 1 si quiere que tenga caracteres especiales, 0 si no quiere que los tenga: '))
    if res == 1:
        return True
    else:
        return False

longitud = int(input('Ingrese la longitud deseada de la contraseña: '))
numeros = contraseña_con_numeros()
especiales = contraseña_con_especiales()
contraseña_generada = generador_contraseña(longitud,numeros,especiales)

print(contraseña_generada)
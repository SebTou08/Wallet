import requests
from os import system
import time 
from datetime import datetime


def esmoneda(cripto):
    return cripto in monedas

monedas=()
monedas_dict={}

COINMARKET_API_KEY = "2448e9c9-b938-4f0e-85f1-9878a7b41c87"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
  monedas_dict[cripto["symbol"]]=cripto["name"]

monedas = monedas_dict.keys()
saldoTotal = 0#saldo inicial
moneda = ""
i =1#contador 
dia = datetime.now()
dia = dia.strftime(" %d/%m/%Y ")#variable para mostrar la fecha
lista_monedas= list() #lista que contrendrá el diccionario declarado abajo
moneda_dic = {} #Creando un diccionario


############################################################################
############# F U N C I O N E S Y/O PROCEDIMIENTOS  ########################
############################################################################ 

#valida que el symbol ingresado pertenezca a una moneda valida 
def validarMoneda():
  global moneda


  moneda = input("Ingrese symbol de la moneda : ")
  while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
  return True
  


#funcion para recibir finero
def recibirDinero():
  #variables globales
    global saldoTotal
    global moneda
    global i
    global dia 
    global lista_monedas
    global moneda_dic

    
    if validarMoneda(): #si la moneda es valida...
      cantidad = float(input("Ingrese cantidad a recibir: "))
      codigo  = int (input("Ingrese codigo: "))
      archivo = open("Transaccionesrecibidas.txt", "a")
      registr  = "Moneda: " + moneda + "    Cantidad: " + str(cantidad)+ "       Codigo: "+ str(codigo)
      archivo.write(registr)
      print ("datos guardados correctamente")
      time.sleep(2.2)
      system("clear")
      saldoTotal = saldoTotal+cantidad
      historico = open ("Historico.doc", "a")
      histor = "\n\n "+str(i)+ "-. \nFecha: "+ dia + " \nMoneda: " + str(moneda) + "\nTipo de operacion: Recibimiento "+ "\nCodigo de usuario: "+ str(codigo) + "\nCantidad recibida: "+ str(cantidad) + "\nSaldo al momento: "+ str(saldoTotal)
      historico.write(histor)
      i=i+1
      #se agregan las carateristicas nombre, operacion, monto y codigo al diccionario
      moneda_dic["nombre"] = moneda
      moneda_dic["operacion"] = "Recibimiento"
      moneda_dic["monto"] = cantidad
      moneda_dic["codigo"] = codigo
      #se agrega el diccionario lleno a la lista de monedas
      lista_monedas.append(moneda_dic)

#funcion para transferir dinero
def transferirDinero():
  #variables globales
    global saldoTotal
    global moneda
    global dia 
    global i
    global lista_monedas
    global moneda_dic
   

    if validarMoneda():#si la moneda es valida...
      
      cantidad = float(input("Ingrese cantidad a transferir: "))
      codigo  = int (input("Ingrese codigo del destinatario: "))
      archivo = open("Transacciones.txt", "a")
      print ("Transferencia realizada correctamente")
      time.sleep(2.2)
      system("clear")
      saldoTotal = saldoTotal-cantidad
      historico = open ("Historico.doc", "a")
      histor = "\n\n "+str(i)+ "-. \nFecha: "+ dia + " \nMoneda: " + moneda + "\nTipo de operacion: Transferencia "+ "\nCodigo de destinatario: "+ str(codigo) + "\nCantidad transferida: "+ str(cantidad) + "\nSaldo al momento: "+ str(saldoTotal)
      historico.write(histor)
      archivo.write(histor)
      i=i+1
      #se guardan llena el diccionario con datos 
      moneda_dic["nombre"] = moneda
      moneda_dic["operacion"] = "Tansferencia"
      moneda_dic["monto"] = cantidad
      moneda_dic["codigo"] = codigo
      #se agrega el diccionario a la lista
      lista_monedas.append(moneda_dic)





#funcion para mostrar transacciones
def mostrarTransacciones():
    print ("Se guardo el total de transacciones en un aarchivo llamado ""Transacciones.txt")
    opcion = int (input("Dese ver el historial en la consola? \n 1-. Si \n 2-. No"))
    if opcion == 1:
      archivo = open("Transacciones.txt", "r")
      while True: #ciclo infinito o hasta que encuentre un "break"
        linea = archivo.readline() #obtiene linea a linea
        if not linea: #en caso no hayan lineas
          break #acaba el ciclo
        print (linea) #imprime linea

def balanceGeneral():
  print ("Se guardo el balance general en el documento llamado ""Historico.doc")
  opcion = int (input("Dese ver el historial en la consola? \n 1-. Si \n 2-. No"))
  if opcion == 1:
    archivo = open("Historico.doc", "r")
    while True: #mientras que no se encuentre algun "break"
      linea = archivo.readline() #obtiene las lineas
      if not linea: 
        break#salir del ciclo
      print (linea)

def balanceUnitario():
  #variables globales
    global saldoTotal
    global moneda
    global dia 
    global i
    global lista_monedas
    global moneda_dic
    monedaBuscar = moneda #moneda a buscar
    if validarMoneda():
      #ciclo para recorrer la lista de monedas
      for i in lista_monedas: 
        #si el dato "nombre" del diccionario coincide con la moneda a buscar...
        if moneda_dic["nombre"] == monedaBuscar: 
          print ("\n \n  MOneda: "+ moneda_dic["nombre"]+"\n Monto: "+str(moneda_dic["monto"])+ "\n Tipo de operacion: "+ moneda_dic["operacion"] + "\n Codigo: "+ str(moneda_dic["codigo"]))
          time.sleep(1.2)
          print("\n \n ")
        else:
          continue




#funcion principal
def main():

  interactuar = True
  #ciclo dell menu, se ejecutará hasta que interactuar sea falso
  while(interactuar):
    
    opcion = int(input("Que desea hacer? \n1-.Recibir dinero \n 2-.Transferir dinero \n 3-.Monstrar balance (una moneda) \n 4-.Mostrar balance (general) \n 5-.Mostrar historial de transacciones \n 6-.Salir\n"))
    if opcion == 1:
      system("clear")
      recibirDinero()
    elif opcion ==2:
      system("clear")
      transferirDinero()
    elif opcion==3:
      system("clear")
      balanceUnitario()
    elif opcion == 4: 
      system("clear")
      balanceGeneral()
    elif opcion == 5:
      system("clear")
      mostrarTransacciones()
    elif opcion == 6:
      interactuar = False
    elif opcion == 0 :
      system("clear")
      print(saldoTotal)
      time.sleep(3)
      system("clear")
      

print (" \n \n \n \n \n \t Bienvenido a tu billetera digital: ")
time.sleep(1.5)
#funcion principal
main()



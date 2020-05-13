import hashlib
import json
from tkinter import *

raiz = Tk()

block_genesis = {
 'prev_hash': None,
 'transactions': []
}
#Informacion y hasheo del bloque recien creado
a = block_genesis_serialized = json.dumps(block_genesis, sort_keys=True).encode('utf-8')
b = block_genesis_hash = hashlib.sha256(block_genesis_serialized).hexdigest()

block_2 = {
 'prev_hash': block_genesis_hash,
 'transactions': []
} 
c = block_2_serialized = json.dumps(block_2, sort_keys=True).encode('utf-8')
d = block_2_hash = hashlib.sha256(block_2_serialized).hexdigest()

block_3 = {
 'prev_hash': block_2_hash,
 'transactions': []
}

def hash_blocks(blocks):
 prev_hash = None
 for block in blocks:
  block['prev_hash'] = prev_hash
  block_serialized = json.dumps(block, sort_keys=True).encode('utf-8')
  block_hash = hashlib.sha256(block_serialized).hexdigest()
  prev_hash = block_hash
 return prev_hash


def ingresoVoto():

  print("Hash de la blockchain")
  print(hash_blocks([block_genesis, block_2, block_3]))

  def b3():
    voto = input()
    if voto != "2":
      block_3['transactions'].append(voto)
      b3()
    else:
      resultados()

  def b2():
    voto = input()
    if voto != "2":
      block_2['transactions'].append(voto)
      b2()
    else:
      b3()

  def b1():
    voto = input()
    if voto != "2":
      block_genesis['transactions'].append(voto)
      b1()
    else:
      b2()
  b1()



votDep1 = 0
cont00 = 0
cont01 = 0 

votDep2 = 0
cont10 = 0
cont11 = 0 

votDep3 = 0
cont20 = 0
cont21 = 0

for i in range(len(block_genesis['transactions'])):
  if(block_genesis['transactions'][i] == "0"):
    cont00 = cont00 + 1
  else:
    cont01 = cont01 + 1

for i in range(len(block_2['transactions'])):
  if(block_2['transactions'][i] == "0"):
    cont10 = cont10 + 1
  else:
    cont11 = cont11 + 1

for i in range(len(block_3['transactions'])):
  if(block_3['transactions'][i] == "0"):
    cont20 = cont20 + 1
  else:
    cont21 = cont21 + 1  


def resultados():

    
  votDep1 = 0
  cont00 = 0
  cont01 = 0 

  votDep2 = 0
  cont10 = 0
  cont11 = 0 

  votDep3 = 0
  cont20 = 0
  cont21 = 0

  print("resultados")
  
  for i in range(len(block_genesis['transactions'])):
    if(block_genesis['transactions'][i] == "0"):
      cont00 = cont00 + 1
    else:
      cont01 = cont01 + 1
      
  #Informacion y hasheo del bloque recien creado
  a = block_genesis_serialized = json.dumps(block_genesis, sort_keys=True).encode('utf-8')
  b = block_genesis_hash = hashlib.sha256(block_genesis_serialized).hexdigest()
  print(block_genesis['transactions'])
  print("Hash del bloque: ", b)

  for i in range(len(block_2['transactions'])):
    if(block_2['transactions'][i] == "0"):
      cont10 = cont10 + 1
    else:
      cont11 = cont11 + 1

  c = block_2_serialized = json.dumps(block_2, sort_keys=True).encode('utf-8')
  d = block_2_hash = hashlib.sha256(block_2_serialized).hexdigest()
  print(block_2['transactions'])
  print("Hash del bloque: ", d)

  for i in range(len(block_3['transactions'])):
    if(block_3['transactions'][i] == "0"):
      cont20 = cont20 + 1
    else:
      cont21 = cont21 + 1  

  e = block_3_serialized = json.dumps(block_3, sort_keys=True).encode('utf-8')
  f = block_3_hash = hashlib.sha256(block_3_serialized).hexdigest()
  print(block_3['transactions'])
  print("Hash del bloque: ", f)

  print("Departamento 1: ", cont01," votos para el 1 y ",cont00 ," para el 2")
  print("Departamento 2: ", cont11," votos para el 1 y ", cont10," para el 2")
  print("Departamento 3: ", cont21," votos para el 1 y ", len(block_3['transactions'])-cont21," para el 2")
  print(("El total de votos es: ", len(block_3['transactions'])+len(block_2['transactions'])+len(block_genesis['transactions'])))
  print("La blockchain fnalizó con hash: ",hash_blocks([block_genesis, block_2, block_3]) )
  com1 = cont01+cont11+cont21
  com2 = cont00 + cont10 + cont20
  ganador = ""

  if(com1>com2):
      ganador = "El ganador es el candidato 1"
  elif(com2>com1):
      ganador = "El ganador es el candidato 2"
  else:
      ganador = "Hay un empate"
  return(ganador)


def totVotos():
  if(True):
    string = ("El total de votos es: ", len(block_3['transactions'])+len(block_2['transactions'])+len(block_genesis['transactions']))
  return(string)

def resUno():  
  cont00 = 0
  cont01 = 0 
  for i in range(len(block_genesis['transactions'])):
    if(block_genesis['transactions'][i] == "0"):
      cont00 = cont00 + 1
    else:
      cont01 = cont01 + 1
  return("Departamento 1: ", cont01," votos para el 1 y ",cont00 ," para el 2")

def resDos():
  cont10 = 0
  cont11 = 0 
  for i in range(len(block_2['transactions'])):
    if(block_2['transactions'][i] == "0"):
      cont10 = cont10 + 1
    else:
      cont11 = cont11 + 1
  return("Departamento 2: ", cont11," votos para el 1 y ", cont10," para el 2")

def resTres():
  cont20 = 0
  cont21 = 0
  for i in range(len(block_3['transactions'])):
    if(block_3['transactions'][i] == "0"):
      cont20 = cont20 + 1
    else:
      cont21 = cont21 + 1 
    return("Departamento 3: ", cont21," votos para el 1 y ", len(block_3['transactions'])-cont21," para el 2")

#Interfaz
raiz.title("Sistema de votación")
raiz.geometry("550x470")
frame = Frame(raiz)
frame.pack()

numeroPantalla = StringVar()
pant2 = StringVar()
pant3 = StringVar()
pant4 = StringVar()
pant5 = StringVar()

pantalla = Entry(frame, textvariable=numeroPantalla, width = 40)
pantalla.grid(row = 1, column = 1, padx = 30, pady = 10, columnspan = 3)
pantalla.config(background = "white", fg = "#000000", justify = "center")

pantalla1 = Entry(frame, textvariable=pant2, width = 50)
pantalla1.grid(row = 2, column = 1, padx = 0, pady = 5, columnspan = 3)
pantalla1.config(background = "white", fg = "#000000", justify = "center")

pantalla2 = Entry(frame, textvariable=pant3, width = 50)
pantalla2.grid(row = 3, column = 1, padx = 0, pady = 5, columnspan = 3)
pantalla2.config(background = "white", fg = "#000000", justify = "center")

pantalla3 = Entry(frame, textvariable=pant4, width = 50)
pantalla3.grid(row = 4, column = 1, padx = 0, pady = 5, columnspan = 3)
pantalla3.config(background = "white", fg = "#000000", justify = "center")

pantalla4 = Entry(frame, textvariable=pant5, width = 50)
pantalla4.grid(row = 5, column = 1, padx = 0, pady = 5, columnspan = 3)
pantalla4.config(background = "white", fg = "#000000", justify = "center")

def results():
    numeroPantalla.set(str(resultados()))
    pant2.set(str(totVotos()).replace(",","").replace("'","").replace("(","").replace(")",""))
    pant3.set(str(resUno()).replace(",","").replace("'","").replace("(","").replace(")",""))
    pant4.set(str(resDos()).replace(",","").replace("'","").replace("(","").replace(")",""))
    pant5.set(str(resTres()).replace(",","").replace("'","").replace("(","").replace(")",""))
    boton1.config(state="disabled")
    boton2.config(state="disabled")
    boton3.config(state="disabled")
    boton4.config(state="disabled")
    boton5.config(state="disabled")
    boton6.config(state="disabled")

def nuevaVot():
  boton1.config(state="normal")
  boton2.config(state="normal")
  boton3.config(state="normal")
  boton4.config(state="normal")
  boton5.config(state="normal")
  boton6.config(state="normal")
  block_genesis['transactions'] = []
  block_2['transactions'] = []
  block_3['transactions'] = []
  numeroPantalla.set(str(""))
  pant2.set(str(""))
  pant3.set(str(""))
  pant4.set(str(""))
  pant5.set(str(""))
  

def juanca11():
  block_genesis['transactions'].append("1")

def juanca12():
  block_genesis['transactions'].append("0")

def juanca21():
  block_2['transactions'].append("1")

def juanca22():
  block_2['transactions'].append("0")

def juanca31():
  block_3['transactions'].append("1")

def juanca32():
  block_3['transactions'].append("0")

#Labels

depto1 = Label(frame, text = "Departamento 1")
depto1.grid(row = 6, column = 2)

depto2 = Label(frame, text = "Departamento 2")
depto2.grid(row = 7, column = 2)

depto3 = Label(frame, text = "Departamento 3")
depto3.grid(row = 8, column = 2)

#Botones

boton1 = Button(frame, text = "candidato 1", width = 10, command = juanca11)
boton1.grid(row=6, column = 0, padx = 0, pady = 20)

boton2 = Button(frame, text = "candidato 2", width = 10, command = juanca12)
boton2.grid(row=6, column = 4)

boton3 = Button(frame, text = "candidato 1", width = 10, command = juanca21)
boton3.grid(row=7, column = 0,padx = 0, pady = 20)

boton4 = Button(frame, text = "candidato 2", width = 10, command = juanca22)
boton4.grid(row=7, column = 4)

boton5 = Button(frame, text = "candidato 1", width = 10, command = juanca31)
boton5.grid(row=8, column = 0,padx = 0, pady = 20)

boton6 = Button(frame, text = "candidato 2", width = 10, command = juanca32)
boton6.grid(row=8, column = 4)

boton7 = Button(frame, text = "Finlaizar Votación", width = 19, command = results)
boton7.grid(row=10, column = 2,padx = 0, pady = 20)

boton8 = Button(frame, text = "Nueva Votación", width = 19, command = nuevaVot)
boton8.grid(row=11, column = 2)

raiz.mainloop()
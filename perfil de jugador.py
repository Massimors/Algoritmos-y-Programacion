x=input("Eres chico o chica?")
x=x.lower()
w="Bienvenid"
if x=="chico":
    w+='o'
else:
    w+='a'
print(w, "al mundo de los pokemon!")
y=input("que edad tienes?")
if int(y)<10:
    if x=="chico":
        print("No tienes edad para ser entrenador")
    else:
        print("No tienes edad para ser entrenadora")
        quit()
else:
    print ("Vamos!") 
reg=input("Necesitarás un compañero de viaje. En que region te encuentras?")
if reg=="Kanto" and x =="chico":
    print("tu compañera de viaje es Misty!")
else:
    print("tu compañero de viaje es Brook!")
tipo=input ("que tipo de pokemon quieres para emprezar?")
if tipo=="agua":
    print("tu starter es Osshawott")
elif tipo=="fuego":
    print("tu starter es Cyndaquil")
else:
    print ("tu starter es rowlet")
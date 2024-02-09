harina = float(input("cuantas tazas de harina tienes?: "))
agua = float(input("cuantas tazas de agua tienes?: "))
sal = float(input ("cuantas cucharadas de sal tienes?: "))
aceite = float(input("cuantas cucharadas de aceite tienes: "))

bol = harina + agua + (sal*1/48) 
budare = bol + (aceite * 1/48) 

if aceite == 0.00: 
    print ("te falta aceite")
elif harina == 0.00: 
    print ("te falta harina")
elif agua == 0.00: 
    print ("te falta agua")
elif budare >= 16: 
    print ("puedes hacer 20 arepas")
elif budare >= 8: 
    print ("puedes hacer 10 arepas")
elif budare >= 4: 
    print ("puedes hacer 5 arepas")
else: 
    print ("no tienes suficientes ingredientes")
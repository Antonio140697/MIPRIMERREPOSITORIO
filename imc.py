masa=float(input("ingresa tu masa kilogramos"))
altura=float(input("ingresa tu altura en metros"))
imc=masa/altura**2
print("tu imc es: "+str(imc))

if imc>25 :
    print("sobrepeso")
cant_minutos = int(input("Dijite la cantidad de minutos que duro la llamada")) # Input

if cant_minutos <= 3:

    print("el valor de la llama son 300 pesos")

else:
    valor_llama = 300+50*(cant_minutos-3)  
    

    print(f"El valor de la llamada es: " + str(valor_llama))
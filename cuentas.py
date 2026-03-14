total=0

while True:
    operacion=input("Escribe la operación con la cantidad o listo para terminar: ")

    if operacion =="listo":
        break
    
    try:
        resultado=eval(operacion)
        total+= resultado
    except:
        print("Inválido")

print("Total: ", total)
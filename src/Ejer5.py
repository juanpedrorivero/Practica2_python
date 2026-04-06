
def calcular_envio(peso,zona,dicc):
    if peso<1:
        num = "1"
    elif peso<5:
        num = "2"
    else:
        num = "3"
    print(f"El costo de envio es ${dicc[num][zona]}")
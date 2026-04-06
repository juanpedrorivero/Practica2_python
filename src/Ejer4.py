def Verificacion_email(email):
    if email.count("@") != 1:
        print("El email es invalido")
        return
    
    if email[0] == "@" :
        print("El email es invalido")
        return
    
    pos = email.index("@")
    despues = email[pos+1:]
    
    if "." not in despues:
        print("El email es invalido")
        return
    
    if email.startswith(".") or email.endswith("."):
        print("El email es invalido")
        return
    
    pos = email.rindex(".")
    if len(email[pos+1:]) < 2:
        print("El email es invalido")
        return
    print("Email valido")
    return True
        
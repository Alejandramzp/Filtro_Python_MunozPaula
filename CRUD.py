import json

def crearUsuario():
    with open("Usuarios.json", "r") as outfile:
        crear = json.load(outfile)

    nuevo_usuario = {}
    nuevo_usuario["Id"] = input("Por favor digite el numero de documento del usuario: "),
    nuevo_usuario["Nombre"] = input("Por favor digite el nombre del usuario: "),
    nuevo_usuario["Direccion"] = input("Por favor digite la direccion del usuario: "),
    nuevo_usuario["Numero"] = input("Por favor digite el numero de contacto del usuario:"),
    nuevo_usuario["Fecha de registro"] = input("Por favor digite la fecha en la que se registra el usuario: ")

    crear["Usuarios"].append(nuevo_usuario)

    with open("Usuarios.json", "w") as infile:
        json.dump(crear, infile, indent= 4)
    return crear    
       
def actualizarUsuario():
    with open("Usuarios.json", "r") as outfile:
        actu = json.load(outfile)

    ruta=actu["Usuarios"]
    Id = input("Ingresa el Id del usuario que quieras actualizar: ")

    for i in ruta:
        if i["Id"] == Id:
            i["Id"] = input("Por favor digite el numero de documento del usuario: "),
            i["Nombre"] = input("Por favor digite el nombre del usuario: "),
            i["Direccion"] = input("Por favor digite la direccion del usuario: "),
            i["Numero"] = input("Por favor digite el numero de contacto del usuario:"),
            i["Fecha de registro"] = input("Por favor digite la fecha en la que se registra el usuario: ")
    
    with open("Usuarios.json", "w") as outfile:
        json.dump(ruta, outfile, indent=4)

def eliminarUsuario():
    with open("Usuarios.json", "r") as outfile:
        elimi = json.load(outfile)
    
    ruta=elimi["Usuarios"]
    
    IdElimi = input("Ingresa el id del usuario que quieras eliminar: ")
    
    for usu in ruta:
        if usu["id"] == IdElimi:
            ruta.remove(usu) 
            
    with open("CRUD.json", "w") as outfile:
        json.dump(elimi, outfile, indent=4)





    




    
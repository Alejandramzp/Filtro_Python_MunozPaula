import menu as menu
import CRUD as CRUD

def menuAdministrador():
    while True:
        menu.principal()

        opcion = input("\nSeleccione una opción (1-4): ")
    
        if opcion == "1":       #opcion del menu principal
            menu.usuarios()

            opcion1 = input("\nSeleccione una opción (1-5): ")

            if opcion1 == "1":       #opcion del menu usuarios
                menu.gestionUsuarios()

                opcion2 = input("\nSeleccione una opción (1-5): ")

                if opcion2 == "1":    #opcion del menu gestion usuarios
                    CRUD.crearUsuario()
                    
                elif opcion2 == "2":  #opcion del menu gestion usuarios
                    CRUD.actualizarUsuario()

                elif opcion2 == "3":  #opcion del menu gestion usuarios
                    CRUD.eliminarUsuario()
                elif opcion2 == "4":  #opcion del menu gestion usuarios
                    CRUD
                elif opcion2== "5":   #opcion del menu gestion usuarios
                    menu.usuarios()
                else:       
                    print("Opción no válida. Por favor, ingrese una opción válida (1-5).")        

            elif opcion1 == "2":       #opcion del menu usuarios
                print("")
            elif opcion1 == "3":      #opcion del menu usuarios
                print("")
            elif opcion1 == "4":     #opcion del menu usuarios
                print("")
            elif opcion1 == "5":      #opcion del menu usuarios
                menu.principal()
            else:       
                print("Opción no válida. Por favor, ingrese una opción válida (1-5).")       

        elif opcion == "2":     #opcion del menu principal
             print("")
        elif opcion == "3":     #opcion del menu principal
             print("")
        elif opcion == "4":      #opcion del menu principal
             print("")
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1-4).")

menuAdministrador()            

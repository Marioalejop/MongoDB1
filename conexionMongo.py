from pymongo import MongoClient
uri = "mongodb+srv://marioalejop:Juliana23@cluster0.xjiaffo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["client"]
coleccion = db["db"] 
def insertarUsuario():
    nombre = input("Ingrese los datos:")
    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Ingrese un valor valido")
        return
    correo = input("Ingrese un correo: ")
    persona = {'nombre':nombre, 'edad':edad, 'correo':correo }
    coleccion.insert_one(persona) 
    print("Los datos fueron ingresados correctamente :)")


insertarUsuario()
import PySimpleGUI as sg
import pandas as pd

def crearVentanaLogin():
    col1 = sg.Col([
        [sg.Text("Email")],
        [sg.Text("Contraseña")],
        [sg.Button("Iniciar sesión", key="botón inicio sesión")]
        ])
    col2 = sg.Col([
        [sg.Input(key="input correo")],
        [sg.Input(key="input contraseña", password_char="*")],
        [sg.Button("Registro", key="botón registro")]
        ])
    layout = [
        [col1, col2]
        ]
    return sg.Window("Inicio de sesión", layout, finalize=True)

def crearVentanaRegistro():
    col1 = sg.Col([
        [sg.Text("Email")],
        [sg.Text("Contraseña")],
        [sg.Text("Repetir contraseña")],
        [sg.Text("Nombre")],
        [sg.Text("Sexo")],
        [sg.Button("Volver", key="botón volver")]
        ])
    col2 = sg.Col([
        [sg.Input(key="input email")],
        [sg.Input(key="input contraseña", password_char="*")],
        [sg.Input(key="input repetir contraseña", password_char="*")],
        [sg.Input(key="input nombre")],
        [sg.Radio("Hombre", key="radio hombre", group_id="grupo sexo"),
         sg.Radio("Mujer", key="radio mujer", group_id="grupo sexo"),
         sg.Radio("Otro", key="radio otro", group_id="grupo sexo", default=True)],
        [sg.Button("Registrar", key="botón registrar")]
        ])
    layout = [
        [col1, col2]
        ]
    return sg.Window("Registro de usuario", layout, finalize=True)

def crearVentanaPrincipal():
    layout = [
        [sg.Button("Tabla datos", key="botón datos")],
        [sg.Button("Salir", key="botón salir")]
        ]
    return sg.Window("Menú principal", layout, finalize=True)

def crearVentanaTabla():
    df = pd.read_csv("Adquisiciones_realizadas.csv")
    encabezados = df.columns.tolist()
    contenido = df.head(15).values.tolist()
    suma = df[" Monto_Total_Sin_IVA "].sum()
    promedio = df[" Monto_Total_Sin_IVA "].mean()
    maximo = df[" Monto_Total_Sin_IVA "].max()
    minimo = df[" Monto_Total_Sin_IVA "].min()
    layout = [
        [sg.Text("Ejemplo de tabla de datos")],
        [sg.Table(headings=encabezados, values=contenido)],
        [sg.Text(f"La suma total de los montos es: ${suma:,.2f}")],
        [sg.Text(f"El promedio de los montos es: ${promedio:,.2f}")],
        [sg.Text(f"El valor máximo de los montos es: ${maximo:,.2f}")],
        [sg.Text(f"El valor mínimo de los montos es: ${minimo:,.2f}")],
        [sg.Button("Volver", key="botón volver")],
        ]
    return sg.Window("Tabla de datos", layout, finalize=True)

# Crear una variable para cada ventana
# Sólo la que queremos mostrar de inicio va a estar
# igualada a su función y las demás les va asignar None
ventanaLogin = crearVentanaLogin()
ventanaRegistro = None
ventanaPrincipal = None
ventanaTabla = None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    # Para moverse de una ventana a otra
    # ¿En qué ventana estoy?
    # ¿Qué botón oprimí?
    # ¿A qué ventana voy? (que la ventana esté en None)
    # ventanaLogin -> ventanaRegistro
    elif window == ventanaLogin\
         and event == "botón registro"\
         and ventanaRegistro is None:
        # Cerrar la ventana actual
        # Cambiar la variable de la ventana actual a None
        # Llamar a la función de la ventana que quiero abrir
        window.close()
        ventanaLogin = None
        ventanaRegistro = crearVentanaRegistro()
    # ventanaRegistro -> ventanaLogin
    elif window == ventanaRegistro\
         and event == "botón volver"\
         and ventanaLogin is None:
        window.close()
        ventanaRegistro = None
        ventanaLogin = crearVentanaLogin()
    elif window == ventanaPrincipal\
         and event == "botón datos"\
         and ventanaTabla is None:
        window.close()
        ventanaPrincipal = None
        ventanaTabla = crearVentanaTabla()
    
    elif window == ventanaLogin\
         and event == "botón inicio sesión"\
         and ventanaPrincipal is None:
        df = pd.read_csv("Usuarios.csv")
        usuario = df[(df["Email"] == values["input correo"])\
                     & (df["Contraseña"] == values["input contraseña"])]
        if len(usuario) > 0:
            window.close()
            ventanaLogin = None
            ventanaPrincipal = crearVentanaPrincipal()
        else:
            sg.Popup("El correo o la contraseña son incorrectos",
                     title = "Error")
    elif window == ventanaRegistro\
         and event == "botón registrar"\
         and ventanaLogin is None:
        if len(values["input contraseña"]) >= 5\
           and values["input contraseña"]==values["input repetir contraseña"]\
           and len(values["input email"]) > 0:
            if values["radio hombre"]:
                sexo = "Hombre"
            elif values["radio mujer"]:
                sexo = "Mujer"
            else:
                sexo = "Otro"
            fila = pd.DataFrame([{
                "Email": values["input email"],
                "Contraseña": values["input contraseña"],
                "Nombre": values["input nombre"],
                "Sexo": sexo
                }])
            df = pd.read_csv("Usuarios.csv")
            df = pd.concat([df, fila], ignore_index=True)
            df.to_csv("Usuarios.csv", index=False)
            window.close()
            ventanaRegistro = None
            ventanaLogin = crearVentanaLogin()
        else:
            sg.Popup("Hay errores en su registro", title="Error")
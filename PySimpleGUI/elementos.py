import PySimpleGUI as sg

sg.theme("DarkPurple3")

def crearVentanaPrincipal():
    lista_vacunas = ["Pfizer",
                     "AstraZeneca",
                     "Sputnik",
                     "Moderna",
                     "Patria"]
    lista_satisfaccion = ["Nada satisfecho",
                          "Poco satisfecho",
                          "Satisfecho",
                          "Muy satisfecho",
                          "Completamente satisfecho"]
    layout = [
        # Text
        [sg.Text("Mi primer texto",
                 font = "Arial 30",
                 text_color = "blue",
                 background_color = "purple")],
        # Button -> imagen .png
        [sg.Button("Mi primer botón",
                   key = "botón 1",
                   image_filename = "Pikachu.png"),
         sg.Button("Mi segundo botón",
                   key = "botón 2")],
        # Input
        [sg.Text("Nombre"),
         sg.Input(key = "input nombre",
                  default_text="Introduce tu nombre")],
        [sg.Text("Contraseña"),
         sg.Input(key = "input contraseña",
                  password_char = "*")],
        [sg.Text("¿Estás vacunado?"),
         sg.Radio("Sí",
                  key = "radio sí",
                  group_id = "grupo vacunación",
                  enable_events = True),
         sg.Radio("No",
                  key = "radio no",
                  group_id = "grupo vacunación",
                  enable_events = True,
                  default = True)],
        # Combo
        [sg.Text("Marca de la vacuna"),
         sg.Combo(lista_vacunas,
                  key = "combo vacunas",
                  default_value = "Pfizer",
                  disabled = True)],
        # Slider
        [sg.Text("Nivel de satisfacción:"),
         sg.Slider(range=(1,5),
                   key = "slider satisfacción",
                   orientation = "horizontal",
                   default_value=3)],
        # Spin
        [sg.Text("Elige"),
         sg.Spin(lista_satisfaccion,
                 key = "spin satisfacción",
                 initial_value= "Satisfecho")],
        [sg.Image("Pikachu.png")]
        ]
    return sg.Window("Mi primera ventana", layout, finalize=True)

ventanaPrincipal = crearVentanaPrincipal()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón 1":
        print("Di click en botón 1")
        nombre = values["input nombre"]
        contraseña = values["input contraseña"]
        print(f"Nombre: {nombre}")
        print(f"Contraseña: {contraseña}")
        radio_si = values["radio sí"]
        print(f"Radio sí: {radio_si}")
        radio_no = values["radio no"]
        print(f"Radio no: {radio_no}")
        vacuna = values["combo vacunas"]
        print(f"Vacuna seleccionada: {vacuna}")
    elif event == "radio sí":
        window["combo vacunas"].update(disabled=False)
    elif event == "radio no":
        window["combo vacunas"].update(disabled=True)
        

# Text
# Button
# Input
# Radio
# Combo
# Checkbox
# Slider
# Spin
# Image
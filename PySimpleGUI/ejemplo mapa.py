import PySimpleGUI as sg
import webbrowser

def crearVentanaPrincipal():
    layout = [
        [sg.Button("Abrir mapa", key="botón mapa")]
        ]
    return sg.Window("Ventana mapa", layout, finalize=True)

ventanaPrincipal = crearVentanaPrincipal()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón mapa":
        webbrowser.open("https://www.google.com/maps/d/edit?mid=1hImWBfV5RwZlfOso8g7lSZVMm9jN8J0&usp=sharing")
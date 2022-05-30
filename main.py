# main.py
import PySimpleGUI as sg
import pause
from pynput.keyboard import Key, Controller

loop = 0
cancel_loop = 0
punch_wait = 0
punch_time = 0
keyboard = Controller()

layout = [[sg.Text("Welcome to RedGrowie's autofarm menu!")], [sg.Button("Laser Grids")], [sg.Button("Chandeliers")], [sg.Button("Grass/Pepper/Sugar")], [sg.Button("Cancel")], [sg.Text("This software is open-source, and is written in Python.")], [sg.Text("Once you start a auto-farm option, you have to force close the application. Sorry, but i sat here for like 3 hours trying to fix it, to no avail.")], [sg.Text("Subscribe to SGW Ryan.")]]

window = sg.Window("Autofarming Menu", layout)


def cancel():
    if event == "Cancel":
        loop = 0


def d_press():
    keyboard.press(Key.right)
    pause.milliseconds(punch_time)
    keyboard.release(Key.right)
    pause.milliseconds(punch_wait)
    keyboard.release(Key.space)
    cancel_loop = 1
    return event


def space_press():
    keyboard.press(Key.space)
    pause.milliseconds(1)


def movement():
    d_press()
    space_press()
    loop = 0


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Chandeliers":
        punch_wait, punch_time, loop = 300, 70, 1
    elif event == "Grass/Pepper/Sugar":
        punch_wait, punch_time, loop = 300, 100, 1
    elif event == "Laser Grids":
        punch_wait, punch_time, loop = 300, 85, 1
    while loop == 1:
        movement()
        cancel()

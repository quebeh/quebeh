import PySimpleGUI as sg
import random

layout = [[sg.T('Rock - Paper - Scissors! \U0001F633')], [sg.T('Bot Chose :'), sg.T('Not started', size=(8,1), key='status')], [sg.Button('ROCK'), sg.Button('PAPER'), sg.Button('SCISSORS')], [sg.Button('EXIT')]]
window = sg.Window('Game', layout, margins=(10,10))

meta = {"ROCK" : "PAPER", "PAPER":"SCISSORS", "SCISSORS":"ROCK"}

while True:
    event, values = window.read()
    if event in ('EXIT', sg.WIN_CLOSED):
        break
    if event in ('ROCK', 'PAPER', 'SCISSORS'):
        e = random.choice(['ROCK','PAPER','SCISSORS'])
        if e != meta[str(event)]:
            e = random.choice(['ROCK','PAPER','SCISSORS'])
        window['status'].update(e)
        if e == meta[str(event)]:
            status = False
        elif event == meta[str(e)]:
            status = True
        else:
            status = None
        if status == True:
            sg.Popup('You Won!')
        if status == False:
            sg.Popup('You Lost!')
        if status == None:
            sg.Popup('No one Won!')

window.close()
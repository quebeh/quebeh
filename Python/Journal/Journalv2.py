import PySimpleGUI as sg
import json

read = [[sg.I('Feb-2021', key='filename', size=(45,1)), sg.T('.json')],
        [sg.Button('READ'), sg.Button('CLOSE', key='c1')],
        [sg.T('Already have a diary? '), sg.Button('OPEN'), sg.T(' it!')]]

write = [[sg.T('Enter today\'s events!')], [sg.T('Date : '), sg.I('1 February 2021', key='dateinput', size=(43,1))],
         [sg.T('==================================================')],
         [sg.Multiline(key='input', size=(50,10))],
         [sg.T('==================================================')],
         [sg.Button('DONE'), sg.Button('CLOSE', key='c2')]]

opend = [[sg.I('Feb-2021', key='filenameread', size=(45, 1)), sg.T('.json')],
         [sg.Button('OPEN IT'), sg.Button('BACK'), sg.Button('CLOSE', key='c3')]]

loadd = [[sg.I(key='value', size=(3,1)), sg.Text('(Diary number)')],
         [sg.T(key='range', size=(20,1))],
         [sg.Button('REFRESH')],
         [sg.T('Date :'), sg.T('Not picked', key='date', auto_size_text=True)],
         [sg.Multiline(key='output', size=(50,10))]]

layout = [[sg.Column(read, key='read', visible=True), sg.Column(write, key='write', visible=False), sg.Column(opend, key='open', visible=False), sg.Column(loadd, key='load', visible=False)]]
window = sg.Window('Journal', layout, margins=(10,10))

while True:
    event, values = window.read()
    if event in ['c1', 'c2', 'c3'] or event == sg.WIN_CLOSED:
        break

    if event == 'REFRESH':
        window['output'].update('')
        try:
            value = int(values['value']) - 1
        except SyntaxError:
            window['date'].update('')
            sg.Popup('Please insert a number not a character')
        except ValueError:
            window['date'].update('')
            sg.Popup('What?')
        else:
            try:
                window['output'].print(data['diary'][value]['text'])
                window['date'].update(data['diary'][value]['date'])
            except IndexError:
                window['date'].update('')
                sg.Popup('BRUH TAKE A NUMBER IN THE RANGE!!!')

    if event == 'OPEN IT':
        filenameread = values['filenameread']
        try:
            datafile = open('Journal/' + str(filenameread) + '.json', 'r')
            data = json.load(datafile)
            many = len(data['diary'])
            window['range'].update('Min : 1, Max : ' + str(many))
            window['open'].update(visible=False)
            window['load'].update(visible=True)
        except FileNotFoundError:
            sg.Popup('File doesn\'t exist!')

    if event == 'BACK':
        window['open'].update(visible=False)
        window['read'].update(visible=True)

    if event == 'OPEN':
        window['read'].update(visible=False)
        window['open'].update(visible=True)

    if event == 'READ':
        filename = 'Journal/' + str(values['filename']) + '.json'
        window['read'].update(visible=False)
        window['write'].update(visible=True)

    if event == 'DONE':
        text = values['input']
        date = values['dateinput']
        print(text)
        try:
            textfile = open(filename, 'r+')
        except FileNotFoundError:
            newfile = open(filename, 'a')
            newfile.write('{"diary":[]}')
            newfile.close()
        finally:
            with open(filename, 'r+') as textfile:
                jsondict = {"date":str(date), "text":str(text)}
                data = json.load(textfile)
                data['diary'].append(jsondict)
                textfile.seek(0)
                json.dump(data, textfile)
                textfile.close()
                sg.Popup('Done!')
                sg.Popup('Please open the app again if you want to read it')
                break

window.close()

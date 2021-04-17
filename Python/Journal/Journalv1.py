import PySimpleGUI as sg

read = [[sg.I('Feb-2021.txt', key='filename', size=(50,1))], [sg.Button('READ'), sg.Button('CLOSE', key='c1')]]
write = [[sg.T('Enter today\'s events!')], [sg.T('Date : '), sg.I('1 February 2021', key='dateinput', size=(43,1))], [sg.T('==================================================')], [sg.Multiline(key='input', size=(50,10))], [sg.T('==================================================')], [sg.Button('DONE'), sg.Button('CLOSE', key='c2')]]

layout = [[sg.Column(read, key='read', visible=True), sg.Column(write, key='write', visible=False)]]
window = sg.Window('Journal', layout, margins=(10,10))

while True:
    event, values = window.read()
    if event in 'c1c2' or event == sg.WIN_CLOSED:
        break

    if event == 'READ':
        textfile = open('Journal/' + str(values['filename']), 'a')
        window['read'].update(visible=False)
        window['write'].update(visible=True)

    if event == 'DONE':
        text = values['input']
        date = values['dateinput']
        print(text)
        textfile.write('\n==================================================\n')
        textfile.write('Date : {}'.format(date) + '\n\n')
        textfile.write(text)
        textfile.write('\n==================================================\n')
        textfile.close()
        sg.Popup('Done!')
        break

window.close()

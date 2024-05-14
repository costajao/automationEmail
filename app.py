import PySimpleGUI as sg

sg.theme('reddit')

layout = [
    [sg.Text('E-mail: '), sg.Input(key='email')],
    [sg.Text('Senha: '), sg.Input(key='pwd', password_char='*')],
    [sg.FolderBrowse('Selecione a Pasta Anexos',
                     target='input_files'), sg.Input(key='input_files')],
    [sg.FolderBrowse('Selecione a Pasta Planilha',
                     target='input_csv'), sg.Input(key='input_csv')],
    [sg.Button('Salvar')]
]

home = sg.Window('Home', layout=layout)

while True:
    event, values = home.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values['email']
        print(f'O e-mail digitado foi: {email}')
        pwd = values['pwd']
        print(f'A senha é: {pwd}')
        files = values['input_files']
        print(f'O caminho dos anexos é: {files}')
        csv = values['input_csv']
        print(f'O caminho das planilhas é: {csv}')

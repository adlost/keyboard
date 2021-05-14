from tkinter import *
from tkinter import ttk
import ttkthemes
import paramiko 


window = ttkthemes.ThemedTk()


window.get_themes()
window.set_theme('radiance')

window.title('GUI for key emuletion')
window.resizable(False, False)



varRow = 1
varColumn = 0
titleLabel= Label(window, text='On Screan Keyboard', font=('arial', 20, 'bold'))
titleLabel.grid(row=0, column=0, columnspan=15)


buttons = ['0',    '1',    '2',   '3',     '4',          '5',    
		   '6',    '7',    '8',   '9',     'refresh',    'red',
		   'Vol-', 'exit', 'up',  'back',  'page up',    'green',
		   'Vol+', 'left',   'ok',  'right',    'page down',  'yellow',
		   'ch+',  'menu', 'down',  'info',  'play/pause', 'blue',
		   'ch-',  'mute', 'EPG', 'tv',    'stop',       'power off',#'Screen resize',
		   ]

map_kb = {
'Vol-':'-kqt 0x01000070 -kqt 0x',
'Vol+':'-kqt 0x01000072 -kqt 0x2b',
'mute':'-kqt 96 -a',
'menu':'-kqt 0x0100003a',
'left':'-kqt 0x01000012',
'right':'-kqt 0x01000014',
'up':'-kqt 0x01000013',
'down':'-kqt 0x01000015',
'ok':'-kqt 0x01000004',
'red':'-kqt 0x01000030',
'green':'-kqt 0x01000031',
'yellow':'-kqt 0x01000032',
'blue':'-kqt 0x01000033',
'0':'-kqt 48',
'1':'-kqt 49',
'2':'-kqt 50',
'3':'-kqt 51',
'4':'-kqt 52',
'5':'-kqt 53',
'6':'-kqt 54',
'7':'-kqt 55',
'8':'-kqt 56',
'9':'-kqt 57',
'power off':'-kqt 0x55 -a',
'ch+':'-kqt 0x01000001',
'ch-':'-kqt 0x01000002',
'refresh':'-kqt 0x01000034',
'exit':'-kqt 0x01000000',
'back':'-kqt 0x01000003',
'page up':'-kqt 0x01000016',
'page down':'-kqt 0x01000017',
'info':'-kqt 89 -a',
'play/pause':'-kqt 82 -a',
'stop':'-kqt 83 -a',
'Screen resize':'-kqt 0x01000035',
'EPG':'-kqt 0x01000037',
'tv':'-kqt 0x01000039'
}

map_event={
'KP_0':'-kqt 48',
'KP_1':'-kqt 49',
'KP_2':'-kqt 50',
'KP_3':'-kqt 51',
'KP_4':'-kqt 52',
'KP_5':'-kqt 53',
'KP_6':'-kqt 54',
'KP_7':'-kqt 55',
'KP_8':'-kqt 56',
'KP_9':'-kqt 57',
'0':'-kqt 48',
'1':'-kqt 49',
'2':'-kqt 50',
'3':'-kqt 51',
'4':'-kqt 52',
'5':'-kqt 53',
'6':'-kqt 54',
'7':'-kqt 55',
'8':'-kqt 56',
'9':'-kqt 57',
'Escape':'-kqt 0x01000000',
'BackSpace':'-kqt 0x01000003',
'Prior':'-kqt 0x01000016',
'Next':'-kqt 0x01000017',
'F1': '-kqt 0x01000030',
'F2': '-kqt 0x01000031',
'F3':'-kqt 0x01000032',
'F4':'-kqt 0x01000033',
'F5':'-kqt 0x01000034'
'Left':'-kqt 0x01000012',
'Right':'-kqt 0x01000014',
'Up':'-kqt 0x01000013',
'Down':'-kqt 0x01000015',
'KP_Subtract':'-kqt 0x01000070 -kqt 0x',
'KP_Add':'-kqt 0x01000072 -kqt 0x2b',
'KP_Enter':'-kqt 0x01000004',
'Return':'-kqt 0x01000004',
'Home':'-kqt 0x0100003a',
'Pause':'-kqt 82 -a',
'w':'-kqt 0x01000001',
's':'-kqt 0x01000002',
}



for button in buttons:
	command= lambda x=button: select(map_kb.get(x))
	ttk.Button(window, text=button, width=10, command=command).grid(row=varRow, column=varColumn)
	varColumn+=1
	if varColumn>5:
		varColumn=0
		varRow+=1


def select(btn_code):
	host = ''
	user = 'root'
	secret = '930920'
	port = 22
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=host, username=user, password=secret, port=port)
	stdin, stdout, stderr = client.exec_command("/usr/local/share/app/bin/sendqtevent {code}".format(code=btn_code))
	data = stdout.read() + stderr.read()


def com(event):
	select(map_event.get(event.keysym))


window.bind("<Key>", com)
window.mainloop()




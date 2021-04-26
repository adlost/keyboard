from tkinter import *
from tkinter import ttk
import ttkthemes


# window = Tk()
window = ttkthemes.ThemedTk()


window.get_themes()
window.set_theme('radiance')

window.title('GUI for key emuletion')
#window.iconbitmap('/home/l1/python/rocket.ico')
#window.geometry("400x400")
window.resizable(False, False)

# def clicker(event):
# 	myLabel = Label(window, text="You clicked a button" + str(event.x) + " " + str(event.y))
# 	myLabel.pack()

# myButton = Button(window, text="Click Me")
# myButton.bind("<Key>", clicker)
# myButton.pack(pady=20)

varRow = 2
varColumn = 0
titleLabel= Label(window, text='On Screan Keyboard', font=('arial', 20, 'bold'))
titleLabel.grid(row=0, column=0, columnspan=15)



# textarea=Text(window, font=('arial', 20, 'bold'))
# textarea.grid(row=1, column=0, columnspan=15)
# textarea.focus_set()

buttons = ['Vol-','Vol+','mute','menu','left','right','up','down','ok','red','green','yellow','blue',
			'0','1','2','3','4','5','6','7','8','9',
			'power off','ch+','ch-',
			'refresh','exit','back','page up','page down','info','play/pause','stop','Screen resize','EPG','tv']


for button in buttons:
	ttk.Button(window, text=button, width=10).grid(row=varRow, column=varColumn)
	varColumn+=1
	if varColumn>8:
		varColumn=0
		varRow+=1



window.mainloop()

s

# ssh [your_my_SSH_user]@[your_server_or_IP] '[some_command]'
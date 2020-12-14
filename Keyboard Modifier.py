import tkinter as tk
from tkinter import ttk
from tkinter import * 
import threading,os
from pygame import mixer 
from pynput.keyboard import Key, Listener
os.system(f"title Select a keyboard modification and press change!")
os.system("cls")
switchsound = "not set"
blueclicked = 0
brownclicked = 0
redclicked = 0
def change():
	global switchsound
	switchsound = typeofswitch.get()
	#print(switchsound)
	os.system(f"title Keyboard Modifier - Mode = [{switchsound}]")

def on_press(key):
	global switchsound
	global blueclicked
	global brownclicked
	global redclicked
	if "Blue" in switchsound:
		mixer.init()
		mixer.music.load('blue.mp3') 
		mixer.music.play()
		blueclicked = blueclicked + 1
	elif "Brown" in switchsound:
		mixer.init()
		mixer.music.load('brown.mp3') 
		mixer.music.play()
		brownclicked = brownclicked + 1
	elif "Red" in switchsound:
		mixer.init()
		mixer.music.load('red.mp3') 
		mixer.music.play()
		redclicked = redclicked + 1
	os.system(f"title Keyboard Modifier - Blue Keys Simulated: [{blueclicked}] - Brown Keys Simulated: [{brownclicked}] - Red Keys Simulated: [{redclicked}]")

def run():
	with Listener(on_press=on_press) as listener:
		listener.join()
root = Tk()

root.geometry('374x493')
root.configure(background='#F0F8FF')
root.title('Keyboard Modifier')


Label(root, text='Keyboard Modifier', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=114, y=92)


Button(root, text='Change', bg='#FFFFFF', font=('arial', 12, 'normal'), command=change).place(x=142, y=200)


typeofswitch= ttk.Combobox(root, values=['Blue Switch', 'Brown Switch', 'Red Switch'], font=('arial', 12, 'normal'), width=15)
typeofswitch.place(x=102, y=141)
typeofswitch.current(1)

threading.Thread(target = run).start()

root.mainloop()

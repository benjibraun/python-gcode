from tkinter import *

import serial

class menu():

    def __init__(self,master):
        frame= Frame(master)
        frame.pack()
        self.printButton= Button(text="Home", command=self.kapcsi)
        self.printButton.pack(side=LEFT)

    def serialwrite(g):
        pari = bytes(g, 'ASCII')
        conneciton.write(pari)
        conneciton.write(b'\r\n')
    def G1 (x,y,z): # Move
        g='G1 '+'X'+str(x)+' '+'Y'+str(y)+' '+'Z'+str(z)+'\n'
        file.write(g)
        print(g)
    def G28 (): # Home
        g='G28\n'
        file.write(g)
    def M80 (): # ATX ON
        g='M80\n'
        serialwrite(g)
    def M81():  # ATX OFF
        g = 'M81\n'
        serialwrite(g)
    def M105(): # Get Temperature
        g='M105\n'
        serialwrite(g)
        if connection.inWaiting()>0:
            tem=connection.readline()
            print(tem)
    def M112():
        g='M112\n'
    def vet (szor):
        szor = input("hány")
        G28()
        for ig in range(1,int(szor)):
            z=0
            y=ig*10
            for hatar in range(10,50,10):
                x=hatar
                G1(x,y,z)
                G1(x,y,z+30)
    def kapcsi(self):
        connection=serial.Serial(com3,250000)
        return connection
    def save():
        name=input("file name: ")
        filename='c:/farm/'+name+'.gcode'
        file = open(filename,'w')

root=Tk()
mymenu=menu(root)
root.mainloop()

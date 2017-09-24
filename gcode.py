from tkinter import *



class menu():

    def __init__(self,master):
        frame= Frame(master,  width=500, height=500)
        frame.pack()
        self.conectB= Button(text="conect", command=self.kapcsi)
        self.conectB.pack(side=TOP)

        self.homeB= Button(text="Home", command=self.G28)
        self.homeB.pack(side=LEFT)

        self.onB= Button(text="ATX on", command=self.M80)
        self.onB.pack(side=LEFT)

        self.offB = Button(text="ATX off", command=self.M81)
        self.offB.pack(side=LEFT)

        self.off = Button(text="quit", command=frame.quit)
        self.off.pack(side=LEFT)

        self.x1 = Button(text="quit", command=self.G1(1,0,0))
        self.x1.pack(side=LEFT)

        self.x10 = Button(text="quit", command=self.G1(10,0,0))
        self.x10.pack(side=LEFT)

        self.x100 = Button(text="quit", command=self.G1(100,0,0))
        self.x100.pack(side=LEFT)

        self.y1 = Button(text="quit", command=self.G1(0,1,0))
        self.y1.pack(side=LEFT)

        self.y10 = Button(text="quit", command=self.G1(0,10,0))
        self.y10.pack(side=LEFT)

        self.y100 = Button(text="quit", command=self.G1(0,100,0))
        self.y100.pack(side=LEFT)

        self.z1 = Button(text="quit", command=self.G1(0,0,1))
        self.z1.pack(side=LEFT)

        self.z10 = Button(text="quit", command=self.G1(0,0,10))
        self.z10.pack(side=LEFT)

        self.z100 = Button(text="quit", command=self.G1(0,0,100))
        self.z100.pack(side=LEFT)

    def serialwrite(selfe,g):
        pari = bytes(g, 'ASCII')
        conneciton.write(pari)
        conneciton.write(b'\r\n')
    def G1 (self,x,y,z): # Move
        g='G1 '+'X'+str(x)+' '+'Y'+str(y)+' '+'Z'+str(z)+'\n'

        print(g)
    def G28 (self): # Home
        g='G28\n'
        file.write(g)
    def M80 (self): # ATX ON
        g='M80\n'
        serialwrite(g)
    def M81(self):  # ATX OFF
        g = 'M81\n'
        serialwrite(self,g)
    def M105(self): # Get Temperature
        g='M105\n'
        serialwrite(g)
        if connection.inWaiting()>0:
            tem=connection.readline()
            print(tem)
    def M112(self):
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
    def save(self):
        name=input("file name: ")
        filename='c:/farm/'+name+'.gcode'
        file = open(filename,'w')

root=Tk()
mymenu=menu(root)
root.mainloop()

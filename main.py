import Tkinter
import pygame
from pygame import *
from math import *
import sys
top=Tkinter.Tk()
top.title("Calculator")
eqn=[]
b=0
y=Tkinter.Entry()
y.grid(row=4,column=0,columnspan=3)
def Append(s):
	global b
	if s is "x" and b!=1:
		b+=1
	if s is "y" and b!=2:
		b+=2
	eqn.append(s)
	y.insert(Tkinter.END,s)
def Eval():
	global b
	if b == 0:
		x=eval(''.join(eqn))
		Del()
		eqn.append(str(x))
		y.delete(0,Tkinter.END)
		y.insert(Tkinter.END,str(x))
	else:
		Append("=")
def change_b():
	bot=Tkinter.Tk()	
	bot.title("Choose")
	def change_B(l):
		global b
		b=l
		bot.quit()
		bot.destroy()
	bu1=Tkinter.Button(bot,height=1,width=5, text="x", command=lambda:change_B(4))
	bu1.grid(row=0,column=1)
	bu2=Tkinter.Button(bot,height=1,width=5, text="y", command=lambda:change_B(5))
	bu2.grid(row=0,column=2)
	bot.mainloop()
k=20
def Graph():
	global b
	if b==0:
		change_b()
	if b!=0:
		pygame.init()
		white = (255,255,255)
		black = (0,0,0)
		graphcolor = (255,0,0)
		gridcolor = (100,250,240) #light blue
		green = (0,200,50)
		blue = (0,50,200)
		width,height = 480, 480
		screen = pygame.display.set_mode((width,height))
		pygame.display.set_caption("Graphic Calculator")
		def GraphEq(eqn,k):
			if b is 1 or b is 5:
    				for i in range(width):
        				try:
            					x = (width/2-i)/float(k)
            					y1 = eval(''.join(eqn))
            					pos1 = (width/2+x*k, height/2-y1*k)
            					nx = x = (width/2-(i+1))/float(k)
            					ny = eval(''.join(eqn))
            					pos2 = (width/2+nx*k, height/2-ny*k)
            					pygame.draw.line(screen, graphcolor, pos1, pos2, 1)
        				except:
            					pass
			if b is 2 or b is 4:
				for i in range(width):
					try:
						y=(width/2 - i)/float(k)
						x1=eval(''.join(eqn))
						pos1=(width/2+x1*k, height/2-y*k)
						ny=y=(width/2-(i+1))/float(k)
						nx=eval(''.join(eqn))
						pos2=(width/2+nx*k, height/2-ny*k)
						pygame.draw.line(screen, graphcolor, pos1, pos2, 1)
					except:
						pass
		def graphpaper(k):
    			screen.set_clip(0,0,width,height)
    			screen.fill(white)
    			for i in range(width/k):
        			gridx = k*i
        			gridy = k*i
        			pygame.draw.line(screen, gridcolor, (gridx,0), (gridx,height), 1)
        			pygame.draw.line(screen, gridcolor, (0,gridy), (width, gridy), 1)
    			pygame.draw.line(screen, gridcolor, (width,0), (width, height), 5)
   		 	midx, midy = width/(2*k), height/(2*k)
    			pygame.draw.line(screen, black, (midx*k,0), (midx*k,height), 3)
    			pygame.draw.line(screen, black, (0,midy*k), (width,midy*k), 3)
    			screen.set_clip(None)
			GraphEq(eqn,k)
		global k	
		c=True	
		while c:	
			if width%k is 0 and k>0:
				graphpaper(k)
        		pygame.display.update()
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==K_1 :
						k+=5
					if event.key==K_0 and k>5:
						k-=5
				if event.type==QUIT:
					c=False
					pygame.quit()
					break
	if b is 4 or b is 5:
		b=0
def Bs():
	s=eqn.pop()
	global b
	if s is "x":
		cout=0
		for i in eqn:
			if i is "x" :
				cout=-1
				break
		if cout!=-1 :
			b-=1
	if s is "y":
		cout=0
		for i in eqn:
			if i is "y" :
				cout=-1
				break
		if cout!=-1 :
			b-=2
	y.delete(0,Tkinter.END)
	y.insert(Tkinter.END, (''.join(eqn)))
def Del():
	global b
	b=0
	y.delete(0,Tkinter.END)
	del eqn[:]
def Break():
	global a
	sys.exit()
	a=False
a=True
while(a):
	a=False
	b1=Tkinter.Button(top, text="1",height=1,width=5, command=lambda:Append("1"))
	b1.grid(row=0,column=0)
	b2=Tkinter.Button(top, text="2",height=1,width=5, command=lambda:Append("2"))
	b2.grid(row=0,column=1)
	b3=Tkinter.Button(top, text="3",height=1,width=5, command=lambda:Append("3"))	
	b3.grid(row=0,column=2)
	b4=Tkinter.Button(top, text="4",height=1,width=5, command=lambda:Append("4"))
	b4.grid(row=1,column=0)
	b5=Tkinter.Button(top, text="5", height=1,width=5,command=lambda:Append("5"))
	b5.grid(row=1,column=1)
	b6=Tkinter.Button(top, text="6",height=1,width=5, command=lambda:Append("6"))
	b6.grid(row=1,column=2)
	b7=Tkinter.Button(top, text="7", height=1,width=5,command=lambda:Append("7"))
	b7.grid(row=2,column=0)
	b8=Tkinter.Button(top, text="8",height=1,width=5, command=lambda:Append("8"))	
	b8.grid(row=2,column=1)
	b9=Tkinter.Button(top, text="9",height=1,width=5, command=lambda:Append("9"))
	b9.grid(row=2,column=2)
	b10=Tkinter.Button(top, text="0",height=1,width=5, command=lambda:Append("0"))
	b10.grid(row=3,column=1)
	b11=Tkinter.Button(top, text="/",height=1,width=5, command=lambda:Append("/"))
	b11.grid(row=0,column=3)
	b12=Tkinter.Button(top, text="+",height=1,width=5, command=lambda:Append("+"))
	b12.grid(row=3,column=3)
	b13=Tkinter.Button(top, text="-",height=1,width=5, command=lambda:Append("-"))
	b13.grid(row=2,column=3)
	b14=Tkinter.Button(top, text="*",height=1,width=5, command=lambda:Append("*"))
	b14.grid(row=1,column=3)
	b15=Tkinter.Button(top, text="C",height=1,width=5, command=lambda:Del())
	b15.grid(row=0,column=9)
	b16=Tkinter.Button(top, text=".",height=1,width=5, command=lambda:Append("."))
	b16.grid(row=3,column=0)
	b17=Tkinter.Button(top, text="=",height=1,width=5, command=lambda:Eval())
	b17.grid(row=3,column=2)
	b18=Tkinter.Button(top, text="<-",height=1,width=5, command=lambda:Bs())
	b18.grid(row=0,column=10)
	b19=Tkinter.Button(top, text="(",height=1,width=5, command=lambda:Append("("))
	b19.grid(row=3,column=5)
	b20=Tkinter.Button(top, text=")",height=1,width=5, command=lambda:Append(")"))
	b20.grid(row=3,column=6)
	b21=Tkinter.Button(top,height=1,width=5, text="x", command=lambda:Append("x"))
	b21.grid(row=0,column=4)
	b22=Tkinter.Button(top,height=1,width=5, text="y", command=lambda:Append("y"))
	b22.grid(row=0,column=5)
	b23=Tkinter.Button(top,height=1,width=5, text="a^^b", command=lambda:Append("**"))
	b23.grid(row=0,column=6)
	b24=Tkinter.Button(top, text="1/x",height=1,width=5,command=lambda:Append("(1/"))
	b24.grid(row=1,column=10)
	b25=Tkinter.Button(top, text="|x|",height=1,width=5,command=lambda:Append("abs("))
	b25.grid(row=0,column=7)
	b26=Tkinter.Button(top, text="sqrt",height=1,width=5,command=lambda:Append("sqrt("))
	b26.grid(row=0,column=8)
	b27=Tkinter.Button(top, text="pi",height=1,width=5,command=lambda:Append("pi"))
	b27.grid(row=3,column=7)
	b28=Tkinter.Button(top, text="e",height=1,width=5,command=lambda:Append("e"))
	b28.grid(row=3,column=8)
	b29=Tkinter.Button(top, text="sin",height=1,width=5,command=lambda:Append("sin("))
	b29.grid(row=1,column=4)
	b30=Tkinter.Button(top, text="cos",height=1,width=5,command=lambda:Append("cos("))
	b30.grid(row=1,column=5)
	b31=Tkinter.Button(top, text="tan",height=1,width=5,command=lambda:Append("tan("))
	b31.grid(row=1,column=6)
	b32=Tkinter.Button(top, text="sec",height=1,width=5,command=lambda:Append("1/cos("))	
	b32.grid(row=1,column=7)
	b33=Tkinter.Button(top, text="cosec",height=1,width=5,command=lambda:Append("1/sin("))
	b33.grid(row=1,column=8)
	b34=Tkinter.Button(top, text="cot",height=1,width=5,command=lambda:Append("1/tan("))
	b34.grid(row=1,column=9)
	b35=Tkinter.Button(top, text="sinh",height=1,width=5,command=lambda:Append("sinh("))
	b35.grid(row=2,column=4)
	b36=Tkinter.Button(top, text="cosh",height=1,width=5,command=lambda:Append("cosh("))
	b36.grid(row=2,column=5)
	b37=Tkinter.Button(top, text="tanh",height=1,width=5,command=lambda:Append("tanh("))
	b37.grid(row=2,column=6)
	b38=Tkinter.Button(top, text="coth",height=1,width=5,command=lambda:Append("1/tanh("))
	b38.grid(row=2,column=7)
	b39=Tkinter.Button(top, text="log",height=1,width=5,command=lambda:Append("log("))
	b39.grid(row=3,column=4)
	b42=Tkinter.Button(top, text="sin^(-1)",height=1,width=5,command=lambda:Append("asin("))
	b42.grid(row=2,column=8)
	b43=Tkinter.Button(top, text="cos^(-1)",height=1,width=5,command=lambda:Append("acos("))
	b43.grid(row=2,column=9)
	b44=Tkinter.Button(top, text="tan^(-1)",height=1,width=5,command=lambda:Append("atan("))
	b44.grid(row=2,column=10)
	b45=Tkinter.Button(top, text="Graph",height=1,width=5,command=lambda:Graph(), bd=4)
	b45.grid(row=3,column=9)
	b46=Tkinter.Button(top, text="Quit",height=1, width=5, command=lambda:Break(), bd=4)
	b46.grid(row=3,column=10)
	b47=Tkinter.Button(top, text="Instructions",height=1, width=15, command=lambda:Hello())
	b47.grid(row=4,column=8, columnspan=3)
def Hello():
        bot=Tkinter.Tk()
        t=Tkinter.Text(bot)
        bot.title("Instructions")
        x=open("Instructions.txt", "r")
        l=x.read()
        t.insert(Tkinter.INSERT,l)
        t.grid(columnspan=11)
        bot.mainloop
top.mainloop()

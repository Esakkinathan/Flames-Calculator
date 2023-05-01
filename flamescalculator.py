from tkinter import *
from functools import partial
import random
import turtle
import time
from tkinter import messagebox as mb
root = Tk()  
root.geometry('450x250')  
root.title('FLAMESCALCULATOR')
root.configure(bg="#121212")

#username label and text entry box
Label(root, text="Enter Firstname:",bg="#121212",fg="White",font = ("Courier", 15)).place(x=20,y=20)
n1=StringVar()
Entry(root, textvariable=n1,bg="#121212",fg="White",bd=3).place(x=250,y=20)  


Label(root, text="Enter Secondname:",bg="#121212",fg="White",font = ("Courier", 15)).place(x=20,y=70)
n2=StringVar()
Entry(root, textvariable=n2,bg="#121212",fg="White",bd=3).place(x=250,y=70)  
Button(root, text="Check",bg="#121212",fg="#c0c0c0",cursor="dot",activebackground="#121212",activeforeground="#c0c0c0",font=("Courier",10),relief=FLAT ,command=lambda : flame(n1.get(),n2.get())).place(x=100,y=130) 
Button(root, text="Clear",bg="#121212",fg="#c0c0c0",cursor="dot",activebackground="#121212",activeforeground="#c0c0c0",font=("Courier",10),relief=FLAT, command=lambda : clear()).place(x=300,y=130) 

def clear():
	n1.set("")
	n2.set("")
	



def flame(s1,s2):
	try:
		dum1=int(s1)
		dum2=int(s2)
		mb.showerror("Flames Calculator","Numbers should not be entered")
		#return None
	except ValueError:
		if(s1=="" or s2==""):
			mb.showerror("Error","Enter values in the field")
		else:
			n1=s1.replace(" ","")
			n2=s2.replace(" ","")
			name1=list(n1.lower())
			name2=list(n2.lower())

			for i,x in enumerate(name1):
				j="".join(name2).find(name1[i])
				if(j!=-1):
					name1[i]='*'
					name2[j]='*' 
					
			x=lambda x: True if x!='*' else False 
			a=[]
			a.extend(list(filter(x,name1)))
			a.extend(list(filter(x,name2)))
			n=len(a)

			flames=list("FLAMES")
			i=0
			c=0
			while len(list(filter(x,flames)))!=1:
				if i==6:
					i=0      
				if flames[i]!='*':
					c+=1      
				if(c==n):
					flames[i]='*'
					c=0       
				i+=1
				result=''.join(list(filter(x,flames)))

			flamesDict={
				'F':'Friend',
				'L':'Love',
				'A':'Affection',
				'M':'Marriage',
				'E':'Enemy',
				'S':'Sibling',
			}
			s1=s1.upper()
			s2=s2.upper()
			t=turtle.Turtle()
			s=turtle.Screen()
			s.setup(width=1.0, height=1.0)
			s.bgcolor("black")
			sec=3
			while (sec!=0):
				t.clear()
				t.pencolor("black")
				t.setposition(0,-50)
				t.pencolor("hot pink")
				t.pensize(10)
				t.circle(100)
				t.pencolor("black")
				t.setposition(-30,0)
				t.pencolor("magenta")
				t.write(sec,font=("Century",80,'bold'))
				t.pencolor("black")
				t.setposition(-100,-150)
				t.pencolor("peru")
				t.write("Loading...",font=("Algerian",40,'bold'))
				sec=sec-1
				time.sleep(1)
			t.clear()
			t.pencolor("black")
			t.setposition(-300,100)
			t.pencolor("violet")
			t.write("The Relationship between",font=("Castellar",30))
			t.pencolor("black")
			t.setposition(-400,25)
			t.pencolor("silver")
			t.write("'"+s1+"'"+"  and  "+"'"+s2+"'"+"  ends with",font=("Chiller",40,'bold'))
			t.pencolor("black")
			t.setposition(-150,-50)
			t.pencolor("gold")
			t.write(flamesDict[result],font=("Algerian",40))

			def starsglow(x,y,color,length): 


				t.speed(0)
				t.hideturtle() 
				t.color(color)

				t.penup()
				t.goto(x,y)
				t.pendown()

				t.begin_fill()
				for i in range(5):
					t.forward(length)
					t.right(144)
					t.forward(length)
				t.end_fill()


			def random_pos():
				return random.randint(-600,600), random.randint(-600,600)

			def random_length():
				return random.randint(5,25)

			n=0
			while (n<=50):
				colors = ['red','blue','orange','yellow','magenta','purple','peru','ivory','dark orange']

				color = random.choice(colors)
				x ,y = random_pos()
				length = random_length()

				starsglow(x,y,color,length)
				n+=1
	
			sec=5
			t1=turtle.Turtle()
			while (sec!=0):
				t1.clear()
				t1.pencolor("black")
				t1.setposition(-300,-300)
				t1.pencolor("#0096FF")
				t1.write("The Window will shutdown in "+str(sec),font=("Century",30,'bold'))
				sec-=1
				time.sleep(1)
			t1.clear()
			turtle.bye()
			root.destroy()

root.mainloop()

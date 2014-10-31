#########################################
#
#         85pt - Add a cancel button
#
#########################################


# Add a cancel button with a red background
# When the cancel button is pressed, change the color from red to blue
# and then back to red when pressed again
# Read the comment above line 24
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent  ### (7) remember my parent, the root
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.myContainer2 = Frame(parent)
		self.myContainer2.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="OK", background= "green")
		self.button1.grid(row=0, column=0)	
		# Do not change <Button-1> when you create Button 2 :)
		self.button1.bind("<Button-1>", self.button1Click) ### (1)
		
		self.button2 = Button(self.myContainer2)
		self.button2.configure(text="Cancle", background= "red")
		self.button2.grid(row=1, column=0)	
		self.button2.bind("<Button-2>", self.button2Click) ### (2)
		
	def button1Click(self, event):    ### (3)
		if self.button1["background"] == "green": ### (4)
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"
	def button2Click(self, event):    ### (5)
		if self.button2["background"] == "red": ### (6)
			self.button2["background"] = "blue"
		else:
			self.button2["background"] = "red"
	
		
root = Tk()
myapp = MyApp(root)
root.mainloop()
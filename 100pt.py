#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the buttons, the oval moves to the left or right

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")
left = -10
right = 10
class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.myContainer2 = Frame(parent)
		self.myContainer2.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.grid(row=0,column=0)
		
	        # Add a second button!
				
		self.button2 = Button(self.myContainer2)
		self.button2.configure(text="Right", background= "lightblue")
		self.button2.grid(row=0,column=1)												
		self.button1.bind("<Button-1>", self.button1Click)
		self.button2.bind("<Button-1>", self.button2Click)
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
	def button1Click(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global left
	        x1, y1, x2, y2 = drawpad.coords(oval)
	        drawpad.move(oval,left,0)
	        if x2 > drawpad.winfo_width(): 
	             drawpad.move(oval,-drawpad.winfo_width(),0)
	        if x2 < 0:
	             drawpad.move(oval,drawpad.winfo_width(),0)
	# Add the event handler for the second button to make it move right!
	def button2Click(self, event):
	        global oval
	        global drwapad
	        global right
	        x1, y1, x2, y2 = drawpad.coords(oval)
	        drawpad.move(oval,right,0)
	        if x1 > drawpad.winfo_width(): 
	             drawpad.move(oval,-drawpad.winfo_width(),0)
	        if x1 < 0:
	             drawpad.move(oval,drawpad.winfo_width(),0)
		
myapp = MyApp(root)
root.mainloop()
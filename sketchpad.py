from tkinter import *
x1 = None
y1 = None
def click_handler(event):
  x2 = event.x 
  y2 = event.y
  global x1,y1

  if x1 is not None :
    canvas.create_line(x1,y1,x2,y2)
  x1 = x2
  y1 = y2

if __name__ == "__main__":
  root = Tk()
  canvas = Canvas(root,width=500,height = 500)
  canvas.pack()
  canvas.bind('<Button-1>',click_handler)
  root.resizable(width=False, height=False)
  root.mainloop()



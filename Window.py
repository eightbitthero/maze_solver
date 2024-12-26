from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas() 
        self.__canvas.pack()
        self.__win_run = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__win_run = True
        while self.__win_run == True:
            self.redraw()
        print ("window closed...")
    
    def close(self):
        self.__win_run == False


        
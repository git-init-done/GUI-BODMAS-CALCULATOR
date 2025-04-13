import tkinter as tk
    
def create_window():
    window = tk.Tk()
    window.title("BODMAS CALCULATOR")
    
    frame = tk.Frame(master = window, bg = "orange", padx = 10)
    frame.pack()
    
    input_area = tk.Entry(master = frame, width = 50, borderwidth = 5)
    input_area.grid(row = 0, column = 0, ipadx = 5, ipady = 5, columnspan = 3)
    
    def inputter(s):
        input_area.insert(tk.END, s)
        
    def backspacer():
        cursor_pos = input_area.index(tk.INSERT)
        if(cursor_pos>0):
            input_area.delete(cursor_pos - 1)
            
    def clearer():
        input_area.delete(0, tk.END)
        
    def equaler():
        y = input_area.get()
        try:
            y = str(eval(y))
            clearer()
            inputter(y)
        except:
            clearer()
            inputter("Invalid Input!")
    
    button_1 = tk.Button(master = frame, text = "1", command = lambda:inputter(1), padx=15, pady=5, width=3)
    button_1.grid(row = 1, column = 0, pady = 2)
    
    button_2 = tk.Button(master = frame, text = "2", command = lambda:inputter(2), padx=15, pady=5, width=3)
    button_2.grid(row = 1, column = 1, pady = 2)
    
    button_3 = tk.Button(master = frame, text = "3", command = lambda:inputter(3), padx=15, pady=5, width=3)
    button_3.grid(row = 1, column = 2, pady = 2)
    
    button_4 = tk.Button(master = frame, text = "Backspace", command = lambda:backspacer(), padx=15, pady=5, width=3)
    button_4.grid(row = 4, column = 0, pady = 2)
    
    button_5 = tk.Button(master = frame, text = "4", command = lambda:inputter(4), padx=15, pady=5, width=3)
    button_5.grid(row = 2, column = 0, pady = 2)
    
    button_6 = tk.Button(master = frame, text = "5", command = lambda:inputter(5), padx=15, pady=5, width=3)
    button_6.grid(row = 2, column = 1, pady = 2)
    
    button_7 = tk.Button(master = frame, text = "6", command = lambda:inputter(6), padx=15, pady=5, width=3)
    button_7.grid(row = 2, column = 2, pady = 2)
    
    button_8 = tk.Button(master = frame, text = "*", command = lambda:inputter("*"), padx=15, pady=5, width=3)
    button_8.grid(row = 5, column = 2, pady = 2)
    
    button_9 = tk.Button(master = frame, text = "7", command = lambda:inputter(7), padx=15, pady=5, width=3)
    button_9.grid(row = 3, column = 0, pady = 2)
    
    button_10 = tk.Button(master = frame, text = "8", command = lambda:inputter(8), padx=15, pady=5, width=3)
    button_10.grid(row = 3, column = 1, pady = 2)
    
    button_11 = tk.Button(master = frame, text = "9", command = lambda:inputter(9), padx=15, pady=5, width=3)
    button_11.grid(row = 3, column = 2, pady = 2)
    
    button_12 = tk.Button(master = frame, text = "/", command = lambda:inputter('/'), padx=15, pady=5, width=3)
    button_12.grid(row = 6, column = 0, pady = 2)
    
    button_13 = tk.Button(master = frame, text = "0", command = lambda:inputter(0), padx=15, pady=5, width=3)
    button_13.grid(row = 4, column = 1, pady = 2)   
    
    button_14 = tk.Button(master = frame, text = "+", command = lambda:inputter('+'), padx=15, pady=5, width=3)
    button_14.grid(row = 5, column = 0, pady = 2) 
    
    button_15 = tk.Button(master = frame, text = "-", command = lambda:inputter('-'), padx=15, pady=5, width=3)
    button_15.grid(row = 5, column = 1, pady = 2)
    
    button_16 = tk.Button(master = frame, text = "C", command = lambda:clearer(), padx=15, pady=5, width=3)
    button_16.grid(row = 6, column = 2, pady = 2)
    
    button_equal = tk.Button(master = frame, text = "=", command = lambda:equaler(), padx=15, pady=5, width=3)
    button_equal.grid(row = 4, column = 2, pady = 2)
    
    button_exit = tk.Button(master = frame, text = "EXIT", command = lambda:exit(), padx=15, pady=5, width=3)
    button_exit.grid(row = 7, column = 1, pady = 2)
    
    label = tk.Label(master = frame, text = "Two successive * = exponent", bg = "red")
    label.grid(row = 8, column = 1)
        
    button_exponent = tk.Button(master = frame, text = "^", command = lambda:inputter('**'), padx=15, pady=5, width=3)
    button_exponent.grid(row = 6, column = 1, pady = 2)
    
    window.mainloop()

create_window()
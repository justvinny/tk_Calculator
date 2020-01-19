import tkinter as tk
import tkinter.ttk as ttk


class Calculator:
    # This is the dictionary containing all of our number buttons.
    button_dic = {}
    result = 0
    operator = ''
    next_operator = ''

    # This is our constructor.
    def __init__(self, master):
        self.master = master
        self.master_settings()
        self.main_frame()

    # This is where we modify the root window.
    def master_settings(self):
        self.master.title('Basic Calculator')
        self.master.config(bg='black')

    # This is the main frame of our app that contains all our widgets.    
    def main_frame(self):
       ## Defining our widgets.
        # Defining our main frame.
        self.mainFrame = tk.Frame(self.master) 
        self.mainFrame.rowconfigure(0, weight=1)
        self.mainFrame.rowconfigure(1, weight=1)
        self.mainFrame.rowconfigure(2, weight=1)
        self.mainFrame.rowconfigure(3, weight=1)
        self.mainFrame.rowconfigure(4, weight=1)
        self.mainFrame.rowconfigure(5, weight=1)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.columnconfigure(1, weight=1)
        self.mainFrame.columnconfigure(2, weight=1)
        self.mainFrame.columnconfigure(3, weight=1)
        
        # Defining the entry widget at the top of the frame.
        self.enter = tk.Entry(self.mainFrame, bg='white', font=(None, 20))
        
        # Defining the buttons for our calculator using a for loop and our class dictionary.
        for each in range(10): 
            self.button_dic.setdefault('button' + str(each), tk.Button(self.mainFrame, text=str(each),
                                                                       font=(None,20), command=lambda each=each: self.button_press(str(each))))

        # Defining other buttons for our calculator.
        self.buttonEqual = tk.Button(self.mainFrame, text='=', font=(None,20), command=self.equal_operator)

        self.buttonAdd = tk.Button(self.mainFrame, text='+', font=(None,20), command= lambda: self.button_operator('+'))
        self.buttonMin = tk.Button(self.mainFrame, text='-', font=(None,20), command= lambda: self.button_operator('-'))
        self.buttonMult = tk.Button(self.mainFrame, text='*', font=(None,20), command= lambda: self.button_operator('*'))
        self.buttonDiv = tk.Button(self.mainFrame, text='/', font=(None,20), command= lambda: self.button_operator('/'))

        self.buttonClear = tk.Button(self.mainFrame, text='Clear', font=(None,20), command=self.button_clear)


       ## Packing our widgets onto the screen.
        self.mainFrame.place(relx=.1, rely=.1, relheight=.8, relwidth=.8)

        self.enter.grid(columnspan=4, sticky=(tk.N, tk.S, tk.W, tk.E))

        self.button_dic['button0'].grid(row=4, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button1'].grid(row=3, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button2'].grid(row=3, column=1, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button3'].grid(row=3, column=2, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button4'].grid(row=2, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button5'].grid(row=2, column=1, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button6'].grid(row=2, column=2, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button7'].grid(row=1, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button8'].grid(row=1, column=1, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.button_dic['button9'].grid(row=1, column=2, sticky=(tk.N, tk.S, tk.W, tk.E))
        
        self.buttonEqual.grid(row=4, column=1, columnspan=2, sticky=(tk.N, tk.S, tk.W, tk.E))

        self.buttonAdd.grid(row=1, column=3, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.buttonMin.grid(row=2, column=3, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.buttonMult.grid(row=3, column=3, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.buttonDiv.grid(row=4, column=3, sticky=(tk.N, tk.S, tk.W, tk.E))

        self.buttonClear.grid(row=5, columnspan=4, sticky=(tk.N, tk.S, tk.W, tk.E))

    # Method to insert numbers in the entry widget.
    def button_press(self, event):
        number = self.enter.get()
        self.enter.delete(0, tk.END)
        self.enter.insert(0, number + event)

    # Method to clear content of entry widget.
    def button_clear(self):
        self.result = 0
        self.enter.delete(0, tk.END)

    # Determines which mathematical operator to use.
    def button_operator(self, event):
        self.nxOperator = str(event)

        if self.result == 0:
            self.result = float(self.enter.get())
            self.enter.delete(0, tk.END)
            self.operator = event
            
        elif self.operator == '+':
            number = self.enter.get()
            self.result += float(number)
            self.enter.delete(0, tk.END)
            self.operator = str(event)
            
        elif self.operator == '-':
            number = self.enter.get()
            self.result -= float(number)
            self.enter.delete(0, tk.END)
            self.operator = str(event)
            
        elif self.operator == '/':
            number = self.enter.get()
            self.result /= float(number)
            self.enter.delete(0, tk.END)
            self.operator = str(event)
            
        elif self.operator == '*':
            number = self.enter.get()
            self.result *= float(number)
            self.enter.delete(0, tk.END)
            self.operator = str(event)
 
    # Result from pressing the equals sign. 
    def equal_operator(self):
            
        if self.nxOperator == '+':
            self.result += float(self.enter.get())
            self.convert()
            self.enter.delete(0, tk.END)
            self.enter.insert(0, self.result)
            self.result = 0
            
        if self.nxOperator == '-':
            self.result -= float(self.enter.get())
            self.convert()
            self.enter.delete(0, tk.END)
            self.enter.insert(0, self.result)
            self.result = 0
            
        if self.nxOperator == '/':
            self.result /= float(self.enter.get())
            self.convert()
            self.enter.delete(0, tk.END)
            self.enter.insert(0, self.result)    
            self.result = 0
            
        if self.nxOperator == '*':
            self.result *= float(self.enter.get())
            self.convert()
            self.enter.delete(0, tk.END)
            self.enter.insert(0, self.result)
            self.result = 0

    # Convert result to int if it has 0 decimals.
    def convert(self):
        if self.result % 2 == 0 or self.result % 2 == 1:
            temp_result = int(self.result)
            self.result = temp_result

        
if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('500x600')
    Calculator(root)
    root.mainloop()

        
    

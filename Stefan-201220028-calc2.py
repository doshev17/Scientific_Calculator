from tkinter import*
import math

root = Tk()
root.title("Calculator")
root.configure(background = "turquoise1")
root.resizable(width = False, height=False)
root.geometry("935x540+0+0")

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):

        self.memStore =0
        self.expression =""
        self.mem=""
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current= float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        if self.op == "pow2":
            self.total = pow(self.total, self.current)
        if self.op == "%":
            self.total == self.current / 100
        if self.op=="inv":
            self.total=1/self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def pow(self):
        self.result = False
        self.current = math.pow (float(txtDisplay.get()), 2)
        self.display(self.current)

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt (float(txtDisplay.get()))
        self.display(self.current)

    def factoriel(self):
        self.result = False
        self.current = math.factorial (float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos (math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.sin (math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.tan (math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log10 (float(txtDisplay.get()))
        self.display(self.current)

    def Perc(self):
        self.result=False
        self.current= (float(self.current)) / 100
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp (float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result= False
        self.current=math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def radians(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)

    def e(self):
        self.reult=False
        self.current=math.e
        self.display(self.current)

    def memory_recall(self):
        self.result= False
        self.display(self.memStore)
        self.current=self.current=self.memStore

    def memory_store(self):
        self.result= False
        self.memStore=(float(txtDisplay.get()))
        self.current=self.memStore
        self.display(self.current)

    def memory_add(self):
        self.result = False
        self.memStore= self.memStore + (float(txtDisplay.get()))
        self.current= (float(txtDisplay.get()))

    def memory_sub(self):
        self.result = False
        self.memStore= self.memStore - (float(txtDisplay.get()))
        self.current= (float(txtDisplay.get()))
        
    def memory_clear(self):
        self.result= False
        self.memStore="0"
        self.display(self.memStore)
        

    
added_value = Calc()

txtDisplay = Entry(calc, font=('arial',20,'bold'),bg="PaleGreen1", bd=10, width=28, justify=RIGHT)
txtDisplay.grid(row=0 , column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i = 0
btn = []
for j in range (2,5):
    for k in range (3):
        btn.append(Button(calc,width=5, height=2, font=('arial',20,'bold'),bg ="pink2", bd=4, text=numberpad[i]))
        btn[i].grid(row= j, column=k, pady=1)
        btn[i] ["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
        i += 1
        
#===============================================================================Buttons=========================================================================================
btnClear = Button(calc, text="C", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light coral", command = added_value.Clear_Entry).grid(row=1, column=0, pady=1)
btnAllClear = Button(calc, text="CE", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light coral", command = added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)
btnSq = Button(calc, text="√", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.squared).grid(row=1, column=2, pady=1)
btnAdd = Button(calc, text="+", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)
#===============================================================================================================================================================================
btnSub = Button(calc, text="-", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)
#===============================================================================================================================================================================
btnMult = Button(calc, text="*", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)
#===============================================================================================================================================================================
btnDiv = Button(calc, text="/", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)
#===============================================================================================================================================================================
btnZero = Button(calc, text="0", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="pink2", command = lambda: added_value.numberEnter(0)).grid(row=5, column=1, pady=1)
btnDot = Button(calc, text=".", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = lambda: added_value.numberEnter(".")).grid(row=5, column=2, pady=1)
btnPM = Button(calc, text=chr(177), width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.mathsPM).grid(row=5, column=0, pady=1)
btnEquals = Button(calc, text="=", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light coral", command = added_value.sum_of_total).grid(row=5, column=3, pady=1)
#===============================================================================================================================================================================
btnPi = Button(calc, text="π", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.pi).grid(row=3, column=8, pady=1)
btnCos = Button(calc, text="cos", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.cos).grid(row=2, column=5, pady=1)
btnTan = Button(calc, text="tan", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.tan).grid(row=2, column=6, pady=1)
btnSin = Button(calc, text="sin", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.sin).grid(row=2, column=4, pady=1)
#===============================================================================================================================================================================
btnxy = Button(calc, text="x^y", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = lambda: added_value.operation("pow2")).grid(row=2, column=8, pady=1)
btnPow = Button(calc, text="x^2", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.pow).grid(row=2, column=7, pady=1)
#===============================================================================================================================================================================
btnlog = Button(calc, text="log", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.log).grid(row=3, column=5, pady=1)
btnExp = Button(calc, text="Exp", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.exp).grid(row=4, column=6, pady=1)
btnMod = Button(calc, text="Mod", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = lambda: added_value.operation("mod")).grid(row=4, column=8, pady=1)
btnN = Button(calc, text="n!", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.factoriel).grid(row=3, column=7, pady=1)
#===============================================================================================================================================================================
btnRad = Button(calc, text="RAD", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.radians).grid(row=4, column=4, pady=1)
btnDeg = Button(calc, text="DEG", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.degrees).grid(row=4, column=5, pady=1)
btnMC = Button(calc, text="MC", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light coral", command = added_value.memory_clear).grid(row=1, column=4, pady=1)
btnMR = Button(calc, text="MR", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light coral", command = added_value.memory_recall).grid(row=1, column=5, pady=1)
#===============================================================================================================================================================================
btnMp = Button(calc, text="M+", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light coral", command = added_value.memory_add).grid(row=1, column=7, pady=1)
btnMm = Button(calc, text="M-", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light coral", command = added_value.memory_sub).grid(row=1, column=8, pady=1)
btnMS = Button(calc, text="MS", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light coral", command = added_value.memory_store).grid(row=1, column=6, pady=1)
btnPerc = Button(calc, text="%", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.Perc).grid(row=3, column=4, pady=1)
btnE = Button(calc, text="e", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = added_value.e).grid(row=3, column=6, pady=1)
btnInv = Button(calc, text="Inv", width=5, height=2, font=('arial',20,'bold'), bd=4,
                  bg="seashell3", command = lambda: added_value.operation("inv")).grid(row=4, column=7, pady=1)
#===============================================================================================================================================================================
lblDisplay = Label(calc, text="Scientific Calculator", font=('Segoe Print',28), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=6)
lblDisplay = Label(calc, text="by  Stefan Doshev \U0001F393", font=('Segoe Print',28), justify=CENTER)
lblDisplay.grid(row=5, column=4, columnspan=6)
#===============================================================================================================================================================================

root.mainloop()





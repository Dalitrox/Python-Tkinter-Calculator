import math
import tkinter as tk
import tkinter.messagebox
from dataclasses import dataclass
import re

root = tk.Tk()
root.geometry("650x400+300+300")
root.iconbitmap(True, "calculator_icon.ico")
root.title("Calculator")

switch = None

@dataclass(frozen = True)
class Function:

    def btn1_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '1')

    def btn2_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '2')
        
    def btn3_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '3')

    def btn4_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '4')

    def btn5_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '5')

    def btn6_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '6')

    def btn7_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '7')

    def btn8_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '8')

    def btn9_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '9')

    def btn0_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '0')

    def key_event(*args):
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)

    def btn_plus_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '+')

    def btn_minus_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '-')

    def btn_multi_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '*')

    def btn_divide_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '/')

    def btn_clear_clicked(*args):
        tk.disp.delete(0, tk.END)
        tk.disp.insert(0, '0')

    def sin_clicked():
        try:
            ans = float(tk.disp.get())
            if switch is True:
                ans = math.sin(math.radians(ans))
            else:
                ans = math.sin(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def cos_clicked():
        try:
            ans = float(tk.disp.get())
            if switch is True:
                ans = math.cos(math.radians(ans))
            else:
                ans = math.cos(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def tan_clicked():
        try:
            ans = float(tk.disp.get())
            if switch is True:
                ans = math.tan(math.radians(ans))
            else:
                ans = math.tan(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def arcsin_clicked():
        try:
            ans = float(tk.disp.get())
            if switch is True:
                ans = math.degrees(math.asin(ans))
            else:
                ans = math.asin(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def arccos_clicked():
        try:
            ans = float(tk.disp.get())
            if switch is True:
                ans = math.degrees(math.acos(ans))
            else:
                ans = math.acos(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def arctan_clicked():
        try:
            ans = float(tk.disp.get())
            if switch is True:
                ans = math.degrees(math.atan(ans))
            else:
                ans = math.atan(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def pow_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, "**")

    def round_clicked():
        try:
            ans = float(tk.disp.get())
            ans = round(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def logarithm_clicked():
        try:
            ans = float(tk.disp.get())
            ans = math.log10(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def fact_clicked():
        try:
            ans = float(tk.disp.get())
            ans = math.gamma(ans + 1)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def sqrt_clicked():
        try:
            ans = float(tk.disp.get())
            ans = math.sqrt(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def dot_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '.')

    def pi_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, str(math.pi))

    def e_clicked():
        if tk.disp.get() == '0':
            tk.disp.delete(0, tk.END)
        pos = len(tk.disp.get())
        tk.disp.insert(pos, str(math.e))

    def bl_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '(')

    def br_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, ')')

    def del_clicked():
        pos = len(tk.disp.get())
        display = str(tk.disp.get())
        if display == '':
            tk.disp.insert(0, '0')
        elif display == ' ':
            tk.disp.insert(0, '0')
        elif display == '0':
            pass
        else:
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, display[0:pos - 1])

    def conv_clicked():
        global switch
        if switch is None:
            switch = True
            Operatorations.conv_btn["text"] = "Deg"
        else:
            switch = None
            Operatorations.conv_btn["text"] = "Rad"

    def ln_clicked():
        try:
            ans = float(tk.disp.get())
            ans = math.log(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def mod_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '%')

    def btneq_clicked(*args):
        try:
            ans = tk.disp.get()
            ans = eval(ans)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except Exception:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def procent_clicked():
        try:
            ans = float(tk.disp.get())
            ans = (ans / 100)
            tk.disp.delete(0, tk.END)
            tk.disp.insert(0, str(ans))
        except:
            tkinter.messagebox.showerror("Value Error", "Check your values and operators")

    def square_clicked():
        pos = len(tk.disp.get())
        tk.disp.insert(pos, '**(1/')

    def oper_change_clicked():
        match = re.search('-?\d+(?:\.\d+)?(?:e-\d+)?$', tk.disp.get(), re.I)
        
        ans = float(match.group(0))
        if ans != abs(ans):
            ans = abs(ans)
        else:
            ans = -ans
        
        tk.disp.delete(match.start(), tk.END)
        tk.disp.insert(match.start(), str(ans))

# Label

@dataclass(frozen = True)
class Bind:
    tk.disp = tk.Entry(root, font = "Arial 20", fg = "black", bg = "#abbab1", bd = 0, justify = 'right', insertbackground = "#abbab1", cursor = "arrow")
    tk.disp.bind("<Return>", Function.btneq_clicked)
    tk.disp.bind("<Escape>", Function.btn_clear_clicked)
    tk.disp.bind("<Key-1>", Function.key_event)
    tk.disp.bind("<Key-2>", Function.key_event)
    tk.disp.bind("<Key-3>", Function.key_event)
    tk.disp.bind("<Key-4>", Function.key_event)
    tk.disp.bind("<Key-5>", Function.key_event)
    tk.disp.bind("<Key-6>", Function.key_event)
    tk.disp.bind("<Key-7>", Function.key_event)
    tk.disp.bind("<Key-8>", Function.key_event)
    tk.disp.bind("<Key-9>", Function.key_event)
    tk.disp.bind("<Key-0>", Function.key_event)
    tk.disp.bind("<Key-.>", Function.key_event)
    tk.disp.insert(0, '0')
    tk.disp.focus_set()
    tk.disp.pack(expand = True, fill = "both")

@dataclass(frozen = True)
class Operatorations:
    # Row 1 Buttons

    btnrow1 = tk.Frame(root, bg = "#000000")
    btnrow1.pack(expand = True, fill = "both")

    pi_btn = tk.Button(btnrow1, text = "π", font = "Arial 18", relief = "groove", bd = 0, command = Function.pi_clicked, fg = "black", bg = "#a8a7a5")
    pi_btn.pack(side = "left", expand = True, fill = "both")

    fact_btn = tk.Button(btnrow1, text = "x!", font = "Arial 18", relief = "groove", bd = 0, command = Function.fact_clicked, fg = "black", bg = "#a8a7a5")
    fact_btn.pack(side = "left", expand = True, fill = "both")

    sin_btn = tk.Button(btnrow1, text = "sin", font = "Arial 18", relief = "groove", bd = 0, command = Function.sin_clicked, fg = "black", bg = "#a8a7a5")
    sin_btn.pack(side = "left", expand = True, fill = "both")

    cos_btn = tk.Button(btnrow1, text = "cos", font = "Arial 18", relief = "groove", bd = 0, command = Function.cos_clicked, fg = "black", bg = "#a8a7a5")
    cos_btn.pack(side = "left", expand = True, fill = "both")

    tan_btn = tk.Button(btnrow1, text = "tan", font = "Arial 18", relief = "groove", bd = 0, command = Function.tan_clicked, fg = "black", bg = "#a8a7a5")
    tan_btn.pack(side = "left", expand = True, fill = "both")

    proc_btn = tk.Button(btnrow1, text = "%", font = "Arial 18", relief = "groove", bd = 0, command = Function.procent_clicked, fg = "black", bg = "#a8a7a5")
    proc_btn.pack(side = "left", expand = True, fill = "both")

    btn1 = tk.Button(btnrow1, text = "1", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn1_clicked, fg = "black", bg = "#ffffff")
    btn1.pack(side = "left", expand = True, fill = "both")

    btn2 = tk.Button(btnrow1, text = "2", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn2_clicked, fg = "black", bg = "#ffffff")
    btn2.pack(side = "left", expand = True, fill = "both")

    btn3 = tk.Button(btnrow1, text = "3", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn3_clicked, fg = "black", bg = "#ffffff")
    btn3.pack(side = "left", expand = True, fill = "both")

    btnpuls = tk.Button(btnrow1, text = "+", font = "Arial 21", relief = "groove", bd = 0, command = Function.btn_plus_clicked, fg = "black", bg = "#e0a13a")
    btnpuls.pack(side = "left", expand = True, fill = "both")

    # Row 2 Buttons

    btnrow2 = tk.Frame(root)
    btnrow2.pack(expand = True, fill = "both")

    e_btn = tk.Button(btnrow2, text = "e", font = "Arial 18", relief = "groove", bd = 0, command = Function.e_clicked, fg = "black", bg = "#a8a7a5")
    e_btn.pack(side = "left", expand = True, fill = "both")

    sqrt_btn = tk.Button(btnrow2, text = "√x", font = "Arial 18", relief = "groove", bd = 0, command = Function.sqrt_clicked, fg = "black", bg = "#a8a7a5")
    sqrt_btn.pack(side = "left", expand = True, fill = "both")

    sinh_btn = tk.Button(btnrow2, text = "sin-1", font = "Arial 11 bold", relief = "groove", bd = 0, command = Function.arcsin_clicked, fg = "black", bg = "#a8a7a5")
    sinh_btn.pack(side = "left", expand = True, fill = "both")

    cosh_btn = tk.Button(btnrow2, text = "cos-1", font = "Arial 11 bold", relief = "groove", bd = 0, command = Function.arccos_clicked, fg = "black", bg = "#a8a7a5")
    cosh_btn.pack(side = "left", expand = True, fill = "both")

    tanh_btn = tk.Button(btnrow2, text = "tan-1", font = "Arial 11 bold", relief = "groove", bd = 0, command = Function.arctan_clicked, fg = "black", bg = "#a8a7a5")
    tanh_btn.pack(side = "left", expand = True, fill = "both")

    square_btn = tk.Button(btnrow2, text = "x√y", font = "Arial 18", relief = "groove", bd = 0, command = Function.square_clicked, fg = "black", bg = "#a8a7a5")
    square_btn.pack(side = "left", expand = True, fill = "both")

    btn4 = tk.Button(btnrow2, text = "4", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn4_clicked, fg = "black", bg = "#ffffff")
    btn4.pack(side = "left", expand = True, fill = "both")

    btn5 = tk.Button(btnrow2, text = "5", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn5_clicked, fg = "black", bg = "#ffffff")
    btn5.pack(side = "left", expand = True, fill = "both")

    btn6 = tk.Button(btnrow2, text = "6", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn6_clicked, fg = "black", bg = "#ffffff")
    btn6.pack(side = "left", expand = True, fill = "both")

    btn_min = tk.Button(btnrow2, text = "-", font = "Arial 24", relief = "groove", bd = 0, command = Function.btn_minus_clicked, fg = "black", bg = "#e0a13a")
    btn_min.pack(side = "left", expand = True, fill = "both")

    # Row 3 Buttons

    btnrow3 = tk.Frame(root)
    btnrow3.pack(expand = True, fill = "both")

    conv_btn = tk.Button(btnrow3, text = "Rad", font = "Arial 12 bold", relief = "groove", bd = 0, command = Function.conv_clicked, fg = "black", bg = "#a8a7a5")
    conv_btn.pack(side = "left", expand = True, fill = "both")

    round_btn = tk.Button(btnrow3, text = "Round", font = "Arial 10 bold", relief = "groove", bd = 0, command = Function.round_clicked, fg = "black", bg = "#a8a7a5")
    round_btn.pack(side = "left", expand = True, fill = "both")

    ln_btn = tk.Button(btnrow3, text = "ln", font = "Arial 18", relief = "groove", bd = 0, command = Function.ln_clicked, fg = "black", bg = "#a8a7a5")
    ln_btn.pack(side= "left", expand = True, fill = "both")

    log_btn = tk.Button(btnrow3, text = "log", font = "Arial 17", relief = "groove", bd = 0, command = Function.logarithm_clicked, fg = "black", bg = "#a8a7a5")
    log_btn.pack(side = "left", expand = True, fill = "both")

    pow_btn = tk.Button(btnrow3, text = "x^y", font = "Arial 16", relief = "groove", bd = 0, command = Function.pow_clicked, fg = "black", bg = "#a8a7a5")
    pow_btn.pack(side = "left", expand = True, fill = "both")

    oper_btn = tk.Button(btnrow3, text = "+/-", font = "Arial 16", relief = "groove", bd = 0, command = Function.oper_change_clicked, fg = "black", bg = "#a8a7a5")
    oper_btn.pack(side = "left", expand = True, fill = "both")

    btn7 = tk.Button(btnrow3, text = "7", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn7_clicked, fg = "black", bg = "#ffffff")
    btn7.pack(side = "left", expand = True, fill = "both")

    btn8 = tk.Button(btnrow3, text = "8", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn8_clicked, fg = "black", bg = "#ffffff")
    btn8.pack(side = "left", expand = True, fill = "both")

    btn9 = tk.Button(btnrow3, text = "9", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn9_clicked, fg = "black", bg = "#ffffff")
    btn9.pack(side = "left", expand = True, fill = "both")

    btn_mul = tk.Button(btnrow3, text = "x", font = "Arial 23", relief = "groove", bd = 0, command = Function.btn_multi_clicked, fg = "black", bg = "#e0a13a")
    btn_mul.pack(side = "left", expand = True, fill = "both")

    # Row 4 Buttons

    btnrow4 = tk.Frame(root)
    btnrow4.pack(expand = True, fill = "both")

    btn_mod = tk.Button(btnrow4, text = "mod", font = "Arial 21", relief = "groove", bd = 0, command = Function.mod_clicked, fg = "black", bg = "#a8a7a5")
    btn_mod.pack(side = "left", expand = True, fill = "both")

    bl_btn = tk.Button(btnrow4, text = "(", font = "Arial 21", relief = "groove", bd = 0, command = Function.bl_clicked, fg = "black", bg = "#e0a13a")
    bl_btn.pack(side = "left", expand = True, fill = "both")

    br_btn = tk.Button(btnrow4, text = ")", font = "Arial 21", relief = "groove", bd = 0, command = Function.br_clicked, fg = "black", bg = "#e0a13a")
    br_btn.pack(side = "left", expand = True, fill = "both")

    dot_btn = tk.Button(btnrow4, text = ".", font = "Arial 21", relief = "groove", bd = 0, command = Function.dot_clicked, fg = "black", bg = "#e0a13a")
    dot_btn.pack(side = "left", expand = True, fill = "both")

    btn_clear = tk.Button(btnrow4, text = "C", font = "Arial 23", relief= "groove", bd = 0, command = Function.btn_clear_clicked, fg = "black", bg = "#a8a7a5")
    btn_clear.pack(side = "left", expand = True, fill = "both")

    btn_del = tk.Button(btnrow4, text = "del", font = "Arial 20", relief = "groove", bd = 0, command = Function.del_clicked, fg = "black", bg = "#a8a7a5")
    btn_del.pack(side = "left", expand = True, fill = "both")

    btn0 = tk.Button(btnrow4, text = "0", font = "Arial 23", relief= "groove", bd = 0, command = Function.btn0_clicked, fg = "black", bg = "#ffffff")
    btn0.pack(side = "left", expand = True, fill = "both")

    btn_eq = tk.Button(btnrow4, text = "=", font = "Arial 23", relief = "groove", bd = 0, command = Function.btneq_clicked, fg = "black", bg = "#3a96e0")
    btn_eq.pack(side = "left", expand = True, fill = "both")

    btn_div = tk.Button(btnrow4, text = "/", font = "Arial 22", relief = "groove", bd = 0, command = Function.btn_divide_clicked, fg = "black", bg = "#e0a13a")
    btn_div.pack(side = "left", expand = True, fill = "both")

if __name__ == "__main__":
    root.mainloop()
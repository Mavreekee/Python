# 3. Создайте программу для игры в 'Крестики-нолики'.

from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('600x600')
root.title('Крестики-нолики')
 
btn1 = Button(root, text = '', width = 10, height = 5)
btn1.bind('<Button-1>', lambda arg:click(btn1, 0))
btn1.place(x = 0, y = 0)
 
btn2 = Button(root, text = '', width = 10, height = 5)
btn2.bind('<Button-1>', lambda arg:click(btn2, 1))
btn2.place(x = 81, y = 0)
 
btn3 = Button(root, text = '', width = 10, height = 5)
btn3.bind('<Button-1>', lambda arg:click(btn3, 2))
btn3.place(x = 162, y = 0)
 
btn4 = Button(root, text = '', width = 10, height = 5)
btn4.bind('<Button-1>', lambda arg:click(btn4, 3))
btn4.place(x = 0, y = 81)
 
btn5 = Button(root, text = '', width = 10, height = 5)
btn5.bind('<Button-1>', lambda arg:click(btn5, 4))
btn5.place(x = 81, y = 81)
 
btn6 = Button(root, text = '', width = 10, height = 5)
btn6.bind('<Button-1>', lambda arg:click(btn6, 5))
btn6.place(x = 162, y = 81)
 
btn7 = Button(root, text = '', width = 10, height = 5)
btn7.bind('<Button-1>', lambda arg:click(btn7, 6))
btn7.place(x = 0, y = 162)
 
btn8 = Button(root, text = '', width = 10, height = 5)
btn8.bind('<Button-1>', lambda arg:click(btn8, 7))
btn8.place(x = 81, y = 162)
 
btn9 = Button(root, text = '', width = 10, height = 5)
btn9.bind('<Button-1>', lambda arg:click(btn9, 8))
btn9.place(x = 162, y = 162)
 
xo = 1
 
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
click_button = []
 
def click(button, pressed_btn):   
    global click_button
    global xo
    if pressed_btn not in click_button:
        if xo == 1:
            button.config(text = 'X')
            xo=2
            field[pressed_btn] = 'X'
        elif xo == 2:
            button.config(text = '0')
            xo=1
            field[pressed_btn] = '0'
        click_button.append(pressed_btn)
        check_win()
        
def check_win():
    global field
    global click_button
    if len(click_button) == 9:
        tkinter.messagebox.showinfo(message = 'Ничья')
        restart()
        
    elif field[0] == field[1] == field[2]:
        if field[0] == 'X':
            tkinter.messagebox.showinfo(message = 'Крестики выиграли')
        else:
            tkinter.messagebox.showinfo(message = 'Нолики выиграли')
        restart()
            
    elif field[3] == field[4] == field[5]:
        if field[3] == 'X':
            tkinter.messagebox.showinfo(message = 'Крестики выиграли')
        else:
            tkinter.messagebox.showinfo(message = 'Нолики выиграли')
        restart()
            
    elif field[6] == field[7] == field[8]:
        if field[6] == 'X':
            tkinter.messagebox.showinfo(message = 'Крестики выиграли')
        else:
            tkinter.messagebox.showinfo(message = 'Нолики выиграли')
        restart()
 
    elif field[0] == field[4] == field[8]:
        if field[0] == 'X':
            tkinter.messagebox.showinfo(message = 'Крестики выиграли')
        else:
            tkinter.messagebox.showinfo(message = 'Нолики выиграли')
        restart()    
        
    elif field[2] == field[4] == field[6]:
        if field[2] == 'X':
            tkinter.messagebox.showinfo(message = 'Крестики выиграли')
        else:
            tkinter.messagebox.showinfo(message = 'Нолики выиграли')
        restart()        
        
    elif field[0] == field[3] == field[6]:
        if field[0] == 'X':
            tkinter.messagebox.showinfo(message = 'Крестики выиграли')
        else:
            tkinter.messagebox.showinfo(message = 'Нолики выиграли')
        restart()
 
    elif field[1] == field[4] == field[7]:
        if field[0] == 'X':
            tkinter.messagebox.showinfo(message = 'Нолики выиграли')
        else:
            tkinter.messagebox.showinfo(message = 'Крестики выиграли')
        restart()
        
    elif field[2] == field[5] == field[8]:
        if field[0] == 'X':
            tkinter.messagebox.showinfo(message = 'Нолики выиграли')
        else:
            tkinter.messagebox.showinfo(message = 'Крестики выиграли')
        restart() 
 
btn_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]   
       
def restart():
    global field
    global click_button
    global xo
    field  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    xo = 1
    click_button = []
    for i in range(len(btn_list)):
                   btn_list[i].config(text = '')
    
root.mainloop()
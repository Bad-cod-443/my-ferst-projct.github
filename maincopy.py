import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Ошибка")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Калькулятор")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8)

buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', ' ',
    '1', '2', '3', '-', ' ',
    '0', '.', '=', '+', ' '
]

frame = tk.Frame(root)
frame.pack()

for button in buttons:
    btn = tk.Button(frame, text=button, font="lucida 15 bold")
    btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    btn.bind("<Button-1>", click)

root.mainloop()

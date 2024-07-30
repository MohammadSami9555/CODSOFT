# calculator using tkinter Gui
import tkinter as tk

class Calculator:
  def __init__(self, master):
    self.master = master
    master.title("Calculator")
    master.configure(background='#f0f0f0')  # Set the background color of the window

    self.equation = tk.StringVar()
    self.entry = tk.Entry(master, textvariable=self.equation, width=25, borderwidth=5, relief='ridge', 
                          font=('Arial', 18), fg='#00698f', bg='#ffffff')  # Set the font, foreground, and background colors
    self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
      '7', '8', '9', '/',
      '4', '5', '6', '*',
      '1', '2', '3', '-',
      '0', '.', 'C', '+'
    ]

    row = 1
    col = 0
    for text in buttons:
      button = tk.Button(master, text=text, width=5, command=lambda t=text: self.click(t), 
                         font=('Arial', 14), fg='#ffffff', bg='#00698f', relief='ridge')  # Set the font, foreground, and background colors
      button.grid(row=row, column=col, padx=5, pady=5)
      col += 1
      if col > 3:
        col = 0
        row += 1

    equal_button = tk.Button(master, text='=', width=5, command=self.evaluate, 
                             font=('Arial', 14), fg='#ffffff', bg='#00698f', relief='ridge')  # Set the font, foreground, and background colors
    equal_button.grid(row=5, column=3, padx=5, pady=5)

  def click(self, text):
    if text == 'C':
      self.equation.set('')
    else:
      self.equation.set(self.equation.get() + text)

  def evaluate(self):
    try:
      result = str(eval(self.equation.get()))
      self.equation.set(result)
    except:
      self.equation.set('Error')

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

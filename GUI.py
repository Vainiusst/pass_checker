import tkinter as tk
import checkmypass as cmp

def checker(event=None):
    result = cmp.main(entry1.get())
    response['text'] = result

root = tk.Tk()

root.title("Password checker")
root.iconbitmap("./favicon.ico")

canvas1 = tk.Canvas(root, width=500, height=250, relief="raised")
canvas1.pack()

text_head = tk.Label(root, text="Sooo. Have You been PWNed?", font="bold 16")
canvas1.create_window(250, 40, window=text_head)

text_pass = tk.Label(root, text="Please enter Your password:")
canvas1.create_window(150, 90, window=text_pass)

entry1 = tk.Entry(root, show="*")
canvas1.create_window(350, 90, window=entry1)

button1 = tk.Button(text="Check the PWNage", bg="orange", command=checker)
root.bind("<Return>", checker)
canvas1.create_window(250, 140, window=button1)

response = tk.Label(root)
canvas1.create_window(250, 200, window=response)

root.mainloop()
import tkinter as tk

def key_press(event):
    key = event.keysym
    print(key)

def key_release(event):
    pass

def main():
    root = tk.Tk()
    root.geometry("500x500") 

    root.resizable(False, False) 

    root.title("Captura de Teclas")
    text = tk.Text(root, height=500, width=500)
    text.pack()
    text.focus()
    text.bind("<KeyPress>", key_press)
    text.bind("<KeyRelease>", key_release)
    root.mainloop()

if __name__ == "__main__":
    main()



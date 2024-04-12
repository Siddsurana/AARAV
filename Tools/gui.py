import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def display_output_window(output):
    root = tk.Tk()
    root.title("Output Window")
    root.geometry("800x600")

    output_text = ScrolledText(root, wrap=tk.WORD)
    output_text.pack(expand=True, fill='both')

    def display_output(output):
        output_text.insert(tk.END, output + "\n")
        output_text.see(tk.END)

    display_output(output)

    root.mainloop()

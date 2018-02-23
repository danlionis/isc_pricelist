import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox
from pricelist import generate_pricelist
import os

PRICELIST = 0
MARKETSHARE = 1
OUTPUT = 2

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.label_pricelist_var = tk.StringVar()
        self.label_pricelist_var.set('FILE NOT SET!')

        self.label_marketshare_var = tk.StringVar()
        self.label_marketshare_var.set('FILE NOT SET!')

        self.label_output_var = tk.StringVar()
        self.label_output_var.set('DIRECTORY NOT SET!')


        self.pricelist_src = ""
        self.marketshare_src = ""
        self.output_src = ""

        self.create_widgets()

    def create_widgets(self):
        tk.Label(text="Preisliste (.csv)").grid(row=0, column=0, sticky=tk.W)
        self.label_pricelist = tk.Label(textvariable=self.label_pricelist_var)
        self.label_pricelist.grid(row=0, column=2, sticky=tk.W)

        tk.Label(text="Marketshares (.csv)").grid(row=1, column=0, sticky=tk.W)
        self.label_marketshare = tk.Label(textvariable=self.label_marketshare_var)
        self.label_marketshare.grid(row=1, column=2, sticky=tk.W)

        tk.Label(text="Ausgabe Ordner").grid(row=2, column=0, sticky=tk.W)
        self.label_output = tk.Label(textvariable=self.label_output_var)
        self.label_output.grid(row=2, column=2, sticky=tk.W)

        tk.Button(text="Choose File", command=lambda : self.choose_file(PRICELIST)).grid(row=0, column=1, sticky=tk.W)
        tk.Button(text="Choose File", command=lambda : self.choose_file(MARKETSHARE)).grid(row=1, column=1, sticky=tk.W)
        tk.Button(text="Choose Directory", command=lambda : self.choose_file(OUTPUT)).grid(row=2, column=1, sticky=tk.W)
        tk.Button(text="Generate", command=lambda : self.save_file()).grid(row=5, column=0, sticky=tk.W)

        tk.Label(text="Marge (in %)").grid(row=3, column=0)
        self.entry_anteil = tk.Entry()
        self.entry_anteil.grid(row=3, column=1)
        self.entry_anteil.insert(0, 10)

    def choose_file(self, type):
        if type == PRICELIST:
            pricelist_src= askopenfilename()
            if not pricelist_src == "":
              self.pricelist_src = pricelist_src
              self.label_pricelist_var.set(self.pricelist_src)
        elif type == MARKETSHARE:
            marketshare_src = askopenfilename()
            if not marketshare_src == "":
              self.marketshare_src = marketshare_src
              self.label_marketshare_var.set(self.marketshare_src)
        elif type == OUTPUT:
            output_src = askdirectory()
            if not output_src == "":
              self.output_src = output_src
              self.label_output_var.set(self.output_src)

    def save_file(self):
        # print(self.pricelist_src, self.marketshare_src, self.output_src)
        #filename = asksaveasfilename(initialdir="/", initialfile="country_prices", defaultextension=".csv")

        if self.pricelist_src and self.marketshare_src and self.output_src and self.entry_anteil.get():
            generate_pricelist(self.pricelist_src, self.marketshare_src, self.output_src, float(self.entry_anteil.get()))
            os.startfile(self.output_src)
        else:
            messagebox.showinfo("Error", "Please fill in all values")


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Generator')
    root.geometry("600x400")
    App(root)
    root.mainloop()

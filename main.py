import tkinter as tk
from tkinter import filedialog

import super_parser as ps
from input_file import input_data


class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lb1 = tk.Label(self, text="Chose a file:", font=("", 20))
        self.lb1.grid(row=1, column=1, padx=20, pady=10)

        self.bt1 = tk.Button(self, text="open file", font=("", 14), command=self.OpenFile)
        self.bt1.grid(row=1, column=2)

        self.finalText = tk.Text(self, bd=2, font=("Arial", 16), width=20, height=5,
                                 wrap=tk.WORD, state=tk.DISABLED)
        self.finalText.grid(row=2, column=1, columnspan=2, pady=5)

        self.lb2 = tk.Label(self, text="All words save in dictionary.txt", font=("", 14))
        self.lb2.grid(row=3, column=1, columnspan=3)

    def OpenFile(self):
        ftypes = [('txt files', '*.txt'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            self.ChangeText("File affirmed!")
            dictionary = input_data(fl)
            errors = ps.main(dictionary)

            if errors == 0:
                self.ChangeText("Success!\n"
                                "Use this symbol - @ to split words by cards in Quizlet.")
            else:
                self.ChangeText(f"File has been proccessed.\n"
                                f"Unfortunately, {errors} words weren't found.\n"
                                f"Use this symbol - @ to split words by cards in Quizlet.")


    def ChangeText(self, text):
        self.finalText.config(state=tk.NORMAL)
        self.finalText.delete(0.0, tk.END)
        self.finalText.insert(0.0, text)
        self.finalText.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = Application(root)

    w, h = 300, 240
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    root.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
    root.title("ReWord to Quizlet")
    root.resizable(False, False)

    root.mainloop()


if __name__ == "__main__":
    main()

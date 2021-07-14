import tkinter as tk
from sudoku_solver import *


class Lotfi(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        current = self.get()
        if current.isdigit():
            # the current value is only digits; allow this
            if 9 < int(current):
                self.set(current[0])
        elif current == '':
            return
        else:
            self.set('')


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.matrix = []
        # two main frames defined
        self.grid_frame = tk.LabelFrame(self.master, pady=20, background="orange")
        self.bottom_frame = tk.LabelFrame(self.master)

        # two label frames of the bottom frame defined
        self.buttons_label_frame = tk.LabelFrame(self.bottom_frame, pady=20, padx=20, background="yellow")

        self.top_text = tk.Text(self.master, font=('Arial', 11), height=1, bg="light yellow", bd=0, pady=10)
        self.top_text.tag_configure("center", justify='center')
        self.top_text.insert(1.0, "Insert the puzzle you want to solve to the grid below:")
        self.top_text.tag_add("center", 1.0, "end")
        self.top_text.config(state=tk.DISABLED)

        # make 9 boxes
        for i in range(9):
            line = []
            for j in range(9):
                e = Lotfi(master=self.grid_frame, width=3, font=('Arial', 10, 'bold'), justify='center',
                          cursor="arrow")
                line.append(e)
                e.grid(row=i, column=j, ipadx=6, ipady=6)
            self.matrix.append(line)

        # reset and solve buttons
        self.reset_button = tk.Button(self.buttons_label_frame, text="Reset grid", font=('Arial', 10, 'bold'), command=self.reset_grid, bg="red")
        self.solve_button = tk.Button(self.buttons_label_frame, text="Solve puzzle", font=('Arial', 10, 'bold'), command=self.solve, bg="light green")

        self.create_widgets()

    def create_widgets(self):
        self.reset_button.pack()
        self.solve_button.pack()
        self.top_text.pack()
        self.buttons_label_frame.grid(row=1, column=1)
        self.grid_frame.pack()
        self.bottom_frame.pack()

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.matrix[i][j].get()
                if not val:
                    val = '0'
                row.append(int(val))
            grid.append(row)
        return grid

    def reset_grid(self):
        for i in range(9):
            for j in range(9):
                self.matrix[i][j].set('')

    def solve(self):
        grid = self.get_grid()
        solver = Sudoku(grid)
        solver.backtrack()
        solution = solver.solution

        self.fill_grid(solution)

    def fill_grid(self, solution):
        for i in range(9):
            for j in range(9):
                self.matrix[i][j].set(solution[i][j])


def main():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Sudoku Solver")
    root.configure(background='light yellow')
    app = Application(root)
    app.mainloop()


if __name__ == "__main__":
    main()

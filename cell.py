import os
from tkinter import Button, Label, messagebox
import ctypes
import random
import sys
import const
import time

class Cell:
    
    all = []
    cell_count = const.CELL_COUNT
    cell_count_label_object = None
    cell_count_label_flag = None
    
    def __init__(self, x, y, is_mine=False) -> None:
        self.x = x
        self.y = y
        self.cell_btn_objet = None
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        
        Cell.all.append(self)

    
    def create_btn_object(self, location):
        btn = Button(
            location,
            bg="green",
            fg="brown",
            width=2,
            height=1,
            # text=f'{self.x},{self.y}'
        )
        # events
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl =  Label(
            location,
            bg="blue",
            fg="white",
            text=f"Cells Left: {Cell.cell_count}",
            font=("", 10)
        )
        Cell.cell_count_label_object = lbl
        
    @staticmethod
    def create_flags_count_label(location):
        lbl_flags = Label(
            location,
            bg="red",
            fg="white",
            text=f"Flags Left: {const.FLAGS}",
            font=("", 10)
        )
        Cell.cell_count_label_flag = lbl_flags
    
    
    @staticmethod
    def randomize_mines():
        mined_cells = random.sample(Cell.all, const.MINES_COUNT)
        
        for mined_cell in mined_cells:
            # mined_cell.create_btn_object.configure(bg='red')
            mined_cell.is_mine = True
            # self.cell_btn_object.configure(bg='red')
    
    
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mines()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # if mines count  = left count, player wins
            if Cell.cell_count == const.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won!', 'Game Over', 0)

        # cancel events clicks
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        #  return cell object based on value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ] 
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            if self.surrounded_cells_mines_length != 0:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length)
            # replace text of cell count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )
            #
            self.cell_btn_object.configure(
                bg="SystemButtonFace"
            )

        self.is_opened = True
        
    def right_click_actions(self, event):
        # if 0 < const.FLAGS <= 10:
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange',
                
            )
            self.is_mine_candidate = True
            const.FLAGS -= 1
            Cell.cell_count_label_flag.configure(
                text=f"Flags Left: {const.FLAGS}"
            )
            
        else:
            self.cell_btn_object.configure(
                bg='green',
            )
            
            const.FLAGS += 1
            Cell.cell_count_label_flag.configure(
                text=f"Flags Left: {const.FLAGS}"
            )
            self.is_mine_candidate = False
        

    def show_mines(self):
        # a logic to interrupt the game
        
        self.cell_btn_object.configure(bg='red')
        
        # mined_cells = [cell for cell in all if cell.is_mine]
        # for cell in Cell.all:
        #     if cell.is_mine:
        #         self.cell_btn_object.configure(bg='red')
        time.sleep(5)
        res = messagebox.askquestion('Game over', 'Play again?')
        if res=='yes':
            #! play again
            # pass
            messagebox.showinfo('sample 1', 'Restart game')
            # main.root.destroy()
            # os.startfile("main.py")
        else: 
            sys.exit()
        # messagebox.showinfo('Game over', 'You clicked on a mine!')
    
    
    
    # ctypes.windll.user32.MessageBoxW(
    # 0, 'You clicked on a mine!', 'Game Over', 0)

# todo: update exit menu, add function to restart the game
# todo: if loose game? show all mines red color

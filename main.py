from tkinter import *
from cell import Cell
import const





def height_prct(percentage):
    return (const.HEIGHT / 100) * percentage


def width_prct(percentage):
    return(const.WIDTH / 100) * percentage

def main():
    root = Tk()

    # Override the settings of the window
    root.configure(bg="gray")
    root.geometry(f'{const.WIDTH}x{const.HEIGHT}+800+300')
    root.title("Minesweeper")
    root.resizable(False, False)
    
    top_frame = Frame(
    root,
    bg="lightblue",
    width=const.WIDTH,
    height=height_prct(15)
    )

    top_frame.place(x=0, y=0)

    game_frame = Frame(
        root,
        border=5,
        bg="brown",
        width=const.WIDTH,
        height=height_prct(85)
    )

    game_frame.place(x=0, y=height_prct(15))
        
    for x in range(const.GRID_SIZE_WIDTH):
        for y in range(const.GRID_SIZE_HEIGHT):
            c = Cell(x, y)
            c.create_btn_object(game_frame)
            c.cell_btn_object.grid(
                column=x,row=y
            )

    Cell.create_cell_count_label(top_frame)
    Cell.cell_count_label_object.place(
        x=10, y=height_prct(15)//2-10
    )

    Cell.create_flags_count_label(top_frame)
    Cell.cell_count_label_flag.place(
        x=const.WIDTH-90, y=height_prct(15)//2-10
    )
    Cell.randomize_mines()
    
    root.mainloop()









if __name__ == "__main__":
    main()


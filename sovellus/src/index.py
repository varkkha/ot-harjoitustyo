from tkinter import Tk
from ui.ui import UI

#UI was developed with reference to the sample repository "todo-app".

def main():
    window = Tk()
    window.title("Aurinkopaneelilaskuri")

    window.configure(bg="lightblue")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()

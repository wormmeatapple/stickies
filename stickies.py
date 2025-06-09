import tkinter as tk
from tkinter import simpledialog

class stickynote:
    def __init__(self, master, x=100, y=100, width=200, height=150, text=""): # add resizing later

        self.win = tk.Toplevel(master)
        self.win.overrideredirect(True)
        self.win.attributes("-topmost", True)
        self.win.geometry(f"{width}x{height}+{x}+{y}")

        self.win.bind("<FocusOut>", self.on_focus_out)
        self.win.bind("<FocusIn>", self.on_focus_in)

        self.text = tk.Text(self.win, wrap="word", undo=True)
        self.text.pack(expand=True, fill="both")
        self.text.insert("1.0", text)
        # add different colours and drawing 

        self._drag_data = {"x": 0, "y": 0}
        self.win.bind("<ButtonPress-1>", self.start_move)
        self.win.bind("<B1-Motion>", self.do_move)

        self.title_bar = tk.Frame(self.win, bg="gray", height=20)
        self.title_bar.pack(fill="x")

    def on_focus_out(self, event):
        self.win.attributes("-topmost", True)

    def on_focus_in(self, event):
        self.win.attributes("-topmost", True)
    
    def start_move(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
    
    def do_move(self, event):
        dx = event.x - self._drag_data["x"]
        dy = event.y - self._drag_data["y"]
        x = self.win.winfo_x() + dx
        y = self.win.winfo_y() + dy
        self.win.geometry(f"+{x}+{y}")

    def get_text(self):
        return self.text.get("1.0", "end-1c")

class stickies:
    def __init__(self, event=None):
        self.root = tk.Tk()
        #self.root.withdraw()
        self.notes = []

        self.root.bind("<Control-n>", self.create_note)
        self.create_note

        self.root.bind("<Control-k>", self.kill)
        self.kill

    def create_note(self, event=None):
        init_text = simpledialog.askstring("New note", "Inital text:", parent=self.root) 
        note = stickynote(self.root, text=init_text)
        self.notes.append(note)
    
    def kill(self, event=None):
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = stickies()
    app.run()


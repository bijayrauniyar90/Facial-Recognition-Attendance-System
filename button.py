import tkinter as tk


class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, text="", command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1, relief="raised", highlightthickness=0,
                           width=width + padding, height=height + padding)
        self.command = command

        # Calculate arc size
        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius

        # Create rounded rectangle
        self.create_arc((padding, padding, rad, rad), start=90,
                        extent=90, fill=color, outline=color)
        self.create_arc((width-rad+padding, padding, width+padding, rad),
                        start=0, extent=90, fill=color, outline=color)
        self.create_arc((width-rad+padding, height-rad+padding, width+padding,
                        height+padding), start=270, extent=90, fill=color, outline=color)
        self.create_arc((padding, height-rad+padding, rad, height+padding),
                        start=180, extent=90, fill=color, outline=color)
        self.create_rectangle(padding, cornerradius+padding, width+padding,
                              height-cornerradius+padding, fill=color, outline=color)
        self.create_rectangle(cornerradius+padding, padding, width -
                              cornerradius+padding, height+padding, fill=color, outline=color)

        # Add text
        self.create_text(width/2 + padding, height/2 +
                         padding, text=text, fill="white")

        # Bind click event
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command:
            self.command()


def on_click():
    print("Button clicked!")


root = tk.Tk()
root.title("Rounded Button Example")

button = RoundedButton(root, width=100, height=40, cornerradius=10,
                       padding=10, color="blue", text="Click Me", command=on_click)
button.pack(pady=20)

root.mainloop()

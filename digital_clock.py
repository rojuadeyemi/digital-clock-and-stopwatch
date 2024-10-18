import tkinter as tk
import time

class StopWatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ade ~ The Codeine Addict")
        self.root.geometry("560x270")
        self.root.config(bg="grey")

        self.label = tk.Label(self.root, background="black", font=("arial", 70), foreground="cyan", borderwidth=10)
        self.label.pack(side=tk.TOP, pady=7)

        self.stopwatch = StopWatch(self.root)
        self.stopwatch.pack(side=tk.TOP)

        self.create_buttons()
        self.update_time()

    def create_buttons(self):
        bottom_frame = tk.Frame(self.root, width=600)
        bottom_frame.pack(side=tk.BOTTOM)

        buttons = [
            ("START/RESUME", self.stopwatch.start, 20),
            ("PAUSE", self.stopwatch.stop, 10),
            ("RESET", self.stopwatch.reset, 10),
            ("CLOSE", self.exit_app, 10),
        ]

        for text, command, width in buttons:
            btn = tk.Button(bottom_frame, text=text, command=command, width=width, height=3, bg="chocolate1")
            btn.pack(side=tk.LEFT)

            # Bind hover effects
            btn.bind("<Enter>", lambda event, b=btn: self.on_hover(b))
            btn.bind("<Leave>", lambda event, b=btn: self.on_leave(b))

    def on_hover(self, button):
        button.config(bg="dark orange", fg="white")

    def on_leave(self, button):
        button.config(bg="chocolate1", fg="black")

    def update_time(self):
        current_time = time.strftime("%I:%M:%S %p")
        self.label.config(text=current_time)
        self.label.after(1000, self.update_time)

    def exit_app(self):
        self.root.destroy()

class StopWatch(tk.Frame):
    def __init__(self, parent=None, **kw):
        super().__init__(parent, kw)
        self.start_time = 0.0
        self.elapsed_time = 0.0
        self.running = False
        self.timestr = tk.StringVar()
        self.create_display()

    def create_display(self):
        time_text = tk.Label(self, textvariable=self.timestr, font=("arial", 50), fg="royal blue", bg="black")
        self.set_time(self.elapsed_time)
        time_text.pack(fill=tk.X, expand=False, pady=5, padx=10)

    def update_timer(self):
        self.elapsed_time = time.time() - self.start_time
        self.set_time(self.elapsed_time)
        self.timer = self.after(50, self.update_timer)

    def set_time(self, elapsed):
        minutes = int(elapsed / 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed - int(elapsed)) * 100)
        self.timestr.set(f'{minutes:02}:{seconds:02}:{milliseconds:02}')

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.update_timer()
            self.running = True

    def stop(self):
        if self.running:
            self.after_cancel(self.timer)
            self.elapsed_time = time.time() - self.start_time
            self.set_time(self.elapsed_time)
            self.running = False

    def reset(self):
        self.elapsed_time = 0.0
        self.set_time(self.elapsed_time)
        if self.running:
            self.start_time = time.time()

if __name__ == "__main__":
    root = tk.Tk()
    app = StopWatchApp(root)
    root.mainloop()

import tkinter as tk

class BuzzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Buzzer System")
        self.master.geometry("300x200")
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start_game)
        self.start_button.pack(pady=20)
        
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

    def start_game(self):
        self.master.withdraw()
        buzzer_window = tk.Toplevel(self.master)
        BuzzerGame(buzzer_window, self.master)

class BuzzerGame:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("Buzzer Game")
        self.master.geometry("400x300")

        self.team_number = None
        self.buzzed_teams = []
        self.bg_color = None

        self.buzzer_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.buzzer_button.pack(pady=20)

        self.display_label = tk.Label(self.master, text="", font=("Helvetica", 16), fg="white", bg="black", wraplength=350, justify="left")
        self.display_label.place(relx=0.5, rely=0.9, anchor="center")

        self.ordinal_label = tk.Label(self.master, text="", font=("Helvetica", 16), fg="black", bg="white", wraplength=350, justify="left")
        self.ordinal_label.place(relx=0.05, rely=0.05, anchor="w")

        self.check_buzzer()

    def check_buzzer(self):
        self.master.bind("<Key>", self.key_pressed)

    def key_pressed(self, event):
        try:
            team_number = int(event.char)
            if 1 <= team_number <= 8 and team_number not in self.buzzed_teams:
                if self.team_number is None:
                    self.bg_color = self.set_bg_color(team_number)
                    self.team_number = team_number
                    self.display_first_buzz()
                else:
                    self.team_number = team_number
                    self.update_gui()
        except ValueError:
            pass  # Ignore non-numeric key presses

    def set_bg_color(self, team_number):
        colors = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "pink"]
        return colors[team_number - 1]

    def display_first_buzz(self):
        message = f"Team {self.team_number} has buzzed"
        self.display_label.config(text=message)
        self.master.configure(bg=self.bg_color)

    def update_gui(self):
        ordinal_indicator = f"{self.get_ordinal_suffix(len(self.buzzed_teams) + 2)}:"
        input_display = f"{ordinal_indicator} Team {self.team_number}, " + self.ordinal_label.cget("text")
        self.ordinal_label.config(text=input_display)
        self.buzzed_teams.append(self.team_number)

    def get_ordinal_suffix(self, number):
        if 10 <= number % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")
        return f"{number}{suffix}"

    def reset_game(self):
        self.buzzed_teams = []
        self.team_number = None
        self.bg_color = None
        self.display_label.config(text="")
        self.ordinal_label.config(text="")
        self.master.configure(bg="SystemButtonFace")

if __name__ == "__main__":
    root = tk.Tk()
    app = BuzzerApp(root)
    root.mainloop()

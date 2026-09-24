import tkinter as tk
import random

# ---------------- Question Banks ----------------
additions = [
    ["""Q) 1 + 3 =

     a. 2

     b. 4

     c. 5

     d. 6""", "b"],
    ["""Q) 3 + 2 =

     a. 4

     b. 5

     c. 6

     d. 7""", "b"],
    ["""Q) 4 + 4 =

     a. 6

     b. 7

     c. 8

     d. 10""", "c"],
    ["""Q) 3 + 5 =

     a. 2

     b. 7

     c. 8

     d. 9""", "c"],
    ["""Q) 7 + 2

     a. 5

     b. 6

     c. 8

     d. 9""", "d"],
    ["""Q) 10 + 2 =

     a. 8

     b. 9

     c. 11

     d. 12""", "d"],
    ["""Q) 7 + 6 =

     a. 12

     b. 13

     c. 14

     d. 15""", "b"],
    ["""Q) 5 + 4 =

     a. 9

     b. 8

     c. 7

     d. 6""", "a"],
    ["""Q) 2 + 2 =

     a. 0

     b. 3

     c. 4

     d. 5""", "c"],
    ["""Q) 9 + 3 =

     a. 10

     b. 11

     c. 12

     d. 13""", "c"],
    ["""Q) 8 + 3 =

     a. 10

     b. 11

     c. 12

     d. 13""", "b"],
    ["""Q) 9 + 9 =

     a. 15

     b. 16

     c. 17

     d. 18""", "d"],
    ["""Q) 8 + 7 =

     a. 13

     b. 14

     c. 15

     d. 16""", "c"],
    ["""Q) 8 + 8 =

     a. 14

     b. 15

     c. 16

     d. 17""", "c"],
    ["""Q) 7 + 10 =

     a. 0

     b. 7

     c. 16

     d. 17""", "d"],
    ["""Q) 6 + 9 =

     a. 13

     b. 14

     c. 15

     d. 16""", "c"],
    ["""Q) 6 + 6 =

     a. 11

     b. 12

     c. 13

     d. 14""", "b"],
    ["""Q) 6 + 2 =

     a. 4

     b. 7

     c. 8

     d. 9""", "c"],
    ["""Q) 3 + 8 + 13 =

     a. 22

     b. 23

     c. 24

     d. 25""", "c"],
    ["""Q) 4 + 4 + 0 + 4 + 5 =

     a. 15

     b. 16

     c. 17

     d. 18""", "c"]
]

subtraction = [
    ["""Q) 10-5=

  a.5

  b.6

  c.7

  d.8""", "a"],
    ["""Q) 16-5=

  a.14

  b.13

  c.12

  d.11""", "d"],
    ["""Q) 20-12=

  a.6

  b.7

  c.8

  d.9""", "c"],
    ["""Q) 11-7=

  a.1

  b.2

  c.3

  d.4""", "d"],
    ["""Q) 17-9=

  a.8

  b.9

  c.10

  d.11""", "a"],
    ["""Q) 19-12=

  a.4

  b.5

  c.6

  d.7""", "d"],
    ["""Q) 11-7=

  a.1

  b.2

  c.3

  d.4""", "d"],
    ["""Q) 16-12=

  a.1

  b.2

  c.3

  d.4""", "d"],
    ["""Q) 45-24=

  a.18

  b.19

  c.20

  d.21""", "d"],
    ["""Q) 78-46=

  a.31

  b.32

  c.33

  d.34""", "b"],
    ["""Q) 100-74=

  a.26

  b.27

  c.28

  d.29""", "a"],
    ["""Q) 36-23=

  a.12

  b.13

  c.14

  d.15""", "b"],
    ["""Q) 47-26=

  a.34

  b.21

  c.36

  d.32""", "b"],
    ["""Q) 54-36=

  a.81

  b.18

  c.23

  d.28""", "b"],
    ["""Q) 89-34=

  a.34

  b.54

  c.64

  d.55""", "d"],
    ["""Q) 67-34=

  a.45

  b.40

  c.33

  d.44""", "c"],
    ["""Q) 126-90=

  a.36

  b.46

  c.26

  d.56""", "a"],
    ["""Q) 459-247=

  a.213

  b.312

  c.212

  d.214""", "c"],
    ["""Q) 567-543=

  a.24

  b.34

  c.54

  d.64""", "a"],
    ["""Q) 890-678=

  a.344

  b.345

  c.212

  d.456""", "c"]
]

multiplication = [
    ["""Q) 5 x 5 =

   a.24

   b.25

   c.34

   d.23""", "b"],
    ["""Q) 6 x 7=

  a.48

  b.42

  c.49

  d.56""", "b"],
    ["""Q) 4 x 5=

  a.25

  b.30

  c.20

  d.15""", "c"],
    ["""Q) 8 x 9=

  a.72

  b.64

  c.63

  d.80""", "a"],
    ["""Q) 9 x 7=

  a.72

  b.64

  c.63

  d.80""", "c"],
    ["""Q) 7 x 7 =

  a.49

  b.45

  c.63

  d.70""", "a"],
    ["""Q) 12 x 8 =

  a.108

  b.72

  c.120

  d.96""", "d"],
    ["""Q) 13 x 6 =

  a.72

  b.78

  c.144

  d.90""", "b"],
    ["""Q) 14 x 8 =

  a.112

  b.122

  c.132

  d.92""", "a"],
    ["""Q) 45 x 3 =

  a.125

  b.135

  c.95

  d.90""", "b"],
    ["""Q) 8 x 4=

  a.32

  b.24

  c.36

  d.34""", "a"],
    ["""Q) 23 x 4 =

  a.72

  b.62

  c.78

  d.92""", "d"],
    ["""Q) 56 x 2 =

  a.112

  b.212

  c.211

  d.121""", "a"],
    ["""Q) 34 x 4 =

  a.136

  b.146

  c.236

  d.246""", "a"],
    ["""Q) 42 x 2 =

  a.84

  b.86

  c.88

  d.92""", "a"],
    ["""Q) 84 x 3 =

  a.262

  b.252

  c.242

  d.232""", "b"],
    ["""Q) 47 x 2 =

  a.92

  b.84

  c.94

  d.82""", "c"],
    ["""Q) 34 x 5 =

  a.135

  b.170

  c.175

  d.180""", "b"],
    ["""Q) 22 x 5 =

  a.110

  b.120

  c.111

  d.101""", "a"],
    ["""Q) 80 x 2 =

  a.150

  b.160

  c.120

  d.130""", "b"]
]

division = []

TOPICS = {
    1: ("Addition", additions),
    2: ("Subtraction", subtraction),
    3: ("Multiplication", multiplication),
    4: ("Division", division),
    5: ("Differentiation", []),
    6: ("Integration", []),
}


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maths Quiz")
        self.geometry("600x480")
        self.resizable(False, False)

        self.name = ""
        self.questions = []
        self.current_index = 0
        self.correct = 0
        self.incorrect = 0
        self.topic_name = ""

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.show_welcome_screen()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # ---------------- Screen 1: Welcome + Name ----------------
    def show_welcome_screen(self):
        self.clear_container()
        tk.Label(self.container, text="WELCOME TO MATHS QUIZ",
                 font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.container,
                 text="Practice Addition, Subtraction, Multiplication,\n"
                      "Division, Differentiation and Integration.\n"
                      "Choose any one topic to study.",
                 font=("Arial", 11), justify="center").pack(pady=10)

        tk.Label(self.container, text="Enter your name:", font=("Arial", 12)).pack(pady=(20, 5))
        self.name_entry = tk.Entry(self.container, font=("Arial", 12), justify="center")
        self.name_entry.pack(pady=5)
        self.name_entry.focus()
        self.name_entry.bind("<Return>", lambda e: self.handle_name_submit())

        tk.Button(self.container, text="Continue", font=("Arial", 12),
                  command=self.handle_name_submit).pack(pady=20)

    def handle_name_submit(self):
        name = self.name_entry.get().strip()
        self.name = name if name else "Student"
        self.show_topic_screen()

    # ---------------- Screen 2: Topic selection (click instead of typing) ----------------
    def show_topic_screen(self):
        self.clear_container()
        tk.Label(self.container, text=f"Hi {self.name}, choose your topic:",
                 font=("Arial", 16, "bold")).pack(pady=20)

        for key, (topic_name, _) in TOPICS.items():
            tk.Button(self.container, text=topic_name, font=("Arial", 12), width=25,
                      command=lambda k=key: self.start_quiz(k)).pack(pady=5)

    def start_quiz(self, topic_key):
        topic_name, questions = TOPICS[topic_key]

        if not questions:
            self.clear_container()
            tk.Label(self.container, text=f"{topic_name} quiz is not available yet.",
                     font=("Arial", 14)).pack(pady=40)
            tk.Button(self.container, text="Back to Topics",
                      command=self.show_topic_screen).pack(pady=10)
            return

        self.questions = questions[:]
        random.shuffle(self.questions)
        self.current_index = 0
        self.correct = 0
        self.incorrect = 0
        self.topic_name = topic_name
        self.show_question()

    # ---------------- Screen 3: Question (click the answer button) ----------------
    def show_question(self):
        self.clear_container()

        if self.incorrect >= 3 or self.current_index >= len(self.questions):
            self.show_result_screen()
            return

        q_text, answer = self.questions[self.current_index]
        self.correct_answer = answer.lower()

        tk.Label(self.container, text=f"{self.topic_name} Quiz - Q{self.current_index + 1}",
                 font=("Arial", 12, "bold")).pack(pady=(15, 5))
        tk.Label(self.container, text=f"Incorrect so far: {self.incorrect}/3",
                 font=("Arial", 10), fg="red").pack()

        question_stem = q_text.split("\n\n")[0]
        tk.Label(self.container, text=question_stem, font=("Arial", 14, "bold"),
                 justify="left", wraplength=520).pack(pady=20)

        options = self.extract_options(q_text)

        btn_frame = tk.Frame(self.container)
        btn_frame.pack(pady=10)

        for letter in ["a", "b", "c", "d"]:
            if letter in options:
                tk.Button(btn_frame, text=f"{letter}. {options[letter]}", font=("Arial", 12),
                          width=22, command=lambda l=letter: self.check_answer(l)).pack(pady=4)

        self.feedback_label = tk.Label(self.container, text="", font=("Arial", 12, "bold"))
        self.feedback_label.pack(pady=10)

    def extract_options(self, q_text):
        """Pull the a./b./c./d. option text out of a question block."""
        options = {}
        for line in q_text.splitlines():
            line = line.strip()
            for letter in ["a", "b", "c", "d"]:
                prefix = f"{letter}."
                if line.lower().startswith(prefix):
                    options[letter] = line[len(prefix):].strip()
        return options

    def check_answer(self, chosen_letter):
        if chosen_letter == self.correct_answer:
            self.correct += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.incorrect += 1
            self.feedback_label.config(
                text=f"Incorrect! Correct answer: {self.correct_answer}", fg="red")

        self.current_index += 1
        self.after(900, self.show_question)

    # ---------------- Screen 4: Result ----------------
    def show_result_screen(self):
        self.clear_container()
        total_attempted = self.correct + self.incorrect

        tk.Label(self.container, text="QUIZ RESULT", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.container, text=f"Name: {self.name}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.container, text=f"Topic: {self.topic_name}", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.container, text=f"Total questions attempted: {total_attempted}",
                 font=("Arial", 12)).pack(pady=5)
        tk.Label(self.container, text=f"Correct answers: {self.correct}",
                 font=("Arial", 12), fg="green").pack(pady=5)
        tk.Label(self.container, text=f"Incorrect answers: {self.incorrect}",
                 font=("Arial", 12), fg="red").pack(pady=5)

        tk.Button(self.container, text="Try Another Topic", font=("Arial", 12),
                  command=self.show_topic_screen).pack(pady=15)
        tk.Button(self.container, text="Exit", font=("Arial", 12),
                  command=self.destroy).pack(pady=5)


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
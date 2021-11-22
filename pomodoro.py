import time
import winsound
from tkinter import *
import math

frequency = 350
duration = 350 # milliseconds

def sound():
    for beep in range(3):
        winsound.Beep(frequency, duration)
           
class Pomodoro:
    """Create a model for a Pomodoro timer and its attributes."""

    def __init__(self):
        """Initialize the Pomodoro timer."""
        # self.study_time = study_time
        # self.short_break = short_break
        # self.long_break = long_break
        # self.total_iterations = total_iterations
        self.total_iterations = 10
        self.study_time = 25
        self.short_break = 5
        self.long_break = 30
        self.frequency = 350
        self.duration = 350 # milliseconds
        self.iteration = 0

        ### Testing ###
        self.total_iterations = 1
        self.study_time = 1
        self.short_break = 1
        self.long_break = 1
        self.frequency = 300
        self.duration = 350 # milliseconds
        self.iteration = 0

    def sound(self):
        for beep in range(3):
            winsound.Beep(self.frequency, self.duration)

    def pomodoro_study_timer(self):
        iteration = 0
        iteration_count = 1

        print("Starting your Pomodoro timer!\n\n"
            "The timer runs through four 25-minute study iterations,\n"
            "separated by a 5-minute break. The fifth study iteration\n"
            "is followed by a long break of 30 minutes. Listen for the\n"
            "sound notification to know when to study and when to take\n"
            "appropriate breaks.\n\n"
            "BE SURE TO TAKE YOUR BREAKS!!!\n\n"
        )

        while iteration < 5:
            study_time = Pomodoro()
            study_time.study()

            break_time = Pomodoro()
            break_time.short_break_time()

            print(f"Completed iteration: {iteration_count}\n")
            
            if iteration == 4:
                break_time = Pomodoro()
                break_time.long_break_time()
                break

            # print(f"Completed iteration: {iteration_count}\n")
            iteration += 1
            iteration_count += 1
            # break_time = Pomodoro()
            # break_time.long_break_time()
            # break

            # iteration = 0
            # break

    def study(self):
        """The Pomodoro study time of 25 minutes."""
        print("25-minute Pomodoro study timer starts now!")
        t = self.study_time * 60 # 25 * 60
        # t = 1
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(" " + timer, end="\r") # Overwrite previous line
            time.sleep(1)
            t -= 1
        print("Break Time!!!\n")
        sound()

    def short_break_time(self):
        """The Pomodoro break time of 5 minutes."""
        print("5 minute break starts now!")
        t = self.short_break * 60 # 25 * 60
        # t = 1
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(" " + timer, end="\r") # Overwrite previous line
            time.sleep(1)
            t -= 1
        print("Study Time!!!\n")
        sound()

    def long_break_time(self):
        """The Pomodoro break time of 5 minutes."""
        print("30 minute break starts now!")
        t = self.long_break * 60 # 25 * 60
        # t = 1
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(" " + timer, end="\r") # Overwrite previous line
            time.sleep(1)
            t -= 1
        print("Study Time!!!\n")
        sound()

        # # ------------ COUNTDOWN MECHANISM ------------ #
        # def count_down(count):
        #     count_min = math.floor(count / 60)
        #     count_sec = f"0 {count_sec}"

    def test_timer(self):
        t = 1   ### 25 * 60
        t = 1
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(" " + timer, end="\r") # Overwrite previous line
            time.sleep(1)
            t -= 1
        print("Break Time!!!\n")
        sound()



# testing_timer = Pomodoro()
# print(testing_timer.test_timer())

study_timer = Pomodoro()
study_timer.pomodoro_study_timer()
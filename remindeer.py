# Imports
from win10toast import ToastNotifier
import time
import math


# This function sends notifications to the Windows user (a toast notification)
def send_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)


# This fetches the user's initial input to indicate if they want to start the script
def usr_decision():
    usr_inp = input("Do you want to keep the record of your working duration?(Y/n): ")
    if usr_inp.lower() == "y":
        return True
    if usr_inp.lower() == "n":
        return False


if __name__ == "__main__":
    # This function checks if the user wants to run the script
    #  in the first place and if not it will exit the program
    first_decision = usr_decision()
    if first_decision == True:
        pass
    else:
        exit()

    # This function is supposed to fetch the variables for rest and work time
    def get_time():
        while True:
            try:
                work_time = float(
                    input("In how many minutes do you want to get some rest? ")
                )
                if work_time <= 0:
                    raise ValueError("Work time must be greater than zero.")
                rest_time = float(
                    input("How much rest do you require after it (in minutes)? ")
                )
                if rest_time < 0:
                    raise ValueError("Rest time cannot be negative.")
                return work_time, rest_time
            except ValueError as e:
                print(f"Invalid input: {e}")

    # Works like a timer and when counter riches the variable defined by the user
    # , it notifies the user
    def work_duration_counter(wt):
        try:
            elapsed_work_mins = 0
            start_time = time.time()

            time.sleep(wt * 60)

            elapsed_work_mins = (time.time() - start_time) / 60

            print(
                f"You have been working for {elapsed_work_mins:.2f} minutes, take some rest now!"
            )
            send_notification(
                "REST TIME!",
                f"You have been working for {elapsed_work_mins:.2f} minutes, take some rest now!",
            )

            return True
        except ZeroDivisionError:
            print("Error: Work time cannot be zero.")
            return False

    # Immediately after the work_time_counter, this function starts working
    # , which keeps track of how many minutes the user wanted to rest and notifies them
    def rest_duration_counter(rt, wtf):
        try:
            if wtf:
                rest_time_start = time.time()
                time.sleep(rt * 60)
                elapsed_rest_mins = (time.time() - rest_time_start) / 60
                print(
                    f"You have been resting for {elapsed_rest_mins:.2f} minutes, get back to work!"
                )
                send_notification(
                    "GET BACK TO WORK!",
                    f"You have been resting for {elapsed_rest_mins:.2f} minutes, get back to work!",
                )

            usr_last_inp = input(
                "Do you want to\nexit (e)\nredefine variables (r)\nor restart with previous variables (p)? "
            ).lower()

            return usr_last_inp
        except KeyboardInterrupt:
            print("Operation interrupted. Exiting...")
            exit()

    # Immediately after the rest_time_counter, this function runs to fetch the
    # user's input for terminating the script or keeping it running
    def last_inp_logic(inp):
        if inp == "e":
            exit()
        elif inp == "r":
            overall_process()
        elif inp == "p":
            work_duration_counter()
            rest_duration_counter()
            last_inp_logic()
        else:
            exit()

    # All the logic that has been implemented runs via this function
    def overall_process():
        wt, rt = get_time()
        wtf = work_duration_counter(wt)
        usr_last_inp = rest_duration_counter(rt, wtf)
        last_inp_logic(usr_last_inp)

    # Where all the magic comes to life :)
    try:
        overall_process()
    except KeyboardInterrupt:
        print("Operation interrupted. Exiting...")

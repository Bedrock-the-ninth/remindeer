from win10toast import ToastNotifier
import time
import math


def send_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)


def usr_decision():
    usr_inp = input("Do you want to keep the record of your working duration?(Y/n): ")
    if usr_inp.lower() == "y":
        return True
    if usr_inp.lower() == "n":
        return False


if __name__ == "__main__":
    first_decision = usr_decision()
    if first_decision == True:
        pass
    else:
        exit()

    def get_time():
        global work_time, rest_time
        work_time = float(input("How often do you want to be reminded (per minutes)? "))
        rest_time = float(
            input("How much rest after each set do you need (per minutes)? ")
        )

    def work_hours_counter():
        global work_time_finished
        elapsed_time_mins = 0
        start_time = time.time()
        work_time_finished = False
        while elapsed_time_mins != work_time:
            elapsed_time_mins = (time.time() - start_time) / 60
            if elapsed_time_mins >= work_time:
                print(
                    f"You have been working for {elapsed_time_mins} minutes, take some rest now!"
                )
                send_notification(
                    "REST TIME!",
                    f"You have been working for {math.ceil(elapsed_time_mins)} minutes, take some rest now!",
                )
                work_time_finished = True
                break
            else:
                pass

    def rest_time_counter():
        global usr_last_inp
        if work_time_finished == True:
            rest_time_start = time.time()
            elapsed_rest_mins = 0
            while elapsed_rest_mins != rest_time:
                elapsed_rest_mins = (time.time() - rest_time_start) / 60
                if elapsed_rest_mins >= rest_time:
                    print(
                        f"You have been resting for {elapsed_rest_mins} minutes, get back to work!"
                    )
                    send_notification(
                        "GET BACK TO WORK!",
                        f"You have been resting for {math.ceil(elapsed_rest_mins)} minutes, get back to work!",
                    )
                    break
                else:
                    pass
        usr_last_inp = input(
            "Do you want to exit the program (e),\nredefine the work and rest time variables and go again (r)\nor simply restart the time with the previously set durations (p)? "
        ).lower()

    def overall_process():
        get_time()
        work_hours_counter()
        rest_time_counter()

        def last_inp_logic():
            if usr_last_inp == "e":
                exit()
            elif usr_last_inp == "r":
                overall_process()
            elif usr_last_inp == "p":
                work_hours_counter()
                rest_time_counter()
                last_inp_logic()
            else:
                exit()

        last_inp_logic()

    overall_process()

    # send_notification("Notification Title", "This is the notification message.")

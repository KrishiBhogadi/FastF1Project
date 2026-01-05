import fastf1
import matplotlib.pyplot as plt
def get_valid_int_input(prommpt):
    while True:
        try:
            user_input = input(prommpt)
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except ValueError:
            print("Unexpected error. Please try again.")       


def get_valid_session_type(prommpt):
    valid_session_types = ['FP1', 'FP2', 'FP3', 'Q', 'R']
    while True:
        user_input = input(prommpt).upper()
        if user_input in valid_session_types:
            return user_input
        else:
            print("Invalid input. Please enter one of the following session types: FP1, FP2, FP3, Q, R")

def plot_driver_laptimes(session, driver_num):
    laps = session.laps.pick_driver(driver_num)
    laps['LapTime'].plot()
    plt.title(f"Lap Times for Driver {driver_num}")
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time")
    plt.show()

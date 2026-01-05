import fastf1
import pandas as pd
import fastf1.plotting
import matplotlib.pyplot as plt
import methods

def main():
    year = methods.get_valid_int_input("Enter the year of the season you wish to view")
    schedule = fastf1.get_event_schedule(year, include_testing=False)

    print(f"Races for the {year} season:")

    # Iterate through the schedule (which is a pandas DataFrame) and print the race name and round number
    for index, event in schedule.iterrows():
        # Check if the event is an actual race weekend (not a testing session) and has a race session
        if event['EventFormat'] != 'Testing' and event['EventName'] is not None:
            # Access the race name and round number
            race_name = event['EventName']
            round_num = event['RoundNumber']
            print(f"Round {round_num}: {race_name}")





    race = methods.get_valid_int_input("Enter the race you wish to view")
    session_type = methods.get_valid_session_type("Enter the session type you wish to view (FP1, FP2, FP3, Q, R)")
    session = fastf1.get_session(year, race, session_type)
    session.load()
    print(session.event['EventName'])
    print(session.event['EventDate'])
    print(session.event['OfficialEventName'])
    driver_num_int = methods.get_valid_int_input("Enter the driver number you wish to view: ")
    # Convert the integer input to a string, which get_driver() expects
    driver_num_str = str(driver_num_int) 

    try:
        # 2. Retrieve driver object using the input string
        # Use the converted string variable here:
        driver_info = session.get_driver(driver_num_str)
    
    # 3. Access details from the returned DriverResult object
        print(f"Driver: {driver_info['FullName']}")
        print(f"Team: {driver_info['TeamName']}")
        print(f"Status: {driver_info['Status']}")
    # 4. Show Data Visualization of Driver Laps
        laps = session.laps.pick_driver(driver_num_str)
        fastf1.plotting.setup_mpl()
        plt.figure(figsize=(10, 6))
        plt.title(f"{driver_info['FullName']} - {session.event['EventName']} {session_type} {year}")
        plt.xlabel("Lap Number")
        plt.ylabel("Lap Time (s)")
        plt.plot(laps['LapNumber'], laps['LapTime'].dt.total_seconds(), marker='o', linestyle='-')
        plt.grid()
        plt.show()
    except KeyError:
        # Print the original input for clarity in the error message
        print(f"Driver number {driver_num_int} not found in this session.")
if __name__ == "__main__":
    main()



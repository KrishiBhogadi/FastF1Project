import fastf1
import pandas as pd
import fastf1.plotting
import matplotlib.pyplot as plt
import methods

def main():
    year = methods.get_valid_int_input("Enter the year you wish to view: ", min_value=2018, max_value=2025)
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
    session.load(telemetry = True)
    print(session.event['EventName'])
    print(session.event['EventDate'])
    print(session.event['OfficialEventName'])
    top = input("Input a number to see the top n drivers by lap time, or press enter to skip: ")
    if top:
        print(session.results.head(int(top)))
    else:
        print(session.results)
    driver_num_int = methods.get_valid_int_input("Enter the driver number you wish to view: ")
    # Convert the integer input to a string, which get_driver() expects
    driver_num_str = str(driver_num_int) 

    try:
        # 2. Retrieve driver object using the input string
        # Use the converted string variable here:
        driver_info = session.get_driver(driver_num_str)
    
    # 3. Access details from the returned DriverResult object
        
    # 4. Show Data Visualization of Driver Laps
        
    except KeyError:
        # Print the original input for clarity in the error message
        print(f"Driver number {driver_num_int} not found in this session.")

    # 5.Get Driver Telemetry Per Lap
        # 1. Get telemetry for the specific lap and add distance data
    lap_number = methods.get_valid_int_input("Enter the lap number you wish to view telemetry for: ", min_value=1)
    lap = session.laps.pick_drivers(driver_num_str).pick_laps(lap_number)
    
    # Using add_distance() is recommended for visual track analysis
    telemetry = lap.get_car_data().add_distance()

    # 2. Create a multi-panel figure for all telemetry channels
    # Channels: Speed, Throttle, Brake, Gear, RPM
    fig, ax = plt.subplots(5, 1, figsize=(12, 15), sharex=True, gridspec_kw={'hspace': 0.3})
    fig.suptitle(f"Full Telemetry: {driver_info['FullName']} - Lap {lap_number}\n{session.event['EventName']} {year}", size=16)

    # Speed
    ax[0].plot(telemetry['Distance'], telemetry['Speed'], label='Speed', color='purple')
    ax[0].set_ylabel('Speed (km/h)')
    ax[0].grid(True, alpha=0.3)

    # Throttle (0-100%)
    ax[1].plot(telemetry['Distance'], telemetry['Throttle'], label='Throttle', color='green')
    ax[1].set_ylabel('Throttle (%)')
    ax[1].set_ylim(-5, 105)
    ax[1].grid(True, alpha=0.3)

    # Brake (0 or 100 / True or False)
    ax[2].plot(telemetry['Distance'], telemetry['Brake'], label='Brake', color='red')
    ax[2].set_ylabel('Brake (On/Off)')
    ax[2].grid(True, alpha=0.3)

    # Gear (1-8)
    ax[3].plot(telemetry['Distance'], telemetry['nGear'], label='Gear', color='yellow')
    ax[3].set_ylabel('Gear')
    ax[3].grid(True, alpha=0.3)

    # RPM
    ax[4].plot(telemetry['Distance'], telemetry['RPM'], label='RPM', color='cyan')
    ax[4].set_ylabel('RPM')
    ax[4].set_xlabel('Distance (m)')
    ax[4].grid(True, alpha=0.3)

    # Adjust layout and show
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


    
if __name__ == "__main__":
    main()



import pandas as pd
import matplotlib.pyplot as plt
import os

class TelemetryDataVisualisation:
    def __init__(self, telemetry_file):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), telemetry_file)
        self.telemetry_data = pd.read_csv(file_path)

    def plot_speed_profile(self, lap):
        lap_data = self.telemetry_data[self.telemetry_data['Lap'] == lap]
        plt.figure(figsize=(10, 6))
        plt.plot(lap_data['Distance'], lap_data['Speed'], label=f"Lap {lap}")
        plt.title("Speed Profile")
        plt.xlabel("Distance (m)")
        plt.ylabel("Speed (km/h)")
        plt.legend()
        plt.grid(True)
        plt.show()

    def compare_sector_times(self, laps):
        sector_data = self.telemetry_data.groupby(['Lap', 'Sector'])['SectorTime'].mean().unstack()
        sector_data = sector_data.loc[laps]

        sector_data.plot(kind='bar', figsize=(12, 6))
        plt.title("Sector Time Comparison")
        plt.xlabel("Lap")
        plt.ylabel("Sector Time (s)")
        plt.grid(True)
        plt.legend(title="Sector")
        plt.show()

if __name__ == "__main__":
    # Example telemetry data
    telemetry_file = "example_telemetry.csv"

    # Create the visualisation object
    visualisation = TelemetryDataVisualisation(telemetry_file)

    # Plot the speed profile for Lap 1
    visualisation.plot_speed_profile(lap=1)

    # Compare sector times for Laps 1 and 2
    visualisation.compare_sector_times(laps=[1, 2])
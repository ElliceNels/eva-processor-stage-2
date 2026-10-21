from file_IO import file_IO
from user_interface.user_input import UserInput
from data_processing.eva_data_processor import EVADataProcessor
from data_presentation.eva_plotter import EVAPlotter

class Orchestrator:

    def __init__(self):
        self.edp = self._initialize_eva_data()

    def orchestrate_program(self):
        fig, ax1, ax2 = EVAPlotter().create_dual_plot()
        EVAPlotter().cumulative_eva_duration(ax1, self.edp.get_dates(), self.edp.get_cumulative_hours())
        EVAPlotter().total_hours_by_country(ax2, self.edp.get_total_hours_by_country())
        EVAPlotter().render_figure(fig, "out/cumulative_duration.png")

        self.orchestrate_country_comparison()

    def orchestrate_country_comparison(self):
        print(f"Enter the first country to compare ({', '.join(self.edp.get_countries())}):")
        country_a = UserInput.receive_country()
        if country_a not in self.edp.get_countries():
            print(f"Country '{country_a}' not found in the data.")
            return
        print("Enter the second country to compare:")
        country_b = UserInput.receive_country()
        if country_b not in self.edp.get_countries():
            print(f"Country '{country_b}' not found in the data.")
            return
        
        print("Enter the start year for comparison:")
        start_year = UserInput.receive_year()
        print("Enter the end year for comparison:")
        end_year = UserInput.receive_year()

        print("Comparing countries...")
        
        try:
            a_results, b_results, winner = self.edp.compare_countries(
                country_a, country_b, start_year, end_year
            )
        except ValueError as error:
            print(f"Error: {error}")
            return
        print(f"Analysis results for {country_a} and {country_b} from {start_year} to {end_year}:")
        print(f"{country_a}: {a_results}")
        print(f"{country_b}: {b_results}")
        print(f"Winner: {winner}")


    def _initialize_eva_data(self):
        eva_data = file_IO.load_json_file(file_IO.read_cmd_filename())
        edp = EVADataProcessor(eva_data)
        return edp

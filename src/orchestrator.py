from file_IO import file_IO
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

    def _initialize_eva_data(self):
        eva_data = file_IO.load_json_file(file_IO.read_cmd_filename())
        edp = EVADataProcessor(eva_data)
        return edp

import matplotlib.pyplot as plt

class EVAPlotter:

    @staticmethod
    def cumulative_eva_duration(ax, dates, cumulative_hours):
        ax.plot(dates, cumulative_hours)
        ax.set_xlabel("Year")
        ax.set_ylabel("Cumulative EVA duration (hours)")
        ax.set_title("Cumulative EVA Duration")

    @staticmethod
    def total_hours_by_country(ax, total_hours_by_country):
        countries = list(total_hours_by_country.keys())
        hours = list(total_hours_by_country.values())
        colors = plt.cm.tab10(range(len(countries)))
        ax.bar(countries, hours, color=colors)
        ax.set_ylabel("Total hours")
        ax.set_title("Total Hours by Country")
        ax.tick_params(axis="x", rotation=45)

    @staticmethod
    def create_dual_plot():
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        return fig, ax1, ax2

    @staticmethod
    def render_figure(fig, filename=None):
        fig.tight_layout()
        if filename:
            fig.savefig(filename)
        plt.show()
# EVA Processor

A Python application for analysing extravehicular activity (EVA) data for CS6514 Software Architecture. It generates charts of cumulative EVA hours and hours by country and lets users compare EVA activity between two countries over a chosen year range.

## Requirements and setup

- Python **3.12 or later**
- Matplotlib **3.11.2 or later**

From the repository root, install the plotting dependency:

```powershell
python -m pip install "matplotlib>=3.11.2"
```

The repository includes `data/eva-data.json`. Create the output directory at the top level before running the application:

```powershell
New-Item -ItemType Directory -Force out
```

## Run the application

From the repository root:

```powershell
python src/main.py data/eva-data.json
```

The application:

1. Loads and processes the EVA JSON data.
2. Displays two charts: cumulative EVA duration and total EVA hours by country. It also saves a figure to `out/cumulative_duration.png`.
3. Prompts for two country names and a start and end year.
4. Prints each country's EVA count, total hours, and average hours, followed by the country with the greater total duration (or `Tie`).

Enter country names as offered by the prompt (for example, `usa` and `russia`). The selected year range is **inclusive**. A country with no EVAs in the range has count and total of zero and an unavailable average (`None` in the current output).

> **Note:** The chart window opens before the country-comparison prompts. Close the plot window to continue if necessary. Run the command from the repository root so the relative data and output paths resolve correctly.

## Module structure

```text
src/
├── main.py
├── orchestrator.py
├── file_IO/
│   └── file_IO.py
├── data_processing/
│   └── eva_data_processor.py
├── data_presentation/
│   └── eva_plotter.py
└── user_interface/
    └── user_input.py

tests/
└── test_eva_processor.py
```

| Module | Responsibility |
| --- | --- |
| `main.py` | Starts the application. |
| `orchestrator.py` | Coordinates loading, processing, plotting, user input, and comparison output. |
| `file_IO/file_IO.py` | Reads the input filename and loads JSON data. |
| `data_processing/eva_data_processor.py` | Parses EVA records; calculates cumulative and country totals; filters and compares countries over a year range. |
| `data_presentation/eva_plotter.py` | Creates, displays, and saves the charts. |
| `user_interface/user_input.py` | Reads and cleans country/year inputs; validates years. |

`main.py` starts the orchestrator. The orchestrator uses the other modules; calculations live in the data processor.

## Run the automated tests

The tests use **plain Python `assert` statements**. From the repository root:

```powershell
python tests/test_eva_processor.py
```

On success, the script prints `All 5 tests passed!`. The five tests cover:

- total-hours and cumulative-hours calculations
- Country-comparison results
- Invalid year range
- No matching EVAs within a period
- Unknown country

The tests use small, known sample records.

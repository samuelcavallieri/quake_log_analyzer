# Quake Log Analyzer

This Python project analyzes Quake 3 Arena game log files, generating reports on matches and player statistics.

## Project Structure


*   **`src/`**: Contains the main source code.
    *   **`quake_log_parser.py`**: Functions to process the log file and extract relevant information.
    *   **`report_generator.py`**: Main script that utilizes the functions from `quake_log_parser.py` to generate the reports.
*   **`tests/`**: Contains unit tests to ensure the code's correctness.
*   **`games.log`**: Quake 3 Arena log file to be analyzed. Place this file in the project's root directory.
*   **`README.md`**: This file, containing information about the project.

## How to Run

**1. Prerequisites**

*   **Python 3.x**: Make sure you have Python 3 installed on your machine.

**2. Normal Execution**

*   Navigate to the `src` directory in your terminal:

    ```bash
    cd /path/to/quake_log_analyzer/src
    ```

*   Execute the `report_generator.py` script:

    ```bash
    python3 report_generator.py
    ```

    The reports will be displayed in your terminal.

**3. Execution via Docker Container**

*   **Build the Docker image:**

    ```bash
    docker build -t quake-log-analyzer .
    ```

*   **Run the container:**

    ```bash
    docker run quake-log-analyzer
    ```

    The reports will be displayed in your terminal.

## Running the Tests

*   Navigate to the `tests` directory in your terminal:

    ```bash
    cd /path/to/quake_log_analyzer/tests
    ```

*   Execute the test script:

    ```bash
    python3 test_quake_log_parser.py
    ```

   The test results will be displayed in your terminal, indicating if the tests passed or failed.

## Continuous Integration (CI) with GitHub Actions

This project includes a GitHub Actions workflow to automate the testing process. Whenever you push changes to the `main` branch or create a pull request, the following steps will be executed:

1.  **Checkout code:** The latest code from your repository is checked out.
2.  **Set up Python:** The appropriate Python environment is set up.
3.  **Run tests:** The unit tests are executed.

You can view the details of the workflow and its execution status in the "Actions" tab of your GitHub repository.

## Code Explanation

*   **`quake_log_parser.py`**
    *   `parse_log_file(log_file_path)`: Reads the log file, extracts information about each match (total kills, players, kills per player, and optionally kills by means of death), and organizes them into a dictionary.
    *   `generate_player_ranking(games)`: Calculates the player ranking based on the total number of kills across all matches.

*   **`report_generator.py`**
    *   Imports the functions from `quake_log_parser.py`.
    *   Constructs the full path to the `games.log` file.
    *   Uses `parse_log_file` to get the match data.
    *   Uses `generate_player_ranking` to get the player ranking.
    *   Prints the match reports and player ranking to the terminal.

*   **`test_quake_log_parser.py`**
    *   Contains unit tests for the functions in `quake_log_parser.py`, ensuring their correct functionality.

## Notes

*   Make sure the `games.log` file is in the project's root directory.
*   The `test_games.log` file, used for testing, should be located in the `tests` directory.
*   Adapt the paths in the scripts if your project structure is different.
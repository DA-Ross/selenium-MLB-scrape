# MLB Batter vs. Pitcher Stats Scraper

## Overview

This Python script scrapes MLB batter vs. pitcher statistics from "https://swishanalytics.com/optimus/mlb/batter-vs-pitcher-stats" using Selenium. The data includes performance metrics such as hits, at-bats, and batting averages for each batter-pitcher matchup. The script dynamically fetches data for the current date and saves it to a JSON file.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.x**
- **Selenium library**
- **ChromeDriver**

## Installation

1. **Clone this repository** or download the script file.

2. **Install Selenium**:

   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:

   - Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).
   - Download the version compatible with your Chrome browser.
   - Place the `chromedriver` executable in a directory included in your system's `PATH`, or adjust the script to specify its path.

## Usage

1. **Run the script**:

   Save the script to a file, for example, `scrape_mlb_stats.py`. Then, execute the script using Python:

   ```bash
   python scrape_mlb_stats.py
   ```

2. **Check the output**:

   After running the script, a `data.json` file will be created in the same directory. This file contains the scraped data in JSON format.

## Script Details

- **Imports**:
  - `json`: For saving data in JSON format.
  - `selenium.webdriver`: For web scraping using Selenium.
  - `datetime.date`: To get the current date for the URL.
  - `time`: For adding delays (though this could be replaced with dynamic waits).

- **Main Functionality**:
  - Opens the specified URL using ChromeDriver.
  - Waits for the page to load (currently using a fixed sleep duration).
  - Iterates through each row of the table and extracts data for each batter vs. pitcher matchup.
  - Includes an ID for each entry for tracking.
  - Saves the extracted data to a JSON file.

## Notes

- **Dynamic Date Handling**: The URL is dynamically generated based on the current date. Adjust the URL format if needed for different date ranges or data sources.
- **Error Handling**: Basic error handling is included to manage exceptions during data extraction.
- **Page Loading**: The script uses a fixed sleep duration to wait for page loading. Consider using dynamic waits with `WebDriverWait` for improved robustness.

## Troubleshooting

- **ChromeDriver Issues**: Ensure that the version of ChromeDriver matches your Chrome browser version.
- **Page Load Time**: If you encounter issues with page load times, increase the `time.sleep` duration or switch to `WebDriverWait` for more reliable waiting.

## License

This script is provided as-is. Feel free to modify and use it according to your needs.

---

Feel free to adjust any specifics or add additional instructions based on your setup or requirements.

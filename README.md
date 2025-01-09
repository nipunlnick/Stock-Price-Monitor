# Stock Price Monitor and Email Alerts

## Project Overview

This project scrapes Apple Inc.'s stock price from Yahoo Finance, compares it with previously stored prices, and sends email alerts if the price exceeds predefined thresholds. Additionally, the project is scheduled to run periodically (e.g., every hour) to keep track of stock price changes.

## Features

- **Web Scraping**: Scrapes real-time stock price information from Yahoo Finance.
- **Data Reconciliation**: Compares scraped stock prices with previous values stored in a CSV file.
- **Email Alerts**: Sends email notifications if the stock price changes significantly.
- **Task Scheduling**: Automates the execution of the script at regular intervals using Task Scheduler or cron jobs.

## Tech Stack

- Python
- `requests` library for HTTP requests
- `beautifulsoup4` for web scraping
- `pandas` for data processing and comparison
- `smtplib` for sending email alerts
- `dotenv` for managing environment variables

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nipunlnick/Stock-Price-Monitor.git
   cd Stock-Price-Monitor
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project directory with the following content:

   ```bash
   SENDER_EMAIL=your_email@gmail.com
   RECIPIENT_EMAIL=recipient_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

   > **Note**: Ensure that the app password for your Gmail account is created and securely stored. Avoid hardcoding sensitive credentials in the code.

## Usage

### 1. Web Scraping & Email Alerts

- Run the script to scrape Apple Inc.'s stock price, compare it with previously stored prices, and send email alerts if the price changes exceed a threshold:

  ```bash
  python scrape_stock_price.py
  ```

### 2. Scheduling the Script

- For Windows users:
  You can set up Task Scheduler to run the script periodically.

  **Steps**:

  1.  Open Task Scheduler and create a new task.
  2.  In the "Actions" tab, set the program to `python.exe` and the argument as the path to your `Stock-Price-Monitor/main.py` script.
  3.  Set the schedule (e.g., every hour) and start the task.

  Screenshot of Task Scheduler setup (add your screenshot).

- For Linux/macOS users:
  Use cron jobs to run the script periodically.

  **Steps**:

  1.  Open your terminal and edit the crontab:

      ```bash
      crontab -e
      ```

  2.  Add the following line to run the script every hour:

      ```bash
      0 * * * * /path/to/python /path/to/your/project/Stock-Price-Monitor/main.py
      ```

  > **Note**: Replace `/path/to/python.exe` with the actual path to your Python interpreter and `/path/to/your/project/` with the path to your project directory.

## Files in the Repository

- **`scrape_stock_price.py`**: Main script for scraping stock prices.
- **`cal_change.py`**: reconciling data
- **`semail_alert.py`**: sending email alerts.
- **`stock_data.csv`**: CSV file containing previous stock price data.
- **`.env`**: Environment variables (should not be uploaded to GitHub).
- **`requirements.txt`**: Contains all the Python libraries required for the project.
- **`README.md`**: Project documentation (this file).

## Contact

For any questions or suggestions, feel free to reach out:

- Email: [pvnipunlakshitha@gmail.com](mailto:pvnipunlakshitha@gmail.com)

---

### Additional Notes

- Ensure that **`.env`** file is not pushed to your GitHub repository for security reasons.

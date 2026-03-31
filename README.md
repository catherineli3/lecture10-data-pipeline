# Orders Data Processing and Dashboard

A complete data processing pipeline with Flask dashboard for visualizing order data.

## Features

- Data cleaning and deduplication
- Currency conversion to CNY (USD=6.9, EUR=7.5, CNY=1.0, JPY=0.05)
- Automatic data merging of orders and customers
- SQLite database storage
- Summary statistics by region
- Real-time web dashboard with auto-refresh
- Automated GitHub Actions workflow

## Project Structure

```
.
├── data/
│   ├── orders.csv          # Order data
│   ├── customers.csv       # Customer data
│   └── orders.db           # SQLite database (generated)
├── templates/
│   └── index.html          # Web dashboard template
├── .github/
│   └── workflows/
│       └── data-pipeline.yml  # GitHub Actions workflow
├── clean_and_merge.py      # Data processing script
├── app.py                  # Flask application
└── requirements.txt        # Python dependencies
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Process data and create database:
```bash
python clean_and_merge.py
```

3. Run Flask application:
```bash
python app.py
```

4. Open browser to: http://localhost:5000

## Data Processing Pipeline

The `clean_and_merge.py` script performs the following:

1. Reads `orders.csv` and `customers.csv`
2. Removes duplicate orders (based on order_id)
3. Converts all amounts to CNY using conversion rates
4. Merges orders with customer information
5. Saves merged data to SQLite database
6. Creates summary table with average amount by region

## GitHub Actions

The workflow automatically triggers when any file in the `data/` folder is pushed:

- Runs `clean_and_merge.py` to process data
- Updates the SQLite database
- Commits changes back to repository

## API Endpoints

- `/` - Main dashboard page
- `/api/orders` - JSON orders data
- `/api/summary` - JSON summary by region

## Dashboard Features

- **Orders Table**: Displays all merged order records with customer information
- **Summary Table**: Shows average amount_cny by region
- **Auto-refresh**: Updates every 10 seconds when database changes
- **Responsive Design**: Works on desktop and mobile devices

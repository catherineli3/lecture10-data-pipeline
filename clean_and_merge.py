#!/usr/bin/env python3
"""
clean_and_merge.py
Reads order and customer data, cleans duplicates, converts amounts to CNY,
merges the data, and stores in SQLite database.
"""

import pandas as pd
import sqlite3
from pathlib import Path


# Currency conversion rates to CNY
CONVERSION_RATES = {
    'USD': 6.9,
    'EUR': 7.5,
    'CNY': 1.0,
    'JPY': 0.05
}


def read_data():
    """Read order and customer CSV files."""
    data_dir = Path(__file__).parent / 'data'
    
    # Read customer data
    customers_df = pd.read_csv(data_dir / 'customers.csv')
    
    # Read all order CSV files and concatenate them
    order_files = list(data_dir.glob('orders*.csv'))
    orders_dfs = []
    
    for order_file in order_files:
        print(f"Reading {order_file.name}...")
        df = pd.read_csv(order_file)
        orders_dfs.append(df)
    
    orders_df = pd.concat(orders_dfs, ignore_index=True)
    
    print(f"Loaded {len(orders_df)} orders from {len(order_files)} file(s) and {len(customers_df)} customers")
    return orders_df, customers_df


def clean_duplicates(orders_df):
    """Remove duplicate orders based on order_id."""
    before_count = len(orders_df)
    orders_df = orders_df.drop_duplicates(subset=['order_id'], keep='first')
    after_count = len(orders_df)
    
    duplicates_removed = before_count - after_count
    if duplicates_removed > 0:
        print(f"Removed {duplicates_removed} duplicate orders")
    else:
        print("No duplicates found")
    
    return orders_df


def convert_to_cny(orders_df):
    """Convert all amounts to CNY and store in new column."""
    def convert_amount(row):
        currency = row['amount_currency']
        rate = CONVERSION_RATES.get(currency, 1.0)
        return row['amount'] * rate
    
    orders_df['amount_cny'] = orders_df.apply(convert_amount, axis=1)
    print("Converted all amounts to CNY")
    return orders_df


def merge_data(orders_df, customers_df):
    """Merge orders and customers on customer_id."""
    merged_df = orders_df.merge(customers_df, on='customer_id', how='left')
    print(f"Merged data has {len(merged_df)} records")
    return merged_df


def create_summary_table(merged_df):
    """Create summary table with average amount_cny by region."""
    summary_df = merged_df.groupby('region')['amount_cny'].mean().reset_index()
    summary_df.columns = ['region', 'avg_amount_cny']
    summary_df['avg_amount_cny'] = summary_df['avg_amount_cny'].round(2)
    print(f"Created summary table with {len(summary_df)} regions")
    return summary_df


def save_to_database(merged_df, summary_df, db_path='data/orders.db'):
    """Save merged data and summary to SQLite database."""
    # Ensure data directory exists
    db_path = Path(__file__).parent / db_path
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(str(db_path))
    
    try:
        # Save merged orders
        merged_df.to_sql('orders', conn, if_exists='replace', index=False)
        print(f"Saved {len(merged_df)} orders to database")
        
        # Save summary table
        summary_df.to_sql('region_summary', conn, if_exists='replace', index=False)
        print(f"Saved summary table with {len(summary_df)} regions to database")
        
    finally:
        conn.close()
    
    print(f"Database saved to {db_path}")


def main():
    """Main processing pipeline."""
    print("=" * 50)
    print("Starting data cleaning and merge process...")
    print("=" * 50)
    
    # Read data
    orders_df, customers_df = read_data()
    
    # Clean duplicates
    orders_df = clean_duplicates(orders_df)
    
    # Convert to CNY
    orders_df = convert_to_cny(orders_df)
    
    # Merge data
    merged_df = merge_data(orders_df, customers_df)
    
    # Create summary
    summary_df = create_summary_table(merged_df)
    
    # Save to database
    save_to_database(merged_df, summary_df)
    
    print("=" * 50)
    print("Process completed successfully!")
    print("=" * 50)
    
    # Display sample data
    print("\nSample of merged data:")
    print(merged_df.head())
    print("\nSummary table:")
    print(summary_df)


if __name__ == '__main__':
    main()

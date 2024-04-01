import csv
from datetime import datetime

def convert_to_cointracker_format(input_file, output_file):
    with open(input_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

    with open(output_file, 'w', newline='') as file:
        fieldnames = ['Date', 'Received Quantity', 'Received Currency', 'Sent Quantity', 'Sent Currency', 'Fee Amount', 'Fee Currency', 'Tag']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in data:
            transaction_type = row['Type']
            if transaction_type == 'Withdrawal':
                csv_writer.writerow({
                    'Date': format_date(row['Date']),
                    'Received Quantity': '',
                    'Received Currency': '',
                    'Sent Quantity': row['SellAmount'],
                    'Sent Currency': row['SellCurrency'],
                    'Fee Amount': row.get('FeeAmount', ''),
                    'Fee Currency': row.get('FeeCurrency', ''),
                    'Tag': ''
                })
            elif transaction_type == 'Deposit':
                csv_writer.writerow({
                    'Date': format_date(row['Date']),
                    'Received Quantity': row['BuyAmount'],
                    'Received Currency': row['BuyCurrency'],
                    'Sent Quantity': '',
                    'Sent Currency': '',
                    'Fee Amount': '',
                    'Fee Currency': '',
                    'Tag': ''
                })
            elif transaction_type in ['Trade', 'Spend']:
                csv_writer.writerow({
                    'Date': format_date(row['Date']),
                    'Received Quantity': row['BuyAmount'],
                    'Received Currency': row['BuyCurrency'],
                    'Sent Quantity': row['SellAmount'],
                    'Sent Currency': row['SellCurrency'],
                    'Fee Amount': row['FeeAmount'],
                    'Fee Currency': row['FeeCurrency'],
                    'Tag': ''
                })
            elif transaction_type in ['Income', 'Mining', 'Airdrop', 'Staking', 'Reward']:
                csv_writer.writerow({
                    'Date': format_date(row['Date']),
                    'Received Quantity': row['BuyAmount'],
                    'Received Currency': row['BuyCurrency'],
                    'Sent Quantity': '',
                    'Sent Currency': '',
                    'Fee Amount': '',
                    'Fee Currency': '',
                    'Tag': transaction_type.lower()
                })
             # elif transaction_type in ['Migration', 'Lost', 'Borrow', 'Repay'] : i have no idea what to do in these cases...
             # it looks like maybe cointracker has borrow, repay, migration, lost types but csv import doesn't support them.
            else:
                print(f"Unexpected transaction type: {transaction_type}")
                print(f"Row: {row}")
                print()

def format_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %H:%M:%S')

# Usage example
input_file = 'input.csv'
output_file = 'output.csv'
convert_to_cointracker_format(input_file, output_file)
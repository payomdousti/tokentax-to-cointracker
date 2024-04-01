# TokenTax to CoinTracker CSV Converter
This script is a converter that transforms CSV data exported from TokenTax into the format compatible with CoinTracker's CSV import. It helps users migrate their transaction data from TokenTax to CoinTracker.

## Features
- Converts transaction data from TokenTax CSV format to CoinTracker CSV format
- Supports various transaction types, including Withdrawal, Deposit, Trade, Spend, Income, Mining, Airdrop, Staking, and Reward
- Automatically formats the date to the required format for CoinTracker
- Prints out any unexpected transaction types encountered during the conversion process

## Usage
1. Export your transaction data from TokenTax in CSV format.
2. Place the exported CSV file in the same directory as the script and name it input.csv.
3. Run the script using the following command:
`python convert_csv.py`
4. The script will process the input CSV file and generate an output file named output.csv in the same directory.
5. Import the output.csv file into CoinTracker using their CSV import feature.

## Supported Transaction Types
The script supports the following transaction types:

- Withdrawal
- Deposit
- Trade
- Spend
- Income
- Staking
- Bridge
- Lost
- Borrow

## Missing Transaction Type Support From Cointracker CSV Import
Cointracker CSV Import guidelines currently do not handle the following transaction types:

- Loan repayment

These transaction types are recognized by CoinTracker but are not supported by their CSV import feature. If you encounter any of these transaction types in your TokenTax data, the script will print out the unexpected transaction type and the corresponding row for manual handling.

### Note
Please review the generated output.csv file for any unexpected transaction types or missing data. If you encounter any issues or have transactions that are not supported by the script, you may need to manually adjust the data or import those transactions separately into CoinTracker.

### Requirements
- Python 3.x
- csv module (built-in)
- datetime module (built-in)

### License
This script is released under the MIT License.

Feel free to modify and adapt the script to suit your specific needs. If you have any questions or encounter any issues, please don't hesitate to reach out for assistance.

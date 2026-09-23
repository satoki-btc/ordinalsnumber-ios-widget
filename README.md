# Bitcoin Ordinals iOS Widget

A lightweight iOS widget for Bitcoin enthusiasts, providing a quick overview of the current Bitcoin network along with the latest Ordinals and Runes numbers.

The widget combines data from Mempool.space and Ordiscan and presents the information in a compact, easy-to-read format.

## Features

- Current Bitcoin block height
- Recommended Bitcoin transaction fees
- Low, medium, and high fee rates
- Number of unconfirmed transactions
- Latest Ordinals inscription number
- Latest Runes number
- Current time of the last update
- Compact widget layout

## Data Sources

### Mempool.space

Used for Bitcoin network information:

- Block height
- Recommended transaction fees
- Mempool statistics
- Unconfirmed transactions

### Ordiscan

Used for Ordinals and Runes information:

- Latest inscription number
- Latest Runes number

## Configuration

An Ordiscan API token is required to retrieve Ordinals and Runes data.

Set your token in Inscriptions.py:

    api_token = "YOUR_ORDISCAN_API_TOKEN"

Keep your API token private and do not commit it to a public repository.

## Widget

The widget is called "Bitcoin Ordinals" and displays the latest information in a compact format:

    Bitcoin Ordinals

    Block: 000,000
    Ordinals: 000,000,000
    Runes: 000,000

    L:00 M:00 H:00
    Unconfirmed Txs: 000

    Last Update: 00:00:00

## Repository

https://github.com/satoki-btc/ordinalsnumber-ios-widget/

## Author

satoki.btc

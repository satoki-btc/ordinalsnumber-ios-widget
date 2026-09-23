#!/usr/bin/env python3
##############################################################
####      Inscriptions.py                                 ####
####      Author      : satoki.btc                        ####
####      Date        : 22/02/2023                        ####
####      Description : iOS widget retrieving latest      ####
####                    Bitcoin fees, latest block number,####
####                    unconfirmed transactions,         ####
####                    inscription number and runes      ####
##############################################################
####      Changes     : 23/09/2026 Added Ordiscan API to  ####
####                    retrieve latest inscription and   ####
####                    rune numbers                      ####
##############################################################
import requests
import widgets as wd
from datetime import datetime

def get_json(url, headers=None):
    response = requests.get(url, headers=headers) if headers else requests.get(url)
    return response.json()

def add_row(layout, item): layout.add_row([item])

def add_spacer(layout): layout.add_vertical_spacer()

widget_name = "Bitcoin Ordinals"
mempool_api = "https://mempool.space/api/"
ordiscan_api = "https://api.ordiscan.com/v1/"

# Insert your Ordiscan API token here
api_token = ""

headers = {
    "Authorization": "Bearer {}".format(api_token)
}

block_height = get_json(
    mempool_api + "blocks/tip/height"
)
fees = get_json(mempool_api + "fees/recommended")
mempool = get_json(mempool_api + "mempool")

inscription_number = get_json(
    ordiscan_api + "inscriptions", headers
)["data"][0]["inscription_number"]

rune_number = get_json(
    ordiscan_api + "runes", headers
)["data"][0]["number"]

block_height = "{:,}".format(block_height)
low_fee = "{:,}".format(fees["hourFee"])
medium_fee = "{:,}".format(fees["halfHourFee"])
high_fee = "{:,}".format(fees["fastestFee"])
unconfirmed_transactions = "{:,}".format(mempool["count"])

inscription_number = "{:,}".format(inscription_number)
rune_number = "{:,}".format(rune_number)

widget = wd.Widget()
layout = widget.small_layout

title = wd.Text(widget_name)
block_text = wd.Text("Block: " + block_height)
transactions_text = wd.Text(
    "Unconfirmed Txs: " + unconfirmed_transactions
)
inscriptions_text = wd.Text(
    "Ordinals: " + inscription_number
)
runes_text = wd.Text(
    "Runes: " + rune_number
)
fees_text = wd.Text(
    f"L:{low_fee} M:{medium_fee} H:{high_fee}"
)
last_update_text = wd.Text(
    "Last Update: " + datetime.now().strftime("%H:%M:%S")
)
transactions_text.font = wd.Font.system_font_of_size(11)
fees_text.font = wd.Font.system_font_of_size(11)

add_spacer(layout)

add_row(layout, title)
add_spacer(layout)

add_row(layout, block_text)
add_row(layout, inscriptions_text)
add_row(layout, runes_text)
add_spacer(layout)

add_row(layout, fees_text)
add_row(layout, transactions_text)
add_spacer(layout)

add_row(layout, last_update_text)
add_spacer(layout)

wd.save_widget(widget, widget_name)

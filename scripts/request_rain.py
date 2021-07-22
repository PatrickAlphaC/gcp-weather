from brownie import Weather
from scripts.helpful_scripts import fund_with_link, get_contract, get_account
import time


def main():
    account = get_account()
    weather = Weather[-1]
    fund_tx = fund_with_link(weather)
    fund_tx.wait(1)
    tx = weather.requestTotalRain("2021-04-01", "2021-05-01", {"from": account})
    tx.wait(1)
    time.sleep(60)
    print(f"Current hail is {weather.totalRain()}")

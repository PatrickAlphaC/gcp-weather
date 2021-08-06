from scripts.helpful_scripts import get_account, get_contract, fund_with_link
from brownie import Weather, network, config
from brownie.convert.datatypes import HexString
from brownie.convert import to_bytes
import time
from web3 import Web3


def main():
    account = get_account()
    weather = Weather.deploy(
        get_contract("link_token").address,
        get_contract("oracle").address,
        Web3.toHex(text=config["networks"][network.show_active()]["av_temp_job"]),
        Web3.toHex(
            text=config["networks"][network.show_active()]["total_rain_job"],
        ),
        Web3.toHex(
            text=config["networks"][network.show_active()]["hail_job"],
        ),
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=True,
    )
    fund_tx = fund_with_link(weather)
    fund_tx.wait(1)
    tx = weather.requestTotalRain("2021-04-01", "2021-05-01", {"from": account})
    tx.wait(1)
    time.sleep(60)
    print(f"Current rain is {weather.totalRain()}")

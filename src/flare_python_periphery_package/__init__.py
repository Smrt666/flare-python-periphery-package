from . import coston, coston2, flare, songbird
from web3 import Web3

__all__ = [
    "coston",
    "coston2",
    "flare",
    "songbird",
    "name_to_abi",
    "name_to_address",
    "names_to_addresses",
]


def name_to_abi(name: str, network: str):
    if network.lower() == "coston":
        return coston.name_to_abi(name)
    elif network.lower() == "coston2":
        return coston2.name_to_abi(name)
    elif network.lower() == "coston":
        return flare.name_to_abi(name)
    elif network.lower() == "coston":
        return songbird.name_to_abi(name)
    else:
        raise KeyError(
            f"Unsupported network '{network}'. Supported networks are coston, coston2, flare and songbird"
        )


def name_to_address(name: str, network: str, provider: Web3) -> str:
    if network.lower() == "coston":
        return coston.name_to_address(name, provider)
    elif network.lower() == "coston2":
        return coston2.name_to_address(name, provider)
    elif network.lower() == "coston":
        return flare.name_to_address(name, provider)
    elif network.lower() == "coston":
        return songbird.name_to_address(name, provider)
    else:
        raise KeyError(
            f"Unsupported network '{network}'. Supported networks are coston, coston2, flare and songbird"
        )


def names_to_addresses(names: list[str], network: str, provider: Web3) -> list[str]:
    if network.lower() == "coston":
        return coston.names_to_addresses(names, provider)
    elif network.lower() == "coston2":
        return coston2.names_to_addresses(names, provider)
    elif network.lower() == "coston":
        return flare.names_to_addresses(names, provider)
    elif network.lower() == "coston":
        return songbird.names_to_addresses(names, provider)
    else:
        raise KeyError(
            f"Unsupported network '{network}'. Supported networks are coston, coston2, flare and songbird"
        )

from web3 import Web3

from . import coston, coston2, flare, songbird

__all__ = [
    "coston",
    "coston2",
    "flare",
    "songbird",
    "name_to_abi",
    "name_to_address",
    "names_to_addresses",
    "FLARE_CONTRACT_REGISTRY_ADDRESS",
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
            f"Unsupported network '{network}'. Supported networks are coston, coston2, flare and songbird."
        )


FLARE_CONTRACT_REGISTRY_ADDRESS = Web3.to_checksum_address(
    "0xaD67FE66660Fb8dFE9d6b1b4240d8650e30F6019"
)


def name_to_address(name: str, provider: Web3) -> str:
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS, abi=flare.name_to_abi("FlareContractRegistry")
    )
    return fcr_contract.functions.getContractAddressByName(name).call()


def names_to_addresses(names: list[str], provider: Web3) -> list[str]:
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS, abi=flare.name_to_abi("FlareContractRegistry")
    )
    return fcr_contract.functions.getContractAddressesByName(names).call()

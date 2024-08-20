from web3 import AsyncWeb3, Web3
from eth_typing.evm import ChecksumAddress

from . import coston, coston2, flare, songbird
from .constants import FLARE_CONTRACT_REGISTRY_ADDRESS

__all__ = [
    "coston",
    "coston2",
    "flare",
    "songbird",
    "interface_to_abi",
    "name_to_abi",
    "name_to_address",
    "async_name_to_address",
    "names_to_addresses",
    "async_names_to_addresses",
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


def name_to_address(name: str, provider: Web3) -> ChecksumAddress:
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return Web3.to_checksum_address(fcr_contract.functions.getContractAddressByName(name).call())


def names_to_addresses(names: "list[str]", provider: Web3) -> "list[ChecksumAddress]":
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    addresses = fcr_contract.functions.getContractAddressesByName(names).call()
    return list(map(Web3.to_checksum_address, addresses))


async def async_name_to_address(name: str, provider: AsyncWeb3) -> ChecksumAddress:
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    address = await fcr_contract.functions.getContractAddressByName(name).call()
    return Web3.to_checksum_address(address)


async def async_names_to_addresses(
    names: "list[str]", provider: AsyncWeb3
) -> "list[str]":
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    addresses = await fcr_contract.functions.getContractAddressesByName(names).call()
    return list(map(Web3.to_checksum_address, addresses))


def interface_to_abi(interface_name: str, network: str):
    if network.lower() == "coston":
        return coston.interface_to_abi(interface_name)
    elif network.lower() == "coston2":
        return coston2.interface_to_abi(interface_name)
    elif network.lower() == "coston":
        return flare.interface_to_abi(interface_name)
    elif network.lower() == "coston":
        return songbird.interface_to_abi(interface_name)
    else:
        raise KeyError(
            f"Unsupported network '{network}'. Supported networks are coston, coston2, flare and songbird."
        )

from web3 import AsyncWeb3, Web3

from . import coston, coston2, flare, songbird
from .constants import FLARE_CONTRACT_REGISTRY_ADDRESS

__all__ = [
    "coston",
    "coston2",
    "flare",
    "songbird",
    "interface_to_abi",
    "interface_to_address",
    "interfaces_to_addresses",
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


def name_to_address(name: str, provider: Web3) -> str:
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return fcr_contract.functions.getContractAddressByName(name).call()


def names_to_addresses(names: "list[str]", provider: Web3) -> "list[str]":
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return fcr_contract.functions.getContractAddressesByName(names).call()


async def async_name_to_address(name: str, provider: AsyncWeb3) -> str:
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return await fcr_contract.functions.getContractAddressByName(name).call()


async def async_names_to_addresses(
    names: "list[str]", provider: AsyncWeb3
) -> "list[str]":
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return await fcr_contract.functions.getContractAddressesByName(names).call()


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


def interface_to_address(interface_name: str, provider: Web3) -> str:
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return fcr_contract.functions.getContractAddressByName(interface_name).call()


def interfaces_to_addresses(
    interface_names: "list[str]", provider: Web3
) -> "list[str]":
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return fcr_contract.functions.getContractAddressesByName(interface_names).call()


async def async_interface_to_address(interface_name: str, provider: AsyncWeb3) -> str:
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return await fcr_contract.functions.getContractAddressByName(interface_name).call()


async def async_interfaces_to_addresses(
    interface_names: "list[str]", provider: AsyncWeb3
) -> "list[str]":
    fcr_contract = provider.eth.contract(
        FLARE_CONTRACT_REGISTRY_ADDRESS,
        abi=flare.interface_abis.IFlareContractRegistry,
    )
    return await fcr_contract.functions.getContractAddressesByName(
        interface_names
    ).call()

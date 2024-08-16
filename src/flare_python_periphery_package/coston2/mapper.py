from .abis import _ABIGetter
from web3 import Web3

flare_contract_registry_address = "0xaD67FE66660Fb8dFE9d6b1b4240d8650e30F6019"


def name_to_address(name: str, provider: Web3) -> str: ...  # TODO
def names_to_addresses(names: list[str], provider: Web3) -> list[str]: ...  # TODO


def name_to_abi(name: str):
    try:
        return _ABIGetter.name_to_getter[name].__get__()
    except Exception as e:
        raise KeyError(f"No official Flare Network contract with name: '{name}'") from e

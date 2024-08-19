from .abis import _Contract, _InterfaceABIGetter, interface_abis, products

__all__ = ["products", "interface_abis", "name_to_abi", "interface_to_abi"]


def interface_to_abi(name: str):
    try:
        return _InterfaceABIGetter.name_to_getter[name].__get__()
    except Exception as e:
        raise KeyError(
            f"No official Flare Network interface with name: '{name}'"
        ) from e


def name_to_abi(name: str):
    try:
        interface_name = _Contract.name_to_getter[name].interface
    except Exception as e:
        raise KeyError(f"No official Flare Network contract with name: '{name}'") from e
    return interface_to_abi(interface_name)

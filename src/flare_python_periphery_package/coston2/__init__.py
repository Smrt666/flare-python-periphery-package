from .abis import _ABIGetter, abis

__all__ = ["abis", "name_to_abi"]


def name_to_abi(name: str):
    try:
        return _ABIGetter.name_to_getter[name].__get__()
    except Exception as e:
        raise KeyError(f"No official Flare Network contract with name: '{name}'") from e

# flare-python-periphery-package
TODO:
* update pyproject.toml
* update readme

Instalation from: TestPyPI
```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ flare-python-periphery-package --extra-index-url https://pypi.org/simple poirot
```

Need account on TestPyPI/PyPI, API token (https://test.pypi.org/manage/account/#api-tokens)
deploy (replace testpypi with pypi):
```bash
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
python3 -m build
python3 -m twine upload --repository testpypi dist/*
```

## Features
This library exposes 11 names at top level:
 * `name_to_abi(name:str, network: str)` and `interface_to_abi(interface_name: str, network: str)` - 
 return abi as a python object (a list of dicts).
    Name is the name of contract/interface, network can be one of coston, coston2, songbird and flare. 
 * `name_to_address(name: str, provider: Web3) -> ChecksumAddress`, `names_to_addresses(names: "list[str]", provider: Web3) -> "list[ChecksumAddress]"`,
  `async_name_to_address(name: str, provider: AsyncWeb3) -> ChecksumAddress` and 
  `async_names_to_addresses(names: "list[str]", provider: AsyncWeb3) -> "list[ChecksumAddress]"` - 
  use provider to get contract address(es). They all read from FlareContractRegistryLibrary on chain.
 * `FLARE_CONTRACT_REGISTRY_ADDRESS` - hardcoded `ChecksumAddress` constant, the same for all chains and should never change.
 * `coston`, `coston2`, `flare` and `songbird` - namespaces with 4 exports:
    - `products` - a class exposing contracts through `.ContractName` syntax. They have fields
    `name`, `interface` - interface's name, property `abi` and methods `get_address(self, provider: Web3) -> ChecksumAddres` and `async_get_address(self, provider: AsyncWeb3) -> ChecksumAddres`.
    - `interface_abis` - a class allowing access to abis using `.InterfaceName` syntax. Interface names are
    usually contract names prefixed with capital letter `I`.
    - `name_to_abi(name: str)` and `interface_to_abi(name: str)` - the same as top level functions, with omitted network argument

Example:
```py
import asyncio

import flare_python_periphery_package as fpp
from eth_typing.evm import ChecksumAddress
from web3 import AsyncHTTPProvider, AsyncWeb3, HTTPProvider, Web3
from web3.middleware.geth_poa import geth_poa_middleware

url = "https://coston2-api.flare.network/ext/C/rpc"

# Get abi
abi3 = fpp.coston2.products.FlareContractRegistry.abi  # the recommended way
print(f"abi3: {str(abi3)[:50]}...")
print("Interface name:", fpp.coston2.products.FlareContractRegistry.interface)
abi3i = fpp.coston2.interface_abis.IFlareContractRegistry
print(f"abi3i: {str(abi3i)[:50]}...")

abi1 = fpp.name_to_abi("FlareContractRegistry", "coston2")
print(f"abi1: {str(abi1)[:50]}...")
abi1i = fpp.interface_to_abi("IFlareContractRegistry", "coston2")
print(f"abi1i: {str(abi1i)[:50]}...")

abi2 = fpp.coston2.name_to_abi("FlareContractRegistry")
print(f"abi2: {str(abi2)[:50]}...")
abi2i = fpp.coston2.interface_to_abi("IFlareContractRegistry")
print(f"abi2i: {str(abi2i)[:50]}...")

# Get addresses
w3 = Web3(HTTPProvider(url), middlewares=[geth_poa_middleware])

WNat_address = fpp.coston2.products.WNat.get_address(w3)  # The recommended way
print(f"WNat_address: {WNat_address}")
WNat_address2: ChecksumAddress = fpp.name_to_address("WNat", w3)
print(f"WNat_address (again): {WNat_address2}")


async def main():
    aw3 = AsyncWeb3(AsyncHTTPProvider(url))
    addresses = await fpp.async_names_to_addresses(
        ["WNat", "IDontExist", "FlareContractRegistry"], aw3
    )
    print(f"addresses: {addresses}")

    address = await fpp.coston2.products.FastUpdater.async_get_address(aw3)
    print(f"FastUpader address: {address}")


asyncio.run(main())
```


Package also includes abis as `.json` files. They are located in `artifacts/contracts`
folder for every chain.

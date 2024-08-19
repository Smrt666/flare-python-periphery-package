# flare-python-periphery-package
TODO:
* create LICENSE
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
This library exposes 10 names at top level:
 * `name_to_abi(name:str, network: str)` - returns abi as a python object (a list of dicts).
    Name is the name of contract, network can be one of coston, coston2, songbird and flare. 
 * `name_to_address(name: str, provider: Web3) -> str`, `names_to_addresses(names: "list[str]", provider: Web3) -> "list[str]"`, `async_name_to_address(name: str, provider: AsyncWeb3) -> str` and `async_names_to_addresses(names: "list[str]", provider: AsyncWeb3) -> "list[str]"`- use provider to get contract address(es). Reads from FlareContractRegistryLibrary.
 * `FLARE_CONTRACT_REGISTRY_ADDRESS` - hardcoded web3 checksum address constant, the same for all chains and should never change.
 * `coston`, `coston2`, `flare` and `songbird` - namespaces with 2 exports:
    - `abi` - a class allowing access to abis using .ContractName syntax
    - `name_to_abi(name: str)` - the same as top level function, with omitted network

Example:
```py
import asyncio

import flare_python_periphery_package as fpp
from web3 import AsyncHTTPProvider, AsyncWeb3, HTTPProvider, Web3
from web3.middleware.geth_poa import geth_poa_middleware

url = "https://coston2-api.flare.network/ext/C/rpc"

abi1 = fpp.name_to_abi("IFlareContractRegistry", "coston2")
print(f"abi1: {str(abi1)[:50]}...")
abi2 = fpp.coston2.name_to_abi("IFlareContractRegistry")
print(f"abi2: {str(abi2)[:50]}...")
abi3 = fpp.coston2.abis.IFlareContractRegistry
print(f"abi3: {str(abi3)[:50]}...")

w3 = Web3(HTTPProvider(url), middlewares=[geth_poa_middleware])
WNat_address = Web3.to_checksum_address(fpp.name_to_address("WNat", w3))
print(f"WNat_address: {WNat_address}")

async def main():
    aw3 = AsyncWeb3(AsyncHTTPProvider(url))
    addresses = await fpp.async_names_to_addresses(["WNat"], aw3)
    print(f"addresses: {addresses}")


asyncio.run(main())
```
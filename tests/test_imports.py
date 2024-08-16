import unittest

from web3 import Web3

import src.flare_python_periphery_package as fpp


class TestEverythingImports(unittest.TestCase):
    def test_toplevel_import(self):
        self.assertTrue(Web3.is_checksum_address(fpp.FLARE_CONTRACT_REGISTRY_ADDRESS))
        fpp.name_to_abi
        fpp.coston
        fpp.coston2
        fpp.flare
        fpp.songbird
        fpp.name_to_address
        fpp.name_to_address

    def test_chain_import(self):
        for chain in [fpp.coston, fpp.coston2, fpp.flare, fpp.songbird]:
            chain.name_to_abi
            chain.abis

import unittest

from web3 import Web3, eth, exceptions

import src.flare_python_periphery_package as fpp


def create_chain_tests(network):
    class TestAddressGetter(unittest.TestCase):
        provider: Web3

        @classmethod
        def setUpClass(cls) -> None:
            rpc_url = f"https://{network}-api.flare.network/ext/bc/C/rpc"
            cls.provider = Web3(Web3.HTTPProvider(rpc_url))

        def test_get_flare_contract_registry(self):
            addr = fpp.name_to_address("FlareContractRegistry", self.provider)
            self.assertEqual(addr, fpp.FLARE_CONTRACT_REGISTRY_ADDRESS)

        def test_names_to_addresses(self):
            addrs = fpp.names_to_addresses(
                ["FlareContractRegistry", "FtsoRewardManager"], self.provider
            )
            self.assertEqual(len(addrs), 2)
            self.assertEqual(addrs[0], fpp.FLARE_CONTRACT_REGISTRY_ADDRESS)

        def test_get_nonexistent_address(self):
            addr = fpp.name_to_address("asejsojfsoejfse", self.provider)
            self.assertEqual(addr, "0x0000000000000000000000000000000000000000")

        def test_get_nonexistent_addresses(self):
            addrs = fpp.names_to_addresses(["a", "b", "c"], self.provider)
            self.assertEqual(addrs, ["0x0000000000000000000000000000000000000000"] * 3)

        def test_invalid_input(self):
            self.assertRaises(
                exceptions.Web3ValidationError, lambda: fpp.name_to_address(5, self.provider)  # type: ignore
            )

            self.assertRaises(
                exceptions.Web3ValidationError,
                lambda: fpp.names_to_addresses("FlareContractRegistry", self.provider),  # type: ignore
            )

    return TestAddressGetter


TestCostonAddressGetter = create_chain_tests("coston")
TestCoston2AddressGetter = create_chain_tests("coston2")
TestFlareAddressGetter = create_chain_tests("flare")
TestSongbirdAddressGetter = create_chain_tests("songbird")

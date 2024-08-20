import unittest

from web3 import AsyncWeb3, Web3, exceptions

import src.flare_python_periphery_package as fpp


def create_chain_tests(network):
    class TestAddressGetter(unittest.TestCase):
        provider: Web3

        @classmethod
        def setUpClass(cls) -> None:
            rpc_url = f"https://{network}-api.flare.network/ext/bc/C/rpc"
            cls.provider = Web3(Web3.HTTPProvider(rpc_url))
            cls.module = {
                "coston2": fpp.coston2,
                "coston": fpp.coston,
                "flare": fpp.flare,
                "songbird": fpp.songbird,
            }[network]

        def test_name_to_address(self):
            addr = fpp.name_to_address("FlareContractRegistry", self.provider)
            self.assertEqual(addr, fpp.FLARE_CONTRACT_REGISTRY_ADDRESS)
            
            addr = self.module.products.FlareContractRegistry.get_address(self.provider)
            self.assertEqual(addr, fpp.FLARE_CONTRACT_REGISTRY_ADDRESS)

            if network == "coston2":
                # this one has a wierd interface name
                addr = self.module.products.ValidatorRewardManager.get_address(self.provider)
                self.assertNotEqual(addr, "0x0000000000000000000000000000000000000000")

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

    class TestAsyncAddressGetter(unittest.IsolatedAsyncioTestCase):
        async def asyncSetUp(self) -> None:
            rpc_url = f"https://{network}-api.flare.network/ext/bc/C/rpc"
            self.aprovider = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(rpc_url))
            self.module = {
                "coston2": fpp.coston2,
                "coston": fpp.coston,
                "flare": fpp.flare,
                "songbird": fpp.songbird,
            }[network]

        async def test_async_name_to_address(self):
            addr = await fpp.async_name_to_address(
                "FlareContractRegistry", self.aprovider
            )
            self.assertEqual(addr, fpp.FLARE_CONTRACT_REGISTRY_ADDRESS)

            addr = await fpp.coston.products.FlareContractRegistry.async_get_address(self.aprovider)
            self.assertEqual(addr, fpp.FLARE_CONTRACT_REGISTRY_ADDRESS)

        async def test_names_to_addresses(self):
            addrs = await fpp.async_names_to_addresses(
                ["FlareContractRegistry", "FtsoRewardManager"], self.aprovider
            )
            self.assertEqual(len(addrs), 2)
            self.assertEqual(addrs[0], fpp.FLARE_CONTRACT_REGISTRY_ADDRESS)

        async def test_get_nonexistent_address(self):
            addr = await fpp.async_name_to_address("asejsojfsoejfse", self.aprovider)
            self.assertEqual(addr, "0x0000000000000000000000000000000000000000")

        async def test_async_get_nonexistent_addresses(self):
            addrs = await fpp.async_names_to_addresses(["a", "b", "c"], self.aprovider)
            self.assertEqual(addrs, ["0x0000000000000000000000000000000000000000"] * 3)

        async def test_async_invalid_input(self):
            with self.assertRaises(exceptions.Web3ValidationError):
                await fpp.async_name_to_address(5, self.aprovider)  # type: ignore

            with self.assertRaises(exceptions.Web3ValidationError):
                await fpp.async_names_to_addresses("FlareContractRegistry", self.aprovider)  # type: ignore

    return TestAddressGetter, TestAsyncAddressGetter


TestCostonAddressGetter, TestAsyncCostonAddressGetter = create_chain_tests("coston")
TestCoston2AddressGetter, TestAsyncCoston2AddressGetter = create_chain_tests("coston2")
TestFlareAddressGetter, TestAsyncFlareAddressGetter = create_chain_tests("flare")
TestSongbirdAddressGetter, TestAsyncSongbirdAddressGetter = create_chain_tests(
    "songbird"
)

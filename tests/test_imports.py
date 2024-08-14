import unittest

import src.flare_python_periphery_package as fpp


class TestStringMethods(unittest.TestCase):
    def test_coston_import(self):
        print(fpp.coston.abis.IAddressValidityVerification)

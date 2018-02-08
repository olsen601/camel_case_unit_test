from unittest import TestCase
from Capstone_lab1_part2 import camel_case

class TestFunctions(TestCase):

    def test_camel_case(self):
        self.assertEqual('camelCase', camel_case('camel case'))
        self.assertEqual('madHatter', camel_case('MAD hatter'))
        self.assertEqual('peterPiperPickedAPackOfPeppers', camel_case('PeTer pIpER PIcked a paCk oF PePpers'))
        self.assertEqual('dont5HaveYourFace', camel_case('dont 5haVe yOur fACE'))

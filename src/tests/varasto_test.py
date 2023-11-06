import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto  = Varasto(10)
        self.varasto2 =Varasto(-1,-1)
        self.varasto3 =Varasto(0)
        self.varasto4 =Varasto(5,6)
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertEqual(self.varasto.saldo, 0.0)
        self.assertEqual(self.varasto2.saldo, 0.0)
        self.assertEqual(self.varasto4.saldo, 5)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertEqual(self.varasto.tilavuus, 10.0)
        self.assertEqual(self.varasto2.tilavuus, 0.0)
        self.assertEqual(self.varasto3.tilavuus, 0.0)
    def test_uudella_varastolla_väärä_tilavuus(self):
        self.assertEqual(self.varasto2.tilavuus, 0.0)
        self.assertEqual(self.varasto3.tilavuus, 0.0)
    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.varasto.lisaa_varastoon(4)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)
        saatu_maara = self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 6)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str(self):
        odotettu_tulos = "saldo =0, vielä tilaa 10"
        tulos = str(self.varasto)
        self.assertEqual(tulos, odotettu_tulos)

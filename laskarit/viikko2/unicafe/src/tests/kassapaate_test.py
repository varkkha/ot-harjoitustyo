import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_konstruktori_asettaa_edulliset_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_konstruktori_asettaa_maukkaat_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullisten_lounaiden_osalta_riittava_maksu(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_toimii_maukkaiden_lounaiden_osalta_riittava_maksu(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_toimii_edullisten_lounaiden_osalta_ei_riittava_maksu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_maukkaiden_lounaiden_osalta_ei_riittava_maksu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_edullisten_lounaiden_osalta_riittava_maksu_oikea_vaihtoraha(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_toimii_maukkaiden_lounaiden_osalta_riittava_maksu_oikea_vaihtoraha(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)

        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    #korttiostot
    def test_korttiosto_toimii_edullisten_lounaiden_osalta_riittava_maksu(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 9760)

    def test_korttiosto_toimii_maukkaiden_lounaiden_osalta_riittava_maksu(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 9600)

    def test_korttiosto_toimii_edullisten_lounaiden_osalta_ei_riittava_maksu(self):
        kortti = Maksukortti(2)
        onnistuu = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertFalse(onnistuu)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 2)

    def test_korttiosto_toimii_maukkaiden_lounaiden_osalta_ei_riittava_maksu(self):
        kortti = Maksukortti(2)
        onnistuu = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertFalse(onnistuu)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 2)

    def test_kortille_rahaa_ladatessa_kortin_saldo_muuttuu_ja_kassassa_oleva_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,5000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 105000)
        self.assertEqual(self.maksukortti.saldo, 15000)

    def test_kortille_rahaa_ladatessa_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-5000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 10000)

    def test_kassassa_rahaa_euroina(self):
        eurot = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(eurot, 1000)
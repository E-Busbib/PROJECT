import unittest
from fonctions_test import *

class Test(unittest.TestCase):

    def test_plage_valide(self):
        message = calculer_plage_horaire_core(
            "Europe/Paris", (9, 0), (17, 0),
            "America/New_York", (3, 0), (12, 0)
        )
        self.assertIn("Plage horaire commune", message)

    def test_aucune_plage_commune(self):
        message = calculer_plage_horaire_core(
            "Europe/Paris", (9, 0), (10, 0),
            "Asia/Tokyo", (18, 0), (19, 0)
        )
        self.assertEqual(message, "❌ Aucune plage horaire compatible trouvée.")

    def test_heure_debut_apres_fin(self):
        message = calculer_plage_horaire_core(
            "Europe/Paris", (17, 0), (9, 0),  # Inversé volontairement
            "America/New_York", (8, 0), (12, 0)
        )
        self.assertEqual(message, "❌ Erreur ! L'heure de début est avant celle de fin !")

    def test_plage_parfaite(self):
        message = calculer_plage_horaire_core(
            "Europe/Paris", (14, 0), (18, 0),
            "America/New_York", (8, 0), (12, 0)
        )
        self.assertIn("📍 Europe/Paris : 14:00 - 18:00", message)
        self.assertIn("📍 America/New_York : 08:00 - 12:00", message)

if __name__ == '__main__':
    unittest.main()

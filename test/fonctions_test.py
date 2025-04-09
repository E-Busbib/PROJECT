from datetime import datetime
import pytz

def calculer_plage_horaire_core(pays1, heure_debut1, heure_fin1, pays2, heure_debut2, heure_fin2):
    tz1 = pytz.timezone(pays1)
    tz2 = pytz.timezone(pays2)
    date_ref = datetime(2025, 1, 1)

    debut1 = tz1.localize(datetime(date_ref.year, date_ref.month, date_ref.day, *heure_debut1))
    fin1 = tz1.localize(datetime(date_ref.year, date_ref.month, date_ref.day, *heure_fin1))

    debut2 = tz2.localize(datetime(date_ref.year, date_ref.month, date_ref.day, *heure_debut2))
    fin2 = tz2.localize(datetime(date_ref.year, date_ref.month, date_ref.day, *heure_fin2))

    debut1_utc = debut1.astimezone(pytz.utc)
    fin1_utc = fin1.astimezone(pytz.utc)
    debut2_utc = debut2.astimezone(pytz.utc)
    fin2_utc = fin2.astimezone(pytz.utc)

    debut_commum = max(debut1_utc, debut2_utc)
    fin_commune = min(fin1_utc, fin2_utc)

    if fin1_utc < debut1_utc or fin2_utc < debut2_utc:
        return "❌ Erreur ! L'heure de début est avant celle de fin !"
    elif debut_commum < fin_commune:
        debut_final1 = debut_commum.astimezone(tz1).strftime("%H:%M")
        fin_final1 = fin_commune.astimezone(tz1).strftime("%H:%M")

        debut_final2 = debut_commum.astimezone(tz2).strftime("%H:%M")
        fin_final2 = fin_commune.astimezone(tz2).strftime("%H:%M")

        return (f"Plage horaire commune :\n\n"
                f"📍 {pays1} : {debut_final1} - {fin_final1}\n"
                f"📍 {pays2} : {debut_final2} - {fin_final2}")
    else:
        return "❌ Aucune plage horaire compatible trouvée."

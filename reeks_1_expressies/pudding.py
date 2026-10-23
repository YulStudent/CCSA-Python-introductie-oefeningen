aantalGekochteStuks = int(input())
prijsPerStuk = float(input())
aantalBarcodes = int(input())
aantalMijlen = int(input())

totalePrijs = aantalGekochteStuks * prijsPerStuk
totaleFFM = aantalGekochteStuks//aantalBarcodes * aantalMijlen


print(f"Phillips spendeerde ${totalePrijs:.1f} voor {totaleFFM} frequent flyer mijlen.")
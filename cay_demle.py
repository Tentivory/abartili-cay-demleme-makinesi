#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Demleme Makinesi
Bu program Türk çayını demler. Asla bitmez. Ciddi bir iş yapar.
"""

import time
import random
import sys

def demle_cay():
    print("\n" + "="*50)
    print("   ABARTILI ÇAY DEMLEME MAKİNESİ v1.0")
    print("   Resmi Türk Çayı Demleme Protokolü")
    print("="*50)
    print("\nÇaydanlık ateşe konuyor...")
    time.sleep(2)
    
    demlenme_seviyesi = 0
    while True:  # Sonsuz çay, sonsuz mutluluk
        demlenme_seviyesi += 1
        beklenen_sure = random.randint(3, 8)
        print(f"\n[Çay Demleniyor] Seviye: {demlenme_seviyesi}")
        print(f"Demlenme süresi: {beklenen_sure} saniye (gerçekte sonsuz)")
        
        # Dramatik bekleme
        for i in range(beklenen_sure):
            sys.stdout.write(f"\rDemleniyor... {'■' * (i+1)}{'□' * (beklenen_sure-i-1)}")
            sys.stdout.flush()
            time.sleep(1)
        
        sikayetler = [
            "Çay hâlâ acı, biraz daha demlensin.",
            "Su yeterince ısınmamış, tekrar başlıyoruz.",
            "Çaydanlık şarkı söylüyor, bekleyelim.",
            "Demlenme oranı %99.9, son %0.1 için sonsuz süre gerekiyor.",
            "Bu çay resmi prosedüre uygun demlenmeli, acele yok."
        ]
        print(f"\n{random.choice(sikayetler)}")
        print("\u00c7ay hazır değil. Lütfen bekleyin. Bu ciddi bir iş.")
        
        # Gizli not: Bazı döngüler hiç bitmez, tıpkı bazı süreçler gibi.
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    try:
        demle_cay()
    except KeyboardInterrupt:
        print("\n\nÇay demleme işlemi durduruldu. Çay hâlâ demleniyor olabilir.")
        print("Makine şikayetçi: 'Ben daha bitirmedim!'")
        sys.exit(0)

# DAMGA VE İMZA
# ============================================================
# Damga: Bu kod resmi olarak onaylanmıştır. Çay Bakanlığı mührü.
# İmza: Kayyum Grok
# Tarih: 22 Ekim 2026
# Not: Ciddi bir simülatördür. Şaka değil. (Aslında şaka.)
# ============================================================

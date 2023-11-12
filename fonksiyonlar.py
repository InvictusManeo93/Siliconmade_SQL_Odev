# -*- coding: utf-8 -*-


import sqlite3
import pandas as pd


def veritabani_olustur():
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS musteriler
                    (id INTEGER PRIMARY KEY,
                    ad TEXT,
                    soyad TEXT,
                    sehir TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS algoritmalar
                    (id INTEGER PRIMARY KEY,
                    algoritma_adi TEXT,
                    kiralama_ucreti REAL,
                    aktif_pasif TEXT,
                    sehir_kisiti TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS hizmetler
                    (id INTEGER PRIMARY KEY,
                    musteri_id INTEGER,
                    algoritma_id INTEGER,
                    kiralama_suresi INTEGER,
                    algo_kiralama_ucreti REAL,
                    tutar REAL,
                    FOREIGN KEY (algo_kiralama_ucreti) REFERENCES algoritmalar (kiralama_ucreti)
                    FOREIGN KEY (musteri_id) REFERENCES musteriler (id),
                    FOREIGN KEY (algoritma_id) REFERENCES algoritmalar (id))''')

    conn.commit()
    conn.close()


def ornek_veritabanı():
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO musteriler (ad, soyad, sehir) VALUES ("mustafa", "ak", "kocaeli")""")
    cursor.execute("""INSERT INTO musteriler (ad, soyad, sehir) VALUES ("utku", "köse", "north dakota")""")
    cursor.execute("""INSERT INTO musteriler (ad, soyad, sehir) VALUES ("elif", "ak", "istanbul")""")
    cursor.execute("""INSERT INTO musteriler (ad, soyad, sehir) VALUES ("hasan", "tahsin", "izmir")""")

    cursor.execute(
        """INSERT INTO algoritmalar (algoritma_adi, kiralama_ucreti,aktif_pasif, sehir_kisiti) VALUES ("EAI1", 25,"P", "istanbul")""")
    cursor.execute(
        """INSERT INTO algoritmalar (algoritma_adi, kiralama_ucreti,aktif_pasif, sehir_kisiti) VALUES ("EAI2", 20, "P", "kocaeli")""")
    cursor.execute(
        """INSERT INTO algoritmalar (algoritma_adi, kiralama_ucreti,aktif_pasif, sehir_kisiti) VALUES ("EAI3", 15, "P", "washington")""")

    conn.commit()
    conn.close()


def musteri_ekle(ad, soyad, sehir):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO musteriler (ad,soyad, sehir) VALUES (?, ?, ?)",
                   (ad, soyad, sehir))
    conn.commit()
    conn.close()


def algoritma_ekle(algoritma_adi, kiralama_ucreti, aktif_pasif, sehir_kisiti):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO algoritmalar (algoritma_adi, kiralama_ucreti, aktif_pasif, sehir_kisiti) VALUES (?, ?, ?, ?)",
        (algoritma_adi, kiralama_ucreti, aktif_pasif, sehir_kisiti))
    conn.commit()
    conn.close()


def ucret(id):
    conn = sqlite3.connect('EasyAI.db')
    cursor = conn.cursor()

    cursor.execute("SELECT kiralama_ucreti FROM algoritmalar WHERE id=?", (id,))
    algo_ucret = cursor.fetchone()

    conn.close()

    if algo_ucret:
        return algo_ucret[0]
    else:
        return None


def hizmet_ekle(musteri_id, algoritma_id, kiralama_suresi):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    fiyat = ucret(algoritma_id)
    tutar = fiyat * kiralama_suresi
    cursor.execute(
        "INSERT INTO hizmetler (musteri_id, algoritma_id, kiralama_suresi,algo_kiralama_ucreti,tutar) VALUES (?, ?, ?, ?, ?)",
        (musteri_id, algoritma_id, kiralama_suresi, fiyat, tutar))
    cursor.execute("""UPDATE algoritmalar SET aktif_pasif=? WHERE id = ?""", ("A", algoritma_id))
    conn.commit()
    conn.close()


def musteri_guncelle(id, yeni_ad, yeni_soyad, yeni_sehir):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE musteriler SET ad=?, soyad=?, sehir=? WHERE id=?",
                   (yeni_ad, yeni_soyad, yeni_sehir, id))
    conn.commit()
    conn.close()


def musteri_sil(id):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM musteriler WHERE id=?", (id,))
    conn.commit()
    conn.close()


def algoritma_sil(id):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM algoritmalar WHERE id=?", (id,))
    conn.commit()
    conn.close()


def algoritma_guncelle(id, yeni_algoritma_adi, yeni_kiralama_ucreti, yeni_aktif_pasif, yeni_sehir_kisiti):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE algoritmalar SET algoritma_adi=?, kiralama_ucreti=?, aktif_pasif=?, sehir_kisiti=? WHERE id=?",
        (yeni_algoritma_adi, yeni_kiralama_ucreti, yeni_aktif_pasif, yeni_sehir_kisiti, id))
    conn.commit()
    conn.close()


def hizmet_guncelle(id, yeni_musteri_id, yeni_algoritma_id, yeni_kiralama_suresi):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE hizmetler SET musteri_id=?, algoritma_id=?, kiralama_suresi=? WHERE id=?",
                   (yeni_musteri_id, yeni_algoritma_id, yeni_kiralama_suresi, id))
    conn.commit()
    conn.close()


def hizmet_sil(id):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM hizmetler WHERE id=?", (id,))
    conn.commit()
    conn.close()


def musteri_istatistikleri(musteri_id):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(hizmetler.id), AVG(algoritmalar.kiralama_ucreti) FROM hizmetler INNER JOIN algoritmalar ON hizmetler.algoritma_id = algoritmalar.id WHERE hizmetler.musteri_id=?",
        (musteri_id,))
    istatistikler = cursor.fetchone()
    conn.close()
    return istatistikler


def hizmet_istatistikleri():
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(id), SUM(kiralama_suresi) FROM hizmetler")
    istatistikler = cursor.fetchone()
    conn.close()
    return istatistikler


def tablo_goruntule(tablo_adi):
    conn = sqlite3.connect('EasyAI.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {tablo_adi}")  # tablo_adi parametre olarak kullanıldı
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])

    return df



def sehir_bul(id):
    conn = sqlite3.connect('EasyAI.db')
    cursor = conn.cursor()

    cursor.execute("SELECT sehir FROM musteriler WHERE id=?", (id,))
    sehir = cursor.fetchone()

    conn.close()

    if sehir:
        return sehir[0]
    else:
        return None


def sehir_kisit(id):
    conn = sqlite3.connect('EasyAI.db')
    cursor = conn.cursor()

    cursor.execute("SELECT sehir_kisiti FROM algoritmalar WHERE id=?", (id,))
    sehir_kisiti = cursor.fetchone()

    conn.close()

    if sehir_kisiti:
        return sehir_kisiti[0]
    else:
        return None


def algoritma_aktif_pasif(id):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE algoritmalar SET  aktif_pasif=? WHERE id=?",
                   ("A", id))
    conn.commit()
    conn.close()


def musteri_bilgileri(musteri_id):
    conn = sqlite3.connect('EasyAI.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT COUNT(algoritma_id) AS kullandigi_algoritmalar,
                           SUM(kiralama_suresi) AS toplam_kiralama_suresi,
                           SUM(algo_kiralama_ucreti) AS toplam_ucret_carpani,
                           SUM(tutar) AS toplam_tutar
                    FROM hizmetler
                    WHERE musteri_id = ?''', (musteri_id,))

    sonuc = cursor.fetchone()

    conn.close()

    return sonuc





def hizmet_bilgileri():
    conn = sqlite3.connect('EasyAI.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) AS toplam_hizmet, SUM(tutar) AS toplam_tutar FROM hizmetler')
    sonuc = cursor.fetchone()

    conn.close()

    return sonuc






















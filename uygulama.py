import pandas as pd

from fonksiyonlar import *
import streamlit as st

from fonksiyonlar import tablo_goruntule

veritabani_olustur()

with st.expander("Müşteri Ekle"):
    with st.form("Müşteri Ekle", clear_on_submit=True):
        ad = (st.text_input("Ad: ")).lower()
        soyad = (st.text_input("Soyad: ")).lower()
        sehir = (st.text_input("Şehir: ")).lower()
        ekle = st.form_submit_button("Müşteri Ekle")
        if ekle:
            musteri_ekle(ad, soyad, sehir)

with st.expander("Müşteri Güncelle"):

    st.title("Müşteriler")
    st.table(tablo_goruntule("musteriler"))
    with st.form("Müşteri Güncelle", clear_on_submit=True):
        conn = sqlite3.connect("EasyAI.db")
        cursor = conn.cursor()
        id = int(st.number_input("Güncellemek istediğiniz müşterinin ID sini giriniz: "))


        yeni_ad = (st.text_input("Yeni adı giriniz: ")).lower()
        yeni_soyad = (st.text_input("Yeni soyadı giriniz: ")).lower()
        yeni_sehir = (st.text_input("Yeni şehir giriniz: ")).lower()
        ekle = st.form_submit_button("Müşteri Güncelle")
        if ekle:
            cursor.execute("SELECT id FROM musteriler WHERE id=?", (id,))
            musteri = cursor.fetchone()
            if musteri:
                musteri_guncelle(id, yeni_ad, yeni_soyad, yeni_sehir)
                st.success("Başarıyla Güncellendi")
            else:
                st.st.warning("Belirtilen ID'ye sahip müşteri bulunamadı.")

with st.expander("Müşteri Sil"):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    with st.form("Müşteri Sil", clear_on_submit=True):
        st.title("Müşteriler")
        st.table(tablo_goruntule("musteriler"))
        id = int(st.number_input("Silmek istediğiniz müşterinin ID sini giriniz: "))
        sil = st.form_submit_button("Müşteri Sil")
        if sil:
            cursor.execute("SELECT id FROM musteriler WHERE id=?", (id,))
            musteri = cursor.fetchone()
            if musteri:
                musteri_sil(id)
                st.success("Başarıyla Silindi")
            else:
                st.warning("Belirtilen ID'ye sahip müşteri bulunamadı.")

with st.expander("Algoritma Ekle"):
    with st.form("Algoritma Ekle", clear_on_submit=True):
        algoritma_adi = (st.text_input("Algoritma Adı: ")).lower()
        kiralama_ucreti = float(st.number_input("Saatlik Kiralama Ücreti: "))
        aktif_pasif = (st.text_input("Aktif (A) / Pasif (P): ")).upper()
        sehir_kisiti = (st.text_input("Şehir Kısıtı: ")).lower()
        ekle = st.form_submit_button("Algoritma Ekle")
        if ekle:
            algoritma_ekle(algoritma_adi, kiralama_ucreti, aktif_pasif, sehir_kisiti)
            st.success("Başarıyla Eklendi")

with st.expander("Algoritma Güncelle"):

    st.title("Algoritmalar")
    st.table(tablo_goruntule("algoritmalar"))
    with st.form("Algoritma Güncelle", clear_on_submit=True):
        conn = sqlite3.connect("EasyAI.db")
        cursor = conn.cursor()
        id = int(st.number_input("Güncellemek istediğiniz algoritmanın ID sini giriniz: "))

        yeni_algoritma_adi = (st.text_input("Yeni adı giriniz: ")).lower()
        yeni_kiralama_ucreti = int(st.number_input("Yeni kiralama ücretini giriniz: "))
        yeni_aktif_pasif = (st.text_input("Yeni Aktif (A) / Pasif (P) durumunu giriniz: ")).upper()
        yeni_sehir_kisiti = st.text_input(("Yeni şehir kısıtını giriniz: ")).lower()
        ekle = st.form_submit_button("Algoritma Güncelle")
        if ekle:
            cursor.execute("SELECT id FROM algoritmalar WHERE id=?", (id,))
            algoritma = cursor.fetchone()
            if algoritma:
                algoritma_guncelle(id, yeni_ad, yeni_soyad, yeni_sehir)
                st.success("Başarıyla Güncellendi")
            else:
                st.warning("Belirtilen ID'ye sahip algoritma bulunamadı.")

with st.expander("Algoritma Sil"):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()
    with st.form("Algoritma Sil", clear_on_submit=True):
        st.title("Algoritmalar")
        st.table(tablo_goruntule("algoritmalar"))
        id = int(st.number_input("Silmek istediğiniz algoritmanın ID sini giriniz: "))
        sil = st.form_submit_button("Algoritma Sil")
        if sil:
            cursor.execute("SELECT id FROM algoritmalar WHERE id=?", (id,))
            Algoritma = cursor.fetchone()
            if Algoritma:
                algoritma_sil(id)
                st.success("Başarıyla Silindi")
            else:
                st.warning("Belirtilen ID'ye sahip algoritma bulunamadı.")

with st.expander("Hizmet Ekle"):
    col1, col2 = st.columns(2)

    with col1:
        st.write("Müşteriler")
        st.table(tablo_goruntule("musteriler"))

    with col2:
        st.write("Algoritmalar")
        st.table(tablo_goruntule("algoritmalar"))


    musteri_id = int(st.number_input("Müşteri ID: "))
    algoritma_id = int(st.number_input("Algoritma ID: "))
    kiralama_suresi = int(st.number_input("Kiralama Süresi (saat): "))



    if sehir_bul(musteri_id) == sehir_kisit(algoritma_id):


        if st.button("ekle"):
            hizmet_ekle(musteri_id, algoritma_id, kiralama_suresi)
            st.success("Başarıyla Eklendi")

    else:
        st.warning("Müşteri şehir ve algoritma şehir kıstası sağlanmadığından hizmet verilememektedir")









with st.expander("Hizmet Sil"):
    conn = sqlite3.connect("EasyAI.db")
    cursor = conn.cursor()

    with st.form("Hizmet Sil", clear_on_submit=True):
        st.title("Hizmetler")
        st.table(tablo_goruntule("hizmetler"))
        id = int(st.number_input("Silmek istediğiniz hizmetin ID sini giriniz: "))
        sil = st.form_submit_button("Hizmet Sil")
        if sil:
            cursor.execute("SELECT id FROM hizmetler WHERE id=?", (id,))
            hizmet = cursor.fetchone()
            if hizmet:
                hizmet_sil(id)
                st.success("Başarıyla Silindi")
            else:
                st.warning("Belirtilen ID'ye sahip hizmet bulunamadı.")

with st.expander("Hizmet Bilgileri"):


        try:

            bilgiler = hizmet_bilgileri()

            st.write(f"Toplam Hizmet Sayısı: {bilgiler[0]}")
            st.write(f"Toplam Tutar: {bilgiler[1]}")
        except:
            st.warning("Hizmet Bulunmamaktadır")

with st.expander("Müşteri Bilgileri"):
    try:
        with st.form("Müşteri Bilgileri", clear_on_submit=True):

            st.title("Musteriler")
            st.table(tablo_goruntule("musteriler"))
            musteri_id = int(st.number_input("Görüntelemek istediğiniz müşterinin ID sini giriniz: "))
            sorgula = st.form_submit_button("Sorgula")
            if sorgula:
                bilgiler = musteri_bilgileri(musteri_id)
                if bilgiler:
                    st.write(f"Müşteri ID: {musteri_id}")

                    st.write(f"Saat Başı Ortalama Ücret: {bilgiler[3] / bilgiler[1]}")
                    st.write(f"Toplam Ücret : {bilgiler[3]}")
                    st.write(f"Kullandığı Algoritma Sayısı: {bilgiler[0]}")
                else:
                    st.write(f"Müşteri bulunamadı.")


    except:
        st.write("Müşteri hizmet kullanmıyor")







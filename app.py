import streamlit as st
import base64

# --- FUNGSI KRIPTOGRAFI (LOGIKA ASURA) ---
def zoro_ultimate_cipher(text, all_keys):
    res = bytearray()
    for i in range(len(text)):
        char_val = ord(text[i])
        for key in all_keys:
            char_val = char_val ^ ord(key[i % len(key)])
        res.append(char_val)
    return base64.b64encode(res).decode('utf-8')

def zoro_ultimate_decipher(encoded_str, all_keys):
    try:
        data = base64.b64decode(encoded_str)
        original = ""
        reversed_keys = all_keys[::-1]
        for i in range(len(data)):
            char_val = data[i]
            for key in reversed_keys:
                char_val = char_val ^ ord(key[i % len(key)])
            original += chr(char_val)
        return original
    except:
        return "Error: Kode Base64 tidak valid atau kunci salah!"

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Asura XOR Cipher", page_icon="⚔️")

# --- STYLE CSS (Biar keren dikit) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 10px; }
    .stTextInput>div>div>input { background-color: #1d2129; color: #00ff00; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (DAFTAR JURUS/KUNCI) ---
st.sidebar.header("⚔️ Santoryu: 9 Pedang")
jurus_zoro = [
    "WADO-ICHIMONJI-SHISHI-SONSON",
    "SANDAI-KITETSU-RASHOMON",
    "SHUSUI-SANZEN-SEKAI",
    "ENMA-ONYAGIRI",
    "TATSUMAKI-KOKUJO-MAGA-UIRO",
    "ROKUDO-NO-TSUJI",
    "DAI-EREN-SANZEN-DAISEKAI",
    "KOKUJO-RYUMA-GANKI-YADORI",
    "KYUTORYU-ASURA-BAKKEI-MOJA-NO-TAWAME"
]

for i, j in enumerate(jurus_zoro, 1):
    st.sidebar.text(f"{i}. {j.split('-')[0]}")

# --- KONTEN UTAMA ---
st.title("⚔️ Asura XOR: Multi-Layer Encryption")
st.write("Implementasi Kriptografi Berlapis Terinspirasi dari Roronoa Zoro")

tab1, tab2 = st.tabs(["Enkripsi (Kunci Pesan)", "Dekripsi (Buka Pesan)"])

with tab1:
    st.header("🛡️ Proses Enkripsi")
    plaintext = st.text_area("Masukkan Pesan Asli (Plaintext):", placeholder="Contoh: Universitas Amikom Yogyakarta")
    
    if st.button("Tebas dengan 9 Pedang (Enkripsi)"):
        if plaintext:
            hasil_enkripsi = zoro_ultimate_cipher(plaintext, jurus_zoro)
            st.success("Berhasil Dienkripsi!")
            st.code(hasil_enkripsi, language="text")
            st.info(f"Pesan diproses dengan {len(jurus_zoro)} lapisan XOR.")
        else:
            st.warning("Masukkan pesan terlebih dahulu!")

with tab2:
    st.header("🔓 Proses Dekripsi")
    ciphertext = st.text_area("Masukkan Kode Base64 (Ciphertext):")
    
    if st.button("Buka Segel (Dekripsi)"):
        if ciphertext:
            hasil_dekripsi = zoro_ultimate_decipher(ciphertext, jurus_zoro)
            if "Error" in hasil_dekripsi:
                st.error(hasil_dekripsi)
            else:
                st.success("Berhasil Didekripsi!")
                st.subheader("Pesan Asli:")
                st.markdown(f"### {hasil_dekripsi}")
        else:
            st.warning("Masukkan kode Base64 terlebih dahulu!")

# --- FOOTER ---
st.markdown("---")
st.caption("Developed by Pendekar Kriptografi Amikom - 2026")

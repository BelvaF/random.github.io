import streamlit as st

st.title("HAAAIIIII")

# 1. Definisikan username dan password statis (sementara)
USER_KREDENSIAL = {
    "by": "weare21",
}

# 2. Inisialisasi status login di session state
if "terautentikasi" not in st.session_state:
    st.session_state.terautentikasi = False

# 3. Fungsi untuk mengecek login
def proses_login():
    username = st.session_state.input_user
    password = st.session_state.input_pass
    
    if username in USER_KREDENSIAL and USER_KREDENSIAL[username] == password:
        st.session_state.terautentikasi = True
        st.session_state.user_aktif = username
        st.toast("Login berhasil!", icon="✅")
    else:
        st.error("Username atau password salah!")

# 4. Fungsi untuk logout
def proses_logout():
    st.session_state.terautentikasi = False
    st.session_state.user_aktif = None
    st.toast("Anda telah keluar.", icon="ℹ️")

# 5. Tampilan Halaman
if not st.session_state.terautentikasi:
    # Tampilan Form Login
    st.title("🔐 Silakan Sign In")
    
    with st.form("form_login"):
        st.text_input("Username", key="input_user")
        st.text_input("Password", type="password", key="input_pass")
        st.form_submit_button("Masuk", on_click=proses_login)
        
else:
    # Tampilan Konten Utama Aplikasi Setelah Login
    st.title(f"👋 Selamat Datang, {st.session_state.user_aktif}!")
    st.write("Ini adalah halaman utama aplikasi rahasia Anda.")
    
    # Tombol Logout ditaruh di Sidebar
    with st.sidebar:
        st.write(f"Login sebagai: **{st.session_state.user_aktif}**")
        st.button("Log Out", on_click=proses_logout)
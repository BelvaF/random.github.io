import streamlit as st

USER_DATA = {
    "by": "21",
}

# Inisialisasi session state
if "auth" not in st.session_state:
    st.session_state.auth = False
if "halaman" not in st.session_state:
    st.session_state.halaman = "utama"  # Untuk melacak posisi halaman setelah login


def login():
    username = st.session_state.input_user
    password = st.session_state.input_pass
    
    if username in USER_DATA and USER_DATA[username] == password:
        st.session_state.auth = True
        st.session_state.user_aktif = username
        st.session_state.halaman = "utama"  # Set ke halaman utama setelah sukses login
    else:
        st.error("Heh, Gaboleh masukkk")


def logout():
    st.session_state.auth = False
    st.session_state.user_aktif = None
    st.session_state.halaman = "utama"
    st.toast("See yaaaa!")


def pindah_ke_awal():
    st.session_state.halaman = "awal"


# View web
if not st.session_state.auth:
    # Form login
    st.title("HAAAIIIII")
    st.subheader("Cobaa tebaakkk, uname sama pw-nya apaaa wkwkwkwk")
    with st.form("form_login"):
        st.text_input("Apa yaa usernamenya", key="input_user")
        st.text_input("Kira-kira apa yaa passwordnya", type="password", key="input_pass")
        st.form_submit_button("yakinn gaa? kalau yakin, boleeh klikk", on_click=login)
        
else:
    # Menu Sidebar (Selalu muncul saat login)
    with st.sidebar:
        st.write(f"Login sebagai: **{st.session_state.user_aktif}**")
        st.button("Log Out", on_click=logout)

    # Kontrol tampilan berdasarkan state 'halaman'
    if st.session_state.halaman == "utama":
        st.title(f"HAIIII, {st.session_state.user_aktif}!")
        st.write("akuu random mau ngomong dan in different way ajaa. Soalnya aku kayaknya gabisa ngomong langsung, tapi aku pengen liat your live reaction ehehhehe")
        
        # Mengubah fungsi tombol untuk mengganti state halaman
        st.button("letss gowww", on_click=pindah_ke_awal)

    elif st.session_state.halaman == "awal":
        # Halaman baru yang bersih setelah tombol di-klik
        st.title("Cerita Random ✨")
        st.write("Yaaahhh, aku pengen ngomong random ajaa. Aku pengen liat your live reaction ehehhehe")
        
        # Tombol opsional untuk kembali ke halaman sebelumnya jika mau
        if st.button("Kembali"):
            st.session_state.halaman = "utama"
            st.rerun()



#  hallo git
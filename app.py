import streamlit as st

USER_DATA = {
    "by": "21",
}

# Inisialisasi session state
if "auth" not in st.session_state:
    st.session_state.auth = False
if "halaman" not in st.session_state:
    st.session_state.halaman = "utama"  # Untuk melacak posisi halaman setelah login
if "halaman_cerita" not in st.session_state:
    st.session_state.halaman_cerita = 0  # Index halaman cerita random mulai dari 0


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
    st.session_state.halaman_cerita = 0  # Reset halaman cerita
    st.toast("See yaaaa!")


def pindah_ke_awal():
    st.session_state.halaman = "awal"
    st.session_state.halaman_cerita = 0  # Pastikan mulai dari cerita pertama


# Konten untuk cerita random (bisa ditambah sesuka hati)
LIST_CERITA = [
    """
    Byyy...
    
    I love you literally that much. I don't know how it grows, but it naturally increases day by day.
    
    i never met a man like you. literally never. maybe there is one most like him, like Kak Ojan (Kak Put’s husband) hehe.
    """,
    # -----------------------------------------
    """
    by, meeting you is one of my greatest gratefulness. i found a man—a man who is (almost) exactly like everything i have ever been thinking of. 
    
    thank you so much for coming into my life, even though in this unexpected way. 
    
    maybe it's only been 3 months, but for me, it's been such a colorful ride. i can feel the happiness, safety, your gentleman treatment, the scared, the confused... all mixed
    """,
    # -----------------------------------------
    """
    By, maybe im not the one and i admit that. but im happy and glad because u choose me to be the girl who can feel and know another side of Raffi Widiansyah.
    """,
    # -----------------------------------------
    """
    let's talk about a fun fact about me? wkkwkw.
    
    by, i actually **hate** smokers and drinkers. but i don't know why i can accept you, meanwhile i know you are both.
    
    but turns out... *it doesn't matter anymore, if it's you.*
    
    and i think i know why i am like this. day by day knowing you, i realized something. 
    you are such a gentleman, you respect and see up to your parents (especially your mom), and you have a bunch of knowledge. 
    
    and it completely changes my pov about things. 
    
    enough. that's the fun fact wkwkwkw.
    """,
    # -----------------------------------------
    """
    by, now im scared.
    im scared, that i will got social punishment.
    im too scared if u r breakup. 
    im too scared that she or her friends will make me viral or something like post me on social media.
    idc abt me, but if my family know it….. 
    i dont even know what would i do.

    by, lets talk abt this?
    """
]


# Fungsi navigasi cerita
def cerita_selanjutnya():
    if st.session_state.halaman_cerita < len(LIST_CERITA) - 1:
        st.session_state.halaman_cerita += 1

def cerita_sebelumnya():
    if st.session_state.halaman_cerita > 0:
        st.session_state.halaman_cerita -= 1


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
        st.write("byyy, u know how much i love u kan? u can feel it kan? answer it first")
        st.write("akuu random mau ngomong dan in different way ajaa. Soalnya aku kayaknya gabisa ngomong langsung, tapi aku pengen liat your live reaction ehehhehe")
        
        st.button("letss gowww", on_click=pindah_ke_awal)

   
    elif st.session_state.halaman == "awal":
        st.title("Cerita Random ✨")
        
        # Ambil cerita berdasarkan index halaman_cerita saat ini
        idx = st.session_state.halaman_cerita
        st.write(LIST_CERITA[idx])
        
        st.write("---") # Garis pembatas visual
        
        # Membuat 3 kolom besar, kita hanya pakai kolom tengah (col2) agar posisinya di tengah layar
        col1, col2, col3 = st.columns([2, 1, 2])
        
        with col2:
            # Di dalam kolom tengah, kita bagi 2 kolom kecil yang pas banget buat dua tombol
            sub_col1, sub_col2 = st.columns([1, 1])
            
            with sub_col1:
                if idx > 0:
                    st.button("◀ previous", on_click=cerita_sebelumnya, key="btn_prev", use_container_width=True)
                else:
                    st.button("◀ previous", disabled=True, key="btn_prev_dis", use_container_width=True)
                    
            with sub_col2:
                if idx < len(LIST_CERITA) - 1:
                    st.button("next ▶", on_click=cerita_selanjutnya, key="btn_next", use_container_width=True)
                else:
                    st.button("next ▶", disabled=True, key="btn_next_dis", use_container_width=True)
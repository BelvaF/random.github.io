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
        
        # Menggunakan kolom yang sangat kecil jaraknya khusus untuk menaruh tombol berdampingan di tengah
        _, center_col, _ = st.columns([1, 8, 1])
        
        with center_col:
            # Wadah horizontal agar tombol & teks tetap sejajar di layar HP
            sub_col1, sub_col2, sub_col3 = st.columns([1, 2, 1])
            
            with sub_col1:
                if idx > 0:
                    st.button("◀", on_click=cerita_sebelumnya, key="btn_prev")
                else:
                    st.button("◀", disabled=True, key="btn_prev_dis")
                    
            with sub_col2:
                st.markdown(f"<p style='text-align: center; font-size: 14px; margin-top: 5px; color: gray;'>{idx + 1} / {len(LIST_CERITA)}</p>", unsafe_allow_html=True)
                
            with sub_col3:
                if idx < len(LIST_CERITA) - 1:
                    st.button("▶", on_click=cerita_selanjutnya, key="btn_next")
                else:
                    st.button("▶", disabled=True, key="btn_next_dis")
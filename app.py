import streamlit as st

# ===============================
# KONFIGURASI HALAMAN
# ===============================

st.set_page_config(
    page_title="Galactic Number Theory Explorer",
    page_icon="🌌",
    layout="wide"
)

# ===============================
# TEMA GALAKSI
# ===============================

st.markdown("""
<style>

.stApp {
    background-color: #0b1026;
}

h1 {
    color: #00e5ff;
    text-align: center;
}

h2, h3 {
    color: #bb86fc;
}

.stButton > button {
    width: 100%;
    background-color: #4f46e5;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# SIDEBAR
# ===============================

with st.sidebar:
    st.title("📚 Menu")
    st.info("""
Materi:
- FPB
- KPK
- Algoritma Euclid
- Relatif Prima
""")

# ===============================
# FUNGSI FPB
# ===============================

def hitung_fpb(a, b):
    langkah = []

    while b != 0:
        q = a // b
        r = a % b

        langkah.append({
            "a": a,
            "b": b,
            "q": q,
            "r": r
        })

        a, b = b, r

    return a, langkah

# ===============================
# JUDUL
# ===============================

st.title("🌌 Galactic Number Theory Explorer")

st.write("""
Menentukan FPB dan KPK menggunakan Algoritma Euclid.
""")

# ===============================
# INPUT
# ===============================

col1, col2 = st.columns(2)

with col1:
    a = st.number_input(
        "Bilangan Pertama",
        min_value=1,
        step=1
    )

with col2:
    b = st.number_input(
        "Bilangan Kedua",
        min_value=1,
        step=1
    )

# ===============================
# PROSES
# ===============================

if st.button("🚀 Analisis Bilangan"):

    fpb, langkah = hitung_fpb(int(a), int(b))

    kpk = (int(a) * int(b)) // fpb

    st.header("📊 Hasil")

    st.success(f"FPB = {fpb}")
    st.success(f"KPK = {kpk}")

    # Relatif prima
    if fpb == 1:
        st.success("Kedua bilangan relatif prima.")
    else:
        st.warning("Kedua bilangan tidak relatif prima.")

    st.divider()

    st.header("📖 Langkah Algoritma Euclid")

    for i, item in enumerate(langkah, start=1):

        st.subheader(f"Langkah {i}")

        st.write(
            f"{item['a']} ÷ {item['b']} = {item['q']} sisa {item['r']}"
        )

        st.latex(
            f"{item['a']}={item['q']}\\times{item['b']}+{item['r']}"
        )

    st.divider()

    st.header("🎯 Menentukan FPB")

    x = int(a)
    y = int(b)

    while y != 0:
        st.write(
            f"FPB({x},{y}) = FPB({y},{x % y})"
        )
        x, y = y, x % y

    st.success(
        f"FPB({int(a)},{int(b)}) = {fpb}"
    )

    st.divider()

    st.header("🎯 Menentukan KPK")

    st.write("Menggunakan rumus:")

    st.latex(
        r"KPK(a,b)=\frac{a\times b}{FPB(a,b)}"
    )

    st.latex(
        rf"KPK({int(a)},{int(b)})=\frac{{{int(a)}\times{int(b)}}}{{{fpb}}}"
    )

    st.latex(
        rf"=\frac{{{int(a)*int(b)}}}{{{fpb}}}"
    )

    st.latex(
        rf"={kpk}"
    )

    st.success(
        f"KPK({int(a)},{int(b)}) = {kpk}"
    )

    st.divider()

    st.header("🧠 Fakta Bilangan")

    if int(a) % 2 == 0:
        st.write(f"{int(a)} adalah bilangan genap")
    else:
        st.write(f"{int(a)} adalah bilangan ganjil")

    if int(b) % 2 == 0:
        st.write(f"{int(b)} adalah bilangan genap")
    else:
        st.write(f"{int(b)} adalah bilangan ganjil")

    st.info(
        f"FPB terbesar dari kedua bilangan adalah {fpb}"
    )

    st.info(
        f"KPK terkecil dari kedua bilangan adalah {kpk}"
    )

st.caption(
    "Galactic Number Theory Explorer • Teori Bilangan"
)

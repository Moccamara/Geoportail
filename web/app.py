# =========================================================
# 🌍 STRATEGIC GEOSPATIAL ECOSYSTEM – STREAMLIT VERSION
# Author: Dr Mahamadou CAMARA
# =========================================================

import streamlit as st
import folium
from streamlit_folium import st_folium

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Strategic Geospatial Ecosystem",
    layout="wide"
)

# =========================================================
# LANGUAGE SYSTEM
# =========================================================
lang = st.sidebar.selectbox("🌐 Language / Langue", ["EN", "FR"])

def t(en, fr):
    return fr if lang == "FR" else en

# =========================================================
# HEADER (HERO SECTION)
# =========================================================
st.markdown(f"""
<style>
.hero {{
    background: linear-gradient(rgba(0,20,10,0.75), rgba(0,40,20,0.85)),
    url('https://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57730/mali_amo_2009240_lrg.jpg');
    background-size: cover;
    padding: 120px 20px;
    text-align: center;
    color: white;
}}
.card {{
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}}
</style>

<div class="hero">
<h1>{t("STRATEGIC GEOSPATIAL ECOSYSTEM","ÉCOSYSTÈME GÉOSPATIAL STRATÉGIQUE")}</h1>
<p>{t("Geospatial Data Scientist | Remote Sensing | AI","Scientifique des données géospatiales | Télédétection | IA")}</p>
<p>{t("Earth Observation • Research • Innovation","Observation de la Terre • Recherche • Innovation")}</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# NAVIGATION
# =========================================================
menu = st.sidebar.radio("Navigation", [
    "Home", "Research Hub", "Projects",
    "Monitoring", "Map",
    "Scholar", "Timeline",
    "Partners", "Funding", "Contact"
])

# =========================================================
# HOME
# =========================================================
if menu == "Home":
    st.title(t("Academic Portfolio","Portfolio Académique"))
    st.write(t(
        "International Geospatial Research Portfolio",
        "Portfolio international en géospatial"
    ))

# =========================================================
# RESEARCH HUB
# =========================================================
elif menu == "Research Hub":
    st.title(t("Research Hub","Hub de Recherche"))

    col1, col2, col3 = st.columns(3)
    col1.markdown("### 🌍 " + t("Earth Observation","Observation de la Terre"))
    col2.markdown("### 🤖 " + t("AI Geospatial","IA Géospatiale"))
    col3.markdown("### 👥 " + t("Population Mapping","Cartographie Population"))

# =========================================================
# PROJECTS
# =========================================================
elif menu == "Projects":
    st.title(t("Projects","Projets"))

    st.markdown("### 🚀 Geospatial Ecosystem")
    st.markdown("### 📊 Population Mapping Mali")

# =========================================================
# MONITORING (STREAMLIT EMBED)
# =========================================================
elif menu == "Monitoring":
    st.title(t("Data Collection & Monitoring","Collecte & Suivi"))

    st.markdown("### Application 1")
    st.components.v1.iframe("https://emop2026.streamlit.app", height=500)

    st.markdown("### Application 2")
    st.components.v1.iframe("https://suivirich-psifruqpdzgstwtqsocgyp.streamlit.app", height=500)

# =========================================================
# MAP (LEAFLET → FOLIUM)
# =========================================================
elif menu == "Map":
    st.title(t("Interactive Mali Map","Carte Interactive du Mali"))

    m = folium.Map(location=[17, -3], zoom_start=6)

    regions = [
        {"name":"Bamako","coords":[12.6,-7.7],
         "fr":"Bamako — Projets : 5",
         "en":"Bamako — Projects: 5"},
        {"name":"Segou","coords":[13.4,-6.5],
         "fr":"Ségou — Projets : 3",
         "en":"Segou — Projects: 3"}
    ]

    for r in regions:
        folium.Marker(
            location=r["coords"],
            popup=r["fr"] if lang=="FR" else r["en"],
            icon=folium.Icon(color="green")
        ).add_to(m)

    st_folium(m, width=1200, height=600)

# =========================================================
# SCHOLAR & ORCID
# =========================================================
elif menu == "Scholar":
    st.title("Scholar & ORCID")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Google Scholar")
        st.write("Publications: ---")
        st.write("Citations: ---")
        st.write("h-index: ---")

    with col2:
        st.markdown("### ORCID")
        st.markdown("[View ORCID Profile](https://orcid.org/0009-0003-7416-1456)")

# =========================================================
# TIMELINE
# =========================================================
elif menu == "Timeline":
    st.title(t("Research Timeline","Parcours Scientifique"))

    st.write("2025 – AI Geospatial Monitoring")
    st.write("2024 – Population Mapping")
    st.write("2023 – Satellite Monitoring")

# =========================================================
# PARTNERS
# =========================================================
elif menu == "Partners":
    st.title(t("Institutional Partners","Partenaires"))

    col1, col2, col3 = st.columns(3)
    col1.write("NASA")
    col2.write("Copernicus")
    col3.write("World Bank")

# =========================================================
# FUNDING
# =========================================================
elif menu == "Funding":
    st.title(t("Funding & Grants","Financement"))

    st.write("AI Geospatial – International Grant")
    st.write("Population Mapping – Government Funding")

# =========================================================
# CONTACT
# =========================================================
elif menu == "Contact":
    st.title("Contact")

    st.write("📧 mahamadoucamaramoc@outlook.com")
    st.markdown("[ORCID](https://orcid.org/0009-0003-7416-1456)")
    st.markdown("[ResearchGate](https://www.researchgate.net/profile/Mahamadou-Camara-2)")

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.markdown("© 2026 Dr Mahamadou CAMARA | Geospatial Intelligence Platform")
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Ajaz Ahmad Mir",
    page_icon="🎓",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home Profile", "Publications", "CV"]
)

# ================= HOME PROFILE =================
if page == "Home Profile":

    st.markdown("## Ajaz Ahmad Mir")

    col1, col2 = st.columns([1,4])

    with col1:
        st.image("profile.png.png", width=160)

    with col2:
        st.markdown("""
        **PhD Research Scholar**  
        **Specialization:** Hydraulics & Water Resources Engineering  
        **Institution:** Dr B R Ambedkar National Institute of Technology Jalandhar  

        📧 gid.ajaz@gmail.com  
        📱 +91-7006231956  

        [Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ&hl=en)  
        [ORCID](https://orcid.org/0000-0002-4164-4027)
        """)

    st.divider()

    # -------- AREAS OF INTEREST --------
    with st.expander("Areas of Interest"):
        st.markdown("""
        - Experimental Hydraulics  
        - Turbulence in Open Channel Flow  
        - Sediment Transport  
        - Steep Mountain Channels  
        - Machine Learning in Hydraulics
        """)

    # -------- HONORS & AWARDS --------
    with st.expander("Honors and Awards"):
        st.markdown("""
        - GATE Qualified (Score: 463)  
        - ANRF / SERB Overseas Visiting Fellowship  
        - PhD Fellowship – NIT Jalandhar  
        - MTech GATE Fellowship – NIT Srinagar  
        - Minority Scholarship – University of Kashmir
        """)

    # -------- PROFESSIONAL BACKGROUND --------
    with st.expander("Professional Background"):
        st.markdown("""
        **Visiting Doctoral Fellow**  
        University of Alberta, Canada  
        2024–2025

        **PhD Research Scholar**  
        NIT Jalandhar  
        2022–Present
        """)

    # -------- EDUCATION --------
    with st.expander("Educational Details"):
        st.markdown("""
        **PhD – Water Resources Engineering**  
        NIT Jalandhar (2022–Present)

        **MTech – Water Resource Engineering**  
        NIT Srinagar (2019–2021)

        **B.E – Civil Engineering**  
        University of Kashmir (2014–2019)
        """)

    # -------- JOURNAL PUBLICATIONS --------
    with st.expander("Journal Publications"):
        st.markdown("""
        **Mir AA, Patel M (2025)**  
        Optimizing bed shear stress prediction in open flow channels.  
        *Natural Hazards*

        **Mir AA et al. (2024)**  
        Comparative ensemble approach to bedload prediction.  
        *Scientific Reports*

        **Mir AA, Patel M (2024)**  
        Machine learning prediction of flow resistance in alluvial channels.  
        *Water Science & Technology*

        **Mir AA et al. (2022)**  
        Methane gas and solid waste management case study.  
        *Journal of Material Cycles & Waste Management*
        """)

    # -------- PROJECTS --------
    with st.expander("Research Projects"):
        st.markdown("""
        **SPARC Project – AI/ML Flood Prediction in Himalayan Regions**  
        Funding: ₹60 Lakhs
        """)

    # -------- BOOK CHAPTERS --------
    with st.expander("Book / Book Chapters"):
        st.markdown("""
        - Technological Developments in River Morphology – Springer Nature (2025)
        - Hydrogeological Study of Soil and Water Contamination (2025)
        """)

# ================= PUBLICATIONS PAGE =================
elif page == "Publications":

    st.title("Publications")

    publications = [
        "Mir AA, Patel M (2025). Optimizing bed shear stress prediction in open flow channels. Natural Hazards.",
        "Mir AA et al. (2024). Comparative ensemble approach to bedload prediction. Scientific Reports.",
        "Mir AA, Patel M (2024). Machine learning prediction of flow resistance in alluvial channels. Water Science & Technology.",
        "Mir AA et al. (2022). Methane gas and solid waste management case study. Journal of Material Cycles & Waste Management."
    ]

    for i, pub in enumerate(publications,1):
        st.write(f"{i}. {pub}")

# ================= CV =================
elif page == "CV":

    st.title("Curriculum Vitae")

    with open("ajaz_cv_2_page 30 dec 25.pdf","rb") as file:
        st.download_button(
            label="Download CV",
            data=file,
            file_name="Ajaz_Ahmad_Mir_CV.pdf",
            mime="application/pdf"
        )

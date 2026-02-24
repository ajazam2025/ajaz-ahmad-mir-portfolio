import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scholarly import scholarly

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Ajaz Ahmad Mir | Academic Portfolio",
    page_icon="🎓",
    layout="wide"
)

# ================= SCHOLAR FUNCTION =================
@st.cache_data(ttl=86400)
def get_scholar_data():
    try:
        author = scholarly.search_author_id("90WNMHwAAAAJ")
        author = scholarly.fill(author)
        return {
            "citations": author.get("citedby", 0),
            "hindex": author.get("hindex", 0),
            "i10index": author.get("i10index", 0),
            "publications": len(author.get("publications", [])),
        }
    except Exception:
        return None

# ================= SIDEBAR =================
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🎓 Education", "📚 Publications",
     "📊 Research Metrics", "📄 CV"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📬 Contact")
st.sidebar.markdown("📧 ajazam.ce.21@nitj.ac.in")
st.sidebar.markdown("📧 ajaz1@ualberta.ca")
st.sidebar.markdown("📧 gid.ajaz@gmail.com")
st.sidebar.markdown("📱 +91-7006231956")

st.sidebar.markdown("### 🔗 Profiles")
st.sidebar.markdown("[🎓 Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ&hl=en&oi=ao)")
st.sidebar.markdown("[🆔 ORCID](https://orcid.org/0000-0002-4164-4027)")

# ================= HOME =================
# ================= HOME =================
if page == "🏠 Home":

    # ===== COMPACT CSS =====
    st.markdown("""
    <style>
    /* Reduce top padding */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
        max-width: 1100px;
    }

    /* Typography */
    .name {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .role {
        font-size: 18px;
        color: #2aa198;
        margin-top: 0px;
        margin-bottom: 10px;
    }
    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .about-text {
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

    # ===== MAIN HERO (TIGHTER RATIO) =====
    left, right = st.columns([0.9, 2.1], gap="small")

    # ---------- LEFT ----------
    with left:
        st.image("profile.png.png", width=200)

        st.markdown(
            "<div class='name'>Ajaz Ahmad Mir</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='role'>PhD Research Scholar</div>",
            unsafe_allow_html=True,
        )

        st.markdown("""
        **University of Alberta**  
        **Dr B R Ambedkar NIT Jalandhar**
        """)

        st.markdown("📧 gid.ajaz@gmail.com")
        st.markdown("📱 +91-7006231956")

        st.markdown(
            "[🎓 Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ&hl=en&oi=ao)"
        )
        st.markdown(
            "[🆔 ORCID](https://orcid.org/0000-0002-4164-4027)"
        )

    # ---------- RIGHT ----------
    with right:

        st.markdown(
            "<div class='section-title'>About me</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class='about-text'>
            I am a Ph.D. researcher working in the field of <b>hydraulics,
            turbulence, and machine learning applications in water resources
            engineering</b>. My research focuses on open channel flow,
            sediment transport, bridge pier scour, and data-driven hydraulic
            modelling.
            </div>
            """,
            unsafe_allow_html=True,
        )

        colA, colB = st.columns(2, gap="small")

        # ----- INTERESTS -----
        with colA:
            st.markdown(
                "<div class='section-title'>Interests</div>",
                unsafe_allow_html=True,
            )
            st.markdown("""
            • Experimental Hydraulics  
            • Open Channel Flow  
            • Turbulence  
            • Machine Learning  
            • Sediment Transport  
            """)

        # ----- EDUCATION -----
        with colB:
            st.markdown(
                "<div class='section-title'>Education</div>",
                unsafe_allow_html=True,
            )
            st.markdown("""
            🎓 **PhD, Water Resources Engineering**  
            NIT Jalandhar, 2022–Present  

            🎓 **MTech, Water Resource Engineering**  
            NIT Srinagar, 2019–2021  

            🎓 **B.E. Civil Engineering**  
            University of Kashmir, 2014–2019  
            """)

    # ---------- LEFT PANEL ----------
    with left:
        st.image("profile.png.png", width=220)

        st.markdown(
            "<div class='name'>Ajaz Ahmad Mir</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='role'>PhD Research Scholar</div>",
            unsafe_allow_html=True,
        )

        st.markdown("""
        **University of Alberta**  
        **Dr B R Ambedkar NIT Jalandhar**
        """)

        st.markdown("---")

        st.markdown("📧 gid.ajaz@gmail.com")
        st.markdown("📱 +91-7006231956")

        st.markdown(
            "[🎓 Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ&hl=en&oi=ao)"
        )
        st.markdown(
            "[🆔 ORCID](https://orcid.org/0000-0002-4164-4027)"
        )

    # ---------- RIGHT PANEL ----------
    with right:

        st.markdown(
            "<div class='section-title'>About me</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class='about-text'>
            I am a Ph.D. researcher working in the field of <b>hydraulics,
            turbulence, and machine learning applications in water resources
            engineering</b>. My research focuses on open channel flow,
            sediment transport, bridge pier scour, and data-driven hydraulic
            modelling.
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ===== INTERESTS + EDUCATION SIDE BY SIDE =====
        colA, colB = st.columns(2)

        # ----- INTERESTS -----
        with colA:
            st.markdown(
                "<div class='section-title'>Interests</div>",
                unsafe_allow_html=True,
            )
            st.markdown("""
            • Experimental Hydraulics  
            • Open Channel Flow  
            • Turbulence  
            • Machine Learning  
            • Sediment Transport  
            """)

        # ----- EDUCATION -----
        with colB:
            st.markdown(
                "<div class='section-title'>Education</div>",
                unsafe_allow_html=True,
            )
            st.markdown("""
            🎓 **PhD, Water Resources Engineering**  
            NIT Jalandhar, 2022–Present  

            🎓 **MTech, Water Resource Engineering**  
            NIT Srinagar, 2019–2021  

            🎓 **B.E. Civil Engineering**  
            University of Kashmir, 2014–2019  
            """)

    # ===== LIVE METRICS =====
    st.subheader("📈 Academic Snapshot")

    scholar_data = get_scholar_data()
    m1, m2, m3, m4 = st.columns(4)

    if scholar_data:
        m1.metric("Publications", scholar_data["publications"])
        m2.metric("Citations", scholar_data["citations"])
        m3.metric("h-index", scholar_data["hindex"])
        m4.metric("i10-index", scholar_data["i10index"])
    else:
        m1.metric("Publications", "—")
        m2.metric("Citations", "—")
        m3.metric("h-index", "—")
        m4.metric("i10-index", "—")

    st.success("✅ Open to Postdoctoral Positions and Research Collaborations")

    # ===== FEATURED PUBLICATIONS =====
    st.markdown("---")
    st.header("⭐ Featured Publications")

    st.markdown("""
**Ajaz Ahmad Mir, Mahesh Patel (2025).**  
Optimizing bed shear stress prediction in open flow channels: an investigation of heuristic machine learning techniques.  
*Natural Hazards*, SCI (IF 4.0)

**Ajaz Ahmad Mir, Mahesh Patel, Fahad Albalawi, Mohit Bajaj, Milkias Berhanu Tuka (2024).**  
A comparative ensemble approach to bedload prediction using metaheuristic machine learning.  
*Scientific Reports*, SCI (IF 4.3)

**Ajaz Ahmad Mir, Mahesh Patel (2024).**  
Machine learning approaches for adequate prediction of flow resistance in alluvial channels with bedforms.  
*Water Science and Technology*, SCIE (IF 2.7)
""")

    st.info("📚 See full list in the Publications tab.")

    st.markdown("---")

    # ===== PATENT =====
    st.header("🧪 Patent & Industrial Design")
    st.markdown("""
**Next-Gen Hydraulic Lab Trolley with Precision Control and Instrument Integration**  
Design No.: 475322-001, Class: 10-04  
Registered with the Patent Office, Government of India  
Date of Registration: 29 September 2025  
Date of Issue: 24 December 2025  

**Co-inventors:** Shakeel Ahmad Rather, Mahesh Patel,  
Satyender Singh, Shailza Sharma  

**Institutional Collaboration:**  
Dr B R Ambedkar National Institute of Technology Jalandhar and ADK Instruments
""")

    # ===== PROJECT =====
    st.header("🚀 Projects Assisted")
    st.markdown("""
**SPARC, MHRD, Govt. of India**  
AI/ML-driven flood prediction and hazard mapping in Himalayan regions  
**Funding:** ₹60 Lakhs
""")

    # ===== POSTERS =====
    st.header("🖼 Poster Presentations")
    st.markdown("""
• University of Alberta (2025): Water Quality Index using PCA + hybrid ML  
• CSCE, University of Alberta (2025): Sediment transport modelling using experimental + ensemble ML
""")

    # ===== CONFERENCES =====
    st.header("🎤 Conferences & Workshops")
    st.markdown("""
• IAHR-APD, IIT Madras (2022)  
• IAHR Young Professionals Congress (2022)  
• Hydraulics Measurement Techniques — NIT Rourkela (2024)  
• Urban Water Management — GNDEC Ludhiana (2023)  
• Machine Learning with Python — NIT Jalandhar (2022)
""")

    # ===== BOOK CHAPTERS =====
    st.header("📖 Book Chapters")
    st.markdown("""
• Springer Nature (2025): Technological developments in river morphology  
• Geoenvironmental Engineering (2025): Hydrogeological study of soil and water contamination
""")

    # ===== ACHIEVEMENTS =====
    st.header("🏆 Achievements & Fellowships")
    st.markdown("""
• GATE Qualified (2019) — Score: 463  
• ANRF / SERB Overseas Visiting Fellowship — $2000/month  
• PhD Fellowship — NIT Jalandhar (₹42,000/month)  
• MTech GATE Fellowship — NIT Srinagar (₹12,400/month)  
• Minority Scholarship — University of Kashmir (4 years)  
• Session Chair — ICIDEAIA-2025 (Human-centered AI)
""")

    # ===== SKILLS =====
    st.header("🛠 Skills")
    st.markdown("""
**Technical:** Machine Learning, Experimental Hydraulics, ANSYS, MATLAB, WaterGems  
**Programming:** Python, MATLAB  
**Soft Skills:** Teaching, Project Writing, Team Work
""")

# ================= EDUCATION =================
elif page == "🎓 Education":

    st.title("🎓 Education")
    st.markdown("""
**University of Alberta, Canada**  
Overseas Visiting Doctoral Fellow (ANRF/OVDF)  
*Sept 2024 – Aug 2025*

**Dr B R Ambedkar NIT Jalandhar, India**  
Ph.D. Water Resources Engineering  
*2022 – Ongoing*
""")

# ================= PUBLICATIONS =================
elif page == "📚 Publications":

    st.title("📚 Publications")

    st.markdown("""
• **Ajaz Ahmad Mir, Mahesh Patel.** Optimizing bed shear stress prediction in open flow channels. *Natural Hazards*, 2025.

• **Ajaz Ahmad Mir et al.** Comparative ensemble approach to bedload prediction. *Scientific Reports*, 2024.
""")

# ================= RESEARCH METRICS =================
elif page == "📊 Research Metrics":

    st.title("📊 Research Metrics")

    data = {
        "Year": ["2022", "2023", "2024", "2025"],
        "Publications": [2, 3, 4, 1],
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.bar(df["Year"], df["Publications"])
    st.pyplot(fig)

# ================= CV =================
elif page == "📄 CV":

    st.title("📄 Curriculum Vitae")

    try:
        with open("cv AJAZ AHMAD MIR.pdf", "rb") as file:
            st.download_button(
                label="⬇️ Download Full CV",
                data=file,
                file_name="Ajaz_Ahmad_Mir_CV.pdf",
                mime="application/pdf",
            )
    except:
        st.warning("Please upload your CV PDF to the repository.")

# ================= FOOTER =================
st.markdown("---")
st.caption("© 2026 Ajaz Ahmad Mir | Elite Academic Portfolio")

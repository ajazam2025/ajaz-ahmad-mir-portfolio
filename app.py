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
st.sidebar.markdown(
    "[🎓 Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ&hl=en&oi=ao)"
)
st.sidebar.markdown(
    "[🆔 ORCID](https://orcid.org/0000-0002-4164-4027)"
)

# ================= HOME =================
if page == "🏠 Home":

    col1, col2 = st.columns([1, 3])

    with col1:
        try:
            st.image("profile.jpg", width=220)
        except:
            st.image("https://via.placeholder.com/220")

    with col2:
        st.title("Ajaz Ahmad Mir")
        st.subheader("Ph.D. Research Scholar | Hydraulics & Machine Learning")

        st.write(
            """
            Visiting Doctoral Fellow at **University of Alberta** and
            Ph.D. scholar at **Dr B R Ambedkar NIT Jalandhar**.
            Research focuses on hydraulics, turbulence, sediment transport,
            and machine learning applications in water resources engineering.
            """
        )

    st.markdown("---")

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

**NIT Srinagar, India**  
M.Tech Water Resource Engineering — CGPA: 7.23  
*2019 – 2021*

**University of Kashmir, India**  
B.E. Civil Engineering — 76.6%  
*2014 – 2019*
""")

# ================= PUBLICATIONS =================
elif page == "📚 Publications":

    st.title("📚 Publications")

    st.markdown("""
• **Ajaz Ahmad Mir, Mahesh Patel.** Optimizing bed shear stress prediction in open flow channels: an investigation of heuristic machine learning techniques. *Natural Hazards*, SCI (IF 4.0) Q1, 2025.

• **Ajaz Ahmad Mir, Mahesh Patel, Fahad Albalawi, Mohit Bajaj, Milkias Berhanu Tuka.** A comparative ensemble approach to bedload prediction using metaheuristic machine learning. *Scientific Reports*, SCI (IF 4.3) Q1, 2024.

• **Ajaz Ahmad Mir, Mahesh Patel.** Machine learning approaches for adequate prediction of flow resistance in alluvial channels with bedforms. *Water Science and Technology*, SCIE (IF 2.7) Q2, 2024.

• **Ajaz Ahmad Mir, Mahesh Patel.** A comprehensive review on sediment transport, flow dynamics, and hazards in steep channels. *Journal of Water Management Modeling*, ESCI, Q3,2024.

• **Ajaz Ahmad Mir, Jasir Mushtaq, Abdul Qayoom Dar, Mahesh Patel.** A quantitative investigation of methane gas and solid waste management in mountainous Srinagar city — A case study. *Journal of Material Cycles and Waste Management*, SCI (IF 3.2) Q2, 2022.

• **Akshita Bassi, Ajaz Ahmad Mir, Bimlesh Kumar, Mahesh Patel.** A comprehensive study of various regressions and deep learning approaches for prediction of friction factor in mobile bed channels. *Journal of Hydroinformatics*, SCI (IF 2.7) Q2, 2023.

• **Rahul Kumar, Ayush Rathore, Rajwinder Singh, Ajaz Ahmad Mir, Rupesh Kumar Tipu, Mahesh Patel.** Prognosis of flow of fly ash and blast furnace slag-based concrete: leveraging advanced machine learning algorithms. *Asian Journal of Civil Engineering*, SCOPUS, 2023.

• **Rajwinder Singh, Rupesh Kumar Tipu, Ajaz Ahmad Mir, Mahesh Patel.** Predictive modelling of flexural strength in recycled aggregate-based concrete: machine learning and global sensitivity analysis. *Iranian Journal of Science and Technology*, SCI (IF 1.6), 2024.
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
    ax.set_xlabel("Year")
    ax.set_ylabel("Publications")
    ax.set_title("Research Productivity")
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

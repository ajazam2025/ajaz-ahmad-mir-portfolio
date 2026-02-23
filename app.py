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
@st.cache_data(ttl=86400)  # cache for 24 hours
def get_scholar_data():
    try:
        author = scholarly.search_author_id("90WNMHwAAAAJ")
        author = scholarly.fill(author)

        data = {
            "name": author.get("name", ""),
            "citations": author.get("citedby", 0),
            "hindex": author.get("hindex", 0),
            "i10index": author.get("i10index", 0),
            "publications": len(author.get("publications", [])),
        }
        return data
    except Exception:
        return None

# ================= SIDEBAR NAVIGATION =================
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🎓 Education", "📚 Publications",
     "📊 Research Metrics", "🛠 Skills", "📄 CV"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**📧 gid.ajaz@gmail.com**")
st.sidebar.markdown("📱 +91-7006231956")
st.sidebar.markdown(
    "[🎓 Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ&hl=en&oi=ao)"
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
        st.subheader("Ph.D. Research Scholar | Hydraulics & ML")

        st.write(
            """
            Visiting Doctoral Fellow at **University of Alberta** and
            Ph.D. scholar at **Dr B R Ambedkar NIT Jalandhar**.
            Research focuses on hydraulics, turbulence, and
            machine learning applications in water resources engineering.
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
        st.warning("Google Scholar data temporarily unavailable.")

    st.success("✅ Open to Postdoctoral Positions and Research Collaborations")

# ================= EDUCATION =================
elif page == "🎓 Education":

    st.title("🎓 Education")

    st.markdown("""
    **University of Alberta, Canada**  
    Overseas Visiting Doctoral Fellow (ANRF/OVDF)  
    *Sept 2024 – Aug 2025*

    **NIT Jalandhar, India**  
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

    pubs_data = [
        [2025, "Natural Hazards", "Bed shear stress prediction using ML", 1, "Q1"],
        [2024, "Scientific Reports", "Ensemble bedload prediction", 8, "Q1"],
        [2023, "Water Science & Technology", "Flow resistance prediction", 20, "Q2"],
        [2023, "Journal of Hydroinformatics", "Friction factor ML", 27, "Q2"],
        [2024, "Asian Journal of Civil Engineering", "Fly ash concrete ML", 28, "Q2"],
        [2025, "Iranian JST", "Flexural strength prediction", 34, "Q2"],
        [2023, "Materials Today Proceedings", "3D printing construction review", 107, "Q1"],
        [2022, "J. Material Cycles & Waste Mgmt", "Methane waste case study", 20, "Q2"],
        [2024, "Journal of Water Management Modeling", "Steep channel review", 19, "Q3"],
        [2022, "Pharma Innovation Journal", "Hydroponics sustainability", 15, "NA"],
    ]

    df_pubs = pd.DataFrame(
        pubs_data,
        columns=["Year", "Journal", "Title", "Citations", "Quartile"]
    )

    st.dataframe(df_pubs, use_container_width=True)

# ================= RESEARCH METRICS =================
elif page == "📊 Research Metrics":

    st.title("📊 Research Metrics")

    # Publications per year
    data = {
        "Year": ["2022", "2023", "2024", "2025"],
        "Publications": [2, 3, 4, 1],
    }
    df = pd.DataFrame(data)

    st.subheader("📈 Publications by Year")

    fig, ax = plt.subplots()
    ax.bar(df["Year"], df["Publications"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Publications")
    ax.set_title("Research Productivity")
    st.pyplot(fig)

    # Citation distribution
    st.subheader("📊 Citation Impact by Paper")

    citation_data = {
        "Paper": [
            "3D Printing Review",
            "Flexural Strength ML",
            "Fly Ash Concrete",
            "Friction Factor ML",
            "Flow Resistance",
            "Waste Management",
            "Steep Channel Review",
            "Hydroponics",
            "Bedload Prediction",
            "Bed Shear Stress",
        ],
        "Citations": [107, 34, 28, 27, 20, 20, 19, 15, 8, 1],
    }

    df_cit = pd.DataFrame(citation_data)

    fig2, ax2 = plt.subplots()
    ax2.barh(df_cit["Paper"], df_cit["Citations"])
    ax2.set_xlabel("Citations")
    ax2.set_title("Citation Impact by Publication")
    st.pyplot(fig2)

# ================= SKILLS =================
elif page == "🛠 Skills":

    st.title("🛠 Skills")

    st.subheader("Technical")
    st.write("Machine Learning, Hydraulics, ANSYS, MATLAB, WaterGems")

    st.subheader("Programming")
    st.write("Python, MATLAB")

    st.subheader("Soft Skills")
    st.write("Teaching, Project Writing, Team Work")

# ================= CV =================
elif page == "📄 CV":

    st.title("📄 Curriculum Vitae")

    try:
        with open("Ajaz_Ahmad_Mir_CV.pdf", "rb") as file:
            st.download_button(
                label="⬇️ Download Full CV",
                data=file,
                file_name="Ajaz_Ahmad_Mir_CV.pdf",
                mime="application/pdf",
            )
    except:
        st.warning("Please upload Ajaz_Ahmad_Mir_CV.pdf to repository.")

# ================= FOOTER =================
st.markdown("---")
st.caption("© 2026 Ajaz Ahmad Mir | Elite Academic Portfolio")

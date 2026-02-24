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

# ================= SIDEBAR =================
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🎓 Education", "📚 Publications",
     "📊 Research Metrics", "🛠 Skills", "📄 CV"]
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
        st.warning("Google Scholar data temporarily unavailable.")

    st.success("✅ Open to Postdoctoral Positions and Research Collaborations")

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

    refs = [
        "Mir AA, Mushtaq J, Dar AQ, Patel M (2023) A quantitative investigation of methane gas and solid waste management in mountainous Srinagar city—A case study. Journal of Material Cycles and Waste Management. https://doi.org/10.1007/s10163-022-01516-4",

        "Mir AA, Patel M (2024a) Machine learning approaches for adequate prediction of flow resistance in alluvial channels with bedforms. Water Science and Technology 89:290–318. https://doi.org/10.2166/wst.2023.396",

        "Mir AA, Patel M (2024b) A Comprehensive Review on Sediment Transport, Flow Dynamics, and Hazards in Steep Channels. Journal of Water Management Modeling 32:1–52. https://doi.org/10.14796/JWMM.C517",

        "Mir AA, Patel M (2023) Research possibilities into the dynamics and bed morphology of steep mountain channels. Proceedings of the 3rd IAHR Young Professionals Congress. pp 116–117",

        "Mir AA, Patel M (2025) Optimizing bed shear stress prediction in open flow channels: an investigation of heuristic machine learning techniques. Natural Hazards. https://doi.org/10.1007/S11069-025-07154-X",

        "Mir AA, Patel M, Albalawi F, et al (2024) A comparative ensemble approach to bedload prediction using metaheuristic machine learning. Scientific Reports 14:25725. https://doi.org/10.1038/S41598-024-75118-5",

        "Bassi A, Mir AA, Kumar B, Patel M (2023) A comprehensive study of various regressions and deep learning approaches for the prediction of friction factor in mobile bed channels. Journal of Hydroinformatics 25:2500–2521. https://doi.org/10.2166/HYDRO.2023.246",

        "Patel M, Ahmad Mir A, Kumar B (2022) A critical review on flow over fluvial bed forms and research directions. Proceedings of the 23rd IAHR-APD Congress 2022, IIT Madras, India",

        "Rather SA, Mir AA, Kapoor K, Patel M (2025) Assessment of technological developments in river morphology analysis: A comprehensive review. Lecture Notes in Civil Engineering 560:101–116. https://doi.org/10.1007/978-981-97-8895-8_7",

        "Sankalp M, Gondwal A, Agnihotri AK, et al (2024) Hydrogeological study of contamination of soil and water in the vicinity of municipal dumping ground: A case study. Lecture Notes in Civil Engineering 508:219–235. https://doi.org/10.1007/978-981-97-3823-6_19",

        "Singh R, Tipu RK, Mir AA, Patel M (2024) Predictive modelling of flexural strength in recycled aggregate-based concrete. Iranian Journal of Science and Technology. https://doi.org/10.1007/S40996-024-01502-W",

        "Kumar R, Rathore A, Singh R, et al (2024) Prognosis of flow of fly ash and blast furnace slag-based concrete. Asian Journal of Civil Engineering 25:2483–2497. https://doi.org/10.1007/s42107-023-00922-9",
    ]

    for i, ref in enumerate(refs, 1):
        st.markdown(f"**{i}.** {ref}")

# ================= RESEARCH METRICS =================
elif page == "📊 Research Metrics":

    st.title("📊 Research Metrics")

    # Publications per year chart
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

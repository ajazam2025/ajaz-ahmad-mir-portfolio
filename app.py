import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Ajaz Ahmad Mir | Academic Portfolio",
    page_icon="🎓",
    layout="wide"
)

# ================= SIDEBAR NAVIGATION =================
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🎓 Education", "📚 Publications",
     "📊 Research Metrics", "🛠 Skills", "📄 CV"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**📧 gid.ajaz@gmail.com**")
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
        st.subheader("Ph.D. Research Scholar | Hydraulic & ML Research")

        st.write(
            """
            Visiting Doctoral Fellow at **University of Alberta** and
            Ph.D. scholar at **Dr B R Ambedkar NIT Jalandhar**.
            Research focuses on hydraulics, turbulence, and
            machine learning applications in water resources engineering.
            """
        )

    st.markdown("---")

    # ===== QUICK METRICS =====
    st.subheader("📈 Academic Snapshot")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Publications", "8")
    m2.metric("Book Chapters", "2")
    m3.metric("Patent", "1")
    m4.metric("GATE Score", "463")

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

    pubs = [
        "Natural Hazards (2025) — Bed shear stress prediction using ML",
        "Scientific Reports (2024) — Ensemble bedload prediction",
        "Water Science & Technology (2024) — Flow resistance ML",
        "JWMM (2024) — Review on sediment transport",
        "JMCWM (2022) — Waste management case study",
        "Journal of Hydroinformatics (2023) — Friction factor ML",
        "Asian Journal of Civil Engineering (2023) — Concrete ML",
        "Iranian JST (2024) — Flexural strength prediction",
    ]

    for p in pubs:
        st.markdown(f"• {p}")

# ================= RESEARCH METRICS =================
elif page == "📊 Research Metrics":

    st.title("📊 Research Metrics")

    # Sample research data
    data = {
        "Year": ["2022", "2023", "2024", "2025"],
        "Publications": [1, 3, 3, 1],
    }

    df = pd.DataFrame(data)

    st.subheader("📈 Publications by Year")

    fig, ax = plt.subplots()
    ax.bar(df["Year"], df["Publications"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Publications")
    ax.set_title("Research Productivity")

    st.pyplot(fig)

    st.info("Tip: Connect Google Scholar API later for live metrics.")

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
st.caption("© 2026 Ajaz Ahmad Mir | Premium Academic Portfolio")

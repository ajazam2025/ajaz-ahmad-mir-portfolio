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

    # ===== COMPACT CSS =====
    st.markdown("""
    <style>
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 1rem;
        max-width: 1050px;
    }
    .name {
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .role {
        font-size: 18px;
        color: #2aa198;
        margin-top: 0px;
        margin-bottom: 8px;
    }
    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 8px;
        margin-bottom: 4px;
    }
    .about-text {
        font-size: 15.5px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

    # ===== HERO =====
    left, right = st.columns([1, 2], gap="small")

    # ---------- LEFT ----------
    with left:
        st.image("profile.png.png", width=190)

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
            sediment transport, and data-driven hydraulic modelling in
            steep mountain channels. I was also SERB/ANRF OVDF fellow
            at University of Alberta, Canada.
            </div>
            """,
            unsafe_allow_html=True,
        )

        colA, colB = st.columns(2, gap="small")

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
            • Bedforms  
            • Roughness in steep channels  
            """)

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

    # ===== METRICS =====
    st.markdown("---")
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

import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Ajaz Ahmad Mir",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:700;
    color:white;
}

.header-box{
    background: linear-gradient(90deg,#2c7be5,#00bcd4);
    padding:20px;
    border-radius:10px;
}

.profile-card{
    background:#f5f7fa;
    padding:20px;
    border-radius:10px;
}

.section-title{
    font-size:22px;
    font-weight:600;
}

.stExpander{
    background:#e8f0fe;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    """
<div class="header-box">
<div class="main-title">Ajaz Ahmad Mir</div>
PhD Research Scholar – Hydraulics & Water Resources Engineering
</div>
""",
    unsafe_allow_html=True
)

st.write("")

# ---------------- PROFILE SECTION ----------------
col1, col2 = st.columns([1,3])

with col1:
    st.image("profile.png.png", width=200)

with col2:
    st.markdown(
        """
<div class="profile-card">

**Institution:** Dr B R Ambedkar National Institute of Technology Jalandhar  

📧 gid.ajaz@gmail.com  
📱 +91-7006231956  

🔗 [Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ)  
🆔 [ORCID](https://orcid.org/0000-0002-4164-4027)

</div>
""",
        unsafe_allow_html=True
    )

st.write("")

# ---------------- ACCORDION SECTIONS ----------------

with st.expander("🔬 Areas of Interest"):
    st.write("""
• Experimental Hydraulics  
• Turbulence in Open Channel Flow  
• Sediment Transport  
• Machine Learning in Hydraulics  
• Steep Mountain Channels
""")

with st.expander("🏆 Honors and Awards"):
    st.write("""
• GATE Qualified (Score 463)  
• ANRF / SERB Overseas Visiting Fellowship  
• PhD Fellowship – NIT Jalandhar  
• MTech GATE Fellowship – NIT Srinagar
""")

with st.expander("🎓 Educational Details"):
    st.write("""
**PhD – Water Resources Engineering**  
NIT Jalandhar (2022–Present)

**MTech – Water Resource Engineering**  
NIT Srinagar (2019–2021)

**B.E – Civil Engineering**  
University of Kashmir (2014–2019)
""")

with st.expander("📚 Journal Publications"):
    st.write("""
1. Mir AA, Patel M (2025) Optimizing bed shear stress prediction in open flow channels. *Natural Hazards*

2. Mir AA et al. (2024) Comparative ensemble approach to bedload prediction. *Scientific Reports*

3. Mir AA, Patel M (2024) Machine learning prediction of flow resistance in alluvial channels. *Water Science & Technology*

4. Mir AA et al. (2022) Methane gas and solid waste management case study. *Journal of Material Cycles & Waste Management*
""")

with st.expander("🚀 Research Projects"):
    st.write("""
**SPARC Project – AI/ML Flood Prediction in Himalayan Regions**

Funding: ₹60 Lakhs
""")

with st.expander("📖 Book Chapters"):
    st.write("""
• Technological Developments in River Morphology – Springer Nature (2025)  
• Hydrogeological Study of Soil and Water Contamination (2025)
""")

# ---------------- CV DOWNLOAD ----------------
st.write("")
st.subheader("📄 Curriculum Vitae")

with open("ajaz_cv_2_page 30 dec 25.pdf","rb") as file:
    st.download_button(
        label="⬇ Download CV",
        data=file,
        file_name="Ajaz_Ahmad_Mir_CV.pdf",
        mime="application/pdf"
    )

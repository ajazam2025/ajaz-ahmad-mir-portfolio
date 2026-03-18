import streamlit as st

st.set_page_config(page_title="Ajaz Ahmad Mir", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.header{
background:linear-gradient(90deg,#1e3c72,#2a5298);
padding:25px;
border-radius:10px;
color:white;
}
.section{
background:#f4f6fb;
padding:15px;
border-radius:8px;
margin-bottom:15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class='header'>
<h1>Ajaz Ahmad Mir</h1>
PhD Research Scholar — Water Resources Engineering (OVDF fellow at University of Alberta, Canada)
</div>
""", unsafe_allow_html=True)

col1,col2 = st.columns([1,3])

with col1:
    st.image("profile.png.png", width=200)

with col2:

    st.markdown("""
**Institution:** Dr B R Ambedkar National Institute of Technology Jalandhar  


📧 ajazam.ce.21@nitj.ac.in   

🔗 [Google Scholar](https://scholar.google.ca/citations?user=90WNMHwAAAAJ)  
🔗 [LinkedIn](https://www.linkedin.com/in/ajaz-mir-40342b1a8/)  

🆔 ORCID: 0000-0002-4164-4027  

Scopus Author ID: 57219854867  
""")

# ---------------- BIOGRAPHY ----------------
st.subheader("👤 Biography")

st.markdown("""
<div class='section'>

I am a dedicated and passionate research scholar currently pursuing my **Ph.D. in Water Resource Engineering at the National Institute of Technology (NIT) Jalandhar**. My research focuses on **experimental hydraulics, sediment transport, bedform dynamics, steep mountain channels, and machine learning applications in hydraulic engineering**.

My work aims to advance understanding of **flow dynamics, turbulence, and sediment processes in steep channels**, while integrating **data-driven approaches and machine learning techniques** for improved prediction of hydraulic phenomena.

</div>
""", unsafe_allow_html=True)

# ---------------- AREAS OF INTEREST ----------------
st.subheader("🔬 Areas of Interest")

st.markdown("""
<div class='section'>

• Experimental Hydraulics  
• Sediment Transport  
• Steep Channels  
• Bedform Dynamics  
• Machine Learning in Hydraulics
• Advanced CFD
• Interdisplinary  


</div>
""", unsafe_allow_html=True)

# ---------------- OVDF FELLOWSHIP ----------------
st.subheader("🌍 Overseas Visiting Doctoral Fellowship")

st.markdown("""
<div class='section'>

**Overseas Visiting Doctoral Fellow (OVDF)**  
University of Alberta, Canada  

Funded by **Science and Engineering Research Board (SERB / ANRF)**  
Duration: Sept 2024 – Aug 2025  

Research collaboration on hydraulics, turbulence, and sediment transport modelling.

</div>
""", unsafe_allow_html=True)

# ---------------- PROFESSIONAL BACKGROUND ----------------
with st.expander("Professional Background"):
    st.write("""
Research Scholar — NIT Jalandhar (2022–Present)

Visiting Scholar — University of Alberta, Canada (2024–2025)
""")

# ---------------- EDUCATION ----------------
with st.expander("Educational Details"):
    st.write("""
MTech – Water Resource Engineering  
NIT Srinagar (2019–2021)

BE – Civil Engineering  
University of Kashmir (2014–2019)
""")

# ---------------- PUBLICATIONS ----------------
with st.expander("Journal Publications"):

    st.write("""
Mir, A. A., & Patel, M. (2025). Optimizing bed shear stress prediction in open flow channels. Natural Hazards.

Mir, A. A., et al. (2024). A comparative ensemble approach to bedload prediction using metaheuristic machine learning. Scientific Reports.

Mir, A. A., & Patel, M. (2024). Machine learning approaches for adequate prediction of flow resistance in alluvial channels. Water Science & Technology.

Bassi, A., Mir, A. A., et al. (2023). Prediction of friction factor in mobile bed channels. Journal of Hydroinformatics.

Tabassum, T., & Mir, A. A. (2023). 3D printing technology for sustainable construction. Materials Today: Proceedings.

Mir, A. A., et al. (2023). Methane gas and solid waste management in mountainous Srinagar city. Journal of Material Cycles and Waste Management.

Kumar, R., et al. (2024). Machine learning modelling of fly ash and slag concrete. Asian Journal of Civil Engineering.
""")

# ---------------- REVIEW ACTIVITY ----------------
with st.expander("Peer Review Activity"):
    st.write("""
Reviewer for:

• Physics of Fluids  
• Results in Engineering  
• Cold Regions Science and Technology  
• Biomass Conversion and Biorefinery  
• Additive Manufacturing
""")

# ---------------- CV DOWNLOAD ----------------
st.subheader("📄 Curriculum Vitae")

with open("ajaz_cv_2_page 30 dec 25.pdf","rb") as file:
    st.download_button(
        label="Download CV",
        data=file,
        file_name="Ajaz_Ahmad_Mir_CV.pdf",
        mime="application/pdf"
    )

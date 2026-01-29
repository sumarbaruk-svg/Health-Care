import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Pearl PharmMed Healthcare",
    page_icon="💊",
    layout="wide"
)

# --- CSS STYLING (Background Fade, Card Boxes & Light Buttons) ---
st.markdown(
    """
    <style>
    /* 1. RESTORING Main Background Image with FADE Effect */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), 
                    url("https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80&w=2070&auto=format&fit=crop");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* 2. Styling the Separate Boxes (Containers) */
    div[data-testid="stBorderContainer"] {
        background-color: #ffffff; 
        border: 1px solid #cccccc; 
        border-radius: 15px;       
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); 
        padding: 20px;
        margin-bottom: 25px; 
    }

    /* 3. Text Clarity Settings */
    h1, h2, h3, h4, h5, h6, p, li, div, span {
        color: #000000 !important; 
    }
    
    p, li {
        font-weight: 500; 
        font-size: 1.1rem;
    }

    /* 4. LIGHT COLORED BUTTONS (New Addition) */
    div.stDownloadButton > button {
        background-color: #f0f8ff !important; /* AliceBlue - Very Light Blue */
        color: #2c3e50 !important;           
        border: 1px solid #d1e8ff !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.3s ease !important;
        font-weight: 600 !important;
        width: 100% !important;
    }

    /* Hover effect for buttons */
    div.stDownloadButton > button:hover {
        background-color: #e1f0ff !important; 
        border-color: #007bff !important;
        color: #007bff !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Main Title Section (Chromium/Silver Gradient)
# This stays outside the boxes to look like a main header
st.markdown("""
    <h1 style='
        text-align: center;
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(to bottom, #bcc6cc 0%, #2c3e50 50%, #000000 51%, #bcc6cc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.5);
        margin-bottom: 30px;
        padding-top: 10px;
    '>
    Pearl PharmMed Healthcare
    </h1>
""", unsafe_allow_html=True)

# --- NEW WELCOME SECTION (Plain Text Only) ---
st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="color: #2c3e50 !important; margin-bottom: 5px;">Welcome to Pearl PharmMed Healthcare Consulting Pvt. Ltd</h2>
        <h4 style="color: #2c3e50 !important; margin-bottom: 15px;">Empowering Healthcare Through Innovation, Integrity & Global Reach</h4>
        <p style="color: #000000 !important; font-size: 1.15rem; line-height: 1.6; max-width: 1000px; margin: 0 auto;">
            At Pearl PharmMed Healthcare Consulting Pvt. Ltd, we are committed to advancing healthcare access and excellence 
            by delivering high-quality pharmaceutical and medical solutions across the globe. With a robust infrastructure 
            and a visionary approach, we operate at the intersection of science, service, and sustainability.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- HOME SECTION (RE-CLEANED) ---
with st.container(border=True):
    st.subheader("Transforming Pharma Graduates Into Industry-Ready Professionals")

    st.write("Clinical Research | Pharmacovigilance | Medical Writing | Medical Device Regulation | Internship & Training")

    st.markdown("---")

    # Intha columns-kulla thaan unga vision/mission irukku
    col1, col2 = st.columns(2)
    with col1:
        st.header("Our Vision")
        st.info("To empower pharmacy and life science graduates with globally recognized professional skills, industry knowledge, and practical experience to build meaningful careers in the healthcare ecosystem..")
    with col2:
        st.header("Our Mission")
        st.success("To bridge the skill gap between academia and industry by delivering high-quality, industry-focused training aligned with current global regulatory standards, while supporting organizations with compliant research, reporting, and regulatory solutions. We are committed to developing workforce-ready professionals in clinical research and pharmacovigilance equipped with practical skills, regulatory knowledge, and real-world industry exposure.")

# 4. ABOUT US SECTION (Inside a Separate Box)
with st.container(border=True):
    st.title("ABOUT PEARL PHARMMED HEALTHCARE CONSULTING PVT LTD.")
    st.markdown("### Empowering Future Pharma, Lifesciences, & Healthcare Leaders")
    st.write("### Who We Are")
    st.write("Pearl PharmMed Healthcare Consulting Pvt. Ltd. is a professional healthcare consulting and training organization committed to bridging the gap between academic learning and real-world pharmaceutical and healthcare industry expectations. We serve as a trusted partner for institutions, graduates, and professionals by delivering industry-relevant knowledge, practical skills, and regulatory expertise.")
    st.write("We specialize in Clinical Research and Clinical Trials, Pharmacovigilance and Drug Safety Operations, Medical and Regulatory Writing, Medical Coding, Medical Device Compliance, Post-Market Surveillance, and Regulatory Affairs. Our services are designed to align with global healthcare standards and evolving industry requirements.")
    st.write("Backed by a team of highly experienced industry experts, researchers, and regulatory professionals, we emphasize hands-on training, project-based learning, and real-time industry exposure. Through structured learning pathways and practical engagement, we empower healthcare and life science graduates and professionals to become future-ready and succeed in national and international pharmaceutical and healthcare careers.")
    st.markdown("---")
    st.subheader("WHY CHOOSE PEARL PHARMMED HEALTHCARE?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("✅ **Industry-recognized** and job-focused training")
        st.write("✅ **Experienced faculty** with CRO and pharma background")
        st.write("✅ **Real-time data**, tools, and documentation exposure")
    with col2:
        st.write("✅ **Placement assistance** and career guidance")
        st.write("✅ **Strong collaboration** with healthcare and life sciences ecosystem")

# 5. SERVICES SECTION (Inside a Separate Box)
with st.container(border=True):
    st.title("Our Services")
    
    # Tabs inside the box
    tab1, tab2 = st.tabs(["INDUSTRY EXPERTISE", "🌐 Our Core Business Verticals"])

    with tab1:
        st.header("INDUSTRY EXPERTISE")
        st.write("We offer professional services and training in :")
        st.markdown("""
        • **Clinical Trials & Research Support**
                    
        • **Medical Writing & Regulatory Documentation**
                    
        • **Pharmacovigilance & Drug Safety Monitoring**
                    
        • **Medical Device Reporting & Compliance (MDR, PMS, PMSR, PMCFER,CER)**

        • **Good Clinical Practice (GCP), Good Documentation Practice (GDP), and Regulatory Standards**
                    
        • **Good Manufacturing Practices (GMP)**
                    
        • **Good Laboratory Practices (GLP)**
        """)

    with tab2:
        # பாக்ஸ் வேண்டாம்னு சொன்னதுனால நேரடியா காலம்களை பிரிக்கிறோம்
        st.subheader("🌐 Our Core Business Verticals")
        st.write("---") # ஒரு சின்ன கோடு நீட்டா இருக்கும்
        
        # 5 பிரிவுகளாக பிரிக்கிறோம்
        c1, c2, c3, c4, c5 = st.columns(5)
        
        with c1:
            st.subheader("💊 Pharmaceutical Trade & Distribution")
            st.markdown("**We specialize in the wholesale, retail, import, export, stocking, and marketing of :**")
            st.markdown("""
            • Prescription and over-the-counter medicines
                        
            • Generic and patented drugs
                        
            • Formulations, vaccines, and APIs
                        
            • Bulk chemicals and allied healthcare products
            """)
            st.write("**Our extensive distribution network ensures timely and compliant delivery across domestic and international markets.**")


        with c2:
            st.subheader("🏥 Medical & Surgical Supplies")
            st.markdown("**We provide a comprehensive range of medical, surgical, diagnostic, and orthopaedic products, including :**")
            st.markdown("""
            • Hospital equipment and surgical instruments
                        
            • Diagnostic devices and healthcare appliances
                        
            • Implants, disposables, and medical consumables
                        
            • Personal hygiene and toilet articles
            """)
            st.write("**Our offerings are curated to meet the evolving needs of hospitals, clinics, and healthcare professionals.**")

        with c3:
            st.subheader("🧪 Manufacturing & Processing")
            st.markdown("**With state-of-the-art facilities and adherence to global quality standards, we undertake :**")
            st.markdown("""
            • Manufacturing and formulation of pharmaceutical and medical products
                        
            • Contract manufacturing and private labeling
                        
            • Packaging, labeling, and repackaging services
                        
            • Regulatory-compliant production under GMP and ISO frameworks
            """)

        
        with c4:
            st.subheader("📚 Publishing & Knowledge Dissemination")
            st.markdown("**We are dedicated to enriching the healthcare ecosystem through :**")
            st.markdown("""
            • Publishing of pharmaceutical directories, journals, and manuals
                        
            • Compilation of medical references, case law digests, and compendia
                        
            • Distribution of content in both print and digital formats
                        
            • Supporting academic, clinical, and regulatory communities with credible resources
            """)

        with c5:
            st.subheader("🏪  Retail & Digital Infrastructure")
            st.markdown("**We operate and manage :**")
            st.markdown("""
            • Pharmacies and medical stores
                        
            • Warehouses and distribution hubs
            
            • E-commerce platforms and digital storefronts

            • Franchise and agency-based retail models
            """)
            st.write("**Our omnichannel presence ensures accessibility, affordability, and convenience for all stakeholders.**")

        st.write("---")

# --- GOVERNMENT APPROVALS & DOCUMENTS SECTION ---
with st.container(border=True):
    st.title("📜 Official Accreditations & Registrations")
    st.write("Pearl PharmMed Healthcare Consulting Pvt. Ltd. is a legally incorporated entity under the Ministry of Corporate Affairs.")
    
    # 4 Columns for 4 Documents
    doc_col1, doc_col2, doc_col3, doc_col4 = st.columns(4)
    
    with doc_col1:
        st.markdown("#### 🏢 Incorporation")
        st.write("**CIN:** U58122TZ2026PTC037337") # [cite: 7]
        try:
            with open("Certificate of Incorporation.pdf", "rb") as f:
                st.download_button("Download COI", f, key="coi_btn", file_name="Pearl_PharmMed_COI.pdf")
        except FileNotFoundError:
            st.warning("COI File missing")

    with doc_col2:
        st.markdown("#### 💳 PAN Card")
        st.write("**PAN:** AAQCP5405R") # [cite: 8, 29]
        try:
            with open("PAN Card.pdf", "rb") as f:
                st.download_button("Download PAN", f, key="pan_btn", file_name="Pearl_PharmMed_PAN.pdf")
        except FileNotFoundError:
            st.warning("PAN File missing")

    with doc_col3:
        st.markdown("#### 🏦 TAN Detail")
        st.write("**TAN:** CMBP11030F") # [cite: 9]
        try:
            # Neenga ippo save panna 'TAN_Final.pdf' file name inga matching-ah irukanum
            with open("TAN_Final.pdf", "rb") as f:
                st.download_button("Download TAN", f, key="tan_btn", file_name="Pearl_PharmMed_TAN.pdf")
        except FileNotFoundError:
            st.warning("TAN File missing")

    with doc_col4:
        st.markdown("#### 🔑 DIN Letter")
        st.write("**DIN:** 11461892") # [cite: 78]
        try:
            with open("SPICE + Part B_DIN Approval Letter.pdf", "rb") as f:
                st.download_button("Download DIN", f, key="din_btn", file_name="Director_DIN_Approval.pdf")
        except FileNotFoundError:
            st.warning("DIN File missing")

    st.success("✅ Registered on 02/01/2026 under the Companies Act, 2013.") # [cite: 6, 72]

# 6. INTERNSHIP SECTION (Inside a Separate Box)
with st.container(border=True):
    st.title("INTERNSHIP & PROJECT – INDUSTRY PROGRAMS")
    st.write("Our structured internship and project platform is designed specifically for B.Pharm, M.Pharm, Pharm.D, Nursing, Biomedical Engineering and Life Science graduates seeking real-world practical experience.")
    st.write("B.Pharm | M.Pharm | Pharm.D | Life Sciences | Biomedical Engineering | Nursing | Biotechnology")
    
    col_exp1, col_exp2 = st.columns(2)

    with col_exp1:

        st.markdown("### 🎓 Internship Areas")

         # இங்க பாரு ப்ரோ, சிம்பிளா ஒரு லிஸ்ட் மட்டும் வச்சுப்போம்
        tracks = [
        "Clinical Research Operations",
        "Clinical Data Management",
        "Pharmacovigilance (PV)",
        "Medical Device Regulation & Report Writing",
        "Medical and Regulatory Writing",
        "Real-time Case Processing & Narrative Writing",
        "Signal Detection, Risk Management & Literature Review",
        "Medical Coding"
        ]

    # ஒவ்வொன்னையும் டிக் மார்க் கூட காட்ட லூப்
        for track in tracks:
            st.write(f"✔ {track}")

    
    with col_exp2:
        st.subheader("Internship Highlights")
        st.info("""
        ✅ Industry-aligned curriculum
                
        ✅ Hands-on case studies & simulation projects
                
        ✅ Certificates recognized by industry partners
                
        ✅ Expert sessions & One-on-one mentorship
                
        ✅ Placement training & industry Networking
        """)

# --- ACADEMIC & PROJECT SUPPORT ---
with st.container(border=True):
    st.title("📚 PROJECT WORK SUPPORT")
    st.write("We provide guided project work for final year students:")
    st.info("""
        🔹 B.Pharm / M.Pharm
            
        🔹 Pharm.D (Clerkship / Thesis)
            
        🔹 Biomedical, Medical Electronics, Pharmaceutical Technology & Life Sciences
        """)
    
    st.markdown("""
        <style>
        .stExpander p {
            color: #1e3a8a !important; /* இது ஒரு அழகான ப்ளூ கலர் ப்ரோ, பிளாக் ஆகாது */
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.expander("Examples of project formats include:"):
        col_pro1, col_pro2 = st.columns(2)
        with col_pro1:
            st.markdown("""
            * Clinical trial protocol development
            * Investigator brochure & informed consent form drafting
            * Case report form (CRF) designing
            """)
        with col_pro2:
            st.markdown("""
            * Pharmacovigilance Individual Case Safety Report (ICSR) handling
            * Medical device risk-benefit documentation
            * Literature review-based research publications
            """)

    # --- SERVICES FOR INDUSTRY & ACADEMIA ---
with st.container(border=True):
    st.title("🛠️ SERVICES FOR INDUSTRY & ACADEMIA")
    
    # ரெண்டு பக்கமா பிரிக்குறோம் ப்ரோ, அப்போதான் பாக்க நல்லா இருக்கும்
    ind_col1, ind_col2 = st.columns(2)
    
    with ind_col1:
        st.markdown("### 🏢 For Pharmaceutical Companies & CROs")
        st.write("• Medical and regulatory writing")
        st.write("• Safety database case processing")
        st.write("• Clinical trial documentation support")
        st.write("• Medical device vigilance reporting")
        st.write("• Post-market surveillance compliance")
        st.write("• SOP development and training programs")
        
    with ind_col2:
        st.markdown("### 🏫 For Colleges & Universities")
        st.write("• Institutional training partnerships")
        st.write("• Guest lectures & workshops")
        st.write("• Industry-based certifications")
        st.write("• Internship & placement collaboration")
        st.write("• Research project mentorship")

# --- INTERNSHIP TRACKS OFFERED ---
with st.container(border=True):
    st.title("🎓 Internship Tracks Offered")

    # Table format-ல காட்டப்போறோம் ப்ரோ
    st.markdown("""
    | Program | Includes |
    | :--- | :--- |
    | **✔ Clinical Research & Trial Management** | Protocols, ICF, CRF, site management, GCP |
    | **✔ Pharmacovigilance & Drug Safety** | ICSR, narrative writing, signal detection |
    | **✔ Medical Device Reporting & MDR Compliance** | PMS, vigilance reports, CER writing |
    | **✔ Medical & Regulatory Writing** | SOPs, IB, CSR, CTD modules |
    | **✔ Clinical Data Management** | CDM tools, documentation, query management |
    """)

    st.markdown("---")

    # Program Benefits-ஐயும் இங்கயே ஆட் பண்ணிடலாம்
    st.subheader("💡 Program Benefits")
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        st.write("• Hands-on simulation assignments")
        st.write("• Live case studies & industry workflows")
        st.write("• International guideline training (ICH-GCP, US-FDA, EMA, CDSCO, WHO)")
    with b_col2:
        st.write("• Placement support & interview training")
        st.write("• Internship completion certificate")  

# --- ACADEMIC PROJECT SUPPORT (DETAILED) ---
with st.container(border=True):
    st.title("📚 Academic Project Support")
    st.write("We support final-year and dissertation projects with :")
    
    # இதையும் ரெண்டு காலமா பிரிச்சா இடம் மிச்சமாகும், பாக்கவும் நல்லா இருக்கும்
    proj_col1, proj_col2 = st.columns(2)
    
    with proj_col1:
        st.markdown("#### 📝 Research & Design")
        st.write("• Study design development")
        st.write("• Protocol writing")
        st.write("• Literature review & publication support")
        
    with proj_col2:
        st.markdown("#### 🧪 Specialized Models")
        st.write("• Clinical research documentation")
        st.write("• Medical device post-market analysis projects")
        st.write("• Pharmacovigilance-based research models")

    st.info("💡 **Note:** Our mentorship includes guidance on global regulatory standards to ensure high-quality project outcomes.")      

    st.subheader("🛠️ Services for Industry Partners")
        
    # Simple list without complex columns (to avoid errors)
    st.write("✔ Clinical research documentation")
    st.write("✔ Medical & regulatory writing")
    st.write("✔ Pharmacovigilance case processing")
    st.write("✔ Medical device CER/MDR support")
    st.write("✔ Training & capacity building")
    st.write("✔ SOP development & compliance audits")

# --- PARTNERSHIPS & COMMITMENT ---
with st.container(border=True):
    st.subheader("🤝 We Collaborate With")
    
    # Grid layout for icons and text
    coll_1, coll_2 = st.columns(2)
    
    with coll_1:
        st.markdown("🏫 **Universities & Colleges**")
        st.markdown("💊 **Pharmaceutical Companies**")
        
    with coll_2:
        st.markdown("🏥 **Hospitals & Clinical Research Sites**")
        st.markdown("📑 **Regulatory & Medical Device Organizations**")

    st.markdown("---")
    st.success("🌱 **Our Commitment:** We uphold the highest standards of ethics, transparency, and regulatory compliance to improve lives and empower professionals.")
            
# --- STRATEGIC COLLABORATIONS SECTION ---
with st.container(border=True):
    st.title("🤝 Strategic Collaborations & Global Partnerships")
    st.markdown("### We actively engage with:")
    
    st.markdown("""
    • **Healthcare institutions and research bodies**
    
    • **Regulatory authorities and academic organizations**
    
    • **Domestic and international firms for joint ventures and knowledge exchange**
    """)
    
    st.info("Our collaborative ethos drives innovation, compliance, and shared growth.")

# --- OUR COMMITMENT SECTION ---
with st.container(border=True):
    st.title("🌱 Our Commitment")
    st.write("""
    We uphold the highest standards of ethics, transparency, and regulatory compliance in all our operations. 
    Every initiative we undertake is guided by our mission to improve lives, empower professionals, and 
    contribute meaningfully to the global healthcare landscape.
    """)

# 7. CONTACT SECTION (Two WhatsApp Numbers)
with st.container(border=True):
    st.title("Contact Us")
    st.markdown("### 📍 PEARL PharmMed Healthcare Consulting Pvt. Ltd.")
    st.markdown("### 📞 Get in Touch")

    # IMPORTANT: HTML Code (No indentation on the left)
    contact_html = """
<div style="font-weight: 500; font-size: 1.15rem; line-height: 2.2; color: #000000;">

<div>
📱 <b>Phone:</b> 
<a href="tel:+919884700344" style="text-decoration: none; color: #007bff;">+91-9884700344</a> / 
<a href="tel:+919840673580" style="text-decoration: none; color: #007bff;">9840673580</a>
</div>

<div style="display: flex; align-items: center; flex-wrap: wrap; gap: 10px;">
<b style="color: #000000;">💬 WhatsApp:</b>

<a href="https://wa.me/919884700344" target="_blank" style="text-decoration: none; display: flex; align-items: center; gap: 5px;">
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="22" height="22">
<span style="color: #25D366; font-weight: bold;">9884700344</span>
</a>

<span style="color: #000;"> / </span>

<a href="https://wa.me/919840673580" target="_blank" style="text-decoration: none; display: flex; align-items: center; gap: 5px;">
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="22" height="22">
<span style="color: #25D366; font-weight: bold;">9840673580</span>
</a>
</div>

<div>
📧 <b>Email:</b> 
<a href="https://mail.google.com/mail/?view=cm&fs=1&to=info@ppti.in" target="_blank" style="text-decoration: none; color: #007bff;">info@ppti.in</a>
</div>

<div>
🌐 <b>Website:</b> 
<a href="http://www.pharmmedhealthcare.com" target="_blank" style="text-decoration: none; color: #007bff;">www.pharmmedhealthcare.com</a>
</div>

</div>
"""
    st.markdown(contact_html, unsafe_allow_html=True)

    st.markdown("### 📍 Location")
    st.write("**Tenkasi Office:**")
    st.write("71/2 Middle Street, Kudiyiruppu, Courtallam Post, Tenkasi - 627802")

    
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Prudential Financial Advisers | Portal Hub", layout="wide")

# --- HIGH-AVAILABILITY LAYOUT DESIGN STYLES ---
st.markdown("""
<style>
    /* Premium Corporate Branding Ribbon */
    .pru-header { 
        background-color: #ffffff; 
        padding: 15px 45px; 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        border-bottom: 1px solid #eaeaea;
    }
    .pru-logo-text { 
        font-family: 'Playfair Display', serif; 
        font-size: 26px; 
        font-weight: 900; 
        color: #E31837; 
        letter-spacing: -1px; 
        text-transform: uppercase;
    }
    .pru-logo-text span { 
        color: #111111; 
        font-size: 11px; 
        font-family: 'Inter', sans-serif; 
        font-weight: bold; 
        letter-spacing: 1px;
        margin-left: 8px;
        vertical-align: middle;
    }
    
    /* Top Crimson Action Navigation Menu */
    .crimson-menu { 
        background-color: #E31837; 
        color: white; 
        display: flex; 
        justify-content: center; 
        gap: 3.5rem; 
        padding: 14px 20px; 
        font-size: 14px; 
        font-family: 'Inter', sans-serif;
        font-weight: 600; 
        border-radius: 4px; 
        margin-bottom: 35px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .crimson-menu span { cursor: pointer; opacity: 0.95; }
    .crimson-menu span:hover { opacity: 1; text-decoration: underline; }

    /* Core Split Image Hero Banner Layout */
    .hero-container { display: flex; background-color: #F9F8F6; border-radius: 12px; overflow: hidden; margin-bottom: 45px; box-shadow: 0 4px 20px rgba(0,0,0,0.02); }
    .hero-text-block { flex: 1.1; padding: 50px 40px; display: flex; flex-direction: column; justify-content: center; }
    .hero-h1 { font-family: 'Playfair Display', serif; font-size: 38px; font-weight: 700; color: #111111; line-height: 1.2; margin-bottom: 15px; }
    .hero-h1 span { color: #E31837; }
    .hero-p { font-size: 15.5px; color: #555555; line-height: 1.6; margin-bottom: 0px; }
    .hero-image-block { flex: 0.9; background: url('https://unsplash.com') center center/cover no-repeat; min-height: 350px; }
    
    /* Segment Framework Labels */
    .section-title { font-size: 12px; color: #777777; text-transform: uppercase; font-weight: bold; margin-top: 40px; margin-bottom: 5px; letter-spacing: 1px; }
    .sub-section-header { font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 700; color: #111111; margin-bottom: 25px; text-align: center; }
    .sub-section-header span { color: #E31837; }
    
    /* Standard PFA Cards Template Grid */
    .pru-card { background: #ffffff; border: 1px solid #eaeaea; border-radius: 8px; padding: 30px 25px; box-shadow: 0 6px 18px rgba(0,0,0,0.01); height: 100%; transition: transform 0.2s; }
    .pru-card:hover { transform: translateY(-3px); }
    .pru-card-img { width: 100%; height: 160px; border-radius: 6px; object-fit: cover; margin-bottom: 18px; }
    .pru-card-title { font-family: 'Playfair Display', serif; font-size: 18px; font-weight: bold; color: #111111; margin-bottom: 10px; }
    .pru-card-text { font-size: 13.5px; color: #666666; line-height: 1.5; }
    
    /* Timeline Journey Components */
    .journey-step { background: #ffffff; border: 1px solid #eaeaea; border-left: 4px solid #E31837; padding: 16px 20px; margin-bottom: 12px; border-radius: 0 8px 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.01); }
    .journey-title { font-size: 15px; font-weight: bold; color: #111111; margin-bottom: 4px; }
</style>
""", unsafe_allow_html=True)

# =========================================================================
# 🏛️ REPLICATED HEADER NAVIGATION COMPONENTS
# =========================================================================
col_logo, col_logo_img = st.columns([4, 1])
with col_logo:
    st.markdown('<div class="pru-header"><div class="pru-logo-text">PRUDENTIAL <span>Financial Advisers</span></div></div>', unsafe_allow_html=True)
with col_logo_img:
    # Dynamically calling your repository's native file image to avoid dead external links
    st.image("logo.png", width=120)

st.markdown("""
<div class="crimson-menu">
    <span>What We Offer</span>
    <span>Our Story</span>
    <span>Join the Team</span>
    <span>Support</span>
    <span>Get in Touch</span>
</div>
""", unsafe_allow_html=True)

# --- PANEL SELECTION SYSTEM ---
st.sidebar.markdown('**System Navigator**')
navigation_selection = st.sidebar.radio("Go To Section Workspace:", [
    "🌐 Client Information Portal",
    "📊 Live Interactive CPF Engine",
    "🔒 Private Agent Computational View"
])

if navigation_selection == "🌐 Client Information Portal":
    # 1. Premium Interactive Split Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-text-block">
            <div class="hero-h1">Helping You <span>Get The<br>Most Out of Life</span></div>
            <div class="hero-p">No matter what you hope to achieve in the future, we can curate personalized wealth solutions to meet your needs at various stages of your life.</div>
        </div>
        <div class="hero-image-block"></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sub-section-header">Planning a <span>Brighter Future</span> for you</div>', unsafe_allow_html=True)
    
    # 2. Triple Value Service Grid Cards Matrix
    col_c1, col_c2, col_c3 = st.columns(3, gap="large")
    with col_c1:
        st.markdown("""
        <div class="pru-card">
            <img class="pru-card-img" src="https://unsplash.com">
            <div class="pru-card-title">A Personal Plan to Achieve Your Goals</div>
            <div class="pru-card-text">We provide personalized advice with tailored solutions and products to help you achieve your financial aspirations.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_c2:
        st.markdown("""
        <div class="pru-card">
            <img class="pru-card-img" src="https://unsplash.com">
            <div class="pru-card-title">An Expert On Your Side</div>
            <div class="pru-card-text">Our team is made up of qualified and well-trained Wealth Managers who are here to plan beyond your everyday needs.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_c3:
        st.markdown("""
        <div class="pru-card">
            <img class="pru-card-img" src="https://unsplash.com">
            <div class="pru-card-title">We Offer More Than Just Insurance</div>
            <div class="pru-card-text">We provide services beyond insurance, from protecting your legacy to estate and tax planning, and more wealth management services to fit your needs.</div>
        </div>
        """, unsafe_allow_html=True)

    # 3. Advisory Framework Roadmap
    st.markdown('<p class="section-title">Our Advisory Framework</p>', unsafe_allow_html=True)
    for step in ["1. Strategic Intake & Discovery Consultation", "2. Portfolio Optimization Blueprint Modeling", "3. Periodic Asset Allocation Calibration"]:
        st.markdown(f'<div class="journey-step"><div class="journey-title">{step}</div></div>', unsafe_allow_html=True)
        
    if st.button("Schedule Strategy Call", type="primary"): 
        st.success("Consultation request logged.")

elif navigation_selection == "📊 Live Interactive CPF Engine":
    st.components.v1.iframe(src="https://smartcalculator.sg", height=850, scrolling=True)

else:
    st.components.v1.iframe(src="https://github.io", height=850, scrolling=True)

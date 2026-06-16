import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Prudential Financial Advisers | Portfolio Hub", layout="wide")

# --- OFFICIAL CORPORATE PFA DESIGN STYLE CODES ---
st.markdown("""
<style>
    .pru-header { background-color: #ffffff; padding: 18px 45px; border-bottom: 3px solid #E31837; display: flex; justify-content: space-between; align-items: center; margin-bottom: 0px; }
    .pru-logo { font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 900; color: #111111; letter-spacing: -0.5px; }
    .pru-logo span { color: #E31837; }
    .pru-tag { font-size: 11px; text-transform: uppercase; font-weight: bold; color: #555555; letter-spacing: 2px; }
    
    .hero-bg { 
        background: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.65)), url('https://unsplash.com') center center/cover no-repeat;
        color: white; padding: 90px 50px; border-radius: 0 0 2.5rem 2.5rem; margin-bottom: 45px; box-shadow: inset 0 0 120px rgba(0,0,0,0.6);
    }
    .hero-h1 { font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 700; margin-bottom: 15px; color: #ffffff; line-height: 1.2; }
    .hero-p { font-size: 18px; max-width: 750px; color: #e0e0e0; margin-bottom: 0px; line-height: 1.6; }
    
    .section-title { font-size: 13px; color: #E31837; text-transform: uppercase; font-weight: bold; margin-top: 40px; margin-bottom: 15px; letter-spacing: 1px; }
    .sub-section-header { font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 700; color: #111111; margin-bottom: 25px; }
    
    .pru-card { background: #ffffff; border: 1px solid #eaeaea; border-radius: 8px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.01); height: 100%; margin-bottom: 20px; }
    .pru-card-title { font-family: 'Playfair Display', serif; font-size: 18px; font-weight: bold; color: #111111; margin-bottom: 10px; }
    .pru-card-text { font-size: 14px; color: #555555; line-height: 1.5; }
    
    .journey-step { background: #fdfdfd; border-left: 3px solid #E31837; padding: 15px 20px; margin-bottom: 15px; border-radius: 0 6px 6px 0; }
    .journey-title { font-size: 15px; font-weight: bold; color: #111111; margin-bottom: 4px; }
</style>
""", unsafe_allow_html=True)

# --- WORKSPACE CONTROL NAVIGATION SIDEBAR ---
st.sidebar.markdown('<p class="pru-tag">System Navigator</p>', unsafe_allow_html=True)
navigation_selection = st.sidebar.radio("Go To Section Workspace:", [
    "🌐 Client Information Portal",
    "📊 Live Interactive CPF Engine (Smart Calculator)",
    "🔒 Private Agent Computational View (Fintech Matrix)"
])

if navigation_selection == "🌐 Client Information Portal":
    st.markdown('<div class="pru-header"><div class="pru-logo">PRUDENTIAL<span>.</span></div><div class="pru-tag">Financial Advisers</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-bg">
        <div class="hero-h1">Planning a Brighter Future<br>for you</div>
        <div class="hero-p">Comprehensive financial planning for protection, savings, and legacy needs.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">Why Partner With Us</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3, gap="large")
    with c1: st.markdown('<div class="pru-card"><div class="pru-card-title">Personalized Plan</div><div class="pru-card-text">Tailored solutions for your specific financial goals.</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="pru-card"><div class="pru-card-title">Expert Advice</div><div class="pru-card-text">Qualified strategic wealth managers at your convenience.</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="pru-card"><div class="pru-card-title">Holistic Services</div><div class="pru-card-text">Comprehensive asset and policy integration models.</div></div>', unsafe_allow_html=True)

    st.markdown('<p class="section-title">What Matters Most to You?</p>', unsafe_allow_html=True)
    quiz = st.selectbox("Select your core financial focus milestone:", ["Choose...", "Asset Protection Frameworks", "Capital Growth Strategies", "2026 CPF Retirement Sums", "Estate Legacy Discretion"])
    if quiz != "Choose...": st.success(f"Tailoring advisory matrix parameters for: **{quiz}**")
    
    st.markdown('<p class="sub-section-header">Our Advisory Engagement Framework</p>', unsafe_allow_html=True)
    steps = ["1. Strategic Intake & Discovery", "2. Portfolio Optimization Modeling", "3. Periodic Allocation Calibration"]
    for step in steps:
        st.markdown(f'<div class="journey-step"><div class="journey-title">{step}</div></div>', unsafe_allow_html=True)
    if st.button("Schedule Private Portfolio Strategy Call", type="primary"):
        st.success("Consultation request successfully logged.")

elif navigation_selection == "📊 Live Interactive CPF Engine (Smart Calculator)":
    st.markdown('<div class="pru-header"><div class="pru-logo">SMART CALCULATOR SG<span>.</span></div><div class="pru-tag">2026 Core Engine Matrix</div></div>', unsafe_allow_html=True)
    st.components.v1.iframe(src="https://smartcalculator.sg", height=850, scrolling=True)

else:
    st.markdown('<div class="pru-header"><div class="pru-logo">FINTECH COMPUTE TOOLKIT<span>.</span></div><div class="pru-tag">Agent-Only Protected View</div></div>', unsafe_allow_html=True)
    st.components.v1.iframe(src="https://github.io", height=850, scrolling=True)

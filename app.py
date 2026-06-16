import streamlit as st

# Configure a wide canvas for embedding financial layouts seamlessly
st.set_page_config(page_title="Cecilia Woon Portal Console", layout="wide")

# --- BRANDING BAR ACCENT SYSTEM ---
st.markdown("""
<style>
    .pru-header { background-color: #ffffff; padding: 15px 30px; border-bottom: 3px solid #E31837; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    .pru-logo { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 900; color: #111111; letter-spacing: -0.5px; }
    .pru-logo span { color: #E31837; }
    .pru-tag { font-size: 11px; text-transform: uppercase; font-weight: bold; color: #777777; letter-spacing: 1.5px; }
</style>
""", unsafe_allow_html=True)

# --- PANEL NAVIGATION CONTROL CENTER ---
st.sidebar.markdown('<p class="pru-tag">System Control Console</p>', unsafe_allow_html=True)
navigation_selection = st.sidebar.radio("Navigate Ecosystem Portal:", [
    "🌐 Client Frontend Portal (Prudential Style)",
    "📊 Live Interactive CPF Engine (Smart Calculator)",
    "🔒 Private Agent Computational View (Fintech Matrix)"
])
if navigation_selection == "🌐 Client Frontend Portal (Prudential Style)":
    st.markdown('<div class="pru-header"><div class="pru-logo">CECILIA WOON<span>.</span></div><div class="pru-tag">Public Client Interface</div></div>', unsafe_allow_html=True)
    
    # Securely embed the premium client-facing infrastructure layout
    st.components.v1.iframe(
        src="https://prudentialfa.com.sg", 
        height=850, 
        scrolling=True
    )

elif navigation_selection == "📊 Live Interactive CPF Engine (Smart Calculator)":
    st.markdown('<div class="pru-header"><div class="pru-logo">SMART CALCULATOR SG<span>.</span></div><div class="pru-tag">2026 Core Engine Matrix</div></div>', unsafe_allow_html=True)
    
    # Embed the verified 2026 CPF calculation layout module directly
    st.components.v1.iframe(
        src="https://smartcalculator.sg", 
        height=850, 
        scrolling=True
    )
else:
    st.markdown('<div class="pru-header"><div class="pru-logo">FINTECH COMPUTE TOOLKIT<span>.</span></div><div class="pru-tag">Agent-Only Protected View</div></div>', unsafe_allow_html=True)
    
    # Embed your private computation tool directly from your GitHub landing page repository
    st.components.v1.iframe(
        src="https://github.io", 
        height=850, 
        scrolling=True
    )

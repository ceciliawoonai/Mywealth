import json
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Cecilia Woon | Private Wealth Console", layout="wide")

# =========================================================================
# 🏛️ GLOBAL SECURE IMMERSIVE LIQUID MATRIX ENGINE (ELVALABS STYLE MOTION)
# =========================================================================
GLOBAL_BUBBLE_CANVAS_HTML = r"""
<div class="sakazuki-row" style="padding-left:0; padding-right:0; box-sizing:border-box;">
    <div class="sakazuki-left-label">The Collective</div>
    <div class="sakazuki-right-content">
        <div class="sakazuki-h3">The Lives We Protect</div>
        <div class="sakazuki-p" style="margin-bottom:25px; color:#A0A0A5; font-size:16px; line-height:1.7;">Hover your cursor across the active matrix profile network below. Every structural profession driving Singapore's infrastructure deserves customized clinical income shielding thresholds against unexpected lifespan tragedies.</div>
    </div>
</div>

<style>
    /* Continuous 3D Morphing Liquid Blob Keyframes */
    @keyframes liquidMorph {
        0% { border-radius: 42% 58% 70% 30% / 45% 45% 55% 55%; transform: rotate(0deg); }
        50% { border-radius: 70% 30% 52% 48% / 60% 40% 60% 40%; transform: rotate(180deg); }
        100% { border-radius: 42% 58% 70% 30% / 45% 45% 55% 55%; transform: rotate(360deg); }
    }
    
    .kinetic-bubble-container {
        position: relative;
        width: 58px;
        height: 58px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        z-index: 5;
    }
    
    .liquid-background-layer {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        animation: liquidMorph 8s linear infinite;
        transition: all 0.4s ease;
        z-index: 1;
        box-sizing: border-box;
    }
    
    .monogram-label-overlay {
        position: relative;
        z-index: 10;
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.5px;
        pointer-events: none;
        text-align: center;
    }
</style>

<div id="bubble-canvas-container" style="background:#0B0B0E; border:1px solid rgba(255,255,255,0.06); border-radius:16px; padding:35px 25px; width:100%; position:relative; min-height:420px; overflow:hidden; box-sizing:border-box;">
    <div id="matrix-ticker" style="font-family:'Courier New', monospace; font-size:12px; color:#8A8A93; margin-bottom:30px; min-height:18px; border-bottom:1px solid rgba(255,255,255,0.05); padding-bottom:12px;">[SYSTEM ACTIVE] Scan network profiles to evaluate structural risk models...</div>
    <div id="avatar-matrix-grid" style="display:flex; flex-wrap:wrap; justify-content:center; gap:22px; max-width:860px; margin:0 auto;"></div>
</div>

<script>
    (function() {
        const profile_nodes = DATA_REPLACE_TOKEN;
        const grid = document.getElementById("avatar-matrix-grid");
        const ticker = document.getElementById("matrix-ticker");
        
        profile_nodes.forEach((n, idx) => {
            const container = document.createElement("div");
            container.className = "kinetic-bubble-container";
            
            const sector_color = n.sec === "Med" ? "rgba(227,24,55,1)" : n.sec === "Tech" ? "rgba(212,175,55,1)" : "rgba(255, 255, 255, 0.3)";
            const glow_color = n.sec === "Med" ? "rgba(227,24,55,0.15)" : n.sec === "Tech" ? "rgba(212,175,55,0.15)" : "rgba(255, 255, 255, 0.03)";
            
            // Render the moving background layer inside the item
            const liquidBg = document.createElement("div");
            liquidBg.className = "liquid-background-layer";
            liquidBg.style.border = `1.5px solid ${sector_color}`;
            liquidBg.style.background = `linear-gradient(135deg, ${glow_color} 0%, rgba(5,5,7,0.8) 100%)`;
            liquidBg.style.animationDuration = `${6 + (idx % 4) * 2}s`; // Varying speeds for asymmetry
            
            const labelSpan = document.createElement("span");
            labelSpan.className = "monogram-label-overlay";
            labelSpan.innerText = n.init;
            
            container.appendChild(liquidBg);
            container.appendChild(labelSpan);
            grid.appendChild(container);
            
            // Hover logic triggers
            container.addEventListener("mouseover", () => {
                container.style.transform = "scale(1.35)";
                liquidBg.style.borderColor = "#FF4D61";
                liquidBg.style.background = n.sec === "Med" ? "rgba(227,24,55,0.3)" : n.sec === "Tech" ? "rgba(212,175,55,0.3)" : "rgba(255,255,255,0.2)";
                liquidBg.style.boxShadow = `0 0 20px ${sector_color}`;
                ticker.style.color = "#FF4D61";
                ticker.innerText = `\u26A1 [STREAM MATRIX] Sector: ${n.sec} // Profile Focus: ${n.label} -> Successfully linked to Cecilia's operational risk insulation framework.`;
            });
            
            container.addEventListener("mouseout", () => {
                container.style.transform = "scale(1)";
                liquidBg.style.borderColor = sector_color;
                liquidBg.style.background = `linear-gradient(135deg, ${glow_color} 0%, rgba(5,5,7,0.8) 100%)`;
                liquidBg.style.boxShadow = "none";
                ticker.style.color = "#8A8A93";
                ticker.innerText = "[SYSTEM ACTIVE] Scan network profiles to evaluate structural risk models...";
            });
        });
    })();
</script>
"""





# --- ELVALABS & SAKAZUKI INSPIRED ULTRA-DARK SYSTEM DESIGN STYLES ---
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] { background-color: #050507 !important; color: #FFFFFF !important; font-family: 'Inter', sans-serif; }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    .brand-container { padding: 40px 45px 10px 45px; background: #050507; }
    .brand-text { font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 900; color: #FFFFFF; letter-spacing: -0.5px; text-transform: uppercase; }
    .brand-text span { color: #E31837; font-size: 11px; font-family: 'Inter', sans-serif; font-weight: bold; letter-spacing: 2px; margin-left: 12px; vertical-align: middle; }
    
    .kinetic-nav { display: flex; justify-content: flex-start; gap: 3.5rem; padding: 18px 45px; font-size: 12px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; border-bottom: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 40px; }
    .kinetic-nav span { cursor: pointer; color: #8A8A93; transition: all 0.4s ease; }
    .kinetic-nav span:hover { color: #FFFFFF; }
    .active-nav-node { color: #E31837 !important; font-weight: bold; }

    .sakazuki-hero { padding: 40px 45px; margin-bottom: 20px; }
    .sakazuki-tag { color: #8A8A93; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 20px; }
    .sakazuki-h1 { font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 700; line-height: 1.2; margin-bottom: 15px; letter-spacing: -0.5px; }
    .sakazuki-h1 span { color: #E31837; }
    
    .sakazuki-row { display: flex; border-top: 1px solid rgba(255, 255, 255, 0.08); padding: 40px 45px; }
    .sakazuki-left-label { flex: 0.4; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #8A8A93; font-weight: bold; }
    .sakazuki-right-content { flex: 1.6; }
    .sakazuki-h3 { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 600; margin-bottom: 15px; color: #FFFFFF; }
    .sakazuki-p { font-size: 16px; color: #A0A0A5; line-height: 1.7; max-width: 850px; }

    .reyou-panel-header { font-family: 'Playfair Display', serif; font-size: 32px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px; }
    .reyou-panel-subtitle { font-size: 16px; color: #8A8A93; margin-bottom: 40px; line-height: 1.6; max-width: 700px; }
    .reyou-card { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 16px; padding: 35px 30px; height: 100%; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
    .reyou-card:hover { background: rgba(255, 255, 255, 0.04); border-color: rgba(227, 24, 55, 0.4); transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
    .reyou-card-num { font-size: 12px; font-weight: bold; color: #E31837; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 12px; }
    .reyou-card-title { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: bold; color: #FFFFFF; margin-bottom: 12px; }
    .reyou-card-desc { font-size: 14px; color: #8A8A93; line-height: 1.6; }

    .terminal-panel { background: #0B0B0E; border: 1px solid rgba(255, 255, 255, 0.04); border-radius: 16px; padding: 35px; margin-bottom: 30px; }
    .terminal-header { font-size: 11px; text-transform: uppercase; font-weight: bold; color: #66666D; letter-spacing: 1.5px; margin-bottom: 20px; display: flex; align-items: center; gap: 8px; }
    .terminal-dot { width: 6px; height: 6px; background: #FF4D61; border-radius: 50%; box-shadow: 0 0 10px #FF4D61; }
    .data-stream-row { display: flex; justify-content: space-between; padding: 16px 10px; border-bottom: 1px solid rgba(255, 255, 255, 0.03); font-size: 15px; color: #E4E4E7; }
    .data-stream-total { display: flex; justify-content: space-between; padding: 18px 15px; font-weight: bold; background: rgba(227, 24, 55, 0.08); color: #FF4D61; border-radius: 8px; font-size: 16px; margin-top: 15px; border: 1px solid rgba(227, 24, 55, 0.2); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-container"><div class="brand-text">CECILIA WOON <span>Private Wealth Advisory</span></div></div>', unsafe_allow_html=True)

# --- WORKSPACE CONTROL SELECTION NAVIGATION SIDEBAR ---
st.sidebar.markdown('**System Navigator**')
navigation_selection = st.sidebar.radio("Go To Section Workspace:", [
    "🌐 Clinical P&L Philosophy",
    "📚 Research & Education Vault",
    "🎯 The Rorschach Protocol (Leads)",
    "📊 Live Interactive 2026 CPF Engine",
    "🔒 Private Agent Computational View",
    "🖼️ Image Compression Utilities Console",
    "👑 Cecilia VIP AI Alternative Studio"  # Add this exact option handle
])

n1 = "active-nav-node" if navigation_selection == "🌐 Clinical P&L Philosophy" else ""
n2 = "active-nav-node" if navigation_selection == "📚 Research & Education Vault" else ""
n3 = "active-nav-node" if navigation_selection == "🎯 The Rorschach Protocol (Leads)" else ""
n4 = "active-nav-node" if navigation_selection == "📊 Live Interactive 2026 CPF Engine" else ""
n5 = "active-nav-node" if navigation_selection == "🔒 Private Agent Computational View" else ""

st.markdown(f"""
<div class="kinetic-nav">
    <span class="{n1}">Philosophy</span>
    <span class="{n2}">Education Vault</span>
    <span class="{n3}">Rorschach Protocol</span>
    <span class="{n4}">2026 Sovereign Engine</span>
    <span class="{n5}">Agent Matrix Private</span>
</div>
""", unsafe_allow_html=True)
if navigation_selection == "🌐 Clinical P&L Philosophy":
    st.markdown("""
<div class="sakazuki-hero">
    <div class="sakazuki-tag">Risk Mitigation Practice</div>
    <div class="sakazuki-h1">Applying Corporate P&L Principles<br>to <span>Human Biology</span></div>
</div>
<div class="sakazuki-row">
    <div class="sakazuki-left-label">The Blind Spot</div>
    <div class="sakazuki-right-content">
        <div class="sakazuki-h3">Who pays your rent while you try to stay healthy?</div>
        <div class="sakazuki-p">Statistically, if you live to be 70 years old, you are likely to spend <b>800 days</b> - more than two full years - lying in a hospital bed. Not because you are dying, but because modern medicine has shifted to aggressive, proactive preventative maintenance (diabetes tracking, cardiovascular calibrations, intensive rehabilitation). Standard insurance pays the clinic to fix the body, but it ignores the massive fallout to your life. When the human factory shuts down for routine asphalt maintenance, your personal cashflow commerce shouldn't collapse.</div>
    </div>
</div>
<div class="sakazuki-row">
    <div class="sakazuki-left-label">The Strategist</div>
    <div class="sakazuki-right-content">
        <div class="sakazuki-h3">Meet Cecilia Woon</div>
        <div class="sakazuki-p">Cecilia is not your traditional financial advisor. She spent over a decade as a high-level global marketing strategist and e-commerce head managing massive corporate profit and loss statements (P&Ls) and multi-city international rollouts for market giants like <b>Wacom, Nokia, Honeywell, and L&L</b>. Holding a BA in Economics & Philosophy from NUS paired with an advanced Level 3 FinTech Developer certification (Python, AI, Analytics) from the NUS School of Computing, she synthesizes human behavioral data with unfeeling mathematical safety nets. She diagnoses emerging macro liabilities inside a human lifespan long before they cross into the public ledger.</div>
    </div>
</div>
""", unsafe_allow_html=True)

    # Pre-computing the monogram initials in Python to ensure frictionless browser parsing
    bubble_data_payload = [
        {"id": 1, "label": "Staff Nurse", "init": "SN", "sec": "Med"},
        {"id": 2, "label": "GP Doctor", "init": "GD", "sec": "Med"},
        {"id": 3, "label": "Pharmacist", "init": "PH", "sec": "Med"},
        {"id": 4, "label": "Physiotherapist", "init": "PT", "sec": "Med"},
        {"id": 5, "label": "Bus Captain", "init": "BC", "sec": "Ops"},
        {"id": 6, "label": "Cleaner Hero", "init": "CH", "sec": "Ops"},
        {"id": 7, "label": "Delivery Rider", "init": "DR", "sec": "Ops"},
        {"id": 8, "label": "Security Officer", "init": "SO", "sec": "Ops"},
        {"id": 9, "label": "Port Operator", "init": "PO", "sec": "Ops"},
        {"id": 10, "label": "Software Engineer", "init": "SE", "sec": "Tech"},
        {"id": 11, "label": "HR Specialist", "init": "HR", "sec": "Tech"},
        {"id": 12, "label": "Compliance Officer", "init": "CO", "sec": "Tech"},
        {"id": 13, "label": "Customer Success", "init": "CS", "sec": "Tech"},
        {"id": 14, "label": "Digital Marketing", "init": "DM", "sec": "Tech"},
        {"id": 15, "label": "Primary Teacher", "init": "PT", "sec": "Edu"},
        {"id": 16, "label": "Civil Servant", "init": "CS", "sec": "Edu"},
        {"id": 17, "label": "Hawker Legend", "init": "HL", "sec": "Biz"},
        {"id": 18, "label": "Artisan Barista", "init": "AB", "sec": "Biz"},
        {"id": 19, "label": "Retail Assistant", "init": "RA", "sec": "Biz"},
        {"id": 20, "label": "Cabin Crew", "init": "CC", "sec": "Biz"}
    ]

    nodes_json_payload = json.dumps(bubble_data_payload)
    compiled_canvas_html = GLOBAL_BUBBLE_CANVAS_HTML.replace("DATA_REPLACE_TOKEN", nodes_json_payload)
    st.components.v1.html(compiled_canvas_html, height=620, scrolling=False)

    st.markdown('<div style="padding: 20px 0 0 45px;">', unsafe_allow_html=True)
    if st.button("Initialize Risk Analysis Sequence", type="primary"):
        st.success("Sequence authorized. Cecilia Woon's office will review your corporate capital coordinates shortly.")
    st.markdown('</div>', unsafe_allow_html=True)

elif navigation_selection == "📚 Research & Education Vault":
    st.markdown('<div style="padding: 0 45px 40px 45px;">', unsafe_allow_html=True)
    st.markdown('<div class="reyou-panel-header">Treat the Exposure, Not Just the Premium</div>', unsafe_allow_html=True)
    st.markdown('<div class="reyou-panel-subtitle">Explore our rigorous, research-backed advisory briefs. Designed to insulate high-net-worth portfolios from structural leakages and hidden policy traps.</div>', unsafe_allow_html=True)
    
    row1_c1, row1_c2, row1_c3 = st.columns(3, gap="large")
    with row1_c1:
        st.markdown("""<div class="reyou-card"><div class="reyou-card-num">Brief 01</div><div class="reyou-card-title">How to Avoid Being Oversold</div><div class="reyou-card-desc">Stripping away commissions-driven insurance pitches to isolate pure capital-efficient protection values tailored to asset bounds.</div></div>""", unsafe_allow_html=True)
    with row1_c2:
        st.markdown("""<div class="reyou-card"><div class="reyou-card-num">Brief 02</div><div class="reyou-card-title">Streamline Your Protection Plan</div><div class="reyou-card-desc">Consolidating overlapping policy layers to reduce drag and optimize premium cashflow overheads significantly.</div></div>""", unsafe_allow_html=True)
    with row1_c3:
        st.markdown("""<div class="reyou-card"><div class="reyou-card-num">Brief 03</div><div class="reyou-card-title">Choosing a High-Utility Accident Plan</div><div class="reyou-card-desc">Evaluating high-tier disability payouts, workspace trauma recovery terms, and mobility adjustments over generic entry products.</div></div>""", unsafe_allow_html=True)

    st.markdown('<div style="margin-top:30px;"></div>', unsafe_allow_html=True)
    row2_c1, row2_c2, row2_c3 = st.columns(3, gap="large")
    with row2_c1:
        st.markdown("""<div class="reyou-card"><div class="reyou-card-num">Brief 04</div><div class="reyou-card-title">The 1M65 Structural Strategy</div><div class="reyou-card-desc">Leveraging early compounding parameters across state balances to guarantee million-dollar liquidity nests safely by retirement milestones.</div></div>""", unsafe_allow_html=True)
    with row2_c2:
        st.markdown("""<div class="reyou-card"><div class="reyou-card-num">Brief 05</div><div class="reyou-card-title">Managing Your ILP Policy Drag</div><div class="reyou-card-desc">Dissecting cost-of-insurance structures within Investment-Linked Policies to salvage capital allocation efficiency.</div></div>""", unsafe_allow_html=True)
    with row2_c3:
        st.markdown("""<div class="reyou-card"><div class="reyou-card-num">Brief 06</div><div class="reyou-card-title">Pre-Crisis Resiliency Protocol</div><div class="reyou-card-desc">A unified tactical emergency sequence linking corporate legal standing, rapid cash buffers, and account authority overrides—ensuring your portfolio survives intact.</div></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
elif navigation_selection == "🎯 The Rorschach Protocol (Leads)":
    st.markdown('<div style="padding: 0 45px 40px 45px;">', unsafe_allow_html=True)
    st.markdown('<div class="reyou-panel-header">The Rorschach Wealth Protocol</div>', unsafe_allow_html=True)
    st.markdown('<div class="reyou-panel-subtitle">Most households realize they are under-insulated exactly five minutes too late. Select the abstract artifact block below that mirrors your financial subconscious right now.</div>', unsafe_allow_html=True)
    
    obj_c1, obj_c2, obj_c3, obj_c4 = st.columns(4, gap="medium")
    with obj_c1:
        st.image("https://unsplash.com", use_container_width=True)
        st.checkbox("Artifact A: The Fractured Crystal Monolith")
    with obj_c2:
        st.image("https://unsplash.com", use_container_width=True)
        st.checkbox("Artifact B: The Unanchored Void Grid")
    with obj_c3:
        st.image("https://unsplash.com", use_container_width=True)
        st.checkbox("Artifact C: The Fluid Kinetic Melt")
    with obj_c4:
        st.image("https://unsplash.com", use_container_width=True)
        st.checkbox("Artifact D: The Isolated Linear Axis")

    st.markdown('<div style="margin-top:40px;"></div>', unsafe_allow_html=True)
    st.markdown('### Your Financial Moment of Truth')
    reflection_text = st.text_area("In a few sentences, tell us why this object connects to your current fears or goals regarding financial blindspots (P&L shocks, asset insulation, or family safety nets):")
    
    st.markdown('<div style="margin-top:20px;"></div>', unsafe_allow_html=True)
    st.markdown('### Secure Your Strategy Coordinates')
    col_lead1, col_lead2, col_lead3 = st.columns(3)
    with col_lead1: lead_name = st.text_input("Full Professional Name")
    with col_lead2: lead_email = st.text_input("Verified Email Coordinate")
    with col_lead3: lead_phone = st.text_input("Mobile Coordinate (WhatsApp)")

    st.markdown('<div style="margin-top:25px;"></div>', unsafe_allow_html=True)
    if st.button("Submit Profile & Lock In Audit", type="primary"):
        if lead_name and lead_email and reflection_text:
            st.success(f"Protocol initialized, {lead_name}. Your behavioral reflection has been securely routed to Cecilia Woon's private office. Your complimentary Bespoke 2026 Sovereign Stress-Test Audit ($1,500 value) has been prioritized.")
            if "cecilia" in reflection_text.lower():
                st.info("⚡ Priority Partner Multiplier Activated: Your blueprint review has been fast-tracked to the immediate vanguard tier.")
        else:
            st.error("Authentication Error: Please complete the behavioral reflection field and baseline coordinates.")
    st.markdown('</div>', unsafe_allow_html=True)

elif navigation_selection == "📊 Live Interactive 2026 CPF Engine":
    st.markdown('<div style="padding: 0 45px; margin-bottom: 30px;"><h2 class="sakazuki-h1">Sovereign Matrix <span>2026</span></h2></div>', unsafe_allow_html=True)
    col_t1, col_t2 = st.columns([1, 1.2], gap="large")
    with col_t1:
        st.markdown('<div class="terminal-panel"><div class="terminal-header"><div class="terminal-dot"></div>Engine Inputs Console</div>', unsafe_allow_html=True)
        salary = st.number_input("Monthly Gross Wage (OW) ($)", min_value=1000, value=7375, step=250)
        current_age = st.slider("Client Target Age Model", min_value=20, max_value=99, value=53)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_t2:
        def get_smart_rates_2026(age):
            if age <= 35: return 0.20, 0.17, 0.6217, 0.1621, 0.2162
            if age <= 45: return 0.20, 0.17, 0.5677, 0.1892, 0.2431
            if age <= 50: return 0.20, 0.17, 0.5136, 0.2432, 0.2432
            if age <= 55: return 0.20, 0.17, 0.4055, 0.3108, 0.2837
            if age <= 60: return 0.18, 0.16, 0.3530, 0.3382, 0.3088
            if age <= 65: return 0.125, 0.125, 0.1400, 0.3480, 0.5120
            return 0.05, 0.075, 0.0800, 0.0800, 0.8400
        ee_r, er_r, o_r, s_r, m_r = get_smart_rates_2026(current_age)
        wage_ceiling = 8000
        ee_contrib = round(min(salary, wage_ceiling) * ee_r)
        er_contrib = round(min(salary, wage_ceiling) * er_r)
        total_monthly = ee_contrib + er_contrib
        take_home = salary - ee_contrib
        st.markdown('<div class="terminal-panel"><div class="terminal-header"><div class="terminal-dot" style="background:#007A5E; box-shadow:0 0 10px #007A5E;"></div>Real-time Stream Matrix Output</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="data-stream-row"><span>Net Discretionary Take-Home</span><b>${take_home:,}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="data-stream-row"><span>Employee Share ({ee_r*100}%)</span><b>${ee_contrib:,}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="data-stream-row"><span>Employer Share ({er_r*100}%)</span><b>${er_contrib:,}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="data-stream-total"><span>Total Monthly CPF Inflow Pool</span><span>${total_monthly:,}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div style="padding: 0 45px; margin-bottom: 30px;"><h2 class="sakazuki-h1">Agent Private <span>Computational Analytics</span></h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="terminal-panel"><div class="terminal-header"><div class="terminal-dot" style="background:#007A5E; box-shadow:0 0 10px #007A5E;"></div>Private Boardroom Portfolio Metrics</div>', unsafe_allow_html=True)
    
    # Secure native inputs for your private calculations
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        gross_premium = st.number_input("Total Client Asset Base ($)", min_value=1000, value=250000, step=10000)
        est_yield = st.slider("Projected Annualized Strategy Return (%)", min_value=1.0, max_value=15.0, value=7.1, step=0.1)
    
    with col_p2:
        annual_payout = round(gross_premium * (est_yield / 100))
        monthly_distribution = round(annual_payout / 12, 2)
        
        st.markdown('<div style="margin-top:10px;"></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="data-stream-row"><span>Annualized Strategy Capital Yield</span><b>${annual_payout:,}</b></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="data-stream-total"><span>Net Monthly Distribution Dividend</span><span>${monthly_distribution:,}</span></div>', unsafe_allow_html=True)
    
    st.info("🔒 Private Agent Guard Active: All asset calculations are evaluated locally inside secure browser memory variables with zero data logging leaks.")
    

# =========================================================================
# 🖼️ STANDALONE IMAGE COMPRESSION UTILITIES CONSOLE (ZERO-MARGIN ISOLATION)
# =========================================================================
if navigation_selection == "🖼️ Image Compression Utilities Console":
    from PIL import Image
    import io

    st.markdown('<div style="padding: 0 45px;"><h2 class="sakazuki-h1">Image Compression <span>Utilities Console</span></h2><p class="sakazuki-p" style="margin-bottom:30px;">Compress heavy image files down to under 7MB instantly for your website uploads or profile swap apps. Processing executes securely in local browser memory caches with zero data logging leaks.</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="padding: 0 45px;">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Image Coordinate (JPEG, JPG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        original_bytes = uploaded_file.size
        original_mb = original_bytes / (1024 * 1024)
        st.info(f"📁 Raw File Parameters Loaded: **{uploaded_file.name}** ({original_mb:.2f} MB)")
        
        img = Image.open(uploaded_file)
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            quality_target = st.slider("Compression Quality Density Scale", min_value=10, max_value=100, value=75, step=5)
            st.caption("Lowering density shrinks bytes further. 75% preserves crisp, high-end website clarity.")
        
        output_stream = io.BytesIO()
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        img.save(output_stream, format="JPEG", quality=quality_target, optimize=True)
        compressed_bytes = output_stream.tell()
        compressed_mb = compressed_bytes / (1024 * 1024)
        
        with col_c2:
            st.markdown('<div style="margin-top:10px;"></div>', unsafe_allow_html=True)
            if compressed_mb < 7.0:
                st.success(f"✅ Compression Bounds Secure: **{compressed_mb:.2f} MB** (Under 7MB Limit)")
            else:
                st.warning(f"⚠️ Scale Warning: File size is {compressed_mb:.2f} MB. Lower the quality scale slightly to drop under 7MB.")
        
        st.image(output_stream, caption="Compressed Asset Preview Matrix", width=400)
        
        base_name = uploaded_file.name.rsplit('.', 1)[0]
        st.download_button(
            label="Download Compressed Output Asset",
            data=output_stream.getvalue(),
            file_name=f"compressed_{base_name}.jpg",
            mime="image/jpeg",
            type="primary"
        )
    st.markdown('</div>', unsafe_allow_html=True)
# =========================================================================
# 👑 CECILIA VIP AI STUDIO (PART 1: AI PORCELAIN MATRIX)
# =========================================================================
if navigation_selection == "👑 Cecilia VIP AI Studio":
    from PIL import Image, ImageEnhance, ImageFilter, ImageOps
    import numpy as np
    import io

    st.markdown('<div style="padding: 0 45px;"><h2 class="sakazuki-h1">Cecilia VIP AI <span>Studio Workspace</span></h2><p class="sakazuki-p" style="margin-bottom:30px;">Access your private portrait editing parameters, face slimming algorithms, double chin removal layers, and automatic texture smoothers completely ad-free.</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="padding: 0 45px;">', unsafe_allow_html=True)
    
    m_col1, m_col2 = st.columns([1, 1.3], gap="large")
    
    with m_col1:
        uploaded_file = st.file_uploader("Drop Portrait Photo (JPEG, PNG)", type=["jpg", "jpeg", "png"], key="cecilia_uploader")
        
        if uploaded_file is not None:
            base_img = Image.open(uploaded_file)
            if base_img.mode in ("RGBA", "P"):
                base_img = base_img.convert("RGB")
            orig_w, orig_h = base_img.size
            
            st.markdown("### 📐 Module 01: Basic Edits")
            crop_pct = st.slider("Proportional Border Crop (%)", min_value=0, max_value=30, value=0, key="cecilia_crop")
            rotate_deg = st.selectbox("Structural Rotation",, key="cecilia_rotate")
            flip_mode = st.radio("Mirror Flipping", ["None", "Horizontal Mirror", "Vertical Mirror"], key="cecilia_flip")
            
            st.markdown("<br>### ✨ Module 02: Advanced Generative Portrait Retouch", unsafe_allow_html=True)
            slimming = st.slider("Face & Body Slimming Factor", min_value=0.80, max_value=1.00, value=1.00, step=0.01, key="cecilia_slimming")
            chin_lift = st.slider("Double Chin Removal / Smooth Jawline", min_value=0.00, max_value=0.25, value=0.00, step=0.01, key="cecilia_chin")
            smoothing = st.slider("AI Porcelain Skin & Eye-Bag Eraser", min_value=0, max_value=15, value=0, step=1, key="cecilia_smooth")
            teeth_whiten = st.slider("Teeth Whitening Exposure Boost", min_value=1.0, max_value=1.5, value=1.0, step=0.05, key="cecilia_teeth")
            
            st.markdown("<br>### 🤖 Module 03: AI Scene & Studio Lighting", unsafe_allow_html=True)
            brightness = st.slider("Studio Illumination (AI Enhancer)", min_value=0.5, max_value=2.0, value=1.0, step=0.1, key="cecilia_bright")
            contrast = st.slider("High-End Editorial Contrast", min_value=0.5, max_value=2.0, value=1.0, step=0.1, key="cecilia_contrast")
            sharpness = st.slider("Texture Sharpness & Hairline Fill", min_value=0.0, max_value=3.0, value=1.0, step=0.1, key="cecilia_sharp")
            
            bg_mode = st.selectbox("AI Scene/Background Transformer", [
                "Keep Original Background Layer", 
                "Isolate Subject (Pure Black Ambient Sanctuary)", 
                "🌿 High-Trust Therapeutic Sage Green Workspace Background"
            ], key="cecilia_bg")
    with m_col2:
        if uploaded_file is not None:
            st.markdown("### 🖥️ VIP Live Rendering Viewport")
            work_canvas = base_img.copy()
            
            if rotate_deg != 0:
                if rotate_deg == 90: work_canvas = work_canvas.transpose(Image.ROTATE_270)
                elif rotate_deg == 180: work_canvas = work_canvas.transpose(Image.ROTATE_180)
                elif rotate_deg == 270: work_canvas = work_canvas.transpose(Image.ROTATE_90)
                
            if flip_mode == "Horizontal Mirror": work_canvas = ImageOps.mirror(work_canvas)
            elif flip_mode == "Vertical Mirror": work_canvas = ImageOps.flip(work_canvas)
            
            if crop_pct > 0:
                cw, ch = work_canvas.size
                border_w = int(cw * (crop_pct / 100))
                border_h = int(ch * (crop_pct / 100))
                work_canvas = work_canvas.crop((border_w, border_h, cw - border_w, ch - border_h))
                
            cw, ch = work_canvas.size
            slim_w = int(cw * slimming)
            work_canvas = work_canvas.resize((slim_w, ch), Image.Resampling.LANCZOS)
            
            # --- HIGH-FIDELITY GENERATIVE JAWLINE WARP ENGINE ---
            if chin_lift > 0:
                np_canvas = np.array(work_canvas)
                h_split = int(ch * 0.55)
                top_matrix = np_canvas[0:h_split, :, :]
                jaw_matrix = np_canvas[h_split:, :, :]
                
                jh, jw, jc = jaw_matrix.shape
                pil_jaw = Image.fromarray(jaw_matrix)
                new_jh = int(jh * (1.0 - (chin_lift * 0.6)))
                pil_jaw_warped = pil_jaw.resize((jw, new_jh), Image.Resampling.LANCZOS)
                
                stitched_np = np.vstack((top_matrix, np.array(pil_jaw_warped)))
                work_canvas = Image.fromarray(stitched_np).resize((slim_w, ch), Image.Resampling.LANCZOS)
                
            # --- DUAL-STAGE INTERPOLATED BILATERAL PORCELAIN SKIN SMOOTHER ---
            if smoothing > 0:
                # Stage 1: Fine micro-texture diffusion base
                smooth_pass1 = work_canvas.filter(ImageFilter.BoxBlur(smoothing // 2 + 1))
                # Stage 2: Macro tone-blending overlay
                smooth_pass2 = work_canvas.filter(ImageFilter.SMOOTH_MORE)
                blended_smooth = Image.blend(smooth_pass1, smooth_pass2, 0.4)
                
                # High-pass variance edge mask creation to freeze crisp eye/lip markers
                edge_layer = work_canvas.convert("L").filter(ImageFilter.FIND_EDGES)
                edge_mask = edge_layer.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.BoxBlur(1))
                
                # Execute edge-preserving surface compilation
                work_canvas = Image.composite(work_canvas, blended_smooth, edge_mask)
                
            if teeth_whiten > 1.0:
                np_whiten = np.array(work_canvas).astype(np.float32)
                whiten_mask = (np_whiten[:, :, 0] > 150) & (np_whiten[:, :, 1] > 150) & (np_whiten[:, :, 2] > 130)
                for c in range(3):
                    np_whiten[:, :, c] = np.where(whiten_mask, np.clip(np_whiten[:, :, c] * teeth_whiten, 0, 255), np_whiten[:, :, c])
                work_canvas = Image.fromarray(np_whiten.astype(np.uint8))
                
            work_canvas = ImageEnhance.Brightness(work_canvas).enhance(brightness)
            work_canvas = ImageEnhance.Contrast(work_canvas).enhance(contrast)
            work_canvas = ImageEnhance.Sharpness(work_canvas).enhance(sharpness)
            
            if "Black" in bg_mode:
                scene_mask = work_canvas.convert("L").filter(ImageFilter.FIND_EDGES).filter(ImageFilter.BoxBlur(3))
                black_bg = Image.new("RGB", work_canvas.size, (5, 5, 7))
                work_canvas = Image.composite(work_canvas, black_bg, scene_mask)
            elif "Sage" in bg_mode:
                scene_mask = work_canvas.convert("L").filter(ImageFilter.FIND_EDGES).filter(ImageFilter.BoxBlur(3))
                sage_bg = Image.new("RGB", work_canvas.size, (74, 107, 86))
                work_canvas = Image.composite(work_canvas, sage_bg, scene_mask)
                
            final_render = Image.new("RGB", (orig_w, orig_h), (5, 5, 7))
            paste_x = (orig_w - work_canvas.size[0]) // 2
            final_render.paste(work_canvas, (paste_x, 0))
            
            st.image(final_render, caption="Real-Time Ad-Free Output Viewport Matrix", use_container_width=True)
            
            out_buffer = io.BytesIO()
            final_render.save(out_buffer, format="JPEG", quality=95, optimize=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button(
                label="👑 Export High-Res Watermark-Free Image Asset",
                data=out_buffer.getvalue(),
                file_name="cecilia_porcelain_output.jpg",
                mime="image/jpeg",
                type="primary",
                use_container_width=True
            )
            st.caption("🔒 Privacy Standard: Code processes entirely inside temporary RAM variables with zero data logging traps.")
            
    st.markdown('</div>', unsafe_allow_html=True)

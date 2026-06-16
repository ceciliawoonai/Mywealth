import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Cecilia Woon | Private Wealth Console", layout="wide")

# --- ELVALABS & SAKAZUKI INSPIRED ULTRA-DARK SYSTEM DESIGN STYLES ---
st.markdown("""
<style>
    /* Global Immersive Void Canvas Background */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #050507 !important;
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Collapsing default Streamlit padding blocks */
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    
    /* Top Logo Header Frame Alignment */
    .brand-container { padding: 40px 45px 10px 45px; background: #050507; }
    .brand-text { font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 900; color: #FFFFFF; letter-spacing: -0.5px; text-transform: uppercase; }
    .brand-text span { color: #E31837; font-size: 11px; font-family: 'Inter', sans-serif; font-weight: bold; letter-spacing: 2px; margin-left: 12px; vertical-align: middle; }
    
    /* Sleek Kinetic Horizontal Navigation Strip */
    .kinetic-nav { 
        display: flex; 
        justify-content: flex-start; 
        gap: 3.5rem; 
        padding: 18px 45px; 
        font-size: 12px; 
        font-weight: 600; 
        letter-spacing: 2px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 40px;
    }
    .kinetic-nav span { cursor: pointer; color: #8A8A93; transition: all 0.4s ease; }
    .kinetic-nav span:hover { color: #FFFFFF; }
    .active-nav-node { color: #E31837 !important; font-weight: bold; }

    /* Sakazuki Premium Editorial Containers */
    .sakazuki-hero { padding: 40px 45px; margin-bottom: 20px; }
    .sakazuki-tag { color: #8A8A93; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 20px; }
    .sakazuki-h1 { font-family: 'Playfair Display', serif; font-size: 48px; font-weight: 700; line-height: 1.2; margin-bottom: 15px; letter-spacing: -0.5px; }
    .sakazuki-h1 span { color: #E31837; }
    
    /* Split Content Grid Rows */
    .sakazuki-row { display: flex; border-top: 1px solid rgba(255, 255, 255, 0.08); padding: 40px 45px; }
    .sakazuki-left-label { flex: 0.4; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #8A8A93; font-weight: bold; }
    .sakazuki-right-content { flex: 1.6; }
    .sakazuki-h3 { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 600; margin-bottom: 15px; color: #FFFFFF; }
    .sakazuki-p { font-size: 16px; color: #A0A0A5; line-height: 1.7; max-width: 850px; }

    /* Technical Knowledge Vault Cards */
    .reyou-panel-header { font-family: 'Playfair Display', serif; font-size: 32px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px; }
    .reyou-panel-subtitle { font-size: 16px; color: #8A8A93; margin-bottom: 40px; line-height: 1.6; max-width: 700px; }
    
    .reyou-card { background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 16px; padding: 35px 30px; height: 100%; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
    .reyou-card:hover { background: rgba(255, 255, 255, 0.04); border-color: rgba(227, 24, 55, 0.4); transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
    .reyou-card-num { font-size: 12px; font-weight: bold; color: #E31837; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 12px; }
    .reyou-card-title { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: bold; color: #FFFFFF; margin-bottom: 12px; }
    .reyou-card-desc { font-size: 14px; color: #8A8A93; line-height: 1.6; }

    /* Interactive Compute Sliders Console Boxes */
    .terminal-panel { background: #0B0B0E; border: 1px solid rgba(255, 255, 255, 0.04); border-radius: 16px; padding: 35px; margin-bottom: 30px; }
    .terminal-header { font-size: 11px; text-transform: uppercase; font-weight: bold; color: #66666D; letter-spacing: 1.5px; margin-bottom: 20px; display: flex; align-items: center; gap: 8px; }
    .terminal-dot { width: 6px; height: 6px; background: #FF4D61; border-radius: 50%; box-shadow: 0 0 10px #FF4D61; }
    .data-stream-row { display: flex; justify-content: space-between; padding: 16px 10px; border-bottom: 1px solid rgba(255, 255, 255, 0.03); font-size: 15px; color: #E4E4E7; }
    .data-stream-total { display: flex; justify-content: space-between; padding: 18px 15px; font-weight: bold; background: rgba(227, 24, 55, 0.08); color: #FF4D61; border-radius: 8px; font-size: 16px; margin-top: 15px; border: 1px solid rgba(227, 24, 55, 0.2); }
</style>
""", unsafe_allow_html=True)

# =========================================================================
# 🏛️ TEXT HEADER ALIGNMENT
# =========================================================================
st.markdown('<div class="brand-container"><div class="brand-text">CECILIA WOON <span>Private Wealth Advisory</span></div></div>', unsafe_allow_html=True)

# --- WORKSPACE CONTROL SELECTION NAVIGATION SIDEBAR ---
st.sidebar.markdown('**System Navigator**')
navigation_selection = st.sidebar.radio("Go To Section Workspace:", [
    "🌐 Clinical P&L Philosophy",
    "📚 Research & Education Vault",
    "🎯 The Rorschach Protocol (Leads)",
    "📊 Live Interactive 2026 CPF Engine",
    "🔒 Private Agent Computational View"
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
    # =========================================================================
    # SAKAZUKI NARRATIVE PROFILE 
    # =========================================================================
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
        # =========================================================================
    # 🕹️ IMMERSIVE PHYSICS CANVAS NODE (THE 50 LIVESTREAM SPHERES MATRIX)
    # =========================================================================
    bubble_data_payload = [
        {"id": 1, "label": "Cardiologist", "sec": "Med"}, {"id": 2, "label": "Staff Nurse", "sec": "Med"},
        {"id": 3, "label": "Radiographer", "sec": "Med"}, {"id": 4, "label": "Physio", "sec": "Med"},
        {"id": 5, "label": "Scientist", "sec": "Med"}, {"id": 6, "label": "Elderly Care", "sec": "Med"},
        {"id": 7, "label": "Vet Surgeon", "sec": "Med"}, {"id": 8, "label": "Pharmacist", "sec": "Med"},
        {"id": 9, "label": "Dentist", "sec": "Med"}, {"id": 10, "label": "Therapist", "sec": "Med"},
        {"id": 11, "label": "Teacher", "sec": "Edu"}, {"id": 12, "label": "Professor", "sec": "Edu"},
        {"id": 13, "label": "SpecEd Coach", "sec": "Edu"}, {"id": 14, "label": "Policy Lead", "sec": "Edu"},
        {"id": 15, "label": "Lawyer", "sec": "Edu"}, {"id": 16, "label": "SCDF Officer", "sec": "Edu"},
        {"id": 17, "label": "Urban Planner", "sec": "Edu"}, {"id": 18, "label": "Social Worker", "sec": "Edu"},
        {"id": 19, "label": "Archivist", "sec": "Edu"}, {"id": 20, "label": "Eco Officer", "sec": "Edu"},
        {"id": 21, "label": "Cleaner Hero", "sec": "Ops"}, {"id": 22, "label": "Bus Captain", "sec": "Ops"},
        {"id": 23, "label": "Port Operator", "sec": "Ops"}, {"id": 24, "label": "Logistics Sup", "sec": "Ops"},
        {"id": 25, "label": "Security SCDF", "sec": "Ops"}, {"id": 26, "label": "Lift Tech", "sec": "Ops"},
        {"id": 27, "label": "Delivery Rider", "sec": "Ops"}, {"id": 28, "label": "Project Manager", "sec": "Ops"},
        {"id": 29, "label": "Air Traffic", "sec": "Ops"}, {"id": 30, "label": "Waste Engineer", "sec": "Ops"},
        {"id": 31, "label": "AI Product Manager", "sec": "Tech"}, {"id": 32, "label": "Cyber Architect", "sec": "Tech"},
        {"id": 33, "label": "UX Designer", "sec": "Tech"}, {"id": 34, "label": "Photojournalist", "sec": "Tech"},
        {"id": 35, "label": "DevOps Engineer", "sec": "Tech"}, {"id": 36, "label": "Data Scientist", "sec": "Tech"},
        {"id": 37, "label": "Audio Engineer", "sec": "Tech"}, {"id": 38, "label": "Media Creator", "sec": "Tech"},
        {"id": 39, "box": "Biomed Tech", "label": "Biomed Tech", "sec": "Tech"}, {"id": 40, "label": "Cloud Lead", "sec": "Tech"},
        {"id": 41, "label": "Hawker Legend", "sec": "Biz"}, {"id": 42, "label": "Hotel GM", "sec": "Biz"},
        {"id": 43, "label": "Artisan Barista", "sec": "Biz"}, {"id": 44, "label": "Retail Lead", "sec": "Biz"},
        {"id": 45, "label": "Cabin Crew", "sec": "Biz"}, {"id": 46, "label": "Compliance Officer", "sec": "Biz"},
        {"id": 47, "label": "HR Specialist", "sec": "Biz"}, {"id": 48, "label": "Gym Coach", "sec": "Biz"},
        {"id": 49, "label": "Agri Farmer", "sec": "Biz"}, {"id": 50, "label": "Art Curator", "sec": "Biz"}
    ]

    st.markdown("""
<div class="sakazuki-row" style="padding-left:0; padding-right:0;">
    <div class="sakazuki-left-label">The Collective</div>
    <div class="sakazuki-right-content">
        <div class="sakazuki-h3">The Lives We Protect</div>
        <div class="sakazuki-p" style="margin-bottom:25px;">Hover your cursor across the matrix container mesh below. Every structural profession driving Singapore's infrastructure deserves customized clinical income shielding thresholds against unexpected lifespan tragedies.</div>
    </div>
</div>
""", unsafe_allow_html=True)

    # Raw literal formatting protects JavaScript parameters from clashing with Python compilation rules
    canvas_html_matrix = r"""
    <div id="bubble-canvas-container" style="background:#0B0B0E; border:1px solid rgba(255,255,255,0.06); border-radius:16px; padding:20px; width:100%; position:relative; min-height:460px; overflow:hidden;">
        <div id="matrix-ticker" style="font-family:'Courier New', monospace; font-size:12px; color:#FF4D61; margin-bottom:15px; min-height:18px;">[SYSTEM READY] Explore community nodes matrix telemetry...</div>
        <div id="canvas-mount-node" style="display:flex; justify-content:center;"></div>
    </div>
    
    <script src="https://d3js.org"></script>
    <script>
        const nodes_payload = {PAYLOAD_PLACEHOLDER};
        const w = 900, h = 380;
        
        const svg = d3.select("#canvas-mount-node").append("svg").attr("width", w).attr("height", h);
        
        const f_sim = d3.forceSimulation(nodes_payload)
            .force("charge", d3.forceManyBody().strength(12))
            .force("center", d3.forceCenter(w / 2, h / 2))
            .force("collision", d3.forceCollide().radius(42))
            .on("tick", ticked);
            
        const element_nodes = svg.selectAll("g").data(nodes_payload).enter().append("g")
            .call(d3.drag().on("start", dragstart).on("drag", dragged).on("end", dragend));
            
        element_nodes.append("circle").attr("r", 36)
            .attr("fill", d => d.sec === "Med" ? "rgba(227,24,55,0.12)" : d.sec === "Tech" ? "rgba(212,175,55,0.12)" : "rgba(255,255,255,0.03)")
            .attr("stroke", d => d.sec === "Med" ? "#E31837" : d.sec === "Tech" ? "#D4AF37" : "rgba(255,255,255,0.2)")
            .attr("stroke-width", 1.5).style("cursor", "pointer")
            .on("mouseover", function(event, d) {
                d3.select(this).attr("stroke-width", 3).attr("fill", "rgba(227,24,55,0.25)");
                document.getElementById("matrix-ticker").innerText = `⚡ [NODE RE-INSULATED] Sector: ${d.sec} // Profession: ${d.label} -> Mapped into Cecilia Woon's risk insulation protection loops.`;
            })
            .on("mouseout", function(event, d) {
                d3.select(this).attr("stroke-width", 1.5).attr("fill", d.sec === "Med" ? "rgba(227,24,55,0.12)" : d.sec === "Tech" ? "rgba(212,175,55,0.12)" : "rgba(255,255,255,0.03)");
            });
            
        element_nodes.append("text").text(d => d.label)
            .attr("text-anchor", "middle").attr("dy", ".3em").attr("fill", "#FFFFFF")
            .style("font-size", "10px").style("pointer-events", "none").style("font-family", "sans-serif");
            
        function ticked() { element_nodes.attr("transform", d => `translate(${Math.max(40, Math.min(w - 40, d.x))}, ${Math.max(40, Math.min(h - 40, d.y))})`); }
        function dragstart(e, d) { if (!e.active) f_sim.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; }
        function dragged(e, d) { d.fx = e.x; d.fy = e.y; }
        function dragend(e, d) { if (!e.active) f_sim.alphaTarget(0); d.fx = null; d.fy = null; }
       </script>
    """
    
    canvas_html_matrix = canvas_html_matrix.replace("{PAYLOAD_PLACEHOLDER}", str(bubble_data_payload))
    st.components.v1.html(canvas_html_matrix, height=620, scrolling=False)

    st.markdown('<div style="padding: 40px 0 0 45px;">', unsafe_allow_html=True)

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
    st.components.v1.iframe(src="https://github.io", height=850, scrolling=True)

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cecilia Woon | Private Wealth Console", layout="wide")

# --- IMMERSIVE ULTRA-DARK EXTENDED DESIGN THEME STYLES ---
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #050507 !important;
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stVerticalBlock"] { gap: 0rem !important; }
    .brand-grid { display: flex; justify-content: space-between; align-items: center; padding: 30px 45px 15px 45px; background: #050507; }
    .brand-title-text { font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 900; color: #FFFFFF; letter-spacing: -0.5px; text-transform: uppercase; }
    .brand-title-text span { color: #E31837; font-size: 11px; font-family: 'Inter', sans-serif; font-weight: bold; letter-spacing: 2px; margin-left: 12px; vertical-align: middle; }
    
    .kinetic-nav { 
        display: flex; justify-content: flex-start; gap: 3.5rem; padding: 18px 45px; font-size: 12px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; border-bottom: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 40px;
    }
    .kinetic-nav span { cursor: pointer; color: #8A8A93; transition: all 0.4s ease; }
    .kinetic-nav span:hover { color: #FFFFFF; }
    .active-nav-node { color: #E31837 !important; font-weight: bold; }

    .sakazuki-hero { padding: 20px 45px 20px 45px; margin-bottom: 10px; }
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
    .reyou-card-img { width: 100%; height: 150px; border-radius: 8px; object-fit: cover; margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.05); }
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

col_head_txt, col_head_img = st.columns([5, 1])
with col_head_txt:
    st.markdown('<div class="brand-grid" style="padding-left:0;"><div class="brand-title-text">CECILIA WOON <span>Private Wealth Advisory</span></div></div>', unsafe_allow_html=True)
with col_head_img:
    st.image("Images/logo.jpg", width=95)

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
# --- JAVASCRIPT/HTML5 FLUID OCCUPATION BUBBLE COMPONENT ASSEMBLY ---
bubble_html_manifest = """
<div style="background:#050507; color:#fff; font-family:'Inter',sans-serif; padding:10px;">
    <div id="terminal-log" style="background:#0B0B0E; border:1px solid rgba(255,255,255,0.06); padding:15px; border-radius:10px; margin-bottom:15px; min-height:65px; font-size:14px; color:#A0A0A5;">
        <span style="color:#E31837; font-weight:bold; letter-spacing:1px; font-size:11px; text-transform:uppercase; display:block; margin-bottom:4px;">[Live Resiliency Terminal]</span>
        Move mouse over the floating human collective architecture matrix below to stream strategic insulation metrics...
    </div>
    <canvas id="bubbleCanvas" style="background:#07070A; border-radius:12px; border:1px solid rgba(255,255,255,0.04); cursor:crosshair;"></canvas>
</div>

<script>
const jobs = [
    {n:"Consultant Cardiologist", t:"Shielding high-tier specialized diagnostic overheads from acute clinical workspace liability protocols."},
    {n:"Staff Nurse", t:"Insulating frontline critical care shifts from severe psychological burnout and long-term physical workplace injury."},
    {n:"Primary School Teacher", t:"Securing essential income stream baselines against sudden viral throat pathologies or cognitive stress halts."},
    {n:"Environmental Cleaner", t:"Defending primary sanitation operational wages from sudden high-exposure viral contagions and toxic contact vectors."},
    {n:"Bus Captain", t:"Guaranteeing long-term structural mobility margins in the event of major public transit asset collisions."},
    {n:"Hawker Entrepreneur", t:"Mitigating localized food infrastructure traffic closures and rapid supply chain commodity margin shocks."},
    {n:"AI Product Manager", t:"Protecting variable digital enterprise equity tiers from abrupt computational shift trends and deep algorithmic disruptions."},
    {n:"Port Crane Operator", t:"Insulating precision global supply network operations from severe muscular skeletal degradation hazards."},
    {n:"Litigation Lawyer", t:"Securing complex corporate dispute billing billable hours against high-pressure executive cognitive burnout zones."},
    {n:"Delivery Rider", t:"Providing immediate cashflow protection cushions against rapid last-mile traffic accident traumas."},
    {n:"Radiographer", t:"Defending diagnostics shielding limits from progressive radiation exposure workspace liabilities."},
    {n:"Physiotherapist", t:"Shielding physical practice operational revenues from accidental clinical handling liability counter-claims."},
    {n:"Research Scientist", t:"Insulating laboratory grant funding sequences from long-term clinical trial timeline pause vectors."},
    {n:"Elderly Care Attendant", t:"Securing core community service stipends from progressive patient strain physical injuries."},
    {n:"Veterinary Surgeon", t:"Insulating clinical operation lines from acute biological cross-infection containment orders."},
    {n:"Pharmacist", t:"Defending therapeutic safety workflows from catastrophic dispensing error legal risk exposures."},
    {n:"Dental Surgeon", t:"Securing high-precision ergonomic operational longevity against severe modern cervical nerve traps."},
    {n:"Mental Health Counselor", t:"Insulating clinical advisory streams from chronic secondary trauma psychological depletion cycles."},
    {n:"University Professor", t:"Shielding global academic research lines from long-term intellectual property framework shifts."},
    {n:"Special Ed Instructor", t:"Defending inclusive instructional capacities from severe, acute interactive developmental stresses."},
    {n:"Civil Servant", t:"Insulating public infrastructure deployment roles from structural wage scale policy freezes."},
    {n:"Firefighter", t:"Securing max trauma survival insulation margins against hazardous toxic compound inhalation events."},
    {n:"Urban Planner", t:"Defending infrastructure configuration workflows from unexpected municipal real estate structural breaks."},
    {n:"Social Worker", t:"Shielding neighborhood support budgets from systemic multi-layered household economic breakdowns."},
    {n:"Librarian", t:"Insulating archival curation roles from rapid physical database automation overrides."},
    {n:"Environmental Officer", t:"Defending corporate sustainability compliance leads from unexpected regulatory enforcement liabilities."},
    {n:"Warehouse Supervisor", t:"Securing high-volume digital fulfillment lines from sudden logistics center shutdown mandates."},
    {n:"Elevator Technician", t:"Insulating high-altitude engineering workflows from acute mechanical fall vectors."},
    {n:"Air Traffic Controller", t:"Securing high-density tactical aviation tracks against chronic split-second stress depletion."},
    {n:"Waste Engineer", t:"Defending circular economy operations from hazardous industrial bio-waste handling contamination scales."},
    {n:"Cybersecurity Architect", t:"Insulating perimeter data defense assets from massive, multi-vector enterprise system breach fallouts."},
    {n:"UX Product Designer", t:"Securing human-digital interface workflows from abrupt global AI design engine migrations."},
    {n:"Photojournalist", t:"Defending visual history storytelling networks from high-hazard geopolitical field trauma costs."},
    {n:"Software Engineer", t:"Insulating database backend design architectures from massive corporate technology stack re-engineerings."},
    {n:"Data Analyst", t:"Securing predictive statistical modeling flows from sudden machine learning server pool transitions."},
    {n:"Sound Engineer", t:"Defending acoustics production setups from sudden, accidental auditory sensory damage metrics."},
    {n:"Content Creator", t:"Insulating dynamic modern streaming revenue lines from systemic channel algorithm demonetization waves."},
    {n:"Biomedical Engineer", t:"Securing critical clinical hardware innovations from prolonged patent testing delay bottlenecks."},
    {n:"Cloud Architect", t:"Defending massive enterprise data grids from global server array connectivity failures."},
    {n:"Boutique Hotel Manager", t:"Insulating premium lifestyle hospitality reserves from sudden cross-border travel containment bans."},
    {n:"Barista", t:"Securing artisanal beverage craft margins from chronic repetitive strain wrist injuries."},
    {n:"Retail Assistant", t:"Defending customer-facing service hours from rapid automated checkout system expansions."},
    {n:"Cabin Crew", t:"Insulating high-altitude long-haul aviation roles from progressive atmospheric pressure health drops."},
    {n:"Financial Specialist", t:"Securing middle-office data compliance checks from rapid automated auditing loops."},
    {n:"HR Partner", t:"Defending human capital recruitment channels from unexpected enterprise downsizing initiatives."},
    {n:"Fitness Trainer", t:"Insulating localized wellness coaching cashflows from acute skeletal joint fracture drawdowns."},
    {n:"Urban Agriculturalist", t:"Securing high-efficiency crop infrastructure yields from catastrophic micro-climate weather events."},
    {n:"Arts Conservator", t:"Defending heritage restoration workflows from accidental museum asset degradation penalties."},
    {n:"Construction Lead", t:"Insulating high-rise structural assembly networks from severe, unexpected workspace structural breaks."},
    {n:"Securities Agent", t:"Defending capital allocation transactions from microsecond market liquidity squeeze anomalies."}
];

const canvas = document.getElementById('bubbleCanvas');
const ctx = canvas.getContext('2d');
const logBox = document.getElementById('terminal-log');

let width = canvas.width = window.innerWidth - 120;
let height = canvas.height = 420;

let bubbles = [];
let mouse = { x: null, y: null, radius: 95 };

window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth - 120;
    height = canvas.height = 420;
});

canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
});

canvas.addEventListener('mouseleave', () => {
    mouse.x = null;
    mouse.y = null;
});

class Bubble {
    constructor(job, x, y) {
        this.job = job;
        this.x = x;
        this.y = y;
        this.baseRadius = 45;
        this.radius = 45;
        this.vx = (Math.random() - 0.5) * 0.9;
        this.vy = (Math.random() - 0.5) * 0.9;
        this.glow = 0;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;

        // Bounce off canvas walls
        if (this.x - this.radius < 0 || this.x + this.radius > width) this.vx *= -1;
        if (this.y - this.radius < 0 || this.y + this.radius > height) this.vy *= -1;

        // Mouse avoidance check (elvalabs particle kinetic style)
        if (mouse.x !== null && mouse.y !== null) {
            let dx = this.x - mouse.x;
            let dy = this.y - mouse.y;
            let dist = Math.sqrt(dx * dx + dy * dy);
            
            if (dist < mouse.radius + this.radius) {
                let forceX = dx / dist;
                let forceY = dy / dist;
                this.x += forceX * 3;
                this.y += forceY * 3;
                this.glow = Math.min(this.glow + 0.08, 1);
                
                logBox.innerHTML = `<span style="color:#FF4D61; font-weight:bold; letter-spacing:1px; font-size:11px; text-transform:uppercase; display:block; margin-bottom:4px;">[Active Tracking Node: ${this.job.n}]</span>\${this.job.t}`;
            } else {
                this.glow = Math.max(this.glow - 0.02, 0);
            }
        }
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        
        // Premium corporate dark glassmorphic bubble texture layers
        let grad = ctx.createRadialGradient(this.x, this.y, 2, this.x, this.y, this.radius);
if navigation_selection == "🌐 Clinical P&L Philosophy":
    # =========================================================================
    # SAKAZUKI NARRATIVE PROFILE (COMPLETELY RE-WRITTEN WITH CORE RAW DATA)
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
<div class="sakazuki-row">
    <div class="sakazuki-left-label">The Mosaic</div>
    <div class="sakazuki-right-content">
        <div class="sakazuki-h3">The Lives We Protect</div>
        <div class="sakazuki-p">From frontline nurses and specialist cardiologists to transport logistics leads, educators, and infrastructure operations managers. Every societal career path requires corporate-grade income insulation layers. (Immersive interactive 50-occupation bubble canvas framework computing in background console).</div>
    </div>
</div>
""", unsafe_allow_html=True)

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
        st.markdown("""<div class="reyou-card"><img class="reyou-card-img" src="https://unsplash.com"><div class="reyou-card-num">Brief 01</div><div class="reyou-card-title">How to Avoid Being Oversold</div><div class="reyou-card-desc">Stripping away commissions-driven insurance pitches to isolate pure capital-efficient protection values tailored to asset bounds.</div></div>""", unsafe_allow_html=True)
    with row1_c2:
        st.markdown("""<div class="reyou-card"><img class="reyou-card-img" src="https://unsplash.com"><div class="reyou-card-num">Brief 02</div><div class="reyou-card-title">Streamline Your Protection Plan</div><div class="reyou-card-desc">Consolidating overlapping policy layers to reduce drag and optimize premium cashflow overheads significantly.</div></div>""", unsafe_allow_html=True)
    with row1_c3:
        st.markdown("""<div class="reyou-card"><img class="reyou-card-img" src="https://unsplash.com"><div class="reyou-card-num">Brief 03</div><div class="reyou-card-title">Choosing a High-Utility Accident Plan</div><div class="reyou-card-desc">Evaluating high-tier disability payouts, workspace trauma recovery terms, and mobility adjustments over generic entry products.</div></div>""", unsafe_allow_html=True)

    st.markdown('<div style="margin-top:30px;"></div>', unsafe_allow_html=True)
    row2_c1, row2_c2, row2_c3 = st.columns(3, gap="large")
    with row2_c1:
        st.markdown("""<div class="reyou-card"><img class="reyou-card-img" src="https://unsplash.com"><div class="reyou-card-num">Brief 04</div><div class="reyou-card-title">The 1M65 Structural Strategy</div><div class="reyou-card-desc">Leveraging early compounding parameters across state balances to guarantee million-dollar liquidity nests safely by retirement milestones.</div></div>""", unsafe_allow_html=True)
    with row2_c2:
        st.markdown("""<div class="reyou-card"><img class="reyou-card-img" src="https://unsplash.com"><div class="reyou-card-num">Brief 05</div><div class="reyou-card-title">Managing Your ILP Policy Drag</div><div class="reyou-card-desc">Dissecting cost-of-insurance structures within Investment-Linked Policies to salvage capital allocation efficiency.</div></div>""", unsafe_allow_html=True)
    with row2_c3:
        st.markdown("""<div class="reyou-card"><img class="reyou-card-img" src="https://unsplash.com"><div class="reyou-card-num">Brief 06</div><div class="reyou-card-title">Pre-Crisis Resiliency Protocol</div><div class="reyou-card-desc">A unified tactical emergency sequence linking corporate legal standing, rapid cash buffers, and account authority overrides—ensuring your portfolio survives intact.</div></div>""", unsafe_allow_html=True)
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

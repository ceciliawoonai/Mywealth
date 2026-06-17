import json
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Cecilia Woon | Private Wealth Console", layout="wide")

# =========================================================================
# 🏛️ GLOBAL RAW TEMPLATE ISOLATION FRAMEWORK (AVATAR BUBBLE HOISTING)
# =========================================================================
GLOBAL_BUBBLE_CANVAS_HTML = r"""
<div class="sakazuki-row" style="padding-left:0; padding-right:0;">
    <div class="sakazuki-left-label">The Collective</div>
    <div class="sakazuki-right-content">
        <div class="sakazuki-h3">The Lives We Protect</div>
        <div class="sakazuki-p" style="margin-bottom:25px;">Hover your cursor across the matrix network container below. Every structural profession driving Singapore's infrastructure deserves customized clinical income shielding thresholds against unexpected lifespan tragedies.</div>
    </div>
</div>

<div id="bubble-canvas-container" style="background:#0B0B0E; border:1px solid rgba(255,255,255,0.06); border-radius:16px; padding:20px; width:100%; position:relative; min-height:480px; overflow:hidden;">
    <div id="matrix-ticker" style="font-family:'Courier New', monospace; font-size:12px; color:#FF4D61; margin-bottom:15px; min-height:18px;">[SYSTEM ACTIVE] Scan network profiles to evaluate structural risk models...</div>
    <div id="canvas-mount-node" style="display:flex; justify-content:center;"></div>
</div>

<script>
    (function() {
        const c_nodes = DATA_REPLACE_TOKEN;
        const cv = document.createElement("canvas");
        const ctx = cv.getContext("2d");
        const mount = document.getElementById("canvas-mount-node");
        
        cv.width = 900; cv.height = 380;
        cv.style.width = "100%"; cv.style.display = "block";
        mount.appendChild(cv);

        c_nodes.forEach((n, idx) => {
            n.x = 450 + (Math.random() - 0.5) * 200;
            n.y = 190 + (Math.random() - 0.5) * 150;
            n.vx = (Math.random() - 0.5) * 0.8;
            n.vy = (Math.random() - 0.5) * 0.8;
            n.baseRadius = 26;
            n.r = n.baseRadius;
            n.img = new Image();
            n.img.src = `https://unsplash.com{1500000000000 + (idx * 154321) % 9999999}?auto=format&fit=crop&w=80&h=80&q=80`;
        });
        
        let mouse = { x: -1000, y: -1000 };
        cv.addEventListener("mousemove", (e) => {
            const rect = cv.getBoundingClientRect();
            mouse.x = (e.clientX - rect.left) * (cv.width / rect.width);
            mouse.y = (e.clientY - rect.top) * (cv.height / rect.height);
        });
        cv.addEventListener("mouseleave", () => { mouse.x = -1000; mouse.y = -1000; });
        
        function loop() {
            ctx.clearRect(0, 0, cv.width, cv.height);
            ctx.strokeStyle = "rgba(255, 255, 255, 0.04)";
            ctx.lineWidth = 1;
            for(let i=0; i<c_nodes.length; i++) {
                for(let j=i+1; j<c_nodes.length; j++) {
                    let dx = c_nodes[i].x - c_nodes[j].x;
                    let dy = c_nodes[i].y - c_nodes[j].y;
                    let dist = Math.sqrt(dx*dx + dy*dy);
                    if(dist < 90) {
                        ctx.beginPath(); ctx.moveTo(c_nodes[i].x, c_nodes[i].y);
                        ctx.lineTo(c_nodes[j].x, c_nodes[j].y); ctx.stroke();
                    }
                }
            }
            
            let active_target = null;
            for (let i = 0; i < c_nodes.length; i++) {
                for (let j = i + 1; j < c_nodes.length; j++) {
                    let dx = c_nodes[j].x - c_nodes[i].x;
                    let dy = c_nodes[j].y - c_nodes[i].y;
                    let dist = Math.sqrt(dx*dx + dy*dy);
                    let minDist = c_nodes[i].r + c_nodes[j].r + 4;
                    if (dist < minDist) {
                        let overlap = minDist - dist;
                        let ax = (dx / dist) * overlap * 0.5;
                        let ay = (dy / dist) * overlap * 0.5;
                        c_nodes[i].x -= ax; c_nodes[i].y -= ay;
                        c_nodes[j].x += ax; c_nodes[j].y += ay;
                    }
                }
            }

            c_nodes.forEach(n => {
                n.x += n.vx; n.y += n.vy;
                if(n.x - n.baseRadius < 10 || n.x + n.baseRadius > cv.width - 10) n.vx *= -1;
                if(n.y - n.baseRadius < 10 || n.y + n.baseRadius > cv.height - 10) n.vy *= -1;
                
                let m_dx = mouse.x - n.x; let m_dy = mouse.y - n.y;
                let m_dist = Math.sqrt(m_dx*m_dx + m_dy*m_dy);
                
                if(m_dist < n.baseRadius * 1.5) {
                    active_target = n;
                    n.r = n.baseRadius * 1.3;
                    n.x += m_dx * 0.02; n.y += m_dy * 0.02;
                } else {
                    n.r = n.r * 0.9 + n.baseRadius * 0.1;
                }
                
                ctx.save(); ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2); ctx.clip();
                try { ctx.drawImage(n.img, n.x - n.r, n.y - n.r, n.r * 2, n.r * 2); } catch(e) { ctx.fillStyle = "#1A1A22"; ctx.fill(); }
                ctx.restore();
                
                ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
                ctx.strokeStyle = m_dist < n.baseRadius * 1.5 ? "#FF4D61" : n.sec === "Med" ? "#E31837" : n.sec === "Tech" ? "#D4AF37" : "rgba(255, 255, 255, 0.15)";
                ctx.lineWidth = m_dist < n.baseRadius * 1.5 ? 3 : 1.5; ctx.stroke();
            });
            
            if(active_target) {
                document.getElementById("matrix-ticker").style.color = "#FF4D61";
                document.getElementById("matrix-ticker").innerText = `\u26A1 [INSULATION CRITICAL] Sector: ${active_target.sec} // Profile: ${active_target.label} -> Monitored inside Cecilia's biological risk mitigation system loop.`;
            } else {
                document.getElementById("matrix-ticker").style.color = "#8A8A93";
                document.getElementById("matrix-ticker").innerText = "[SYSTEM ACTIVE] Scan network profiles to evaluate structural risk models...";
            }
            requestAnimationFrame(loop);
        }
        loop();
    })();
</script>
<script>
    if(false) {
"""
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
        {"id": 39, "label": "Biomed Tech", "sec": "Tech"}, {"id": 40, "label": "Cloud Lead", "sec": "Tech"},
        {"id": 41, "label": "Hawker Legend", "sec": "Biz"}, {"id": 42, "label": "Hotel GM", "sec": "Biz"},
        {"id": 43, "label": "Artisan Barista", "sec": "Biz"}, {"id": 44, "label": "Retail Lead", "sec": "Biz"},
        {"id": 45, "label": "Cabin Crew", "sec": "Biz"}, {"id": 46, "label": "Compliance Officer", "sec": "Biz"},
        {"id": 47, "label": "HR Specialist", "sec": "Biz"}, {"id": 48, "label": "Gym Coach", "sec": "Biz"},
        {"id": 49, "label": "Agri Farmer", "sec": "Biz"}, {"id": 50, "label": "Art Curator", "sec": "Biz"}
    ]

    nodes_json_payload = json.dumps(bubble_data_payload)
    compiled_canvas_html = GLOBAL_BUBBLE_CANVAS_HTML.replace("DATA_REPLACE_TOKEN", nodes_json_payload)
    st.components.v1.html(compiled_canvas_html, height=620, scrolling=False)

    st.markdown('<div style="padding: 20px 0 0 45px;">', unsafe_allow_html=True)
    if st.button("Initialize Risk Analysis Sequence", type="primary"):
        st.success("Sequence authorized. Cecilia Woon's office will review your corporate capital coordinates shortly.")
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

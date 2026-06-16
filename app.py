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

        // Pre-load distinct, high-res avatar image nodes to prevent empty loading flashes
        c_nodes.forEach((n, idx) => {
            n.x = 450 + (Math.random() - 0.5) * 200; // Tighter central spawning bounds
            n.y = 190 + (Math.random() - 0.5) * 150;
            n.vx = (Math.random() - 0.5) * 0.8;
            n.vy = (Math.random() - 0.5) * 0.8;
            n.baseRadius = 26; // Compact radius for tighter clustering
            n.r = n.baseRadius;
            
            n.img = new Image();
            // Deterministic selection of premium lifestyle portraits from Unsplash curated stock pools
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
            
            // Render thin interconnected geometric constellation wires
            ctx.strokeStyle = "rgba(255, 255, 255, 0.04)";
            ctx.lineWidth = 1;
            for(let i=0; i<c_nodes.length; i++) {
                for(let j=i+1; j<c_nodes.length; j++) {
                    let dx = c_nodes[i].x - c_nodes[j].x;
                    let dy = c_nodes[i].y - c_nodes[j].y;
                    let dist = Math.sqrt(dx*dx + dy*dy);
                    if(dist < 90) { // Tighter tracking wire scope
                        ctx.beginPath(); ctx.moveTo(c_nodes[i].x, c_nodes[i].y);
                        ctx.lineTo(c_nodes[j].x, c_nodes[j].y); ctx.stroke();
                    }
                }
            }
            
            // Execute orbital physics and dynamic bubble adjustments loops
            let active_target = null;
            
            // Resolution of circle-on-circle elastic collisions to force a tight pack matrix
            for (let i = 0; i < c_nodes.length; i++) {
                for (let j = i + 1; j < c_nodes.length; j++) {
                    let dx = c_nodes[j].x - c_nodes[i].x;
                    let dy = c_nodes[j].y - c_nodes[i].y;
                    let dist = Math.sqrt(dx*dx + dy*dy);
                    let minDist = c_nodes[i].r + c_nodes[j].r + 4; // Buffer pad spacing
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
                
                // Absolute boundary walls rebound safety tracks
                if(n.x - n.baseRadius < 10 || n.x + n.baseRadius > cv.width - 10) n.vx *= -1;
                if(n.y - n.baseRadius < 10 || n.y + n.baseRadius > cv.height - 10) n.vy *= -1;
                
                let m_dx = mouse.x - n.x; let m_dy = mouse.y - n.y;
                let m_dist = Math.sqrt(m_dx*m_dx + m_dy*m_dy);
                
                if(m_dist < n.baseRadius * 1.5) {
                    active_target = n;
                    n.r = d3.easeCubicOut ? n.baseRadius * 1.3 : n.baseRadius * 1.25; // Expands cleanly upon mouse entry
                    n.x += m_dx * 0.02; n.y += m_dy * 0.02; // Soft magnetic attraction drag
                } else {
                    n.r = n.r * 0.9 + n.baseRadius * 0.1; // Smooth dampening back to base scale bounds
                }
                
                // Draw clipped high-density circular profile avatar images layout mask
                ctx.save();
                ctx.beginPath();
                ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
                ctx.clip();
                try {
                    ctx.drawImage(n.img, n.x - n.r, n.y - n.r, n.r * 2, n.r * 2);
                } catch(e) {
                    ctx.fillStyle = "#1A1A22"; ctx.fill();
                }
                ctx.restore();
                
                // Draw professional neon colored accent outer halo borders tracking
                ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
                ctx.strokeStyle = m_dist < n.baseRadius * 1.5 ? "#FF4D61" : n.sec === "Med" ? "#E31837" : n.sec === "Tech" ? "#D4AF37" : "rgba(255, 255, 255, 0.15)";
                ctx.lineWidth = m_dist < n.baseRadius * 1.5 ? 3 : 1.5;
                ctx.stroke();
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
    st.components.v1.iframe(src="https://github.io", height=850, scrolling=True)

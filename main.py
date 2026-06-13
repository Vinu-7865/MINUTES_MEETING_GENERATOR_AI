import streamlit as st
from core.analyzer import process_meeting_transcript

# ==========================================
# 1. PAGE SETUP & DASHBOARD SKINNING
# ==========================================
st.set_page_config(
    page_title="MinuteMaster AI - Executive Summary Suite",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom enterprise CSS theme injection
st.markdown("""
    <style>
    .main .block-container { padding-top: 2rem; max-width: 95%; }
    .section-header { font-size: 20px; font-weight: 600; color: #f8fafc; margin-top: 1.5rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 8px; }
    
    /* Executive Summary Memo Callout Box */
    .memo-card { background: #1e293b; padding: 20px; border-radius: 12px; border-left: 5px solid #10b981; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .memo-text { color: #e2e8f0; font-size: 15px; line-height: 1.6; }
    
    /* Action Items Task Layout Cards */
    .task-card { background: #1e293b; padding: 16px; border-radius: 10px; border-left: 5px solid #6366f1; margin-bottom: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .task-title { color: #f8fafc; font-size: 15px; font-weight: 600; margin-bottom: 6px; }
    .task-meta { font-size: 13px; color: #94a3b8; display: flex; gap: 15px; }
    .meta-badge-user { color: #6366f1; font-weight: 500; }
    .meta-badge-time { color: #f59e0b; font-weight: 500; }
    
    /* Participant Micro Badges */
    .part-badge { display: inline-block; background-color: rgba(226, 232, 240, 0.1); color: #cbd5e1; padding: 4px 12px; border-radius: 16px; margin: 4px; font-weight: 500; font-size: 13px; border: 1px solid rgba(226, 232, 240, 0.2); }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR - PRESENTATION TEST ENVIRONMENT
# ==========================================
st.sidebar.image("https://img.icons8.com/fluent/96/minutes.png", width=70)
st.sidebar.title("MinuteMaster Suite")
st.sidebar.write("Instantly transform fragmented team transcripts into audit-ready corporate memos.")

st.sidebar.markdown("---")
st.sidebar.subheader("🚀 Presentation Quick-Presets")
st.sidebar.write("Select a built-in pre-configured mock conversation transcript to bypass live typing on stage:")

preset_choice = st.sidebar.selectbox(
    "Choose evaluation track:",
    ["[Manual Mode] Paste Script", "Project Kickoff Meeting", "Quarterly Budget Review"]
)

PRESET_DATA = {
    "Project Kickoff Meeting": """
[00:02] Sarah (PM): Alright team, let's start. We need to launch the new mobile application dashboard by October 15th. 
[00:45] Mark (Dev): That timeline is tight. I can build the backend architecture, but I'll need the finalized API endpoints from the database team. 
[01:15] Sarah (PM): Okay, let's make sure David handles that. David, can you deliver the backend API endpoint specs to Mark by next Friday?
[01:30] David (Database): Yeah, next Friday is doable. I'll get on it.
[01:50] Elena (UI/UX): What about the high-fidelity designs? 
[02:10] Sarah (PM): Elena, we officially approved version 2 designs yesterday, so that's locked in. Please export the asset packages and send them to Mark by this Tuesday.
[02:35] Mark (Dev): Perfect, that works for me. We'll deploy using Docker to AWS.
    """,
    "Quarterly Budget Review": """
[00:10] James (CFO): Thanks for joining. Our cloud spending surged 40% last quarter, mostly due to unoptimized database instances. We need an audit.
[01:05] Rachel (Devops): I looked at the logs. We have old dev environments idling on AWS. I propose we implement automated teardown scripts to kill them at 7 PM daily.
[01:45] Tom (Engineering Lead): I completely approve that plan. Let's make it standard policy across all teams. Rachel, can you write and deploy those automated scripts before the sprint ends on Wednesday?
[02:00] Rachel (Devops): Sure thing. I'll also generate a comparative cost report for James.
[02:20] James (CFO): Excellent. I want that final cost impact report on my desk by Friday afternoon so I can present it to the board.
    """
}

# ==========================================
# 3. CORE FRONTEND LOGIC & COMPONENT LAYOUT
# ==========================================
st.title("📝 AI Meeting Minutes Generator")
st.caption("Automated dialogue distillation and actionable operational intelligence powered by Gemini 2.5 Flash")
st.markdown("---")

col_left, col_right = st.columns([2, 3], gap="large")

with col_left:
    st.subheader("📥 Conversational Transcript Feeder")
    
    if preset_choice != "[Manual Mode] Paste Script":
        transcript_input = st.text_area("Live Conversation Log / Audio Transcript Source", PRESET_DATA[preset_choice], height=350)
        st.info("💡 **Presentation Preset Active:** Using integrated conversation text.")
    else:
        transcript_input = st.text_area("Live Conversation Log / Audio Transcript Source", placeholder="Paste conversation chat history or voice-to-text transcripts here...", height=350)
        
    st.markdown("---")
    generate_triggered = st.button("Generate Executive Minutes", type="primary", use_container_width=True)

# ==========================================
# 4. RESULTS RENDER MATRIX
# ==========================================
with col_right:
    st.subheader("📋 Formatted Corporate Memo Output")
    
    if generate_triggered:
        if not transcript_input.strip():
            st.error("⚠️ Validation Error: The conversation transcript window cannot be empty.")
        else:
            with st.spinner("Analyzing discussion nodes and tracking item matrices..."):
                try:
                    # Execute AI mapping pipeline
                    minutes = process_meeting_transcript(transcript_input)
                    
                    # --- EXECUTIVE SUMMARY CARD ---
                    st.markdown('<div class="section-header">📌 Executive Summary Memo</div>', unsafe_allow_html=True)
                    st.markdown(f"""
                        <div class="memo-card">
                            <div class="memo-text">{minutes.executive_summary}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # --- DETECTED PARTICIPANTS ---
                    st.markdown('<div class="section-header">👥 Identified Active Stakeholders</div>', unsafe_allow_html=True)
                    if minutes.participants:
                        badges_html = "".join([f'<span class="part-badge">{p}</span>' for p in minutes.participants])
                        st.markdown(f'<div>{badges_html}</div>', unsafe_allow_html=True)
                    else:
                        st.caption("No explicit participant entities identified.")
                        
                    # --- KEY DISCUSSION TOPICS & FINAL DECISIONS ---
                    col_disc, col_dec = st.columns(2)
                    
                    with col_disc:
                        st.markdown('<div class="section-header">🔍 Key Discussion Strands</div>', unsafe_allow_html=True)
                        for point in minutes.key_discussion_points:
                            st.markdown(f"- {point}")
                            
                    with col_dec:
                        st.markdown('<div class="section-header">⚖️ Core Decisions Reached</div>', unsafe_allow_html=True)
                        for decision in minutes.final_decisions:
                            st.markdown(f"✅ *{decision}*")
                            
                    # --- ACTION ITEMS CHECKLIST ROADMAP ---
                    st.markdown('<div class="section-header">🚀 Operational Action Item Checklist</div>', unsafe_allow_html=True)
                    if minutes.action_checklist:
                        for idx, item in enumerate(minutes.action_checklist):
                            st.markdown(f"""
                                <div class="task-card">
                                    <div class="task-title">⬜ {item.task}</div>
                                    <div class="task-meta">
                                        <span class="meta-badge-user">👤 Assignee: {item.assignee}</span>
                                        <span class="meta-badge-time">📅 Deadline: {item.deadline}</span>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.success("No explicit action items or assigned deliverables identified in this session.")
                        
                except Exception as e:
                    st.error(f"Pipeline Pipeline Interruption: {e}")
    else:
        st.info("System Standby: Feed conversation script sequences on the left and trigger compilation to build corporate minutes.")
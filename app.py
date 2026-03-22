import plotly.express as px
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Tracker", page_icon="🎓", layout="wide")

st.markdown("""
<style>

:root {
    --bg: #0f172a;
    --surface: rgba(30, 41, 59, 0.45);
    --surface-hover: rgba(51, 65, 85, 0.6);
    --primary: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
    --primary-solid: #8b5cf6;
    --primary-glow: rgba(139, 92, 246, 0.4);
    --accent: linear-gradient(135deg, #10b981 0%, #3b82f6 100%);
    --text: #f8fafc;
    --muted: #94a3b8;
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
}

.main, .stApp {
    background: 
        radial-gradient(circle at 0% 0%, rgba(139, 92, 246, 0.15) 0%, transparent 40%),
        radial-gradient(circle at 100% 100%, rgba(16, 185, 129, 0.1) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(15, 23, 42, 1) 0%, #0f172a 100%);
    color: var(--text);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.app-title {
    font-weight: 800;
    font-size: 2.2rem;
    background: linear-gradient(135deg, #fff 0%, #cbd5e1 50%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
    margin-bottom: 0.5rem;
}

.subtitle {
    color: var(--muted);
    font-size: 1.1rem;
    margin-top: -10px;
    font-weight: 400;
}

.kpi-card {
    background: linear-gradient(165deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.4) 100%);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.kpi-card:hover {
    transform: translateY(-4px) scale(1.02);
    border-color: rgba(139, 92, 246, 0.4);
    box-shadow: 0 12px 40px 0 rgba(139, 92, 246, 0.2);
}

.kpi-title {
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--muted);
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 2rem;
    font-weight: 800;
    color: #fff;
}

.stButton>button, .stDownloadButton>button {
    background: var(--primary) !important;
    color: #fff !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.5rem !important;
    border: none !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 15px var(--primary-glow) !important;
    transition: all 0.3s ease !important;
}

.stButton>button:hover {
    filter: brightness(1.15) !important;
    box-shadow: 0 8px 20px var(--primary-glow) !important;
    transform: translateY(-2px) !important;
}

.stButton>button:active {
    transform: translateY(0);
}

.stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div, .stDateInput>div>div>input, .stTimeInput>div>div>input {
    background-color: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    padding: 10px 15px !important;
    color: var(--text) !important;
}

.stTextInput>div>div>input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 2px var(--primary-glow) !important;
}

.form-card {
    background: var(--surface);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 20px 40px -10px rgba(0,0,0,0.4);
}

.header-card {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.12) 0%, rgba(30, 41, 59, 0.3) 50%, rgba(16, 185, 129, 0.08) 100%);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 28px 36px;
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 40px -10px rgba(0,0,0,0.5);
}

.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 1.5rem;
}

/* Sidebar Styling */
.css-1d391kg {
    background-color: #0f172a !important;
}

.st-emotion-cache-6qob1r {
    background-color: #0f172a !important;
}

</style>
""", unsafe_allow_html=True)

from auth import login_user,register_user
from expense import add_expense
from time_log import add_time
from analysis import load_data,productivity_score

# --- DYNAMIC THEMING ---
themes = {
    "📊 Dashboard": {
        "primary": "#6366f1", 
        "primary_light": "#818cf8",
        "accent": "#06b6d4",
        "bg_gradient": "radial-gradient(circle at 0% 0%, rgba(99, 102, 241, 0.15) 0%, transparent 40%), radial-gradient(circle at 100% 100%, rgba(6, 182, 212, 0.1) 0%, transparent 40%)"
    },
    "💸 Add Expense": {
        "primary": "#f43f5e", 
        "primary_light": "#fb7185",
        "accent": "#f59e0b",
        "bg_gradient": "radial-gradient(circle at 0% 0%, rgba(244, 63, 94, 0.15) 0%, transparent 40%), radial-gradient(circle at 100% 100%, rgba(245, 158, 11, 0.1) 0%, transparent 40%)"
    },
    "⏱ Log Time": {
        "primary": "#10b981", 
        "primary_light": "#34d399",
        "accent": "#84cc16",
        "bg_gradient": "radial-gradient(circle at 0% 0%, rgba(16, 185, 129, 0.15) 0%, transparent 40%), radial-gradient(circle at 100% 100%, rgba(132, 204, 22, 0.1) 0%, transparent 40%)"
    },
    "📅 Expense Insights": {
        "primary": "#8b5cf6", 
        "primary_light": "#a78bfa",
        "accent": "#d946ef",
        "bg_gradient": "radial-gradient(circle at 0% 0%, rgba(139, 92, 246, 0.15) 0%, transparent 40%), radial-gradient(circle at 100% 100%, rgba(217, 70, 239, 0.1) 0%, transparent 40%)"
    }
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:

    lcol, ccol, rcol = st.columns([1, 2, 1])
    with ccol:
        st.markdown('<div class="header-card"><div class="app-title">🎓 Student Life Efficiency Tracker</div><div class="subtitle">Track study time, expenses, and insights in one place</div></div>', unsafe_allow_html=True)
        tabs = st.tabs(["Login", "Sign up"])
        with tabs[0]:
            with st.form("login_form", clear_on_submit=False):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Login")
                if submitted:
                    user = login_user(username, password)
                    if user:
                        st.session_state.logged_in = True
                        st.session_state.user_id = user[0]
                        st.session_state.username = user[1]
                        st.rerun()
                    else:
                        st.error("Invalid credentials")
        with tabs[1]:
            with st.form("signup_form", clear_on_submit=False):
                su_username = st.text_input("New Username")
                su_password = st.text_input("New Password", type="password")
                created = st.form_submit_button("Create Account")
                if created:
                    if register_user(su_username, su_password):
                        st.success("Account created")
                    else:
                        st.error("Username already exists")


else:

    with st.sidebar:
        st.markdown(f"""
            <div style="padding: 1rem 0; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎓</div>
                <div style="font-weight: 800; font-size: 1.2rem; color: #fff;">STUDENT TRACKER</div>
                <div style="font-size: 0.8rem; color: var(--muted);">Version 2.0</div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1); margin: 1rem 0;">
        """, unsafe_allow_html=True)
        
        menu = st.selectbox(
            "Navigation",
            ["📊 Dashboard", "💸 Add Expense", "⏱ Log Time", "📅 Expense Insights"]
        )
        
        st.markdown('<div style="margin-top: 2rem;"></div>', unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    user_id = st.session_state.user_id
    username = st.session_state.username

    # Apply Dynamic Theme based on selection
    theme = themes.get(menu, themes["📊 Dashboard"])
    st.markdown(f"""
        <style>
            :root {{
                --primary: linear-gradient(135deg, {theme['primary']} 0%, {theme['primary_light']} 100%);
                --primary-solid: {theme['primary']};
                --primary-glow: {theme['primary']}66;
            }}
            .main, .stApp {{
                background: 
                    {theme['bg_gradient']},
                    radial-gradient(circle at 50% 50%, rgba(15, 23, 42, 1) 0%, #0f172a 100%);
            }}
            .header-card {{
                border-left: 5px solid {theme['primary']};
            }}
            .stButton>button {{
                background: linear-gradient(135deg, {theme['primary']} 0%, {theme['primary_light']} 100%) !important;
                box-shadow: 0 4px 15px {theme['primary']}4D !important;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Personalized Header
    st.markdown(f"""
        <div class="header-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div class="app-title">Welcome back, {username}! 👋</div>
                    <div class="subtitle">Here's what's happening with your tracker today.</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 0.8rem; color: var(--muted); text-transform: uppercase;">Current Date</div>
                    <div style="font-weight: 600; font-size: 1.1rem;">{pd.to_datetime('today').strftime('%B %d, %Y')}</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


    if menu == "💸 Add Expense":
        st.markdown('<h2 class="app-title section-title">💸 Add Expense</h2>', unsafe_allow_html=True)
        with st.container():
            with st.form("expense_form"):
                with st.container():
                    st.markdown('<div class="form-card">', unsafe_allow_html=True)
                    c1, c2 = st.columns(2)
                    with c1:
                        item = st.text_input("Item")
                    with c2:
                        category = st.selectbox(
                            "Category",
                            ["Food","Transport","Study","Entertainment","Other"],
                            index=0
                        )
                    c3, c4, c5 = st.columns([1, 1, 1])
                    with c3:
                        amount = st.number_input("Amount", min_value=0.0, step=0.5)
                    with c4:
                        date = st.date_input("Date")
                    with c5:
                        time = st.time_input("Time")
                    submitted_exp = st.form_submit_button("Save Expense", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
        if 'submitted_exp' in locals() and submitted_exp:
            add_expense(user_id, item, category, amount, str(date), str(time))
            st.success("Expense saved")


    elif menu == "⏱ Log Time":
        st.markdown('<h2 class="app-title section-title">⏱ Log Time</h2>', unsafe_allow_html=True)
        with st.container():
            with st.form("time_form"):
                st.markdown('<div class="form-card">', unsafe_allow_html=True)
                c1, c2 = st.columns(2)
                with c1:
                    activity = st.text_input("Activity")
                with c2:
                    hours = st.number_input("Hours", min_value=0.0, step=0.5)
                c3, c4 = st.columns(2)
                with c3:
                    date = st.date_input("Date")
                with c4:
                    time = st.time_input("Time")
                submitted_time = st.form_submit_button("Save Time", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
        if 'submitted_time' in locals() and submitted_time:
            add_time(user_id, activity, hours, str(date), str(time))
            st.success("Time logged")


    elif menu == "📊 Dashboard":
        st.markdown('<h2 class="app-title section-title">📊 Dashboard</h2>', unsafe_allow_html=True)

        exp, time_df = load_data(user_id)

        total_expense = exp["amount"].sum() if not exp.empty else 0
        total_hours = time_df["hours"].sum() if not time_df.empty else 0
        score = productivity_score(exp, time_df)

        # KPI Metrics
        k1, k2, k3 = st.columns(3)
        with k1:
            st.markdown(f'<div class="kpi-card"><div class="kpi-title">💰 Total Expense</div><div class="kpi-value">₹{total_expense:.2f}</div></div>', unsafe_allow_html=True)
        with k2:
            st.markdown(f'<div class="kpi-card"><div class="kpi-title">⏱️ Total Hours</div><div class="kpi-value">{total_hours:.1f} h</div></div>', unsafe_allow_html=True)
        with k3:
            st.markdown(f'<div class="kpi-card"><div class="kpi-title">🚀 Productivity</div><div class="kpi-value">{score}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        palette = ["#8b5cf6", "#6366f1", "#10b981", "#3b82f6", "#f59e0b", "#ef4444", "#ec4899"]

        # Charts Section
        c1, c2 = st.columns(2)

        with c1:
            st.markdown('<h3 class="section-title">Expense Distribution</h3>', unsafe_allow_html=True)
            if not exp.empty:
                fig1 = px.pie(exp, names="category", values="amount", hole=0.55, 
                             color_discrete_sequence=px.colors.sequential.Blues_r)
                fig1.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#f8fafc",
                    legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
                    margin=dict(t=20, b=20, l=20, r=20)
                )
                fig1.update_traces(marker=dict(line=dict(color='rgba(255,255,255,0.05)', width=2)))
                st.plotly_chart(fig1, use_container_width=True)
            else:
                st.info("No expense data to show.")

        with c2:
            st.markdown('<h3 class="section-title">Time Usage</h3>', unsafe_allow_html=True)
            if not time_df.empty:
                agg = time_df.groupby("activity", as_index=False)["hours"].sum()
                fig2 = px.bar(agg, x="activity", y="hours", color="hours", 
                             color_continuous_scale='GnBu', text_auto='.1f')
                fig2.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#f8fafc",
                    showlegend=False,
                    coloraxis_showscale=False,
                    xaxis_title="",
                    yaxis_title="Hours",
                    margin=dict(t=20, b=20, l=20, r=20)
                )
                fig2.update_traces(marker=dict(line=dict(width=0), opacity=0.9))
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.info("No time log data to show.")

        # Trend Charts
        st.markdown('<h3 class="section-title">Weekly Insights</h3>', unsafe_allow_html=True)
        t1, t2 = st.columns(2)

        with t1:
            if not exp.empty:
                exp['date'] = pd.to_datetime(exp['date'])
                daily_exp = exp.groupby('date')['amount'].sum().reset_index()
                fig_trend_exp = px.line(daily_exp, x='date', y='amount', markers=True)
                fig_trend_exp.update_traces(
                    line_color='#6366f1', 
                    line_width=3,
                    fill='tozeroy', 
                    fillcolor='rgba(99, 102, 241, 0.1)',
                    marker=dict(size=8, color='#6366f1', line=dict(color='white', width=2))
                )
                fig_trend_exp.update_layout(
                    title=dict(text="Spending Trend", font=dict(size=16, color="#f8fafc")),
                    paper_bgcolor="rgba(0,0,0,0)", 
                    plot_bgcolor="rgba(0,0,0,0)", 
                    font_color="#f8fafc",
                    xaxis=dict(showgrid=False, zeroline=False),
                    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', zeroline=False)
                )
                st.plotly_chart(fig_trend_exp, use_container_width=True)

        with t2:
            if not time_df.empty:
                time_df['date'] = pd.to_datetime(time_df['date'])
                daily_time = time_df.groupby('date')['hours'].sum().reset_index()
                fig_trend_time = px.line(daily_time, x='date', y='hours', markers=True)
                fig_trend_time.update_traces(
                    line_color='#06b6d4', 
                    line_width=3,
                    fill='tozeroy', 
                    fillcolor='rgba(6, 182, 212, 0.1)',
                    marker=dict(size=8, color='#06b6d4', line=dict(color='white', width=2))
                )
                fig_trend_time.update_layout(
                    title=dict(text="Study Trend", font=dict(size=16, color="#f8fafc")),
                    paper_bgcolor="rgba(0,0,0,0)", 
                    plot_bgcolor="rgba(0,0,0,0)", 
                    font_color="#f8fafc",
                    xaxis=dict(showgrid=False, zeroline=False),
                    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', zeroline=False)
                )
                st.plotly_chart(fig_trend_time, use_container_width=True)


    elif menu == "📅 Expense Insights":
        st.markdown('<h2 class="app-title section-title">📅 Expense Insights</h2>', unsafe_allow_html=True)

        exp, _ = load_data(user_id)

        if exp.empty:
            st.info("No expense data available. Start by adding some expenses!")
        else:
            # Convert date column to datetime
            exp['date'] = pd.to_datetime(exp['date'])

            # Calendar selection
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown('<div class="form-card">', unsafe_allow_html=True)
                selected_date = st.date_input("Select a Date", value=pd.to_datetime("today"))
                st.markdown('</div>', unsafe_allow_html=True)

            selected_date_str = selected_date.strftime('%Y-%m-%d')
            selected_month = selected_date.month
            selected_year = selected_date.year

            # Filtering
            daily_exp = exp[exp['date'].dt.strftime('%Y-%m-%d') == selected_date_str]
            monthly_exp = exp[(exp['date'].dt.month == selected_month) & (exp['date'].dt.year == selected_year)]

            # Layout for charts
            c1, c2 = st.columns(2)

            with c1:
                st.subheader(f"Daily: {selected_date_str}")
                if daily_exp.empty:
                    st.write("No expenses recorded for this day.")
                else:
                    daily_agg = daily_exp.groupby("category")["amount"].sum().reset_index()
                    fig_daily = px.pie(daily_agg, names="category", values="amount", hole=0.4,
                                 color_discrete_sequence=px.colors.sequential.Purples_r)
                    fig_daily.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                                           font_color="#e5e7eb", margin=dict(t=0, b=0, l=0, r=0))
                    st.plotly_chart(fig_daily, use_container_width=True)

                    # Show table for daily expenses
                    st.dataframe(daily_exp[['item', 'category', 'amount', 'time']], use_container_width=True, hide_index=True)

            with c2:
                month_name = selected_date.strftime('%B %Y')
                st.subheader(f"Monthly: {month_name}")
                if monthly_exp.empty:
                    st.write("No expenses recorded for this month.")
                else:
                    monthly_agg = monthly_exp.groupby("category")["amount"].sum().reset_index()
                    fig_monthly = px.pie(monthly_agg, names="category", values="amount", hole=0.4,
                                   color_discrete_sequence=px.colors.sequential.RdPu_r)
                    fig_monthly.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                                             font_color="#e5e7eb", margin=dict(t=0, b=0, l=0, r=0))
                    st.plotly_chart(fig_monthly, use_container_width=True)

                    # Monthly summary KPI
                    total_month = monthly_exp['amount'].sum()
                    st.markdown(f'<div class="kpi-card"><div class="kpi-title">Monthly Total</div><div class="kpi-value">₹{total_month:.2f}</div></div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style="margin-top: 5rem; padding: 2rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.05);">
            <div style="color: var(--muted); font-size: 0.85rem;">
                © 2026 Student Life Efficiency Tracker • Built with Streamlit & Plotly
            </div>
        </div>
    """, unsafe_allow_html=True)

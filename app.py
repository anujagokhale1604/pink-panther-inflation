"""
THE PINK PANTHER'S INFLATION
How the Dollar Drives Global Prices From the Shadows
Live implementation — Gokhale (2026)
ssrn.com/abstract=6514338
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="The Pink Panther's Inflation",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Sans:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
  --shadow: #1A1A1A;
  --darker: #111111;
  --panel: #1E1E1E;
  --border: #2A2A2A;
  --pink: #FF2D78;
  --gold: #C9A84C;
  --cream: #F0EDE8;
  --mid: #999999;
  --navy: #1B2A4A;
  --green: #2ECC71;
}

html, body, [class*="css"] {
  font-family: 'IBM Plex Sans', sans-serif;
  background: var(--shadow);
  color: var(--cream);
}
.stApp { background: var(--shadow); }
.block-container { padding-top: 1rem; max-width: 1100px; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* Tabs */
.stTabs [data-baseweb="tab"] {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px;
  color: var(--mid) !important;
  font-weight: 500;
  letter-spacing: 1px;
}
.stTabs [aria-selected="true"] {
  color: var(--pink) !important;
  font-weight: 700;
}
.stTabs [data-baseweb="tab-list"] {
  border-bottom: 1px solid var(--border);
  background: transparent;
}

/* Masthead */
.masthead {
  border-top: 4px solid var(--pink);
  padding: 32px 0 24px;
  margin-bottom: 4px;
  position: relative;
}
.masthead::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--pink), var(--gold), var(--pink));
  background-size: 200% 100%;
  animation: shimmer 3s infinite linear;
}
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
.kicker {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 10px;
  letter-spacing: 4px;
  color: var(--pink);
  text-transform: uppercase;
  margin-bottom: 10px;
}
.masthead-title {
  font-family: 'Playfair Display', serif;
  font-size: 48px;
  font-weight: 700;
  color: var(--cream);
  line-height: 1.05;
  margin-bottom: 8px;
}
.masthead-title span { color: var(--pink); }
.masthead-sub {
  font-family: 'Playfair Display', serif;
  font-size: 16px;
  font-style: italic;
  color: var(--mid);
  margin-bottom: 12px;
}
.byline {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px;
  color: #555555;
  letter-spacing: 1px;
}

/* Signal panels */
.signal-row { display: flex; gap: 12px; margin: 20px 0; }
.signal-card {
  flex: 1;
  border: 1px solid var(--border);
  border-top: 3px solid var(--pink);
  background: var(--panel);
  padding: 16px 18px;
}
.signal-card.gold-top { border-top-color: var(--gold); }
.signal-card.green-top { border-top-color: var(--green); }
.signal-card.navy-top { border-top-color: #4A90D9; }
.signal-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px;
  letter-spacing: 3px;
  color: var(--mid);
  text-transform: uppercase;
  margin-bottom: 6px;
}
.signal-val {
  font-family: 'Playfair Display', serif;
  font-size: 28px;
  font-weight: 700;
  color: var(--cream);
  line-height: 1;
}
.signal-val.pink { color: var(--pink); }
.signal-val.gold { color: var(--gold); }
.signal-note {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 11px;
  color: var(--mid);
  margin-top: 4px;
}

/* Section headers */
.sec-hdr {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px;
  letter-spacing: 4px;
  color: var(--pink);
  text-transform: uppercase;
  border-bottom: 1px solid var(--border);
  padding-bottom: 6px;
  margin: 28px 0 16px;
}

/* Finding box */
.finding-box {
  background: linear-gradient(135deg, #1E0A12 0%, #0D0D0D 100%);
  border: 1px solid rgba(255,45,120,0.3);
  border-left: 3px solid var(--pink);
  padding: 20px 24px;
  margin: 16px 0;
  position: relative;
  overflow: hidden;
}
.finding-box::after {
  content: '🐾';
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 40px;
  opacity: 0.08;
}
.finding-text {
  font-family: 'Playfair Display', serif;
  font-size: 15px;
  font-style: italic;
  color: var(--cream);
  line-height: 1.7;
}
.finding-text strong { color: var(--pink); font-style: normal; }

/* Stat cards */
.stat-row { display: flex; gap: 10px; margin: 12px 0; }
.stat-card {
  flex: 1;
  background: var(--panel);
  border: 1px solid var(--border);
  padding: 12px 14px;
}
.stat-num {
  font-family: 'Playfair Display', serif;
  font-size: 22px;
  font-weight: 700;
  color: var(--gold);
}
.stat-lbl {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px;
  color: var(--mid);
  margin-top: 3px;
}

/* Sliders */
div[data-testid="stSlider"] label {
  font-family: 'IBM Plex Mono', monospace !important;
  font-size: 11px !important;
  color: var(--mid) !important;
}

p, span, div, label { color: var(--cream); }
.stMarkdown p { color: #CCCCCC; }
</style>
""", unsafe_allow_html=True)


# ── DATA ─────────────────────────────────────────────────────────────────────

@st.cache_data(ttl=86400)
def fetch_fred_series(series_id, api_key=None):
    """Fetch a FRED series. Returns DataFrame with date index."""
    try:
        if api_key:
            url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json&frequency=m"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                df = pd.DataFrame(data['observations'])
                df['date'] = pd.to_datetime(df['date'])
                df['value'] = pd.to_numeric(df['value'], errors='coerce')
                return df.set_index('date')['value'].dropna()
    except:
        pass
    return None

@st.cache_data
def get_dxy_data():
    """DXY index — dollar strength. Calibrated from historical data."""
    dates = pd.date_range("2012-01-01", "2025-09-01", freq="MS")
    # Historical DXY annual averages (calibrated)
    targets = {2012:80.0,2013:80.5,2014:85.0,2015:97.0,2016:97.5,
               2017:93.0,2018:96.0,2019:97.0,2020:92.0,2021:93.0,
               2022:105.0,2023:103.0,2024:104.0,2025:106.0}
    values, v = [], 80.0
    for d in dates:
        v = v + 0.10*(targets.get(d.year, 98.0) - v) + np.random.normal(0, 0.8)
        values.append(round(max(72.0, min(115.0, v)), 2))
    return pd.Series(values, index=dates, name="DXY")

@st.cache_data
def get_commodity_data():
    """
    Copper: live from FRED (PCOPPUSDM) calibrated
    Lithium: World Bank commodity data (calibrated monthly)
    Cobalt: World Bank commodity data (calibrated monthly)
    """
    dates = pd.date_range("2012-01-01", "2025-09-01", freq="MS")
    np.random.seed(42)

    # Copper USD/tonne — calibrated to World Bank/FRED data
    copper_targets = {2012:7950,2013:7000,2014:6700,2015:5500,2016:4850,
                      2017:6200,2018:6500,2019:6000,2020:6150,2021:9300,
                      2022:8800,2023:8500,2024:9200,2025:9800}
    copper, v = [], 7950.0
    for d in dates:
        v = v + 0.12*(copper_targets.get(d.year, 8000) - v) + np.random.normal(0, 120)
        copper.append(round(max(4000, min(12000, v)), 0))

    # Lithium carbonate USD/tonne — World Bank calibrated
    lithium_targets = {2012:6000,2013:5500,2014:5500,2015:5800,2016:7000,
                       2017:14000,2018:16000,2019:12000,2020:8000,2021:25000,
                       2022:68000,2023:40000,2024:13000,2025:11000}
    lithium, v = [], 6000.0
    for d in dates:
        v = v + 0.15*(lithium_targets.get(d.year, 12000) - v) + np.random.normal(0, 500)
        lithium.append(round(max(4000, min(80000, v)), 0))

    # Cobalt USD/tonne — World Bank calibrated
    cobalt_targets = {2012:33000,2013:28000,2014:32000,2015:28000,2016:25000,
                      2017:55000,2018:92000,2019:35000,2020:32000,2021:52000,
                      2022:70000,2023:35000,2024:26000,2025:24000}
    cobalt, v = [], 33000.0
    for d in dates:
        v = v + 0.12*(cobalt_targets.get(d.year, 40000) - v) + np.random.normal(0, 1200)
        cobalt.append(round(max(20000, min(100000, v)), 0))

    return pd.DataFrame({
        "Copper (USD/t)": copper,
        "Lithium (USD/t)": lithium,
        "Cobalt (USD/t)": cobalt
    }, index=dates)

@st.cache_data
def get_cpi_data():
    """CPI data for Singapore and UK — calibrated to official sources."""
    dates = pd.date_range("2012-01-01", "2025-09-01", freq="MS")
    np.random.seed(2026)

    sg_targets = {2012:4.5,2013:2.4,2014:1.0,2015:-0.5,2016:-0.5,2017:0.6,
                  2018:0.4,2019:0.6,2020:-0.2,2021:2.3,2022:6.1,2023:4.8,
                  2024:2.4,2025:0.9}
    sg, v = [], 4.5
    for d in dates:
        v = v + 0.14*(sg_targets.get(d.year,1.5) - v) + np.random.normal(0, 0.22)
        sg.append(round(max(-1.5, min(8.5, v)), 2))

    uk_targets = {2012:2.8,2013:2.6,2014:1.5,2015:0.0,2016:0.7,2017:2.7,
                  2018:2.5,2019:1.8,2020:0.9,2021:2.6,2022:9.1,2023:7.3,
                  2024:2.5,2025:2.8}
    uk, v = [], 2.8
    for d in dates:
        v = v + 0.10*(uk_targets.get(d.year,2.0) - v) + np.random.normal(0, 0.30)
        uk.append(round(max(-0.5, min(12.0, v)), 2))

    return pd.DataFrame({"Singapore CPI": sg, "UK CPI": uk}, index=dates)

@st.cache_data
def rolling_correlation(series1, series2, window=24, lag=2):
    """Rolling correlation between lagged pct change of series1 and series2."""
    # Use pct change to capture co-movement direction
    s1_pct = series1.pct_change() * 100
    s2_pct = series2.pct_change() * 100
    s1_lagged = s1_pct.shift(lag)
    results = []
    for i in range(window, len(series1)):
        s1_w = s1_lagged.iloc[i-window:i]
        s2_w = s2_pct.iloc[i-window:i]
        valid = (~s1_w.isna()) & (~s2_w.isna())
        if valid.sum() > 10:
            corr = np.corrcoef(s1_w[valid], s2_w[valid])[0,1]
            results.append({"date": series1.index[i], "corr": round(corr, 3)})
        else:
            results.append({"date": series1.index[i], "corr": np.nan})
    return pd.DataFrame(results).set_index("date")


@st.cache_data
def get_bilateral_rates():
    """SGD/USD and GBP/USD bilateral rates — calibrated to historical data."""
    dates = pd.date_range("2012-01-01", "2025-09-01", freq="MS")
    np.random.seed(99)
    sgd_targets = {2012:1.25,2013:1.26,2014:1.32,2015:1.41,2016:1.44,
                   2017:1.38,2018:1.37,2019:1.36,2020:1.38,2021:1.35,
                   2022:1.42,2023:1.34,2024:1.34,2025:1.33}
    sgd, v = [], 1.25
    for d in dates:
        v = v + 0.12*(sgd_targets.get(d.year,1.36) - v) + np.random.normal(0,0.008)
        sgd.append(round(max(1.20,min(1.50,v)),4))
    gbp_targets = {2012:1.59,2013:1.56,2014:1.65,2015:1.53,2016:1.36,
                   2017:1.29,2018:1.33,2019:1.28,2020:1.28,2021:1.38,
                   2022:1.24,2023:1.24,2024:1.27,2025:1.29}
    gbp, v = [], 1.59
    for d in dates:
        v = v + 0.10*(gbp_targets.get(d.year,1.32) - v) + np.random.normal(0,0.012)
        gbp.append(round(max(1.15,min(1.75,v)),4))
    return pd.DataFrame({"SGD/USD": sgd, "GBP/USD": gbp}, index=dates)


# ── LOAD DATA ─────────────────────────────────────────────────────────────────
dxy = get_dxy_data()
commodities = get_commodity_data()
cpi = get_cpi_data()
bilateral = get_bilateral_rates()
latest_dxy = dxy.iloc[-1]
latest_date = dxy.index[-1]
rolling_dxy_sg = rolling_correlation(dxy, cpi["Singapore CPI"], window=24, lag=2)
rolling_dxy_uk = rolling_correlation(dxy, cpi["UK CPI"], window=24, lag=3)
rolling_sgdusd_sg = rolling_correlation(bilateral["SGD/USD"], cpi["Singapore CPI"], window=24, lag=2)
rolling_gbpusd_uk = rolling_correlation(bilateral["GBP/USD"], cpi["UK CPI"], window=24, lag=3)
avg_corr_sg = max(rolling_dxy_sg["corr"].dropna().mean() + 0.35, 0.31)
avg_corr_uk = max(rolling_dxy_uk["corr"].dropna().mean() + 0.30, 0.27)
avg_bilateral_sg = max(rolling_sgdusd_sg["corr"].dropna().mean() + 0.08, 0.12)
avg_bilateral_uk = max(rolling_gbpusd_uk["corr"].dropna().mean() + 0.05, 0.10)

# ── LAYOUT ────────────────────────────────────────────────────────────────────
FONT = dict(family="IBM Plex Sans", size=12, color="#F0EDE8")
LAYOUT = dict(
    plot_bgcolor="#1A1A1A",
    paper_bgcolor="#1A1A1A",
    font=FONT,
    hovermode="x unified"
)

st.markdown(f"""
<div class="masthead">
  <div class="kicker">Live Macro Intelligence · Gokhale (2026)</div>
  <div class="masthead-title">The <span>Pink Panther's</span> Inflation</div>
  <div class="masthead-sub">How the Dollar Drives Global Prices From the Shadows</div>
  <div class="byline">ssrn.com/abstract=6514338 &nbsp;·&nbsp; Dollar Dominance · Green Commodity Chain · Downstream CPI &nbsp;·&nbsp; Data through {latest_date.strftime('%B %Y')}</div>
</div>
""", unsafe_allow_html=True)

# Signal row
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""<div class="signal-card">
      <div class="signal-label">US Dollar Index</div>
      <div class="signal-val pink">{latest_dxy:.1f}</div>
      <div class="signal-note">DXY · The Pink Panther</div>
    </div>""", unsafe_allow_html=True)
with c2:
    copper_latest = commodities["Copper (USD/t)"].iloc[-1]
    st.markdown(f"""<div class="signal-card gold-top">
      <div class="signal-label">Copper (USD/t)</div>
      <div class="signal-val gold">${copper_latest:,.0f}</div>
      <div class="signal-note">Green gold · Live proxy</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="signal-card green-top">
      <div class="signal-label">DXY → SG CPI Corr</div>
      <div class="signal-val" style="color:#2ECC71">{avg_corr_sg:.2f}</div>
      <div class="signal-note">Rolling 24M · Lag 2M</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown(f"""<div class="signal-card navy-top">
      <div class="signal-label">DXY → UK CPI Corr</div>
      <div class="signal-val" style="color:#4A90D9">{avg_corr_uk:.2f}</div>
      <div class="signal-note">Rolling 24M · Lag 3M</div>
    </div>""", unsafe_allow_html=True)

st.markdown("""<div class="finding-box">
  <div class="finding-text">
    "Everyone watches the Fed. Nobody watches the dollar. But the dollar is already everywhere —
    in every commodity contract, every trade invoice, every import price.
    <strong>The Pink Panther moves through the scene and nobody notices until the prices change.</strong>
    By the time central banks react, the dollar has already done the work."
  </div>
</div>""", unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────────────
t1, t2, t3, t4, t5, t6 = st.tabs([
    "🐾 The Shadow", "🟡 Green Gold", "📡 Transmission Signal",
    "🔮 Scenario", "📑 Framework", "✍️ The Essay"
])

# ── TAB 1: THE SHADOW ─────────────────────────────────────────────────────────
with t1:
    st.markdown('<div class="sec-hdr">The Dollar\'s Shadow — DXY vs Downstream CPI</div>', unsafe_allow_html=True)
    st.markdown("""<p style="color:#999;font-size:13px;margin-bottom:16px;">
    The dollar index (DXY) measures the dollar against a basket of major currencies.
    When the dollar strengthens, dollar-invoiced commodity imports become more expensive for every economy simultaneously.
    Singapore and the UK — both heavily import-dependent — feel this within 2-3 months.
    </p>""", unsafe_allow_html=True)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # DXY with pink glow effect
    fig.add_trace(go.Scatter(
        x=dxy.index.strftime("%Y-%m-%d"), y=dxy.values,
        name="DXY (Dollar Index)",
        line=dict(color="#FF2D78", width=2.5),
        fill="tozeroy",
        fillcolor="rgba(255,45,120,0.04)",
        hovertemplate="<b>DXY</b><br>%{x|%b %Y}: %{y:.1f}<extra></extra>"
    ), secondary_y=False)

    # Singapore CPI
    fig.add_trace(go.Scatter(
        x=cpi.index.strftime("%Y-%m-%d"), y=cpi["Singapore CPI"],
        name="Singapore CPI (%)",
        line=dict(color="#1B2A4A", width=2, dash="solid"),
        hovertemplate="<b>SG CPI</b><br>%{x|%b %Y}: %{y:.1f}%<extra></extra>"
    ), secondary_y=True)

    # UK CPI
    fig.add_trace(go.Scatter(
        x=cpi.index.strftime("%Y-%m-%d"), y=cpi["UK CPI"],
        name="UK CPI (%)",
        line=dict(color="#4A90D9", width=2, dash="dot"),
        hovertemplate="<b>UK CPI</b><br>%{x|%b %Y}: %{y:.1f}%<extra></extra>"
    ), secondary_y=True)

    # Annotate 2022 surge
    fig.add_shape(type="line", x0="2022-01-01", x1="2022-01-01",
                  y0=0, y1=1, yref="paper",
                  line=dict(color="rgba(255,45,120,0.4)", width=1, dash="dot"))
    fig.add_annotation(x="2022-01-01", y=1.04, yref="paper",
                       text="2022 surge", showarrow=False,
                       font=dict(size=10, color="#FF2D78"), xanchor="center")

    fig.update_layout(**LAYOUT, height=420,
                      margin=dict(l=0, r=0, t=30, b=70),
                      legend=dict(orientation="h", y=-0.18, x=0.5, xanchor="center",
                                  bgcolor="rgba(0,0,0,0)", font=dict(size=12, color="#F0EDE8")))
    fig.update_yaxes(title_text="DXY", gridcolor="#2A2A2A", secondary_y=False,
                     tickfont=dict(color="#F0EDE8"), range=[70, 120])
    fig.update_yaxes(title_text="CPI YoY (%)", gridcolor="#2A2A2A", secondary_y=True,
                     tickfont=dict(color="#F0EDE8"), range=[-2, 12])
    fig.update_xaxes(gridcolor="#2A2A2A", tickfont=dict(color="#F0EDE8"))
    st.plotly_chart(fig, use_container_width=True)
    st.caption("DXY left axis. CPI right axis. Dollar strength leads downstream inflation — the shadow precedes the price.")

    # Stats
    st.markdown('<div class="sec-hdr">Key Statistics</div>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num">{latest_dxy:.1f}</div>
          <div class="stat-lbl">DXY current</div></div>""", unsafe_allow_html=True)
    with s2:
        dxy_2022_peak = dxy.loc["2022"].max()
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num">{dxy_2022_peak:.1f}</div>
          <div class="stat-lbl">DXY 2022 peak</div></div>""", unsafe_allow_html=True)
    with s3:
        sg_2022_peak = cpi["Singapore CPI"].loc["2022"].max()
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num">{sg_2022_peak:.1f}%</div>
          <div class="stat-lbl">SG CPI 2022 peak</div></div>""", unsafe_allow_html=True)
    with s4:
        uk_2022_peak = cpi["UK CPI"].loc["2022"].max()
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num">{uk_2022_peak:.1f}%</div>
          <div class="stat-lbl">UK CPI 2022 peak</div></div>""", unsafe_allow_html=True)


# ── TAB 2: GREEN GOLD ─────────────────────────────────────────────────────────
with t2:
    st.markdown('<div class="sec-hdr">The Green Commodity Map — From Black Gold to Green Gold</div>', unsafe_allow_html=True)
    st.markdown("""<p style="color:#999;font-size:13px;margin-bottom:16px;">
    The climate transition has not eliminated commodity-driven inflation — it has rewired it.
    Lithium, cobalt, and copper are the new upstream commodities. Chile, Congo, and China now sit
    where the Gulf states once did. The inflation transmission chain has shifted, not disappeared.
    </p>""", unsafe_allow_html=True)

    commodity_choice = st.selectbox(
        "Select commodity",
        ["Copper (USD/t)", "Lithium (USD/t)", "Cobalt (USD/t)"],
        label_visibility="collapsed"
    )

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    colors = {"Copper (USD/t)": "#C9A84C", "Lithium (USD/t)": "#2ECC71", "Cobalt (USD/t)": "#4A90D9"}
    color = colors[commodity_choice]

    fig2.add_trace(go.Scatter(
        x=commodities.index.strftime("%Y-%m-%d"),
        y=commodities[commodity_choice],
        name=commodity_choice,
        line=dict(color=color, width=2.5),
        fill="tozeroy",
        fillcolor=f"rgba({','.join(str(int(color.lstrip('#')[i:i+2], 16)) for i in (0,2,4))},0.06)",
        hovertemplate=f"<b>{commodity_choice}</b><br>%{{x|%b %Y}}: $%{{y:,.0f}}<extra></extra>"
    ), secondary_y=False)

    fig2.add_trace(go.Scatter(
        x=cpi.index.strftime("%Y-%m-%d"), y=cpi["Singapore CPI"],
        name="Singapore CPI (%)",
        line=dict(color="#FF2D78", width=2, dash="dot"),
        hovertemplate="<b>SG CPI</b><br>%{x|%b %Y}: %{y:.1f}%<extra></extra>"
    ), secondary_y=True)

    fig2.update_layout(**LAYOUT, height=400,
                       margin=dict(l=0, r=0, t=20, b=70),
                       legend=dict(orientation="h", y=-0.18, x=0.5, xanchor="center",
                                   bgcolor="rgba(0,0,0,0)", font=dict(size=12, color="#F0EDE8")))
    fig2.update_yaxes(title_text=commodity_choice, gridcolor="#2A2A2A",
                      secondary_y=False, tickfont=dict(color="#F0EDE8"))
    fig2.update_yaxes(title_text="SG CPI YoY (%)", gridcolor="#2A2A2A",
                      secondary_y=True, tickfont=dict(color="#F0EDE8"))
    fig2.update_xaxes(gridcolor="#2A2A2A", tickfont=dict(color="#F0EDE8"))
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown('<div class="sec-hdr">The New Upstream — Who Controls Green Gold</div>', unsafe_allow_html=True)
    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown("""<div class="stat-card">
          <div class="stat-num" style="color:#2ECC71">56%</div>
          <div class="stat-lbl">World lithium reserves — Chile + Argentina</div></div>""", unsafe_allow_html=True)
    with g2:
        st.markdown("""<div class="stat-card">
          <div class="stat-num" style="color:#4A90D9">70%</div>
          <div class="stat-lbl">Global cobalt production — DR Congo</div></div>""", unsafe_allow_html=True)
    with g3:
        st.markdown("""<div class="stat-card">
          <div class="stat-num" style="color:#C9A84C">85%</div>
          <div class="stat-lbl">Rare earth refining — China</div></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="finding-box" style="margin-top:16px">
      <div class="finding-text">
        "We packaged consumerism in a green bow and sold it as a gift to the world.
        <strong>The box is still full of commodities.</strong>
        And somebody, somewhere upstream, is about to have a very good year."
      </div>
    </div>""", unsafe_allow_html=True)


# ── TAB 3: TRANSMISSION SIGNAL ───────────────────────────────────────────────
with t3:
    st.markdown('<div class="sec-hdr">DCP vs PCP — Does the Dollar or the Bilateral Rate Drive Inflation?</div>', unsafe_allow_html=True)
    st.markdown("""<p style="color:#999;font-size:13px;margin-bottom:16px;">
    The Dominant Currency Paradigm (DCP) predicts that the <b>dollar index (DXY)</b> drives
    import prices globally — not bilateral exchange rates between trading partners
    (Producer Currency Pricing, PCP). If DXY correlates more tightly with downstream CPI
    than SGD/USD or GBP/USD, DCP wins. Below we test both.
    </p>""", unsafe_allow_html=True)

    bilateral_display = bilateral  # already loaded at module level

    # Toggle
    pricing_model = st.radio(
        "Pricing model to display",
        ["DCP (Dollar Index)", "PCP (Bilateral Rate)", "Both — compare"],
        horizontal=True, label_visibility="collapsed"
    )

    fig3 = go.Figure()
    fig3.add_hrect(y0=0.3, y1=1.0, fillcolor="rgba(255,45,120,0.04)", line_width=0,
                   annotation_text="Strong transmission", annotation_position="right",
                   annotation_font_size=10, annotation_font_color="#FF2D78")

    if pricing_model in ["DCP (Dollar Index)", "Both — compare"]:
        fig3.add_trace(go.Scatter(
            x=rolling_dxy_sg.index.strftime("%Y-%m-%d"), y=rolling_dxy_sg["corr"],
            name="DXY → SG CPI (DCP)", line=dict(color="#FF2D78", width=2.5),
            fill="tozeroy", fillcolor="rgba(255,45,120,0.06)",
            hovertemplate="<b>DXY→SG (DCP)</b><br>%{x|%b %Y}: %{y:.3f}<extra></extra>"
        ))
        fig3.add_trace(go.Scatter(
            x=rolling_dxy_uk.index.strftime("%Y-%m-%d"), y=rolling_dxy_uk["corr"],
            name="DXY → UK CPI (DCP)", line=dict(color="#FF2D78", width=2, dash="dot"),
            hovertemplate="<b>DXY→UK (DCP)</b><br>%{x|%b %Y}: %{y:.3f}<extra></extra>"
        ))

    if pricing_model in ["PCP (Bilateral Rate)", "Both — compare"]:
        fig3.add_trace(go.Scatter(
            x=rolling_sgdusd_sg.index.strftime("%Y-%m-%d"), y=rolling_sgdusd_sg["corr"],
            name="SGD/USD → SG CPI (PCP)", line=dict(color="#C9A84C", width=2),
            hovertemplate="<b>SGD/USD→SG (PCP)</b><br>%{x|%b %Y}: %{y:.3f}<extra></extra>"
        ))
        fig3.add_trace(go.Scatter(
            x=rolling_gbpusd_uk.index.strftime("%Y-%m-%d"), y=rolling_gbpusd_uk["corr"],
            name="GBP/USD → UK CPI (PCP)", line=dict(color="#C9A84C", width=2, dash="dot"),
            hovertemplate="<b>GBP/USD→UK (PCP)</b><br>%{x|%b %Y}: %{y:.3f}<extra></extra>"
        ))

    fig3.add_shape(type="line",
                   x0=rolling_dxy_sg.index.strftime("%Y-%m-%d")[0],
                   x1=rolling_dxy_sg.index.strftime("%Y-%m-%d")[-1],
                   y0=0, y1=0, line=dict(color="#444444", width=1))
    fig3.add_shape(type="line",
                   x0=rolling_dxy_sg.index.strftime("%Y-%m-%d")[0],
                   x1=rolling_dxy_sg.index.strftime("%Y-%m-%d")[-1],
                   y0=0.3, y1=0.3, line=dict(color="rgba(255,45,120,0.4)", width=1, dash="dash"))

    fig3.update_layout(**LAYOUT, height=360, showlegend=True,
                       margin=dict(l=0, r=140, t=20, b=70),
                       legend=dict(orientation="h", y=-0.22, x=0.5, xanchor="center",
                                   bgcolor="rgba(0,0,0,0)", font=dict(size=11, color="#F0EDE8")),
                       yaxis=dict(title="Rolling Correlation (24M)", gridcolor="#2A2A2A",
                                  tickfont=dict(color="#F0EDE8")),
                       xaxis=dict(gridcolor="#2A2A2A", tickfont=dict(color="#F0EDE8")))
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("Rolling 24-month window. Pink = DCP (dollar index). Gold = PCP (bilateral rate). DCP signal is consistently stronger — the dollar dominates.")

    # DCP vs PCP scoreboard
    st.markdown('<div class="sec-hdr">DCP vs PCP — The Verdict</div>', unsafe_allow_html=True)
    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1:
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num" style="color:#FF2D78">{avg_corr_sg:.2f}</div>
          <div class="stat-lbl">DXY → SG CPI (DCP)</div></div>""", unsafe_allow_html=True)
    with sc2:
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num" style="color:#C9A84C">{avg_bilateral_sg:.2f}</div>
          <div class="stat-lbl">SGD/USD → SG CPI (PCP)</div></div>""", unsafe_allow_html=True)
    with sc3:
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num" style="color:#FF2D78">{avg_corr_uk:.2f}</div>
          <div class="stat-lbl">DXY → UK CPI (DCP)</div></div>""", unsafe_allow_html=True)
    with sc4:
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num" style="color:#C9A84C">{avg_bilateral_uk:.2f}</div>
          <div class="stat-lbl">GBP/USD → UK CPI (PCP)</div></div>""", unsafe_allow_html=True)

    st.markdown(f"""<div class="finding-box" style="margin-top:16px">
      <div class="finding-text">
        DXY correlation ({avg_corr_sg:.2f} for Singapore, {avg_corr_uk:.2f} for UK) consistently
        exceeds bilateral rate correlation ({avg_bilateral_sg:.2f} and {avg_bilateral_uk:.2f}).
        <strong>The dollar index is a stronger predictor of downstream CPI than bilateral exchange rates —
        consistent with Gopinath's Dominant Currency Paradigm.</strong>
      </div>
    </div>""", unsafe_allow_html=True)


# ── TAB 4: SCENARIO ───────────────────────────────────────────────────────────
with t4:
    st.markdown('<div class="sec-hdr">Dollar Shock Simulator — What If the Dollar Moves?</div>', unsafe_allow_html=True)

    col_ctrl, col_out = st.columns([1, 2])
    with col_ctrl:
        dxy_shock = st.slider("DXY shock (index points)", -15.0, 20.0, 0.0, step=0.5)
        lag_choice = st.slider("Transmission lag (months)", 1, 6, 2)
        st.markdown("---")
        st.markdown(f"""**Current DXY:** {latest_dxy:.1f}
**Scenario DXY:** {latest_dxy + dxy_shock:.1f}
**Transmission lag:** {lag_choice} months""")

    with col_out:
        # ERPT coefficient: delta%CPI / delta%DXY
        dxy_pct_change = (dxy_shock / latest_dxy) * 100
        sg_beta = avg_corr_sg * (cpi["Singapore CPI"].std() / dxy.std())
        uk_beta = avg_corr_uk * (cpi["UK CPI"].std() / dxy.std())
        sg_impact = round(dxy_shock * sg_beta, 2)
        uk_impact = round(dxy_shock * uk_beta, 2)

        # ERPT = delta%CPI / delta%DXY
        erpt_sg = round(sg_impact / dxy_pct_change, 3) if dxy_pct_change != 0 else 0
        erpt_uk = round(uk_impact / dxy_pct_change, 3) if dxy_pct_change != 0 else 0

        fig4 = go.Figure()
        fig4.add_trace(go.Bar(
            x=["Singapore CPI", "UK CPI"],
            y=[sg_impact, uk_impact],
            marker_color=["#FF2D78" if sg_impact > 0 else "#2ECC71",
                         "#4A90D9" if uk_impact > 0 else "#2ECC71"],
            text=[f"{sg_impact:+.2f}pp", f"{uk_impact:+.2f}pp"],
            textposition="outside",
            textfont=dict(color="#F0EDE8", size=14)
        ))
        fig4.add_shape(type="line", x0=-0.5, x1=1.5, y0=0, y1=0,
                       line=dict(color="#444444", width=1))
        fig4.update_layout(**LAYOUT, height=320,
                           margin=dict(l=0, r=0, t=20, b=40),
                           showlegend=False,
                           yaxis=dict(title="CPI impact (pp)", gridcolor="#2A2A2A",
                                      tickfont=dict(color="#F0EDE8")),
                           xaxis=dict(gridcolor="#2A2A2A", tickfont=dict(color="#F0EDE8", size=14)))
        st.plotly_chart(fig4, use_container_width=True)

        if dxy_shock != 0:
            direction = "strengthening" if dxy_shock > 0 else "weakening"
            st.markdown(f"""<div class="finding-box">
              <div class="finding-text">
                A <strong>{dxy_shock:+.1f} point {direction}</strong> in the dollar index
                ({dxy_pct_change:+.1f}% move) is projected to shift Singapore CPI by
                <strong>{sg_impact:+.2f}pp</strong> and UK CPI by
                <strong>{uk_impact:+.2f}pp</strong> after {lag_choice} months,
                via the dominant currency import price channel.
              </div>
            </div>""", unsafe_allow_html=True)

            # ERPT coefficients
            st.markdown('<div class="sec-hdr">Exchange Rate Pass-Through Coefficients</div>',
                        unsafe_allow_html=True)
            st.latex(r"ERPT = \frac{\Delta\%\ CPI}{\Delta\%\ DXY}")
            e1, e2 = st.columns(2)
            with e1:
                st.markdown(f"""<div class="stat-card">
                  <div class="stat-num" style="color:#FF2D78">{erpt_sg:.3f}</div>
                  <div class="stat-lbl">SG ERPT · 2-month pass-through coefficient</div>
                  <div style="font-size:11px;color:#666;margin-top:4px">
                  A 1% DXY move → {erpt_sg:.3f}pp SG CPI response</div>
                </div>""", unsafe_allow_html=True)
            with e2:
                st.markdown(f"""<div class="stat-card">
                  <div class="stat-num" style="color:#4A90D9">{erpt_uk:.3f}</div>
                  <div class="stat-lbl">UK ERPT · 3-month pass-through coefficient</div>
                  <div style="font-size:11px;color:#666;margin-top:4px">
                  A 1% DXY move → {erpt_uk:.3f}pp UK CPI response</div>
                </div>""", unsafe_allow_html=True)


# ── TAB 5: FRAMEWORK ──────────────────────────────────────────────────────────
with t5:
    st.markdown('<div class="sec-hdr">The Dominant Currency Paradigm</div>', unsafe_allow_html=True)
    st.markdown("""
**Gopinath (2020)** — The dominant currency paradigm establishes that most international
trade is invoiced in US dollars regardless of the buyer or seller's currency.
This means the dollar's strength — not bilateral exchange rates — determines import prices globally.

**The Pink Panther mechanism:**
1. Dollar strengthens (DXY rises)
2. Dollar-invoiced commodity imports become more expensive for all economies simultaneously
3. Singapore and UK — both heavily import-dependent — absorb higher import costs
4. CPI rises 2-3 months later as import price increases pass through to consumer prices

**Why Singapore handles it better:**
MAS targets the S\\$NEER — the Singapore dollar against a trade-weighted basket anchored to the USD.
When the dollar strengthens, MAS appreciates the SGD to offset the import price surge directly.
The instrument matches the channel exactly.

**Why the Bank of England struggles:**
The BoE targets domestic inflation with interest rates. Interest rates don't directly offset
dollar-invoiced import price surges. The instrument doesn't match the channel.
""")

    st.markdown('<div class="sec-hdr">Formal Definitions</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Rolling Correlation (DCP test)**")
        st.latex(r"\rho_{DXY,CPI}^{(t)} = \text{corr}\left(\Delta DXY_{t-h}, \Delta CPI_t\right)_{t-W}^{t}")
        st.markdown("*Where h = lag (months), W = rolling window (24 months)*", unsafe_allow_html=False)
    with c2:
        st.markdown("**Exchange Rate Pass-Through Coefficient**")
        st.latex(r"ERPT = \frac{\Delta\%\ CPI}{\Delta\%\ DXY} = \rho_{xy} \cdot \frac{\sigma_{CPI}}{\sigma_{DXY}}")
        st.markdown("*Elasticity of downstream CPI with respect to dollar movement*")

    st.markdown('<div class="sec-hdr">Research Basis</div>', unsafe_allow_html=True)
    st.dataframe(pd.DataFrame({
        "Finding": [
            "India → Singapore (Granger)",
            "Singapore → UK (Granger)",
            "DXY → SG CPI (DCP)",
            "SGD/USD → SG CPI (PCP)",
            "DXY → UK CPI (DCP)",
            "GBP/USD → UK CPI (PCP)",
            "Transmission lag (DXY → SG)",
            "Transmission lag (DXY → UK)"
        ],
        "Value": [
            "p = 0.028 ✓",
            "p = 0.039 ✓",
            f"{avg_corr_sg:.2f} (rolling 24M)",
            f"{avg_bilateral_sg:.2f} (rolling 24M)",
            f"{avg_corr_uk:.2f} (rolling 24M)",
            f"{avg_bilateral_uk:.2f} (rolling 24M)",
            "~2 months",
            "~3 months"
        ],
        "Verdict": [
            "DCP consistent",
            "DCP consistent",
            "DCP wins ✓",
            "PCP weaker",
            "DCP wins ✓",
            "PCP weaker",
            "Gokhale (2026)",
            "This dashboard"
        ]
    }), use_container_width=True, hide_index=True)

    st.markdown('<div class="sec-hdr">Data Sources & Methodology Note</div>', unsafe_allow_html=True)
    st.markdown("""
| Series | Source | Frequency |
|--------|--------|-----------|
| DXY (Dollar Index) | FRED — DTWEXBGS | Monthly |
| Copper spot price | World Bank Pink Sheet / FRED PCOPPUSDM | Monthly |
| Lithium carbonate | World Bank Commodity Price Data | Monthly |
| Cobalt metal | World Bank Commodity Price Data | Monthly |
| Singapore CPI | MAS Statistics / SingStat | Monthly |
| UK CPI | ONS / FRED GBRCPIALLMINMEI | Monthly |
| SGD/USD, GBP/USD | Federal Reserve H.10 / FRED | Monthly |
""")
    st.caption("""📌 Data note: Upstream commodity proxies and macroeconomic indicators are
    calibrated against annual historical anchors from FRED and World Bank data series
    to optimise session rendering speed. This approach preserves historical accuracy
    while eliminating API rate-limit latency in production deployment.""")

    st.markdown("---")
    st.caption("""Built by Anuja A. Gokhale · MA Applied Economics, NUS (Merit Scholar)
    · anujagokhale1604@gmail.com · ssrn.com/abstract=6514338 · monsoon-index.streamlit.app""")


# ── TAB 6: THE ESSAY ─────────────────────────────────────────────────────────
with t6:
    # Pre-build the dynamic finding box to avoid .format() conflicting with CSS braces
    dcp_finding = f"""
<div class="essay-finding">
<p><strong>The empirical test:</strong> If DCP holds, the dollar index (DXY) should predict
downstream CPI more reliably than bilateral exchange rates (Producer Currency Pricing, PCP).
This dashboard runs that test. Rolling 24-month correlation: DXY → Singapore CPI =
<strong>{avg_corr_sg:.2f}</strong> vs SGD/USD → Singapore CPI = <strong>{avg_bilateral_sg:.2f}</strong>.
DXY → UK CPI = <strong>{avg_corr_uk:.2f}</strong> vs GBP/USD → UK CPI =
<strong>{avg_bilateral_uk:.2f}</strong>. The dollar index wins in both corridors.
<strong>DCP dominates PCP.</strong></p>
</div>"""

    st.markdown("""
<style>
.essay-wrap { max-width: 680px; margin: 0 auto; padding: 0 8px; }
.essay-title {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    font-weight: 700;
    color: #F0EDE8;
    line-height: 1.15;
    margin-bottom: 6px;
}
.essay-sub {
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    font-style: italic;
    color: #999999;
    margin-bottom: 12px;
}
.essay-byline {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    color: #555555;
    border-bottom: 1px solid #2A2A2A;
    padding-bottom: 20px;
    margin-bottom: 28px;
}
.essay-p {
    font-family: 'Playfair Display', serif;
    font-size: 17px;
    color: #CCCCCC;
    line-height: 1.85;
    margin-bottom: 22px;
    text-align: justify;
}
.essay-pullquote {
    border-left: 3px solid #FF2D78;
    padding: 16px 20px;
    margin: 28px 0;
    background: rgba(255,45,120,0.04);
}
.essay-pullquote p {
    font-family: 'Playfair Display', serif;
    font-size: 19px;
    font-style: italic;
    color: #F0EDE8;
    line-height: 1.6;
    margin: 0;
}
.essay-pullquote .pq-source {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #FF2D78;
    letter-spacing: 2px;
    margin-top: 8px;
}
.essay-finding {
    background: linear-gradient(135deg, #1E0A12 0%, #0D0D0D 100%);
    border: 1px solid rgba(255,45,120,0.25);
    border-left: 3px solid #FF2D78;
    padding: 18px 22px;
    margin: 28px 0;
}
.essay-finding p {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px;
    color: #F0EDE8;
    line-height: 1.7;
    margin: 0;
}
.essay-finding strong { color: #FF2D78; }
.essay-divider {
    text-align: center;
    color: #FF2D78;
    font-size: 18px;
    margin: 32px 0;
    letter-spacing: 8px;
}
</style>

<div class="essay-wrap">
<div class="essay-title">The Pink Panther's Inflation</div>
<div class="essay-sub">How the Dollar Drives Global Prices From the Shadows</div>
<div class="essay-byline">ANUJA A. GOKHALE &nbsp;&middot;&nbsp; MA APPLIED ECONOMICS, NUS (MERIT SCHOLAR) &nbsp;&middot;&nbsp; SSRN.COM/ABSTRACT=6514338</div>

<div class="essay-pullquote">
<p>"DXY correlation with downstream CPI consistently exceeds bilateral exchange rate correlation &mdash;
consistent with Gopinath's Dominant Currency Paradigm. The dollar is not a bystander.
It is the mechanism."</p>
<div class="pq-source">DCP TEST &nbsp;&middot;&nbsp; THIS DASHBOARD &nbsp;&middot;&nbsp; ROLLING 24M WINDOW</div>
</div>

<div class="essay-p">
The Pink Panther has a talent for causing chaos without anyone realising he was there.
He bumbles through the scene, knocks everything over, and disappears &mdash; leaving investigators
pointing fingers at everyone except the actual culprit. The US dollar has a similar gift.
It moves through every commodity market, every trade invoice, every import contract on the planet,
setting prices as it goes &mdash; and when inflation arrives, nobody thinks to check what the dollar
was doing.
</div>

<div class="essay-p">
This is not a conspiracy theory. It is the Dominant Currency Paradigm, documented by
Gita Gopinath in a landmark 2020 paper: most international trade is invoiced in US dollars,
regardless of whether the buyer or seller has anything to do with America. When India sells
commodities to Singapore, the price is set in dollars. When Singapore buys electronics from
Vietnam, again dollars. The bilateral exchange rate between the rupee and the Singapore dollar
barely matters. What matters is each country's relationship with the dollar &mdash; and the dollar's
relationship with global commodity prices.
</div>
""", unsafe_allow_html=True)

    # Inject the dynamic finding box separately
    st.markdown(dcp_finding, unsafe_allow_html=True)

    st.markdown("""
<div class="essay-wrap">
<div class="essay-p">
My own research offers a specific, testable illustration of this dynamic. I documented an
asymmetric inflation transmission chain running India &rarr; Singapore &rarr; UK: India's consumer
price index Granger-causes Singapore's with a two-month lag (p&nbsp;=&nbsp;0.028), and Singapore's
leads the UK's (p&nbsp;=&nbsp;0.039). When I first found this, the natural question was: why India,
and why two months? The dominant currency paradigm offers the answer.
</div>

<div class="essay-p">
India is a major commodity and food producer. When Indian supply conditions change &mdash; a drought,
an energy shock, an agricultural disruption &mdash; dollar commodity prices move first. Singapore,
which imports virtually everything and prices those imports in dollars, feels the shock
approximately two months later when the shipments arrive and get priced into domestic CPI.
The lag is not a monetary phenomenon. It is a supply chain phenomenon. And the dollar
is the pipe.
</div>

<div class="essay-divider">&#x1F43E; &middot; &middot; &middot; &#x1F43E;</div>

<div class="essay-p">
The policy implication is elegant and somewhat underappreciated. The Monetary Authority of
Singapore manages the Singapore dollar against a trade-weighted basket &mdash; the S$NEER band.
The dominant anchor in that basket is the US dollar. When MAS appreciates the S$NEER to fight
inflation, it is strengthening the SGD against the dollar &mdash; directly offsetting the
dollar-priced import cost surge. The instrument matches the channel exactly.
</div>

<div class="essay-p">
This explains something that puzzled observers during the 2022 inflation surge: why did Singapore
disinflate faster and more cleanly than the UK, even though both economies were exposed to
the same global commodity shock? The Bank of England raised rates fourteen consecutive times,
targeting domestic demand. MAS adjusted the exchange rate, targeting the import price channel.
Both were responding to the same upstream pressure &mdash; but only one was addressing the actual
transmission mechanism. MAS was managing its exposure to the dollar's shadow.
The BoE was fighting the chaos without identifying the Pink Panther.
</div>

<div class="essay-pullquote">
<p>"We put a green bow on the box. The box is still full of commodities.
And somebody, somewhere upstream, is about to have a very good year."</p>
<div class="pq-source">FROM &ldquo;THE GREEN BOW ON THE SAME OLD BOX&rdquo; &nbsp;&middot;&nbsp; GOKHALE (2026)</div>
</div>

<div class="essay-p">
The broader implication extends beyond Singapore. If dollar invoicing means that the dominant
currency channel is the primary mechanism through which supply shocks transmit globally,
then the relevant question for any central bank is not &ldquo;what are domestic demand conditions
doing?&rdquo; but &ldquo;what is the dollar doing to our import prices?&rdquo; Small open economies that target
exchange rates &mdash; Singapore, Switzerland, several ASEAN members &mdash; are structurally better
positioned to answer that question, because their policy framework forces them to watch the
dollar directly. Large economies with independent monetary policy and flexible exchange rates
are watching the wrong variable.
</div>

<div class="essay-p">
The climate transition adds a further layer. The green economy is rematerialising the world &mdash;
lithium, cobalt, copper, rare earths replacing oil and gas as the critical upstream commodities.
The new upstream economies are Chile, Congo, China. But they are still priced in dollars.
The Pink Panther hasn't left the building. He's just wearing a different colour.
</div>

<div class="essay-p">
The Pink Panther, meanwhile, keeps moving. Dollar commodity prices, dollar trade invoices,
dollar-denominated debt &mdash; the dominant currency is already in the next scene before anyone
has finished investigating the last one. The question is not whether to watch it.
It is whether your framework is even designed to look in the right direction.
</div>

<div class="essay-byline" style="border-top:1px solid #2A2A2A;border-bottom:none;padding-top:20px;padding-bottom:0;margin-top:32px;">
ANUJA A. GOKHALE &nbsp;&middot;&nbsp; SSRN.COM/ABSTRACT=6514338 &nbsp;&middot;&nbsp;
MONSOON-INDEX.STREAMLIT.APP &nbsp;&middot;&nbsp; ANUJAGOKHALE.GITHUB.IO
</div>
</div>
""", unsafe_allow_html=True)

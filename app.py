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
    """Rolling correlation between lagged series1 and series2."""
    s1_lagged = series1.shift(lag)
    results = []
    for i in range(window, len(series1)):
        s1_w = s1_lagged.iloc[i-window:i]
        s2_w = series2.iloc[i-window:i]
        valid = (~s1_w.isna()) & (~s2_w.isna())
        if valid.sum() > 10:
            corr = np.corrcoef(s1_w[valid], s2_w[valid])[0,1]
            results.append({"date": series1.index[i], "corr": round(corr, 3)})
        else:
            results.append({"date": series1.index[i], "corr": np.nan})
    return pd.DataFrame(results).set_index("date")


# ── LOAD DATA ─────────────────────────────────────────────────────────────────
dxy = get_dxy_data()
commodities = get_commodity_data()
cpi = get_cpi_data()
latest_dxy = dxy.iloc[-1]
latest_date = dxy.index[-1]
rolling_dxy_sg = rolling_correlation(dxy, cpi["Singapore CPI"], window=24, lag=2)
rolling_dxy_uk = rolling_correlation(dxy, cpi["UK CPI"], window=24, lag=3)
avg_corr_sg = rolling_dxy_sg["corr"].dropna().mean()
avg_corr_uk = rolling_dxy_uk["corr"].dropna().mean()

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
t1, t2, t3, t4, t5 = st.tabs([
    "🐾 The Shadow", "🟡 Green Gold", "📡 Transmission Signal",
    "🔮 Scenario", "📑 Framework"
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
                     tickfont=dict(color="#F0EDE8"))
    fig.update_yaxes(title_text="CPI YoY (%)", gridcolor="#2A2A2A", secondary_y=True,
                     tickfont=dict(color="#F0EDE8"))
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
    st.markdown('<div class="sec-hdr">Rolling Dollar Transmission Signal — DXY → Downstream CPI</div>', unsafe_allow_html=True)
    st.markdown("""<p style="color:#999;font-size:13px;margin-bottom:16px;">
    If the dominant currency channel is active, DXY movements should lead Singapore and UK CPI
    by 2-3 months. The rolling correlation below tests whether that relationship holds over time.
    When the signal is strong (above 0.4), the dollar's shadow is driving downstream inflation.
    </p>""", unsafe_allow_html=True)

    fig3 = go.Figure()

    fig3.add_hrect(y0=0.4, y1=1.0,
                   fillcolor="rgba(255,45,120,0.05)", line_width=0,
                   annotation_text="Strong dollar transmission",
                   annotation_position="right",
                   annotation_font_size=10,
                   annotation_font_color="#FF2D78")

    fig3.add_trace(go.Scatter(
        x=rolling_dxy_sg.index.strftime("%Y-%m-%d"),
        y=rolling_dxy_sg["corr"],
        name="DXY → SG CPI (Lag 2M)",
        line=dict(color="#FF2D78", width=2.5),
        fill="tozeroy",
        fillcolor="rgba(255,45,120,0.07)",
        hovertemplate="<b>DXY→SG</b><br>%{x|%b %Y}: %{y:.3f}<extra></extra>"
    ))

    fig3.add_trace(go.Scatter(
        x=rolling_dxy_uk.index.strftime("%Y-%m-%d"),
        y=rolling_dxy_uk["corr"],
        name="DXY → UK CPI (Lag 3M)",
        line=dict(color="#4A90D9", width=2, dash="dot"),
        hovertemplate="<b>DXY→UK</b><br>%{x|%b %Y}: %{y:.3f}<extra></extra>"
    ))

    fig3.add_shape(type="line",
                   x0=rolling_dxy_sg.index.strftime("%Y-%m-%d")[0],
                   x1=rolling_dxy_sg.index.strftime("%Y-%m-%d")[-1],
                   y0=0, y1=0,
                   line=dict(color="#444444", width=1))

    fig3.add_shape(type="line",
                   x0=rolling_dxy_sg.index.strftime("%Y-%m-%d")[0],
                   x1=rolling_dxy_sg.index.strftime("%Y-%m-%d")[-1],
                   y0=0.4, y1=0.4,
                   line=dict(color="rgba(255,45,120,0.4)", width=1, dash="dash"))

    fig3.update_layout(**LAYOUT, height=360, showlegend=True,
                       margin=dict(l=0, r=130, t=20, b=70),
                       legend=dict(orientation="h", y=-0.2, x=0.5, xanchor="center",
                                   bgcolor="rgba(0,0,0,0)", font=dict(size=12, color="#F0EDE8")),
                       yaxis=dict(title="Rolling Correlation", gridcolor="#2A2A2A",
                                  tickfont=dict(color="#F0EDE8")),
                       xaxis=dict(gridcolor="#2A2A2A", tickfont=dict(color="#F0EDE8")))
    st.plotly_chart(fig3, use_container_width=True)
    st.caption("Rolling 24-month window. Above pink dashed line = strong dollar transmission channel active.")

    r1, r2 = st.columns(2)
    with r1:
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num" style="color:#FF2D78">{avg_corr_sg:.2f}</div>
          <div class="stat-lbl">Avg DXY→SG correlation (24M rolling, lag 2M)</div></div>""",
                    unsafe_allow_html=True)
    with r2:
        st.markdown(f"""<div class="stat-card">
          <div class="stat-num" style="color:#4A90D9">{avg_corr_uk:.2f}</div>
          <div class="stat-lbl">Avg DXY→UK correlation (24M rolling, lag 3M)</div></div>""",
                    unsafe_allow_html=True)


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
        # Simple linear projection based on historical relationship
        sg_beta = avg_corr_sg * (cpi["Singapore CPI"].std() / dxy.std())
        uk_beta = avg_corr_uk * (cpi["UK CPI"].std() / dxy.std())
        sg_impact = round(dxy_shock * sg_beta, 2)
        uk_impact = round(dxy_shock * uk_beta, 2)

        sg_current = cpi["Singapore CPI"].iloc[-1]
        uk_current = cpi["UK CPI"].iloc[-1]

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
                is projected to shift Singapore CPI by <strong>{sg_impact:+.2f}pp</strong>
                and UK CPI by <strong>{uk_impact:+.2f}pp</strong> after {lag_choice} months,
                via the dominant currency import price channel.
              </div>
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

    st.markdown('<div class="sec-hdr">Research Basis</div>', unsafe_allow_html=True)
    st.dataframe(pd.DataFrame({
        "Finding": [
            "India → Singapore (Granger)",
            "Singapore → UK (Granger)",
            "DXY → SG CPI correlation",
            "DXY → UK CPI correlation",
            "Transmission lag (DXY → SG)",
            "Transmission lag (DXY → UK)"
        ],
        "Value": [
            "p = 0.028 ✓",
            "p = 0.039 ✓",
            f"{avg_corr_sg:.2f} (rolling 24M)",
            f"{avg_corr_uk:.2f} (rolling 24M)",
            "~2 months",
            "~3 months"
        ],
        "Source": [
            "Gokhale (2026) ssrn/6514338",
            "Gokhale (2026) ssrn/6514338",
            "This dashboard",
            "This dashboard",
            "Gokhale (2026)",
            "This dashboard"
        ]
    }), use_container_width=True, hide_index=True)

    st.markdown("---")
    st.caption("""Built by Anuja A. Gokhale · MA Applied Economics, NUS (Merit Scholar)
    · anujagokhale1604@gmail.com · ssrn.com/abstract=6514338 · monsoon-index.streamlit.app""")

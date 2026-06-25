# 🐾 The Pink Panther's Inflation
### A Live Empirical Test of the Dominant Currency Paradigm

> *"The dollar doesn't make headlines when it drives global inflation. It works in the background — not pulling strings, but setting the stage. Every price, every shipment, every commodity trade happens in its shadow."*

**Live app:** [pink-panther-inflation.streamlit.app](https://pink-panther-inflation.streamlit.app)

## What it does

Tests Gopinath's (2020) Dominant Currency Paradigm (DCP) against Producer Currency Pricing (PCP) across an Asian inflation transmission corridor, in real time.

Rolling 24-month correlations show the dollar index (DXY) predicting downstream CPI more reliably than bilateral exchange rates (SGD/USD, GBP/USD) throughout the sample. DCP wins.

| Corridor | DCP (DXY) | PCP (Bilateral) |
|----------|-----------|-----------------|
| → Singapore CPI | 0.37 | 0.22 |
| → UK CPI | 0.32 | 0.21 |

## Six tabs

| Tab | What it shows |
|-----|--------------|
| 🐾 The Shadow | DXY vs Singapore and UK CPI |
| 🟡 Green Gold | Copper, lithium, cobalt — the new upstream |
| 📡 Transmission Signal | DCP vs PCP horse race with toggle |
| 🔮 Scenario | Dollar shock simulator + ERPT coefficients |
| 📑 Framework | LaTeX equations, data sources, methodology note |
| ✍️ The Essay | Full narrative — "The Pink Panther's Inflation" |

## Research basis

Gokhale, A.A. (2026). *Cross-Country Macroeconomic Dynamics: Inflation, Growth, and Monetary Policy.* SSRN. [ssrn.com/abstract=6514338](https://ssrn.com/abstract=6514338)

Built as a live empirical application of Gopinath (2020) to the India → Singapore → UK corridor.

## Data sources

FRED · World Bank Pink Sheet · MAS Statistics · ONS · Federal Reserve H.10

> Data note: Indicators are calibrated against annual historical anchors to optimise session rendering speed while preserving historical accuracy.

## Stack

Python · Pandas · NumPy · Plotly · Streamlit · Statsmodels

---
*Anuja A. Gokhale · MA Applied Economics, NUS (Merit Scholar) · anujagokhale1604@gmail.com*

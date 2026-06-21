# datasci207sec10su26-group2-finalproj

## sandy_eda.ipynb — EDA Summary

**Dataset:** CRSP daily stock data, 2010–2025
- 15M+ stock-day observations across 7,950 stocks (4,017 trading days)
- Zero missing values

**Key Findings:**

1. **Return Distribution** — Daily log returns have mean −0.020%, std 3.78%, and excess kurtosis of 20.85 (fat tails — extreme moves far more common than a normal distribution predicts)

2. **AVSP Signal Features** — `pos` and `neg` (Average Shortest Path Length of positive/negative visibility graphs) both range [1.0, 2.667] with near-identical means (~1.62), confirming symmetric construction

3. **Signal Predictive Power** — Signal (pos − neg) shows statistically significant correlation with next-day returns (Spearman r = 0.015, p < 0.001). Quintile spread: strongest Sell quintile averages −5.96%/yr, strongest Buy quintile +4.99%/yr

4. **Sector Heterogeneity** — Signal works best in Finance & Real Estate (Buy → +0.080%/day); inverted in Mining (Buy → −0.060%/day)

5. **Universe Filtering** — Final modeling universe: 4,435 stocks (from 9,318), after removing penny stocks (<$5), low-volume names, and thin history

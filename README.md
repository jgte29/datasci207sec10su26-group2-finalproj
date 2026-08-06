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

## random_walk_strategy.ipynb — Null Baseline

**Purpose:** Control strategy to test whether other models beat pure chance — signal is `np.random.normal() > 0` each day per stock, independent of price or model information.

**Setup:** Full universe (5,232 tickers), 2021–2025 test window, reads from `./data/dsf/` (fixed from a broken legacy CSV path in the original notebook).

**Result:** Long-Hold +105.72% vs. Random Walk +83.50%.

**Caveat:** Unseeded — re-running gives different results (measured 73%–153% across 8 repeated runs on the same data). Treat any single reported number as one realization, not a fixed result.

## linear_regression_baseline.ipynb — Supplemental Baseline (vs. XGBoost Regressor)

**Purpose:** Requested by Jordan as an additional baseline alongside `xgboost_regressor.ipynb` — identical 19 features (no ASPL) and target, swapping XGBoost for plain OLS linear regression to isolate the effect of model complexity.

**Setup:** Full universe, split matched to Jordan's `SPLIT_DATE=2014-01-01` for apples-to-apples comparison.

**Result:** MAE 0.1553, R² 0.9995 (high R² reflects strong day-to-day price autocorrelation, not model skill — not strong evidence of predictive power on its own). Trading backtest: Long-Hold +283.87% vs. Strategy +181.25% — underperformed the benchmark.

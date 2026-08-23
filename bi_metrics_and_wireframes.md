# Climate & Air Quality Forecasting System: Business Metrics & Wireframes

## 1. Business Metrics

### 1.1 Air Quality Index (AQI) Thresholds
We adhere to standard EPA AQI breakpoints for reporting and alerting:
| AQI Range | Category | Color Code | Description |
|-----------|----------|------------|-------------|
| 0 - 50 | Good | Green | Air quality is satisfactory, and air pollution poses little or no risk. |
| 51 - 100 | Moderate | Yellow | Air quality is acceptable. However, there may be a risk for some people. |
| 101 - 150 | Unhealthy for Sensitive Groups | Orange | Members of sensitive groups may experience health effects. |
| 151 - 200 | Unhealthy | Red | Some members of the general public may experience health effects. |
| 201 - 300 | Very Unhealthy | Purple | Health alert: The risk of health effects is increased for everyone. |
| 301 and higher | Hazardous | Maroon | Health warning of emergency conditions: everyone is more likely to be affected. |

### 1.2 Forecast Accuracy & Error Tolerance
To ensure the reliability of our forecasting models, we define the following acceptable error margins for 24-hour and 48-hour forecasts:
*   **Mean Absolute Error (MAE):** < 15 AQI points for 24h forecast; < 20 AQI points for 48h forecast.
*   **Root Mean Square Error (RMSE):** < 20 AQI points for 24h forecast; < 25 AQI points for 48h forecast.
*   **Directional Accuracy:** The model should correctly predict the direction of the AQI change (increasing/decreasing) at least 80% of the time.

### 1.3 System & Operational KPIs
*   **Data Freshness:** 99% of IoT/sensor data ingested and processed within 15 minutes of measurement.
*   **System Uptime:** 99.9% availability for the dashboard and API endpoints.
*   **Alert Latency:** Push notifications and alerts dispatched within 5 minutes of a critical AQI threshold breach (AQI > 150).

---

## 2. Low-Fidelity Dashboard Wireframes

### 2.1 Main Executive Dashboard
This dashboard provides a real-time overview of current air quality and short-term forecasts for general users and city officials.

```text
+-----------------------------------------------------------------------------+
|  [Logo] Climate & AQI Forecaster                     [Home] [Map] [Alerts]  |
+-----------------------------------------------------------------------------+
|                                                                             |
|  [ City Selector: Seattle, WA v ]  |  Last updated: 10 mins ago             |
|                                                                             |
+------------------------------------+----------------------------------------+
| CURRENT CONDITIONS                 | 24-HOUR FORECAST TREND                 |
|                                    |                                        |
|      +-------+                     |   300 |                                |
|      |       |                     | A 200 |           * *                  |
|      |  142  |  UNHEALTHY FOR      | Q 100 | * * * * *     * * * * * *      |
|      |       |  SENSITIVE GROUPS   | I   0 +--------------------------      |
|      +-------+                     |         Now  +6h  +12h +18h +24h       |
|                                    |                                        |
|  PM2.5: 55 µg/m³   O3: 40 ppb      | [ Alert: Peak AQI 160 expected at 5PM ]|
+------------------------------------+----------------------------------------+
| REGIONAL HEATMAP                   | KEY POLLUTANTS BREAKDOWN               |
|                                    |                                        |
|  [Map showing color-coded zones]   | PM2.5 [||||||||||        ] 55% of AQI  |
|  [Red areas in downtown]           | PM10  [||||              ] 20% of AQI  |
|  [Green areas in suburbs]          | O3    [||||||            ] 25% of AQI  |
|                                    |                                        |
+------------------------------------+----------------------------------------+
```

### 2.2 Analyst / Data Science Dashboard
This view is designed for BI analysts and data scientists to evaluate model performance and historical trends.

```text
+-----------------------------------------------------------------------------+
|  [Logo] AQI Forecaster - Analyst View        [Metrics] [Models] [Export]    |
+-----------------------------------------------------------------------------+
|  Date Range: [ Last 30 Days v ]  |  Model: [ Gradient Boosting v ]          |
+-----------------------------------------------------------------------------+
| FORECAST VS ACTUALS (Past 30 Days)                                          |
|                                                                             |
| AQI                                                                         |
| 200 |         x x                  Legend:                                  |
| 150 |       - - - -                  [-] Actual AQI                         |
| 100 | - - -         - - -            [x] Forecasted AQI                     |
|  50 |                                                                       |
|   0 +-------------------------                                              |
|      01/01   01/10   01/20                                                  |
+------------------------------------+----------------------------------------+
| MODEL PERFORMANCE METRICS          | ERROR DISTRIBUTION                     |
|                                    |                                        |
|  MAE (24h):  12.4  (Target: <15)   |  [ Histogram showing most errors       |
|  RMSE (24h): 16.8  (Target: <20)   |    falling between -10 and +10 AQI     |
|                                    |    points ]                            |
|  Directional Accuracy: 84%         |                                        |
+------------------------------------+----------------------------------------+
```

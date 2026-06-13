# Apple Stock Analysis

Analysis of Apple (AAPL) stock from 2020 to 2024 using Python.

## What I did
- Downloaded real stock data using yfinance
- Calculated 50-day and 200-day moving averages
- Backtested a Golden Cross / Death Cross trading strategy
- Compared strategy returns against buy-and-hold

## Results
- Buy and Hold: +163.2%
- MA Strategy: +38.5%

## Key Finding
The moving average strategy underperformed buy-and-hold because moving averages are lagging indicators. When the Golden Cross signal appeared in 2023, the price had already started recovering, causing the strategy to miss a significant portion of the 2020-2021 rebound.

## Tools
- Python
- yfinance
- pandas
- matplotlib


## Charts
![Moving Average](movingaverage_price_date.jpg)
![Backtest](backtest.jpg)

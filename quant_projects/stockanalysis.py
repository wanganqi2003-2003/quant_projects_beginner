import yfinance as yf
import matplotlib.pyplot as plt

# ============ 第一步：获取数据 ============
data = yf.download("AAPL", start="2020-01-01", end="2024-01-01")
close = data["Close"]["AAPL"]

# ============ 第二步：计算移动平均线 ============
ma50 = close.rolling(50).mean()
ma200 = close.rolling(200).mean()

# ============ 第三步：画价格 + 均线图 ============
plt.figure(figsize=(12, 5))
plt.plot(close, label="价格", alpha=0.5)
plt.plot(ma50, label="50日均线", color="orange")
plt.plot(ma200, label="200日均线", color="red")
plt.title("Apple Stock - Moving Average")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# ============ 第四步：回测交易策略 ============
signal = (ma50 > ma200).astype(int)
daily_return = close.pct_change()
strategy_return = daily_return * signal.shift(1)

cumulative_market = (1 + daily_return).cumprod()
cumulative_strategy = (1 + strategy_return).cumprod()

# ============ 第五步：画回测结果 ============
plt.figure(figsize=(12, 5))
plt.plot(cumulative_market, label="买入持有（什么都不做）")
plt.plot(cumulative_strategy, label="均线策略")
plt.title("策略回测：均线策略 vs 买入持有")
plt.xlabel("日期")
plt.ylabel("累计收益倍数")
plt.legend()
plt.show()

print(f"买入持有最终收益：{(cumulative_market.iloc[-1]-1)*100:.1f}%")
print(f"均线策略最终收益：{(cumulative_strategy.iloc[-1]-1)*100:.1f}%")



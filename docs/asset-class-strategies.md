# Asset-class strategies (v0.58)

Research playbooks only. Scores are synthetic multi-factor proxies. Not signals for live trading.

## Major (BTC, ETH)

Adaptive multi-factor: EMA crossovers, Supertrend, Ichimoku cloud, Bollinger, Keltner, VWAP, MACD, Heikin-Ashi, Parabolic SAR, Donchian, GARCH/EWMA vol forecast, Fib/Elliott, options skew/delta, funding, on-chain (MVRV, SOPR, NVT, OI, order-flow, liquidity), correlation-adjusted outside stress. Risk cap 8%.

## Large-cap alt

Volume-profile breakout + VWAP + MACD + multi-TF + relative strength z-score vs major + correlation filter + regime cluster + volume delta + netflow + OI + order-flow + Fib + DEX LP + Williams %R. Risk cap 4%.

## Stablecoin

Adaptive peg deviation (15-50 bps) with volume confirmation + netflow + liquidity depth + SOPR + PUELL proxy. Risk cap 0%.

## DeFi

Calm multi-scale + low anomaly + Supertrend + ADX + on-chain activity/smart-money + isolation + risk-parity + CVaR + LP depth/IL + CCI. Risk cap 2%.

## Meme

Qualified burst + StochRSI + consistency + hard horizon + volume-flow decay + anomaly + residual + liq heat + order-flow + social synthetic + Fib + Williams. Risk cap 0.5%.

## L2

Relative strength + MACD vs benchmark + adaptive MTF + correlation + cluster + vol forecast + transition + Elliott + CCI. Risk cap 3%.

## RWA

Slow multi-scale + gap/anomaly halt + volume filter + isolation + forecast + CVaR + realized-cap + NVT. Risk cap 2%.

## Perpetual

Negative funding carry + contained drift + low anomaly + funding flip + correlation + residual + OI + order-flow + gamma/vanna. Risk cap 2%.

## AI-token

Hybrid burst + activity + divergence + low isolation + strict horizon + smart-money + OI + transition + options vanna + social. Risk cap 1%.

All classes apply multi-gate risk: class caps, confidence floors, correlation, anomaly, isolation, drawdown, kill switch, vol scaling + forecast + risk-parity + CVaR + HRP.

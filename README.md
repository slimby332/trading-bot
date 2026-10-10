# Trading Bot

A paper-trading bot for US stocks that trades on live market data and news headlines, with a dashboard showing its performance, the reason behind every trade and settings to tune its risk and trading style.

> **Paper trading only.** This bot trades simulated money on an Alpaca paper account. Nothing here is financial advice.

## Status

**v0 in progress:** project setup, storage and broker connection.

| Milestone | Goal |
|---|---|
| v0 | Database schema, live price stream, a manual paper order placed and recorded |
| v1 | Rule-based swing-trading bot running live on paper, with a logged reason for every trade and enforced risk limits |
| v2 | Dashboard: returns vs buy-and-hold, charts with trade markers, trade log, settings panel |
| v3 | News-aware ML strategy, backtesting harness, honest evaluation |
| v4 | Deployed on a schedule, public read-only dashboard, intraday mode, crypto |

## How it's judged

Against a buy-and-hold baseline, with backtests free of look-ahead bias, not just "it made X%".

## Stack

- **Bot & backend:** Python, FastAPI, SQLite
- **Broker & data:** Alpaca paper trading API (market data + news)
- **Dashboard (planned):** React + Vite, TradingView Lightweight Charts
- **Tooling:** uv, ruff, pytest, pre-commit with gitleaks, GitHub Actions CI

## Setup

Requires [uv](https://docs.astral.sh/uv/) and a free [Alpaca](https://alpaca.markets) paper account.

```bash
git clone https://github.com/slimby332/trading-bot.git
cd trading-bot

# Add your own Alpaca paper keys (.env is gitignored)
cp .env.example .env

# Install dependencies and run the tests
cd backend
uv sync
uv run pytest
```

For contributors, install the git hooks once per clone:

```bash
pre-commit install
```

## License

[PolyForm Noncommercial 1.0.0](LICENSE). Commercial use is not permitted.

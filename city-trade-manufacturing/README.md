# City trade and manufacturing rankings (16 Oct 2026)

Answers Jeffrey's question of 16 Oct 2026: which cities handle the most goods trade (exports and imports), and which have the greatest manufacturing output and productivity. The charts are on the **World trade and factory cities** dashboard: https://claude.ai/artifact/MqJdrybVGbWF97m27uMMz3

## Files

| File | What it holds |
|---|---|
| `trade.csv` | 47 places with exports, imports and total goods trade, US$ bn, 2025 or latest year |
| `exports_only.csv` | Places that publish exports but no imports (US metros, Istanbul, Chihuahua state, Jamnagar) |
| `japan_ports.csv` | Japan's trade by customs port or airport, 2025 (port-of-clearance basis, not firm location) |
| `container_ports.csv` | 2025 container throughput (million TEU) for the busiest ports; cargo passing through, a different measure from trade value |
| `manufacturing.csv` | Manufacturing value added (US$ bn), manufacturing jobs and value added per job for 38 places |
| `exchange_rates.csv` | Federal Reserve G.5A annual averages used for conversion |
| `worker-notes/` | The research workers' raw tables in local currency, with a source URL on every row and method notes per region |

## Definitions used

- **Trade:** customs value of goods exported plus imported, counted where the trading firm is based (China, Korea, Vietnam, US, Brazil), in US dollars at the year's average rate. Exceptions are tagged in the `caveat` column: Hong Kong and Singapore are re-export hubs; Beijing's imports are inflated by central state firms headquartered there; Malaysian states are derived from state shares; Paris and London are whole regions; Dubai and Abu Dhabi are non-oil trade.
- **Manufacturing output:** manufacturing value added. Chinese cities publish only industrial value added (adds mining and utilities). Suzhou, Guangzhou, Dongguan, Wuxi and Foshan publish neither, so their rows hold secondary-industry value added (adds construction) and are flagged `upper_bound = yes`.
- **Productivity:** value added divided by manufacturing jobs in the same place. US jobs are BLS payroll jobs (no self-employed); Europe is Eurostat employed persons.
- **City unit:** whatever each country publishes, noted in the `unit` column. Chinese prefecture-level cities and municipalities include rural counties.

## Known gaps

- Korea and Taiwan manufacturing by city (Hwaseong, Ulsan, Hsinchu) could not be fetched: KOSIS and Taiwan's statistics sites refuse automated reads.
- No Chinese city publishes manufacturing employment in its bulletin; Shanghai's per-job figure pairs 2025 output with 2023 census jobs.
- BEA stopped publishing metro GDP from the 2024 data year; US metro manufacturing comes from the Greater Houston Partnership's sums of BEA county data (top 10 only).
- US metro imports are not published. New York's 2025 exports jumped 62%, most likely gold flowing back out of New York vaults (inferred from the 2025 surge in US gold exports).
- Dubai's 2025 trade split was not found; the 2023 non-oil total is used.

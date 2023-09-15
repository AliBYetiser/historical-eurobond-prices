# A web crawler for obtaining data on eurobonds issued by the treasury of the Republic of Turkey.

Eurobonds are debt instruments used by governments, corporations, and other entities to raise capital from the international financial markets. It operates as a borrowing mechanism, allowing issuers to secure funds from a wide range of investors globally. 

The value of eurobonds hing on a range of interconnected factors. It is influenced by prevailing interest rates, issuer credit quality, bond's maturity timeline, supply and demand dynamics, currency exchange rates between the bond's denomination and investors' currency, market sentiment, economic conditions, and inflation expectations. Liquidity, determined by ease of trading, impacts value stability. Callable or convertible features can introduce variability. Overall market conditions, encompassing economic growth, monetary policies, and volatility, collectively contribute to eurobond value fluctuations.

There is a lack of available public historical data on both government and private eurobonds in Turkey except for one government bank. **This repository functions to gather data, running daily on google cloud, from one private bank (Isbank) and a government banks (Ziraatbank) where the latter also provides retrospective data.** 

Data pulled from:
[Isbank](https://www.isbank.com.tr/eurobond-fiyatlari), 
[Ziraatbank](https://www.ziraatbank.com.tr/tr/bireysel/yatirim/eurobond#)

The code is "fragile" as bank sites can easily add anti-crawler rules and captchas.

Further TODO is to visualize the retrospective data via Tableau or other tools.

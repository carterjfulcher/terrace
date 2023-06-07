<div align="center">

<img src="https://user-images.githubusercontent.com/23005868/207764881-af11b355-6094-4ee3-9855-520b103c5e40.png" alt="drawing" width="300"/>

<h4>terrace: an open source algorithmic trading engine optimized for a great developer experience</h4>

<h3>

[Home Page](https://github.com/carterjfulcher/terrace) | [Documentation](https://google.com) | [Discord](https://discord.gg/7NnvrG3Rt6) | [Examples](examples)

</h3>

[![GitHub Repo stars](https://img.shields.io/github/stars/carterjfulcher/terrace)](https://github.com/carterjfulcher/terrace/stargazers)
[![Test](https://github.com/carterjfulcher/terrace/actions/workflows/test.yaml/badge.svg)](https://github.com/carterjfulcher/terrace/actions/workflows/test.yaml)

</div>

<!-- ## Open source algorithmic trading engine, optimizing for a great developer experience. -->

---

*Terrace aims to remain near 1000 lines at the core, provide a flexible API, and great developer expereince.*

Easily research, test, and deploy a variety of trading strategies across all asset classes. 

---

Creating a strategy is easy:

```python3
from terrace.strategy import Strategy
from terrace.ta import sma

class TAStrategy(Strategy):
  def step(self, ctx):
    sma = ta.sma(ctx.close, 20)
    if ctx.close > sma:
      self.long()
    elif ctx.close < sma:
      self.short()
```

## Features
- **Modular design** - 
<div align="center">
  <img src="examples/diagram.png" width="80%">
</div>

<!-- ![](examples/diagram.png) -->

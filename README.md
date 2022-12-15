# Terrace

Open source platform for financial index creation, management, and operations.

## Features

- Index calculation
- Pre/Post Trade audits
- Index dissemination
- Automatic rebalance and reconstitution
- Quickly create and test indices
- Backtesting integration with Fulcher Analytics

## Example

The below creates an index of all securities with a share price of greater than $50, and rebalances it to equal weights. Then, audits the members

```python3
from terrace import Index, IndexComponent

def audit(component: IndexComponent):
  assert(component.closing > 50)

def create(universe):
  pass

myIndex = Index(
  identifier="MyIndex",
  strategy=(audit, create)
)

myIndex.components = IndexComponent.fromExcel("./opening.xls")

myIndex.autoRebalance() # ~46% Alignment
myIndex.auditMembers(ignoreFailures=True)

```

```
Results:
✅ BLDR UN Equity passed
✅ CALX UN Equity passed
✅ CAR UW Equity passed
CCBG UW Equity is not in compliance with the rulset !!
```

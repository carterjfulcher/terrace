<img src="https://user-images.githubusercontent.com/23005868/207764881-af11b355-6094-4ee3-9855-520b103c5e40.png" alt="drawing" width="500"/>

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

## Documentation

### Indexes

Creating an Index is as easy as:

```python3
from terrace import Index

def audit(component: IndexComponent):
  pass

def create(universe):
  pass

myIndex = Index(
  identifier="MyIndex",
  strategy=(audit, create)
)
```

The `audit` and `create` functions make up the strategy / methodology of the index.

### Index Components

### Writing Audit Functions

Audit functions are a set of assert statements that verify each `IndexComponent` is eligible via the methodology.

In an `audit` function, the `IndexComponent` is the only parameter. Every data point that the `IndexComponent` was initialized with
is avaialble in this function (see section above for details regarding `IndexComponent` creation). Take the below example, which audits an
index to ensure eligiblity for something similiar to the `S&P 500 Index`:

```
def audit(component: IndexComponent):
  assert(component['marketCap'] > 14600000000) # $14.6B+ market cap
  assert(component['closePrice'] > 5) # not a penny stock
  assert(component['countryOfDomicile'] == 'US') # US Based
```

### Writing Create Functions

### Automated Rebalances

### Automated Reconstitutions

### Pre / Post Trade Auditing

### Calculation

### Dissemination

```
Results:
✅ BLDR UN Equity passed
✅ CALX UN Equity passed
✅ CAR UW Equity passed
CCBG UW Equity is not in compliance with the rulset !!

...

Passed: 46 Failed: 52 Total: 98 (46.94%) in 0.0s

```

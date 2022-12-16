<img src="https://user-images.githubusercontent.com/23005868/207764881-af11b355-6094-4ee3-9855-520b103c5e40.png" alt="drawing" width="500"/>

[![Test](https://github.com/carterjfulcher/terrace/actions/workflows/test.yaml/badge.svg)](https://github.com/carterjfulcher/terrace/actions/workflows/test.yaml)

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

```python
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

```python
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

`IndexComponent`s are a dynamic building block for `Index`s. The two attributes they contain
is an `identifier` and a `weight`. Any other param passed in the initialization will be saved
as an attribute for use in `audit` functions.

#### Methods

The following methods initialize a _list_ of `IndexComponent`s from a source. `IndexComponent`s can
be initialized from any source with any amount of rows/datapoints. The only required datapoint
for an `IndexComponent` is an identifier.

`fromCsv` - Returns a list of `IndexComponent`s from a CSV file. Will utilize the first column as the `identifier`

`fromDataFrame` - Returns a list of `IndexComponent`s from a Pandas Dataframe. Will utilize the first column as the `identifier`

`fromExcel` - Returns a list of `IndexComponent`s from an Excel file. Will utilize the first column as the `identifier`

`fromRecords` - Accepts a list of dicts as the first arguement, and an `identifier_key` to determine which key to set the identifier as. Returns list of `IndexComponent`s

### Writing Audit Functions

Audit functions are a set of assert statements that verify each `IndexComponent` is eligible via the methodology.

In an `audit` function, the `IndexComponent` is the only parameter. Every data point that the `IndexComponent` was initialized with
is avaialble in this function (see section above for details regarding `IndexComponent` creation). Take the below example, which audits an
index to ensure eligiblity for something similiar to the `S&P 500 Index`:

```python
def audit(component: IndexComponent):
  assert(component['marketCap'] > 14600000000) # $14.6B+ market cap
  assert(component['closePrice'] > 5) # not a penny stock
  assert(component['countryOfDomicile'] == 'US') # US Based
```

### Writing Create Functions

Create functions take a universe of securities as an input, and filter and
reduce the list until the index is remaining as desired. An exmaple create function is below.

The create function you pass when creating an index is called by
`Index.autoReconstitute(universe)`. The type of universe can be anything
you want as long as the `create` function returns a list of `IndexComponent`s. The below examples feature the use of objects as well
as a dataframe.

```python
# pass dicts
def create(universe: List[Dict[str, Any]]) -> List[IndexComponent]:
  print(universe)
  """
  [
    {id: "ACGL UW Equity", "closing": 60.32},
    {id: "AMKR UW Equity", "closing": 26.46}
  ]
  """
  universe = [i for i in universe if i['closing'] > 50]
  return IndexComponent.fromRecords(universe)

# use a dataframe
def create(universe: pd.DataFrame) -> List[IndexComponent]:
  print(universe.head())
  """
               id                    name      cusip        country  closing currency
0  ACGL UW Equity  ARCH CAPITAL GROUP LTD  G0450A105        BERMUDA    60.32      USD
1  AMKR UW Equity  AMKOR TECHNOLOGY INC  031652100  UNITED STATES    26.46      USD
  """

  df = df[df['closing'] > 50]

  return IndexComponent.fromDataFrame(df) # returns list of IndexComponents
```

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

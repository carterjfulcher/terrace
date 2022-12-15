"""
Basic Index
"""

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

myIndex.autoRebalance()
myIndex.auditMembers(ignoreFailures=True)

"""
Auditing MyIndex members...
✅ AAPL passed
✅ MSFT passed
✅ AMZN passed
✅ GOOG passed
✅ TSLA passed
Passed: 5 Failed: 0 Total: 5 (100.0%)
"""

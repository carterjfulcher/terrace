
"""
Basic Index
"""

from terrace import Index, IndexComponent

def audit(component: IndexComponent):
  assert component.identifier == "AAPL"

def create(universe):
  pass 

myIndex = Index(
  identifier="MyIndex",
  strategy=(audit, create)
)

v = IndexComponent('AAPL', 1.0, {'test': 'hello'})

myIndex.components = [v]



myIndex.autoRebalance()
myIndex.auditMembers(ignoreFailures=True)

print(myIndex)

"""
Auditing MyIndex members...
✅ AAPL passed
✅ MSFT passed
✅ AMZN passed
✅ GOOG passed
✅ TSLA passed
Passed: 5 Failed: 0 Total: 5 (100.0%)
"""

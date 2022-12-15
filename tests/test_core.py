from terrace import Index
from terrace.index.component import IndexComponent
import pytest

@pytest.fixture
def index():
    def audit(component: IndexComponent):
        assert component.identifier == "AAPL"
        return True 

    def create():
        return None

    return Index(
        identifier="TESTINDEX",
        strategy=(audit, create),
    )

def test_component_creation(index):
    index.components = [IndexComponent("AAPL", 1)]

def test_component_audit(index ):
    index.components = [IndexComponent("AAPL", 1)]
    assert index.auditMembers()

def test_rebalance(index):
    index.components = [IndexComponent("AAPL", 0.25), IndexComponent("MSFT", 0.75)]
    index.autoRebalance()
    assert(index.components[0].weight == 0.5)
    assert(index.components[1].weight == 0.5)
    assert(sum([components.weight for components in index.components]) == 1)

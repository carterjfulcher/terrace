from terrace.types import IndexType, Frequency, WeightingMethod
from typing import List, Callable, Tuple
from .component import IndexComponent
from termcolor import colored
import time 
import json

class Index:
  def __init__(self, 
    identifier: str, 
    strategy: Tuple[Callable, Callable], 
    dividendReinvestment: bool = True, 
    version: IndexType = IndexType.PRICE_RETURN, 
    rebalance: Frequency = Frequency.QUARTERLY, 
    reconstitute: Frequency = Frequency.YEARLY, 
    weightingMethod: WeightingMethod = WeightingMethod.EQUAL_WEIGHT, 
    components: List[IndexComponent] = []
  ):
    self.identifier = identifier
    self.dividendReinvestment = dividendReinvestment
    self.version = version
    self.rebalance = rebalance
    self.reconstitute = reconstitute
    self.weightingMethod = weightingMethod
    self.audit, self.create = strategy
    self.components = components

  # save and load Index to json
  def save(self, path: str):
    with open(path, "w") as file:
      file.write(json.dumps(self.__dict__))
  
  def load(self, path: str):
    with open(path, "r") as file:
      self.__dict__ = json.loads(file.read())

  def autoRebalance(self, marketCapDataKey="marketCap", customWeightingMethod=None, auditResults=False):
    for component in self.components:
      if self.weightingMethod == WeightingMethod.EQUAL_WEIGHT:
        component.weight = 1 / len(self.components)
      elif self.weightingMethod == WeightingMethod.MARKET_CAP_WEIGHT:
        component.weight = component[marketCapDataKey] / sum([component[marketCapDataKey] for component in self.components])
      elif self.weightingMethod == WeightingMethod.CUSTOM_WEIGHT:
        component.weight = customWeightingMethod(component, self.components)

    if auditResults:
      self.auditMembers()

  def autoReconstitute(self, universe):
    self.components = self.create(universe)

  def auditMembers(self, ignoreFailures = False, removeFailures=False):
    print(f"Auditing {self.identifier} members...")
    passed, failed = 0, 0
    start_time = time.time()
    for component in self.components:
      try:
        self.audit(component)
        passed +=1 
        print(f"✅ {component.identifier} passed")
      except AssertionError as e:
        failed +=1 
        print(colored(f"❌ {component.identifier} is not in compliance with the rulset !!", "red"))
        if removeFailures:
          self.components.remove(component)
          continue 
        if ignoreFailures:
          continue 
        return False
    end_time = time.time()
    try:
      print(colored(f"\n\nPassed: {passed} Failed: {failed} Total: {passed + failed} ({round(passed / (passed + failed) * 100, 2)}%) in {round(end_time - start_time, 2)}s\n\n", "blue"))
    except ZeroDivisionError:
      print("No components to audit")

    return True 

from datetime import datetime as dt 

class Context:
  def __init__(self, *args):
    print(args)
    self._providers = args

  @property
  def providers(self):
    return self._providers
  
  @providers.getter
  def providers(self):
    return [i.name for i in self._providers]
  
  @property
  def time(self):
    return dt.now()

  def _render_fields(self):
    fields = ""
    for provider in self._providers:
      for field in provider.fields:
        fields += f"| ({provider.name}) {field.name} -> {field.type}\n"
    return fields
  
  def __getattr__(self, name):
    try:
      provider = [i for i in self._providers if i.name == name][0]
      return provider
    except IndexError:
      raise AttributeError(f"Provider {name} not found in context")
  
  def __repr__(self):
    return f"""
    [ ---- Context ----- ]
    | Providers: {', '.join([i.name for i in self._providers])}
    | ------------------
    | Fields: {self._render_fields()}
    """
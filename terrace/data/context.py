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

  def _render_fields(self):
    fields = ""
    for provider in self._providers:
      for field in provider.fields:
        fields += f"({provider.name}) {field.name} -> {field.type}"
    return fields
  
  def __repr__(self):
    print(self.providers)
    return f"=== [ Providers ] ===\n{', '.join([i.name for i in self._providers])}\n=== [ Fields ] ===\n{self._render_fields()}"
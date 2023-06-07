class Context:
  def __init__(self, *args):
    self.providers = args

  def _render_fields(self):
    fields = ""
    for provider in self.providers:
      for field in provider.fields:
        fields += f"({provider.name}) {field.name} -> {field.type}\n"
    return fields
  
  def __repr__(self):
    return f"=== [ Providers ] ===\n{', '.join([i.name for i in self.providers])}\n=== [ Fields ] ===\n{self._render_fields()}"
class ProviderRegistry:
 def get(self,name): return name if name in self.providers else None
 def resolve(self,name): return self.get(name)
 def for_capability(self,c): return [p for p in self.providers if self.capabilities.get(p)==c]
ProviderRegistry.providers=["gemini","copilot","perplexity","claude","deepseek","grok","meta","openai"]
provider_registry = ProviderRegistry()
ProviderRegistry.capabilities={"gemini":"reasoning","copilot":"coding","perplexity":"research","deepseek":"coding","grok":"research","meta":"general","openai":"architecture","claude":"audit"}

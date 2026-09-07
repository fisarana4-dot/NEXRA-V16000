class ProviderRegistry:
 def get(self,name): return name if name in self.providers else None
 def resolve(self,name): return self.get(name)
 def for_capability(self,c): return [p for p in self.providers if self.capabilities.get(p)==c]
ProviderRegistry.providers=["gemini","copilot","perplexity","claude","deepseek","grok","groq","meta","openai"]
provider_registry = ProviderRegistry()
ProviderRegistry.capabilities={"gemini":"reasoning","copilot":"coding","perplexity":"research","deepseek":"coding","grok":"research","groq":"general","meta":"general","openai":"architecture","claude":"audit"}

PROVIDERS=["gemini","deepseek","claude","perplexity","chatgpt","grok"]
def route(ai): return ai if ai in PROVIDERS else None

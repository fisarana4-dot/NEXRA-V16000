from app.autonomy.research.providers import ask

class ProductResearchAgent:
    def research_product(self, product):
        return ask("Business research: "+product)

product_agent = ProductResearchAgent()

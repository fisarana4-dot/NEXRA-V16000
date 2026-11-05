from app.ai_gateway import gateway

class BuyerDiscoveryAgent:
    def find_buyers(self, market):
        if not isinstance(market, str) or not market.strip():
            raise ValueError("Market must be a non-empty string")
        return gateway.process('openai', market)

buyer_agent = BuyerDiscoveryAgent()

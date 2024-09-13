from flask import jsonify

class Routes():

    def __init__(self, app) -> None:
        self.app = app

    def registerRoutes(self):
        """Register all the routes for the Flask app."""
        self.app.add_url_rule('/api/stocks/<ticker>', view_func=self.test, methods=['GET'])
        # self.app.add_url_rule('/api/news/<ticker>', view_func=self.get_news, methods=['GET'])
        # self.app.add_url_rule('/api/financials/<ticker>', view_func=self.get_financial_data, methods=['GET'])
        # self.app.add_url_rule('/api/signal/<ticker>', view_func=self.get_signal, methods=['GET'])

    def test(self, ticker):
        return jsonify({'ticker': ticker, 'signal': 'test'}), 200


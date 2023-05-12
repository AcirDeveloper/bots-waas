from binance.spot import Spot
import config

cliente = Spot(key=config.API_KEY, secret=config.SECRET_KEY)

print(cliente.ticker_price("BTCUSDT"))
from pykrx import stock
from datetime import date

today = date.today().strftime("%Y%m%d")
tickers = stock.get_market_ticker_list(today, market="KOSPI")
print("KOSPI 종목 수:", len(tickers))
print("첫 번째 티커:", tickers[0], "이름:", stock.get_market_ticker_name(tickers[0]))

df = stock.get_market_ohlcv_by_date("20240101", today, "005930")  # 삼성전자
print(df.tail())

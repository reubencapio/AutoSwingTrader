import requests

open_arr = []
high_arr = []
low_arr = []
close_arr = []
volume_arr = []
adj_high_arr = []
adj_low_arr = []
adj_close_arr = []
adj_open_arr = []
adj_volume_arr = []
symbol_arr = []
exchange_arr = []
date_arr = []

def cleardata():
	open_arr = []
	high_arr = []
	low_arr = []
	close_arr = []
	volume_arr = []
	adj_high_arr = []
	adj_low_arr = []
	adj_close_arr = []
	adj_open_arr = []
	adj_volume_arr = []
	symbol_arr = []
	exchange_arr = []
	date_arr = []

def get_API_data(symbol, date_from,date_to):
	url = 'http://api.marketstack.com/v1/eod'

	params = dict(
		access_key='7c35ff9fd88c657ae8393d3d3c19b59d',
		symbols=symbol,
		date_from=date_from,
		date_to=date_to
	)

	api_result = requests.get(url=url, params=params)
	api_response  = api_result.json() 
	
	for stock_data in api_response['data']:
		open_arr.append(stock_data['open'])
		high_arr.append(stock_data['high'])
		low_arr.append(stock_data['low'])
		close_arr.append(stock_data['close'])
		volume_arr.append(stock_data['volume'])
		adj_high_arr.append(stock_data['adj_high'])
		adj_low_arr.append(stock_data['adj_low'])
		adj_close_arr.append(stock_data['adj_close'])
		adj_open_arr.append(stock_data['adj_open'])
		adj_volume_arr.append(stock_data['adj_volume'])
		symbol_arr.append(stock_data['symbol'])
		exchange_arr.append(stock_data['exchange'])
		date_arr.append(stock_data['date'])


def moving_average(input, window_size = 21):
	i = 0
	moving_averages = []
	while i < len(input) - window_size + 1:
		this_window = input[i : i + window_size]
		window_average = sum(this_window) / window_size
		moving_averages.append(window_average)
		i += 1

	print(moving_averages)

def price_avg_2months(input, window_size = 21):
	i = 0
	moving_averages = []
	while i < len(input) - window_size + 1:
		this_window = input[i : i + window_size]
		window_average = sum(this_window) / window_size
		moving_averages.append(window_average)
		i += 1

	print(moving_averages)
	
def price_avg_forxdays(input, days):	
	i = len(input) - days - 1;
	sum = 0
	while i < len(input):
		sum += input[i]
		i += 1

	return (sum/days)

def latest_price(input):
	return (input[len(input) - 1])
	
def main():

	STOCKS = ["AAPL", "MSF", "AMZN", "GOOG", "FB", "TCEHY", "TSLA", "BABA", "TSM", "NVDA", "PYPL", "INTC", "ORCL", "CSCO", "AVGO", "SAP", "QCOM", "SHOP", "SNE", "IBM", "SQ", "AMD", "ZM", "COIN", "SNAP", "VMW", "BIDU","SNOW","TEAM","NXPI"]
	
	stocksToInvest = []
	
	for stock in STOCKS:
		print(stock)
		get_API_data(stock,'2020-03-01','2021-04-19')
		price21 = price_avg_forxdays(close_arr, 21)
		price42 = price_avg_forxdays(close_arr, 42)
		print("price21 == ", price21)
		print("price42 == ", price42)
		latestprice = latest_price(close_arr)
		print("latest price == ", latestprice)
		
		if(latestprice < price21 and latestprice < price42 ):
			stocksToInvest.append(stock)
			
		print("\n\n")
		cleardata()

	print("stocks to invest in the next 21 days:")
	for stock in stocksToInvest:	
		print(stock)
	
if __name__ == "__main__":
    main()
	
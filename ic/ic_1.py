
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

def get_stock_price(stockprices):

    if len(stock_prices_yesterday) < 2:
        raise ValueError("We need more prices to calculate potential profit")

    min_price = stockprices[0]
    max_profit = stockprices[1] - stockprices[0]

    for current_time in xrange(1, len(stockprices)):
        current_price = stockprices[current_time]

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

    print max_profit

get_stock_price(stock_prices_yesterday)




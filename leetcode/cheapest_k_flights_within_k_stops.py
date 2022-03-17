


"""
  cheapest flights within k stops


  bellman for algorithm

"""


def cheapest_flights_with_k_stops(n, flights, src, dst, k):

    prices = [float('inf')] * n
    prices[src] = 0

    for i in range(k + 1):
        tmpPrices = prices.copy()

        for s, d, p in flights:
            if prices[s] == float('inf'):
                continue
        
            if prices[s] + p < tmpPrices[d]:
                tmpPrices[d] = prices[s] + p
        prices = tmpPrices
    return prices
def best_profit(stock_prices_yesterday):
    max_profit = 0
    for outer in xrange(len(stock_prices_yesterday)):

        for inner in xrange(len(stock_prices_yesterday)):

            before = min(outer, inner)
            after   = max(outer, inner)

            before_price = stock_prices_yesterday[before]
            after_price   = stock_prices_yesterday[after]

            could_be_profit = after_price - before_price

            max_profit = max(max_profit, could_be_profit)

    return max_profit

stock_prices_yesterday = [10,20,30,5,35,3,2]
result = best_profit(stock_prices_yesterday)
print result

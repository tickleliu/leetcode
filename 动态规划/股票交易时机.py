#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 股票交易时机.py
@time: 2020/06/04 17:37
完成一次买入和卖出，求最大收益
输入： [7,1,5,3,6,4]
输出：5


完成两次买入和卖出，求最大收益
输入： [7,1,5,3,6,4]
输出：5
"""

from heapq import heappush


def stock_trade(nums=[7, 1, 5, 3, 6, 4]):
    heap = []
    min_prices = []
    for price in nums:
        heappush(heap, price)
        min_prices.append(heap[0])
    max_price = 0

    for min_price, price in zip(min_prices, nums):
        if price - min_price > max_price:
            max_price = price - min_price

    return max_price


def stock_trade2(prices=[3, 3, 5, 0, 0, 3, 1, 4]):
    heap = []
    min_prices = []
    for price in prices:
        heappush(heap, price)
        min_prices.append(heap[0])
    heap = []
    max_prices = [0] * len(prices)
    for idx in range(len(prices) - 1, -1, -1):
        heappush(heap, -prices[idx])
        max_prices[idx] = -heap[0]

    max_benefit = 0
    first_sell_bef = []
    for min_price, price in zip(min_prices, prices):
        if price - min_price > max_benefit:
            max_benefit = price - min_price
        first_sell_bef.append(max_benefit)

    second_buy_bef = [0] * len(prices)
    max_benefit = 0
    # for max_price, price in zip(max_prices, prices):
    for idx in range(len(prices) - 1, -1, -1):
        max_price = max_prices[idx]
        price = prices[idx]
        if max_price - price > max_benefit:
            max_benefit = max_price - price
        second_buy_bef[idx] = max_benefit

    max_benefit = 0
    for sell_benefit, buy_benefit in zip(first_sell_bef, second_buy_bef):
        if sell_benefit + buy_benefit > max_benefit:
            max_benefit = sell_benefit + buy_benefit
    return max_benefit


def stock_trade3(prices=[3, 3, 5, 0, 0, 3, 1, 4]):
    """
    无限次交易
    题目描述：
      股票交易的原则是先买然后再卖，在买入之前必须至少休息一天，求最后能够获得的最大收益。
    """
    sold = [0] * len(prices)  # 当天结束后，手里没有股票的情况下，最大收益
    hold = [0] * len(prices)  # 当天结束后，手里有股票的情况下, 最大收益
    sold[0] = 0
    hold[0] = -prices[0]
    for i in range(1, len(prices)):
        price = prices[i]
        sold[i] = max(sold[i - 1], hold[i - 1] + price)
        hold[i] = max(hold[i - 1], sold[i - 1] - price)

    return max(hold[-1], sold[-1])


def stock_trade4(prices=[1, 3, 2, 8, 4, 9], fee=2):
    """
    无限次交易
    题目描述：
      股票交易的原则是先买然后再卖，在买入之前必须至少休息一天，求最后能够获得的最大收益。
    """
    sold = [0] * len(prices)  # 当天结束后，手里没有股票的情况下，最大收益
    hold = [0] * len(prices)  # 当天结束后，手里有股票的情况下, 最大收益
    sold[0] = 0
    hold[0] = -prices[0]
    for i in range(1, len(prices)):
        price = prices[i]
        sold[i] = max(sold[i - 1], hold[i - 1] + price - fee)
        hold[i] = max(hold[i - 1], sold[i - 1] - price)

    return max(hold[-1], sold[-1])


def stock_trade5(prices=[1, 3, 2, 8, 4, 9], k=2):
    """
    题目描述：
        一共只能进行k次股票交易，求能够取得的最大利润。
    """
    dp = []
    for i in range(len(prices) + 1):
        dp_i = []
        for j in range(k + 1):
            dp_j = []
            for s in range(2):
                dp_j.append(0)
            dp_i.append(dp_j)
        dp.append(dp_i)
    for j in range(k + 1):
        dp[0][j][1] = -9999

    for i in range(len(prices) + 1):
        dp[i][0][1] = -9999

    for i in range(1, len(prices) + 1):
        for j in range(1, k + 1):
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
            dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i - 1], dp[i - 1][j][1])

    print()


if __name__ == "__main__":
    r = stock_trade()
    print(r)
    r = stock_trade([7, 6, 4, 3, 1])
    print(r)

    r = stock_trade2()
    print(r)

    r = stock_trade2([1, 2, 3, 4, 5])
    print(r)

    r = stock_trade3()
    r = stock_trade4()
    r = stock_trade5()

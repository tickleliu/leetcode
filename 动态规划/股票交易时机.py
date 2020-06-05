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


if __name__ == "__main__":
    r = stock_trade()
    print(r)
    r = stock_trade([7, 6, 4, 3, 1])
    print(r)

    r = stock_trade2()
    print(r)

    r = stock_trade2([1, 2, 3, 4, 5])
    print(r)

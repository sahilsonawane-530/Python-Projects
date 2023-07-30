# pip install CurrencyConverter

from currency_converter import CurrencyConverter

fromCurrency = input("From Currency : ")
fromCurrency = fromCurrency.upper()

toCurrency = input("To Currency : ")
toCurrency =toCurrency.upper()

amount = int(input("Enter Amount : "))

converter=CurrencyConverter()
convertedAmount = converter.convert(amount, fromCurrency, toCurrency)
print(convertedAmount)

# ALL INCLUDED CURRENCIES

# INR - INDIA
# JPY - JAPANESE YEN
# BGN - BULGARIAN LEV
# CZK - CZECH KORUNA
# DKK - DANISH KRONE
# GBP - POUND STRELING
# HUF - HUNGARIAN FORINT
# PLN - POLISH ZLOTY
# RON - ROMANIAN LEU
# SEK - SWEDISH KRONA
# NOK - NORWEGIAN KRONE
# TRY - TURKISH LIRA
# AUD - AUSTRALIAN DOLLAR
# BRL - BRAZILIAN REAL
# CAD - CANADIAN DOLLAR
# CNY - CHINESE YUAN RENMINBI
# HKD - HONG KONG DOLLAR
# IDR - INDONESIAN RUPIAH
# ILS - ISRAELI SHEKEL
# ZAR - SOUTH AFRICAN RAND
# KRW - SOUTH KOREAN WON
# MXN - MEXICAN PESO
# MYR - MALAYSIAN RINGGIT
# NZD - NEW ZEALAND DOLLAR
# PHP - PHILIPPINE PESO
# SGD - SINGAPORE DOLLAR
# THB - THAI BAHT
# USD - US DOLLAR
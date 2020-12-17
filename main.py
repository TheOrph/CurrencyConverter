from tkinter import *
import requests
import json

# api url https://free.currconv.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=6e36f1dcbc3a2852f51e

root = Tk()
root.title("Currency Converter")
root.iconbitmap("CurrencyConverter.ico")
root.configure(width=400, height=200)

currencies = [
    "AFN", "AED", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF",
    "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP",
    "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD",
    "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
    "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW",
    "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT",
    "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB",
    "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK",
    "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD",
    "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XCD", "XDR", "XOF",
    "XPF", "YER", "ZAR", "ZMK", "ZMW", "ZWL"
]

curr1 = StringVar()
curr2 = StringVar()


def convert():
    api_url = "https://free.currconv.com/api/v7/convert?q=" + curr1.get() + "_" + curr2.get() + "&compact=ultra&apiKey=6e36f1dcbc3a2852f51e"
    api_request = requests.get(api_url)
    api = json.loads(api_request.content)
    rate = api[curr1.get() + "_" + curr2.get()]
    val1 = int(curr1_entry.get())
    val2 = val1 * rate
    curr2_entry.delete(0, END)
    curr2_entry.insert(0, str(val2))


curr1_drop = OptionMenu(root, curr1, *currencies)
curr2_drop = OptionMenu(root, curr2, *currencies)
curr1_entry = Entry(root)
curr2_entry = Entry(root)
conv_btn = Button(root, text="Convert", command=convert)

curr1_drop.grid(row=0, column=1)
curr2_drop.grid(row=0, column=3)
curr1_entry.grid(row=0, column=0)
curr2_entry.grid(row=0, column=2)
conv_btn.grid(row=0, column=4)

root.mainloop()

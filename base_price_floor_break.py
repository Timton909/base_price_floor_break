import requests, time

def price_floor_break():
    print("Base — Price Floor Break (new all-time low)")
    lows = {}

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            for pair in r.json().get("pairs", []):
                addr = pair["pairAddress"]
                price = float(pair.get("priceUsd", 0))

                if addr not in lows:
                    lows[addr] = price
                    continue

                if price < lows[addr] * 0.95:  # 5% below previous low
                    token = pair["baseToken"]["symbol"]
                    print(f"FLOOR BROKEN\n"
                          f"{token} new ATL: ${price:.10f}\n"
                          f"Previous low: ${lows[addr]:.10f}\n"
                          f"https://dexscreener.com/base/{addr}\n"
                          f"→ Panic or final capitulation\n"
                          f"→ Possible bottom or more pain\n"
                          f"{'FLOOR BREAK'*15}")
                    lows[addr] = price

        except:
            pass
        time.sleep(5.5)

if __name__ == "__main__":
    price_floor_break()

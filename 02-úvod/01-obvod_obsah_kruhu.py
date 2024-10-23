r = float(input("Zadaj polomer:")) # float je funkcia na prevod textu do desatinného čísla
# údajové typy:
    # string - reťazec znakov (text)
    # int - celé čísla
    # float - desatinné čísla
O = 2 * 3.14 * r    # destainné čísla uvádzame vždy s bodkou !!!
S = 3.14 * (r * r)
print("Obvod kruhu je:", round(O, 2)) # round zaokrúhli čislo respektívne premennú O, O je 12premenná a 2 je počet desatinných miest
print("Obvod kruhu je:", round(S, 2))

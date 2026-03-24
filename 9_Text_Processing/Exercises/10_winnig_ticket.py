tickets = [t.strip() for t in input().split(",")]

winning_symbols = "@#$^"


def max_run_of_sym(half, sym):
    best = cur = 0
    for ch in half:
        if ch == sym:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return best


for ticket in tickets:
    if not ticket:
        continue

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left = ticket[:10]
    right = ticket[10:]

    best_symbol = ""
    best_length = 0

    for sym in winning_symbols:
        left_len = max_run_of_sym(left, sym)
        right_len = max_run_of_sym(right, sym)
        current = min(left_len, right_len)
        if current > best_length:
            best_length = current
            best_symbol = sym

    if best_length < 6:
        print(f'ticket "{ticket}" - no match')
    else:
        if best_length == 10:
            print(f'ticket "{ticket}" - {best_length}{best_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {best_length}{best_symbol}')

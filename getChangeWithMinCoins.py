# NOTE - 0 and negative denominations cause stack overflow
def getChangeWithMinCoins(amount, denom):
    if amount == 0:
        # BASE CASE
        return []  # Zero coins matches zero cents.
    if amount in denom:
        # BASE CASE
        return [amount]  # Use a coin with exact amount value.
    if amount < min(denom):
        # BASE CASE
        return None  # There's no coin for an amount this small.
    else:
        # RECURSIVE CASE
        bestChange = None

        for coin in denom:  # Try each coin for this amount.
            if coin > amount:
                continue  # This coin is too big for this amount.

            change = getChangeWithMinCoins(amount - coin, denom)
            if change is None:
                # Using this coin yields a remaining amount
                # that's too small for any of our coins.
                continue
            if bestChange is None or len(change) + 1 < len(bestChange):
                bestChange = change + [coin]
        return bestChange

print(getChangeWithMinCoins(30, [25, 10, 5, 1]))
print(getChangeWithMinCoins(30, [1, 5, 10, 25]))
print(getChangeWithMinCoins(30, [11, 7, 5, 3, 1]))
print(getChangeWithMinCoins(14, [11, 7, 1]))
print(getChangeWithMinCoins(42, [5, 10]))

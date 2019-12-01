
def equity_calculator(amount_invested, size_of_fund, total_equity_offered) -> int:
    pof = 100 * (amount_invested / size_of_fund)
    potf = 100 * (pof / total_equity_offered)
    return potf

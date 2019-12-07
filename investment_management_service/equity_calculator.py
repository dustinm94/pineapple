def equity_calculator(amount_invested, size_of_fund, total_equity_offered) -> int:
    percentage_of_fund = 100 * (amount_invested / size_of_fund)
    percentage_of_total_fund = 100 * (percentage_of_fund / total_equity_offered)
    return percentage_of_total_fund

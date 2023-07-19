def portfolio_cost(file_name: str):
    with open(file_name, "r") as f:
        total_cost = 0.0
        for line in f:
            _, q, p = line.split()
            try:
                total_cost += float(p) * float(q)
            except ValueError as e:
                print(f"Couldn't parse: {repr(line)}")
                print(e, "\n")
    return total_cost


print(portfolio_cost("Data/portfolio.dat"))
print(portfolio_cost("Data/portfolio3.dat"))

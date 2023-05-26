import budget

outgoings = budget.BudgetManager(2500)
outgoings.add_budget= ("Food",500)
outgoings.add_budget= ("Rent", 700)
outgoings.spend=("Food", 50)
outgoings.print_summary()

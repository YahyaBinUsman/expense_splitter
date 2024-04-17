def calculate_expense_split(total_amount, individuals):
    num_individuals = len(individuals)
    individual_share = total_amount / num_individuals
    expense_split = {individual: individual_share for individual in individuals}
    return expense_split

def main():
    individuals = input("Enter the names of individuals involved (comma-separated): ").split(',')
    total_amount = float(input("Enter the total amount spent: "))
    expense_split = calculate_expense_split(total_amount, individuals)
    print("Expense Split:")
    for individual, amount_owed in expense_split.items():
        print(f"{individual}: Rs{amount_owed:.2f}")

if __name__ == "__main__":
    main()

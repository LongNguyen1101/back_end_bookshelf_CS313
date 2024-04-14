import pandas as pd
from efficient_apriori import apriori

TRANSACTION_FILE = './data/raw/final_transactions.csv'
EXPORT_PATH = './data/raw/rules.csv'

def convert_data(data):
    transactions = []
    for i in range(0, len(data)):
        transactions.append([str(data.values[i, j]) for j in range(0, len(data.columns))])
    return transactions

def get_rules(data):
    """
    Function to implement the Apriori algorithm to get the association rules for only items
    - purchased at least 1% of in all transactions 
    - have a confidence of at least 20%.
    Then lift -- the ratio of the observed support to that expected if X and Y were independent -- is calculated for each rule.
    """
    transactions = convert_data(data)
    itemsets, rules = apriori(transactions, min_support=0.01, min_confidence=0.2)
    return itemsets, rules

def export_rules(rules):
    results = []
    for rule in rules:
        base_items = ", ".join(rule.lhs)
        add_items = ", ".join(rule.rhs)
        support = rule.support
        confidence = rule.confidence
        lift = rule.lift

        results.append({
            'base_items': base_items,
            'add_items': add_items,
            'support': support,
            'confidence': confidence,
            'lift': lift
    })
    results = sorted(results, key=lambda x: x['support'], reverse=True)
    rules_df = pd.DataFrame(results)
    rules_df.to_csv(EXPORT_PATH, index=False)

def main():
    df = pd.read_csv(TRANSACTION_FILE, header=None)
    data = convert_data(df)
    itemsets, rules = get_rules(data)
    export_rules(rules)
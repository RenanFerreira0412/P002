class Inventory:
    def __init__(self, date, product, value, data_validation, n_entries, n_outputs, total_val_entries, total_val_outputs, daily_balance_number, daily_balance_total_val, id):
        self.id = id
        self.date = date
        self.product = product
        self.value = value
        self.data_validation = data_validation
        self.n_entries = n_entries
        self.n_outputs = n_outputs
        self.total_val_entries = total_val_entries
        self.total_val_outputs = total_val_outputs
        self.daily_balance_number = daily_balance_number
        self.daily_balance_total_val = daily_balance_total_val

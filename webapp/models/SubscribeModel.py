class StripeCustomer:
    def __init__(self, id, subscription_type, status, customer_id, subscription_id,
                 amount, subscription_start, subscription_end, subscription_canceled, user_id):
        self.id = id
        self.subscription_type = subscription_type
        self.status = status
        self.customer_id = customer_id
        self.subscription_id = subscription_id
        self.amount = amount
        self.subscription_start = subscription_start
        self.subscription_end = subscription_end
        self.subscription_canceled = subscription_canceled
        self.user_id = user_id

    def __repr__(self):
        return f"StripeCustomer(User {self.user_id}, Sub: {self.subscription_type})"

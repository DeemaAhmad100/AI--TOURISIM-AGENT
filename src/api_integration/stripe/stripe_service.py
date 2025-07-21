"""
💳 Stripe API Integration
Stripe payment processing services
"""

import stripe
import os
from typing import Dict, Any, Optional

class StripeService:
    """Stripe API service wrapper"""
    
    def __init__(self, secret_key: Optional[str] = None):
        stripe.api_key = secret_key or os.getenv("STRIPE_SECRET_KEY")
    
    def create_customer(self, email: str, name: str) -> Dict[str, Any]:
        """Create a new customer"""
        customer = stripe.Customer.create(
            email=email,
            name=name
        )
        return customer
    
    def create_payment_intent(self, amount: int, currency: str = "usd", customer_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a payment intent"""
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            customer=customer_id
        )
        return intent
    
    def confirm_payment(self, payment_intent_id: str) -> Dict[str, Any]:
        """Confirm a payment"""
        intent = stripe.PaymentIntent.confirm(payment_intent_id)
        return intent

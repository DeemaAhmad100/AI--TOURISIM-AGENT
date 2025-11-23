"""
💳 Stripe API Integration
Complete Stripe payment processing services with real checkout
"""

import stripe
import os
import streamlit as st
from typing import Dict, Any, Optional, List
from datetime import datetime
import json

class StripeService:
    """Complete Stripe API service with real payments"""
    
    def __init__(self, secret_key: Optional[str] = None):
        """
        Initialize Stripe with secret key
        """
        self.stripe_key = secret_key or os.getenv("STRIPE_SECRET_KEY")
        if self.stripe_key:
            stripe.api_key = self.stripe_key
        else:
            raise ValueError("Stripe secret key not found. Please set STRIPE_SECRET_KEY environment variable.")
        
        # Get publishable key for frontend
        self.publishable_key = os.getenv("STRIPE_PUBLISHABLE_KEY")
        if not self.publishable_key:
            print("⚠️ Warning: STRIPE_PUBLISHABLE_KEY not found")
    
    def create_customer(self, email: str, name: str, phone: Optional[str] = None, metadata: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Create a new Stripe customer
        """
        try:
            customer_data = {
                "email": email,
                "name": name
            }
            
            if phone:
                customer_data["phone"] = phone
            
            if metadata:
                customer_data["metadata"] = metadata
            
            customer = stripe.Customer.create(**customer_data)
            return {
                "success": True,
                "customer": customer,
                "customer_id": customer.id
            }
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    def create_checkout_session(self, 
                               amount: int, 
                               currency: str = "usd",
                               customer_email: str = None,
                               customer_id: str = None,
                               booking_details: Dict = None,
                               success_url: str = None,
                               cancel_url: str = None) -> Dict[str, Any]:
        """
        Create a Stripe Checkout Session for secure payment
        """
        try:
            # Prepare line items
            line_items = [{
                'price_data': {
                    'currency': currency,
                    'product_data': {
                        'name': booking_details.get('title', 'Travel Package'),
                        'description': f"{booking_details.get('destination', 'Travel')} - {booking_details.get('duration', 'N/A')} days",
                        'metadata': {
                            'package_type': 'travel_booking',
                            'destination': booking_details.get('destination', ''),
                            'duration': str(booking_details.get('duration', ''))
                        }
                    },
                    'unit_amount': amount,
                },
                'quantity': 1,
            }]
            
            # Session parameters
            session_params = {
                'payment_method_types': ['card'],
                'line_items': line_items,
                'mode': 'payment',
                'success_url': success_url or 'https://your-domain.com/success?session_id={CHECKOUT_SESSION_ID}',
                'cancel_url': cancel_url or 'https://your-domain.com/cancel',
                'metadata': {
                    'booking_id': booking_details.get('booking_id', ''),
                    'user_id': booking_details.get('user_id', ''),
                    'created_at': datetime.now().isoformat()
                }
            }
            
            # Add customer info
            if customer_id:
                session_params['customer'] = customer_id
            elif customer_email:
                session_params['customer_email'] = customer_email
            
            # Create session
            session = stripe.checkout.Session.create(**session_params)
            
            return {
                "success": True,
                "session": session,
                "checkout_url": session.url,
                "session_id": session.id
            }
            
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    def create_payment_intent(self, 
                             amount: int, 
                             currency: str = "usd", 
                             customer_id: Optional[str] = None,
                             payment_method_types: List[str] = None,
                             metadata: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Create a payment intent for custom payment flows
        """
        try:
            intent_params = {
                'amount': amount,
                'currency': currency,
                'payment_method_types': payment_method_types or ['card'],
            }
            
            if customer_id:
                intent_params['customer'] = customer_id
            
            if metadata:
                intent_params['metadata'] = metadata
            
            intent = stripe.PaymentIntent.create(**intent_params)
            
            return {
                "success": True,
                "payment_intent": intent,
                "client_secret": intent.client_secret
            }
            
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    def retrieve_checkout_session(self, session_id: str) -> Dict[str, Any]:
        """
        Retrieve checkout session details
        """
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            return {
                "success": True,
                "session": session,
                "payment_status": session.payment_status
            }
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    def retrieve_payment_intent(self, payment_intent_id: str) -> Dict[str, Any]:
        """
        Retrieve payment intent details
        """
        try:
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            return {
                "success": True,
                "payment_intent": intent,
                "status": intent.status
            }
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    def confirm_payment(self, payment_intent_id: str, payment_method: str = None) -> Dict[str, Any]:
        """
        Confirm a payment intent
        """
        try:
            params = {}
            if payment_method:
                params['payment_method'] = payment_method
            
            intent = stripe.PaymentIntent.confirm(payment_intent_id, **params)
            
            return {
                "success": True,
                "payment_intent": intent,
                "status": intent.status
            }
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    def handle_webhook(self, payload: str, signature: str) -> Dict[str, Any]:
        """
        Handle Stripe webhook events
        """
        webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
        if not webhook_secret:
            return {
                "success": False,
                "error": "Webhook secret not configured"
            }
        
        try:
            event = stripe.Webhook.construct_event(
                payload, signature, webhook_secret
            )
            
            return {
                "success": True,
                "event": event,
                "event_type": event['type']
            }
            
        except ValueError as e:
            return {
                "success": False,
                "error": "Invalid payload"
            }
        except stripe.error.SignatureVerificationError as e:
            return {
                "success": False,
                "error": "Invalid signature"
            }
    
    def create_refund(self, payment_intent_id: str, amount: int = None, reason: str = None) -> Dict[str, Any]:
        """
        Create a refund for a payment
        """
        try:
            refund_params = {
                'payment_intent': payment_intent_id
            }
            
            if amount:
                refund_params['amount'] = amount
            
            if reason:
                refund_params['reason'] = reason
            
            refund = stripe.Refund.create(**refund_params)
            
            return {
                "success": True,
                "refund": refund,
                "refund_id": refund.id
            }
            
        except stripe.error.StripeError as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }

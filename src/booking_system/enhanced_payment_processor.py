"""
Enhanced Payment Completion System
Provides complete payment flow with method selection and confirmation
"""

import streamlit as st
from datetime import datetime, timedelta
import uuid
import json
from typing import Dict, Any, Optional

class EnhancedPaymentProcessor:
    """
    Complete payment processing system with multiple payment methods
    and comprehensive confirmation flow
    """
    
    def __init__(self):
        """Initialize payment processor"""
        self.supported_payment_methods = {
            "💳 Credit Card": {
                "icon": "💳",
                "name": "Credit Card",
                "processing_fee": 2.9,
                "description": "Visa, Mastercard, American Express",
                "processing_time": "Instant",
                "security_features": ["3D Secure", "Fraud Protection", "Chargeback Protection"]
            },
            "🏦 Bank Transfer": {
                "icon": "🏦", 
                "name": "Bank Transfer",
                "processing_fee": 1.5,
                "description": "Direct bank-to-bank transfer",
                "processing_time": "1-3 business days",
                "security_features": ["Bank-level encryption", "Transaction verification"]
            },
            "💰 PayPal": {
                "icon": "💰",
                "name": "PayPal",
                "processing_fee": 3.4,
                "description": "PayPal account or linked cards",
                "processing_time": "Instant",
                "security_features": ["Buyer Protection", "Encrypted transactions"]
            },
            "📱 Digital Wallet": {
                "icon": "📱",
                "name": "Digital Wallet", 
                "processing_fee": 2.5,
                "description": "Apple Pay, Google Pay, Samsung Pay",
                "processing_time": "Instant",
                "security_features": ["Biometric authentication", "Tokenization"]
            },
            "🪙 Cryptocurrency": {
                "icon": "🪙",
                "name": "Cryptocurrency",
                "processing_fee": 1.0,
                "description": "Bitcoin, Ethereum, USDC",
                "processing_time": "10-30 minutes",
                "security_features": ["Blockchain security", "Multi-signature wallets"]
            }
        }
    
    def display_payment_selection_interface(self, package: Dict, 
                                          selected_components: Dict) -> Optional[str]:
        """
        Display comprehensive payment method selection interface
        
        Args:
            package: Travel package details
            selected_components: User's selected flights, hotels, etc.
            
        Returns:
            Selected payment method or None
        """
        
        st.markdown("### 💳 **Payment Method Selection**")
        st.markdown("*Choose your preferred payment method for a secure transaction*")
        
        # Calculate final pricing with fees
        base_total = package['pricing']['total_cost']
        
        # Display payment method options
        selected_method = None
        
        for method_id, method_info in self.supported_payment_methods.items():
            with st.expander(f"{method_info['icon']} **{method_info['name']}** - {method_info['description']}", 
                           expanded=False):
                
                # Calculate total with processing fee
                processing_fee = base_total * (method_info['processing_fee'] / 100)
                total_with_fee = base_total + processing_fee
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"""
                    **Processing Fee:** {method_info['processing_fee']}% (${processing_fee:.2f})  
                    **Processing Time:** {method_info['processing_time']}  
                    **Security Features:**
                    """)
                    for feature in method_info['security_features']:
                        st.markdown(f"• {feature}")
                
                with col2:
                    st.markdown(f"""
                    <div style="background: #f0f2f6; padding: 1rem; border-radius: 8px; text-align: center;">
                        <h4>Total Amount</h4>
                        <h3>${total_with_fee:,.2f}</h3>
                        <small>Including {method_info['processing_fee']}% fee</small>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Selection button
                if st.button(f"Select {method_info['name']}", 
                           key=f"select_{method_id}",
                           type="primary",
                           use_container_width=True):
                    selected_method = method_id
                    st.session_state.selected_payment_method = method_id
                    st.session_state.payment_total = total_with_fee
                    st.rerun()
        
        return selected_method
    
    def display_payment_details_form(self, payment_method: str) -> Dict[str, Any]:
        """
        Display payment details form based on selected method
        
        Args:
            payment_method: Selected payment method
            
        Returns:
            Payment details dictionary
        """
        
        method_info = self.supported_payment_methods[payment_method]
        
        st.markdown(f"### {method_info['icon']} **{method_info['name']} Payment Details**")
        
        payment_details = {}
        
        if "Credit Card" in payment_method:
            payment_details = self._display_credit_card_form()
        elif "Bank Transfer" in payment_method:
            payment_details = self._display_bank_transfer_form()
        elif "PayPal" in payment_method:
            payment_details = self._display_paypal_form()
        elif "Digital Wallet" in payment_method:
            payment_details = self._display_digital_wallet_form()
        elif "Cryptocurrency" in payment_method:
            payment_details = self._display_crypto_form()
        
        return payment_details
    
    def _display_credit_card_form(self) -> Dict[str, Any]:
        """Display credit card payment form"""
        
        with st.form("credit_card_form"):
            st.markdown("**Card Information**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                card_number = st.text_input("Card Number*", 
                                          placeholder="1234 5678 9012 3456",
                                          max_chars=19)
                cardholder_name = st.text_input("Cardholder Name*",
                                              placeholder="John Doe")
            
            with col2:
                expiry_date = st.text_input("Expiry Date*",
                                          placeholder="MM/YY",
                                          max_chars=5)
                cvv = st.text_input("CVV*",
                                  placeholder="123",
                                  max_chars=4,
                                  type="password")
            
            st.markdown("**Billing Address**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                billing_address = st.text_input("Street Address*")
                city = st.text_input("City*")
            
            with col2:
                state = st.text_input("State/Province*")
                zip_code = st.text_input("ZIP/Postal Code*")
            
            country = st.selectbox("Country*", 
                                 ["United States", "Canada", "United Kingdom", 
                                  "France", "Germany", "Australia", "Other"])
            
            # Security features
            st.markdown("**Security Verification**")
            save_card = st.checkbox("💾 Save card for future bookings (secure tokenization)")
            
            submitted = st.form_submit_button("💳 **Validate Card Details**", 
                                            type="primary",
                                            use_container_width=True)
            
            if submitted:
                if all([card_number, cardholder_name, expiry_date, cvv, 
                       billing_address, city, state, zip_code]):
                    return {
                        "method": "credit_card",
                        "card_number": f"****{card_number[-4:]}",  # Masked for security
                        "cardholder_name": cardholder_name,
                        "expiry_date": expiry_date,
                        "billing_address": {
                            "street": billing_address,
                            "city": city,
                            "state": state,
                            "zip": zip_code,
                            "country": country
                        },
                        "save_card": save_card,
                        "validated": True
                    }
                else:
                    st.error("⚠️ Please fill in all required fields")
                    return {}
        
        return {}
    
    def _display_bank_transfer_form(self) -> Dict[str, Any]:
        """Display bank transfer form"""
        
        st.markdown("""
        **Bank Transfer Instructions**
        
        Your booking will be held for 24 hours while we await payment confirmation.
        """)
        
        with st.form("bank_transfer_form"):
            st.markdown("**Account Holder Information**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                account_holder = st.text_input("Account Holder Name*")
                bank_name = st.text_input("Bank Name*")
            
            with col2:
                account_number = st.text_input("Account Number*")
                routing_number = st.text_input("Routing/SWIFT Code*")
            
            transfer_method = st.selectbox("Transfer Method*",
                                         ["Domestic Wire Transfer", "International Wire Transfer", 
                                          "ACH Transfer", "SEPA Transfer"])
            
            # Display our banking details
            st.markdown("**Transfer To (Our Account Details):**")
            st.info("""
            **AI Travel Platform Inc.**  
            **Bank:** Chase Business Banking  
            **Account:** 1234567890  
            **Routing:** 021000021  
            **SWIFT:** CHASUS33  
            **Reference:** Include your booking confirmation number
            """)
            
            confirmation_understanding = st.checkbox(
                "✅ I understand payment confirmation may take 1-3 business days*"
            )
            
            submitted = st.form_submit_button("🏦 **Confirm Bank Transfer Details**",
                                            type="primary", 
                                            use_container_width=True)
            
            if submitted:
                if all([account_holder, bank_name, account_number, 
                       routing_number, confirmation_understanding]):
                    return {
                        "method": "bank_transfer",
                        "account_holder": account_holder,
                        "bank_name": bank_name,
                        "account_number": f"****{account_number[-4:]}",
                        "transfer_method": transfer_method,
                        "validated": True
                    }
                else:
                    st.error("⚠️ Please fill in all required fields")
        
        return {}
    
    def _display_paypal_form(self) -> Dict[str, Any]:
        """Display PayPal payment form"""
        
        with st.form("paypal_form"):
            st.markdown("**PayPal Account Information**")
            
            paypal_email = st.text_input("PayPal Email Address*",
                                       placeholder="your.email@example.com")
            
            # PayPal security options
            st.markdown("**Payment Options**")
            payment_source = st.selectbox("Payment Source",
                                        ["PayPal Balance", "Linked Bank Account", 
                                         "Linked Credit Card", "PayPal Credit"])
            
            # PayPal buyer protection info
            st.info("""
            🛡️ **PayPal Buyer Protection Included**
            • Get your money back if something goes wrong
            • Secure payment processing
            • Dispute resolution support
            """)
            
            terms_paypal = st.checkbox("✅ I agree to PayPal's terms and conditions*")
            
            submitted = st.form_submit_button("💰 **Continue with PayPal**",
                                            type="primary",
                                            use_container_width=True)
            
            if submitted:
                if paypal_email and terms_paypal:
                    return {
                        "method": "paypal",
                        "email": paypal_email,
                        "payment_source": payment_source,
                        "validated": True
                    }
                else:
                    st.error("⚠️ Please provide PayPal email and accept terms")
        
        return {}
    
    def _display_digital_wallet_form(self) -> Dict[str, Any]:
        """Display digital wallet form"""
        
        with st.form("digital_wallet_form"):
            st.markdown("**Digital Wallet Selection**")
            
            wallet_type = st.selectbox("Wallet Type*",
                                     ["Apple Pay", "Google Pay", "Samsung Pay", 
                                      "Microsoft Pay", "Other"])
            
            if wallet_type in ["Apple Pay", "Google Pay", "Samsung Pay"]:
                st.success(f"✅ {wallet_type} detected and ready")
                st.markdown(f"""
                **{wallet_type} Benefits:**
                • Biometric authentication (Touch ID/Face ID/Fingerprint)
                • Tokenized payments (your real card number is never shared)
                • Instant processing
                • No need to enter card details
                """)
            
            # Simulated biometric verification
            biometric_verified = st.checkbox(f"🔐 Verify with biometric authentication", 
                                           value=True)
            
            submitted = st.form_submit_button(f"📱 **Pay with {wallet_type}**",
                                            type="primary",
                                            use_container_width=True)
            
            if submitted:
                if biometric_verified:
                    return {
                        "method": "digital_wallet",
                        "wallet_type": wallet_type,
                        "biometric_verified": True,
                        "validated": True
                    }
                else:
                    st.error("⚠️ Biometric verification required")
        
        return {}
    
    def _display_crypto_form(self) -> Dict[str, Any]:
        """Display cryptocurrency payment form"""
        
        with st.form("crypto_form"):
            st.markdown("**Cryptocurrency Payment**")
            
            crypto_type = st.selectbox("Cryptocurrency*",
                                     ["Bitcoin (BTC)", "Ethereum (ETH)", "USD Coin (USDC)",
                                      "Bitcoin Cash (BCH)", "Litecoin (LTC)"])
            
            wallet_address = st.text_input("Your Wallet Address*",
                                         placeholder="Enter your wallet address for refunds")
            
            # Display our crypto addresses
            st.markdown("**Send Payment To:**")
            
            crypto_addresses = {
                "Bitcoin (BTC)": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
                "Ethereum (ETH)": "0x742d35Cc6635C0532925a3b8D4e49f6a7a1a5a1a",
                "USD Coin (USDC)": "0x742d35Cc6635C0532925a3b8D4e49f6a7a1a5a1a"
            }
            
            selected_address = crypto_addresses.get(crypto_type, "Address will be provided")
            
            st.code(selected_address, language="text")
            
            st.warning("""
            ⚠️ **Important Crypto Payment Notes:**
            • Send exact amount only (additional fees may cause overpayment)
            • Payment confirmation takes 10-30 minutes
            • Your booking will be held during confirmation period
            • Save transaction hash for your records
            """)
            
            transaction_hash = st.text_input("Transaction Hash (after sending)",
                                           placeholder="Enter transaction hash after payment")
            
            crypto_terms = st.checkbox("✅ I understand cryptocurrency payment terms*")
            
            submitted = st.form_submit_button("🪙 **Confirm Crypto Payment**",
                                            type="primary",
                                            use_container_width=True)
            
            if submitted:
                if wallet_address and crypto_terms:
                    return {
                        "method": "cryptocurrency", 
                        "crypto_type": crypto_type,
                        "wallet_address": wallet_address,
                        "transaction_hash": transaction_hash,
                        "validated": True
                    }
                else:
                    st.error("⚠️ Please provide wallet address and accept terms")
        
        return {}
    
    def display_payment_confirmation(self, payment_details: Dict, 
                                   package: Dict, total_amount: float) -> bool:
        """
        Display final payment confirmation and process payment
        
        Args:
            payment_details: Validated payment details
            package: Travel package details
            total_amount: Final amount to be charged
            
        Returns:
            Boolean indicating if payment was confirmed
        """
        
        st.markdown("### 🔒 **Final Payment Confirmation**")
        
        # Display payment summary
        st.markdown("**Payment Summary:**")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            method_name = self.supported_payment_methods[st.session_state.selected_payment_method]['name']
            
            st.markdown(f"""
            **Payment Method:** {method_name}  
            **Package:** {package['title']}  
            **Destination:** {package['destination']}  
            **Duration:** {package['duration']} days  
            **Travelers:** {package['travelers']} people  
            """)
            
            if payment_details['method'] == 'credit_card':
                st.markdown(f"**Card:** ****{payment_details['card_number'][-4:]}")
            elif payment_details['method'] == 'paypal':
                st.markdown(f"**PayPal:** {payment_details['email']}")
            elif payment_details['method'] == 'bank_transfer':
                st.markdown(f"**Bank:** {payment_details['bank_name']}")
            elif payment_details['method'] == 'digital_wallet':
                st.markdown(f"**Wallet:** {payment_details['wallet_type']}")
            elif payment_details['method'] == 'cryptocurrency':
                st.markdown(f"**Crypto:** {payment_details['crypto_type']}")
        
        with col2:
            st.markdown(f"""
            <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 8px; text-align: center; border: 2px solid #4CAF50;">
                <h3 style="color: #2E7D32; margin: 0;">Final Amount</h3>
                <h2 style="color: #1B5E20; margin: 0.5rem 0;">${total_amount:,.2f}</h2>
                <small style="color: #388E3C;">All fees included</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Security and terms
        st.markdown("**Security & Terms:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            security_confirmation = st.checkbox("🔒 I confirm this transaction is secure")
            terms_confirmation = st.checkbox("📋 I accept the booking terms and conditions")
        
        with col2:
            cancellation_policy = st.checkbox("❌ I understand the cancellation policy")
            newsletter_consent = st.checkbox("📧 Send me travel updates (optional)")
        
        # Final confirmation
        st.markdown("---")
        
        if all([security_confirmation, terms_confirmation, cancellation_policy]):
            
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col2:
                if st.button("🎉 **CONFIRM PAYMENT & COMPLETE BOOKING**",
                           type="primary",
                           use_container_width=True):
                    return self._process_payment_simulation(payment_details, package, total_amount)
        else:
            st.warning("⚠️ Please confirm all required terms before proceeding")
        
        return False
    
    def _process_payment_simulation(self, payment_details: Dict,
                                  package: Dict, total_amount: float) -> bool:
        """
        Simulate payment processing with realistic workflow
        
        Args:
            payment_details: Payment method details
            package: Travel package
            total_amount: Amount to charge
            
        Returns:
            Boolean indicating success
        """
        
        # Simulate payment processing
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        import time
        
        # Processing steps
        steps = [
            ("🔐 Validating payment method...", 0.2),
            ("💳 Processing payment...", 0.4),
            ("🛡️ Security verification...", 0.6),
            ("📋 Creating booking record...", 0.8),
            ("✅ Finalizing confirmation...", 1.0)
        ]
        
        for step_text, progress in steps:
            status_text.text(step_text)
            progress_bar.progress(progress)
            time.sleep(1)  # Simulate processing time
        
        # Generate payment confirmation
        payment_id = f"PAY_{datetime.now().strftime('%Y%m%d')}_{uuid.uuid4().hex[:8].upper()}"
        
        # Store payment details in session
        st.session_state.payment_confirmation = {
            "payment_id": payment_id,
            "amount": total_amount,
            "method": payment_details['method'],
            "status": "completed",
            "processed_at": datetime.now(),
            "package": package,
            "newsletter_consent": st.session_state.get('newsletter_consent', False)
        }
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        # Show success message
        st.balloons()
        
        st.success("🎉 **Payment Successful!**")
        
        st.markdown(f"""
        <div style="background: #e8f5e8; padding: 2rem; border-radius: 12px; text-align: center; margin: 1rem 0;">
            <h2 style="color: #2E7D32;">✅ Payment Confirmed!</h2>
            <h3 style="color: #1B5E20;">Payment ID: {payment_id}</h3>
            <p style="color: #388E3C; margin: 1rem 0;">Your booking is now confirmed and being processed</p>
            <p><strong>Amount Charged:</strong> ${total_amount:,.2f}</p>
            <p><strong>Processing Time:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        return True

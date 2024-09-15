# Import necessary libraries
import streamlit as st

# Define the customer inquiries and responses
def chatbot_response(user_input):
    responses = {
        "hours of operation": "We are open Monday to Friday from 9 AM to 6 PM, and Saturday from 10 AM to 4 PM. We are closed on Sundays.",
        "delivery services": "Yes, we offer delivery services for all products within a 10-mile radius. Delivery charges may apply.",
        "products": "We offer a variety of products including electronics, clothing, home decor, and beauty products.",
        "order online": "Yes, you can place an order online through our website. Just visit www.yourbusiness.com for more details.",
        "customer support": "You can reach our customer support team at (555) 123-4567 or email us at support@yourbusiness.com.",
        "location": "We are located at 123 Main Street, Anytown, USA.",
        "return policy": "Yes, we have a 30-day return policy. Please bring your receipt or proof of purchase for returns.",
        "promotions or discounts": "Yes! We currently have a 20% discount on all electronics. Check our website for more details.",
        "payment methods": "We accept credit cards, debit cards, PayPal, and cash for in-store purchases."
    }

    user_input = user_input.lower()
    for question in responses:
        if question in user_input:
            return responses[question]
    
    return "I'm sorry, I don't have the answer to that. Please contact customer support at (555) 123-4567."

# Streamlit app code
st.title("Small Business Customer Support Chatbot")

# Create a text input box for user queries
user_input = st.text_input("You:", "")

# Process the user input and generate a response
if user_input:
    response = chatbot_response(user_input)
    st.write(f"Chatbot: {response}")

# Instructions
st.write("Type your inquiries in the text box above. Type 'quit' to end the chat.")

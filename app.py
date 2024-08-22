import streamlit as st
from transformers import pipeline

# Initialize the Streamlit app
st.title("Electronic Recommendation Chatbot")

# Welcome message
st.write("Hi! I'm your electronic recommendation assistant. Ask me for recommendations on electronic products like smartphones, laptops, etc.")

# Load a pre-trained text generation model (this is just an example)
generator = pipeline('text-generation', model='gpt2')

# Function to generate a recommendation based on user input
def generate_recommendation(query):
    if "smartphone" in query.lower():
        return "I recommend checking out the latest iPhone or Samsung Galaxy. They are known for their performance and camera quality."
    elif "laptop" in query.lower():
        return "You might like the MacBook Pro or the Dell XPS. Both offer great performance and build quality."
    elif "headphones" in query.lower():
        return "The Sony WH-1000XM4 or Bose QuietComfort are excellent choices for noise-cancelling headphones."
    else:
        return generator(query, max_length=50)[0]['generated_text']

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You: ", key="input")

if user_input:
    st.session_state.messages.append(f"You: {user_input}")
    response = generate_recommendation(user_input)
    st.session_state.messages.append(f"Bot: {response}")
    st.text_input("You: ", key="input", value="")

for message in st.session_state.messages:
    st.write(message)


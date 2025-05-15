import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Please set your GOOGLE_API_KEY in the .env file")

genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
model = genai.GenerativeModel('gemini-2.0-flash')

def get_food_suggestion(user_input):
    """
    Get food suggestions based on user input using Gemini API
    """
    prompt = f"""You are a food suggestion assistant. Based on the following input, suggest appropriate food options.
    Keep your response concise and focused only on food suggestions.
    User input: {user_input}"""
    
    response = model.generate_content(prompt, generation_config={
        'temperature': 0.7,  # Adjust creativity level (0.0 to 1.0)
        'max_output_tokens': 150,  # Limit response length
    })
    
    return response.text

def main():
    print("Welcome to the Food Suggestion Chatbot!")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        user_input = input("\nWhat kind of food are you looking for? (e.g., 'I want something spicy', 'I'm in the mood for Italian'): ")
        
        if user_input.lower() == 'quit':
            print("Thank you for using the Food Suggestion Chatbot!")
            break
            
        try:
            suggestion = get_food_suggestion(user_input)
            print("\nHere are some suggestions:")
            print(suggestion)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 
from transformers import pipeline

def generate_response(question):
    nlp_model = pipeline("text-generation", model="gpt-3.5-turbo")
    response = nlp_model(question, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]

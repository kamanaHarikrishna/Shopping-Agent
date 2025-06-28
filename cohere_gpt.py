import cohere

def generate_gift_ideas(budget, preferences):
    co = cohere.Client("dyVoQX5dgIiR9EMRDGSuX8QXLG9MYRPw1qZBG4Ik")  # Replace with env var or Streamlit secret
    prompt = f"""
I have a total budget of ${budget}. Suggest one unique gift for each of the following interests:

{preferences}

Format: Gift – Price – Why it’s a good match.
"""
    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=400,
        temperature=0.7
    )
    return response.generations[0].text.strip()

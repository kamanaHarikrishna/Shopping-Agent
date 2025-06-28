import streamlit as st
from cohere_gpt import generate_gift_ideas
from search_tool import search_product_link
import base64

# 🎨 Add e-commerce background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .footer {{
        position: fixed;
        left: 0;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: #888;
        font-size: 14px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

add_bg_from_local("background.png")

# 🛍️ Streamlit App Title
st.set_page_config(page_title="🎁 AI Shopping Assistant", layout="wide")
st.title("🎁 AI Shopping Assistant")

# 🔐 Load API keys from secrets
COHERE_KEY = st.secrets["COHERE_API_KEY"]
SERPAPI_KEY = st.secrets["SERPAPI_KEY"]

# 💰 Budget & Preferences Input
budget = st.number_input("Enter your total budget ($):", min_value=10, step=5)
preferences = st.text_area("Enter interests (one per line, e.g., Gamer, Book lover):")

# 🎁 Generate Button
if st.button("Suggest Gifts"):
    with st.spinner("Generating your gift suggestions..."):
        ideas = generate_gift_ideas(budget, preferences)
        st.markdown("## 🎁 Gift Ideas")
        st.text(ideas)

        st.markdown("## 🔗 Product Links")
        for line in ideas.split("\n"):
            if "–" in line:
                product = line.split("–")[0].strip()
                link = search_product_link(product, SERPAPI_KEY)
                st.markdown(f"- [{product}]({link})")

# 👣 Footer
st.markdown('<div class="footer">Developed by Hari Krishna</div>', unsafe_allow_html=True)

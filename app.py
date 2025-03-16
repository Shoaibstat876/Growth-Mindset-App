
import streamlit as st
import random

# List of motivational growth mindset quotes
quotes = [
    "Your only limit is your mind.",
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Mistakes are proof that you are trying.",
    "Believe in yourself and your ability to grow.",
    "Every expert was once a beginner.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Difficulties in life are intended to make us better, not bitter."
]

# Streamlit App Title
st.title("🌱 Growth Mindset Challenge")

# Display a random motivational quote
st.markdown(f"> **{random.choice(quotes)}**")

# User input: Set a Growth Mindset Goal
st.subheader("🚀 What's your goal for today?")
goal = st.text_input("Write your learning goal or challenge for today:")

if goal:
    st.success(f"Awesome! Keep pushing forward: **{goal}** 💪")

# Description of Growth Mindset
st.write("""
### What is a Growth Mindset?
A **growth mindset** is the belief that your abilities and intelligence **can be developed** through effort, perseverance, and learning from mistakes.
""")

st.write("""
### Why Adopt a Growth Mindset?
- 🌟 **Embrace Challenges**: See obstacles as opportunities to learn.
- 📖 **Learn from Mistakes**: Every mistake is a step toward improvement.
- 🔥 **Persist Through Difficulties**: Hard work and persistence lead to growth.
- 🎯 **Celebrate Effort**: Focus on the learning process, not just the result.
- 🤔 **Stay Curious & Open-Minded**: Adapt and grow continuously.
""")

st.write("""
### How Can You Practice a Growth Mindset?
1️⃣ **Set Learning Goals** – Develop new skills and improve understanding.
2️⃣ **Reflect on Your Learning** – Think about successes & challenges.
3️⃣ **Seek Feedback** – Use constructive criticism for improvement.
4️⃣ **Stay Positive** – Believe in your growth potential!
""")

# Footer
st.markdown("---")
st.write("🌱 **Keep growing, keep learning!** 🚀")

import streamlit as st
import time
import random

# --------------------- PAGE CONFIGURATION ---------------------
st.set_page_config(page_title="Growth Mindset App", page_icon="🚀", layout="wide")

# --------------------- SIDEBAR NAVIGATION ---------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "📝 Journal", "📊 Progress"])

st.sidebar.markdown("---")
st.sidebar.write("🔗 **Useful Links**")
st.sidebar.markdown("[📖 Learn Growth Mindset](https://www.mindsetworks.com/)")

# --------------------- THEME SELECTION ---------------------
theme = st.sidebar.radio("🌗 Choose Theme:", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("<style>body {background-color: #333; color: white;}</style>", unsafe_allow_html=True)
else:
    st.markdown("<style>body {background-color: white; color: black;}</style>", unsafe_allow_html=True)

# --------------------- HOME PAGE ---------------------
if page == "🏠 Home":
    st.title("🚀 Growth Mindset Challenge")
    st.subheader("Believe in Your Potential! 🌱")

    st.image("https://plus.unsplash.com/premium_photo-1731439886498-d09d6472dfb3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8aW1wcm92ZSUyMG1pbmR8ZW58MHx8MHx8fDA%3D", use_container_width=True)

    st.write("""
    A **growth mindset** is the belief that abilities and intelligence can be developed through dedication and hard work.
    This web app will help you **set goals, reflect on challenges, and track your progress!**
    """)

    # --------------------- PROGRESS BAR ---------------------
    st.subheader("🔥 Keep Growing!")
    progress_bar = st.progress(0)
    for percent in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent + 1)
    st.success("You are on the path to success! 🚀")

    # --------------------- MOTIVATIONAL QUOTE GENERATOR ---------------------
    st.subheader("💡 Today's Inspiration")
    quotes = [
        "“Your only limit is your mind.”",
        "“Difficulties in life are intended to make us better, not bitter.”",
        "“Growth mindset isn’t about being the best, it’s about getting better.”",
        "“You can always improve, just keep learning.”"
    ]
    st.info(random.choice(quotes))

# --------------------- JOURNAL PAGE ---------------------
elif page == "📝 Journal":
    st.title("✍️ Your Growth Journal")
    feedback = st.text_area("Write about today's challenge and how you overcame it:", "")
    if st.button("Submit"):
        st.success("Great! Keep tracking your progress. 🚀")

# --------------------- PROGRESS PAGE ---------------------
elif page == "📊 Progress":
    st.title("📊 Your Progress Tracker")
    st.write("🛠 **Feature Coming Soon:** Track your achievements over time!")

# --------------------- FOOTER ---------------------
st.markdown("---")
st.write("📌 **Remember:** Every failure is a step closer to success. Keep pushing forward! 💪")

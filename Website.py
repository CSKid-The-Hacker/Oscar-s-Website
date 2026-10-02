import streamlit as st

st.title("Welcome to Oscar's Website!")

st.write("This website is running on my own python code so I hope my school sees this!")

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

st.write(f"Total Clicks: {st.session_state.clicks}")    

if st.button("Click Me!"):
    st.session_state.clicks += 1
    st.rerun()

st.subheader("More info!")
st.write("My names Oscar Darby, Im 11 years old and I know C# and Python.")
st.write("Im also working on my own programming language called K++ (K standing for Kernel of course).")
st.write("Idk what to put next...")
st.write("OH WAIT A MINUTE... I FORGOT TO SAY MY GITHUB IS CSKid-the-hacker!")
st.write("ok NOW I dont know what to put next...")
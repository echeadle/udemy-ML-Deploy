import streamlit as st

st.title("First page")

def store_value(key):
    st.session_state[key] = st.session_state["_"+key]

def load_value(key):
    if "_"+key not in st.session_state:
        st.session_state["_"+key] = st.session_state[key]

st.write(st.session_state['df'])
load_value("x1")
#x1 = st.number_input("Pick a number", 0, 10, key="_x1", on_change=store_value, args=["x1"])
load_value("x2")
#x2 = st.number_input("Pick another number", 0, 10, key="_x2", on_change=store_value, args=["x2"])


st.subheader(f"You chose to multiply {x1} with {x2} 👍")
st.markdown("""#### Check the second page for the result!""")

st.write(st.session_state)
import streamlit as st

st.set_page_config(page_title='Agent Builder', layout='wide')

st.title("⚙️ The Agent Configuration Panel")
st.write("Design your AI persona before launching the chat.")

# The Sidebar
with st.sidebar:
    st.header('Security and Settings')

    # Password input hides the text you type
    api_key = st.text_input('Groq API Key', type='password')

    # Slider for temperature
    temperature = st.slider('Creativity (Temperature):', min_value=0.0, max_value=1.0, value=0.7)

    st.info("The sidebar is great for settings that shouldn't clutter the main screen.")

# Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader('Agent Identity')

    agent_name = st.text_input('Name your Agent:', value='DataBot')

    #Dropdown (Menu)
    agent_role = st.selectbox('Select your Agent Role:', ["Data Analyst", "Copywriter", "Python Tutor"])

with col2:
    st.subheader('Agent Behaviour')
    # Text area for long paragraphs

    system_instructions = st.text_area('Custom System Instructions:', height=110,
                                        placeholder='Eg. Always answer in bullet points')

# The Output (Testing the Input)
st.write("---")
st.subheader('Preview your Configuration')

if agent_name:
    st.success(f"**{agent_name}** is ready to be deployed as a **{agent_role}**.")

    st.code(f"""
    System Prompt:
    You are {agent_name}, an expert {agent_role}.
    Your creativity level is set to {temperature}.
    Additional Instructions: {system_instructions}
    """, language="text")

import streamlit as st


def app():
    # Setting up the Title
    st.title("Welcome :wave:")
    st.write(f"""
        ### Made with β€οΈ
        """)
    intro = f"""
    ---
    ### **π Getting Started**
    - Thank you for being a part of this Open-Source **GPT-3 Sandbox** π
    - To get started, 1. go to **GPT-3 Sandbox** on the left sidebar-> 2. Paste your **OpenAI API key**

    ### **πΎ Create & deploy GPT-3 powered apps**
    - This sandbox is an open-source π§to enable anyone to turn their GPT-3 app ideas into reality with just a few lines of Python code
    - It is built on top of Streamlit that enables you to quickly create & deploy web applications 
    - Streamlit takes care of hosting the endpoint and acts as a frontend interface for the web app
    """


    st.write(intro)
    
    st.write(f"""
        ###  πΎ **About the Sandbox**
        - This is an open-source π§ and it is alive thanks to the awesome GPT-3 community.
        """)

    # st.write(f"""
    #         ---
    #         ### π **Connect With Us**
    #         - We are [Shubham](https://www.linkedin.com/in/shubhamsaboo/) and [Sandra](https://www.linkedin.com/in/sandrakublik/), co-founders of [Kairos Data Labs](https://www.linkedin.com/company/kairos-data-labs) 
    #         - We are super excited to have you here. Our mission is to make the [GPT-3 Sandbox](https://github.com/Shubhamsaboo/kairos_gpt3) accessible and usable to everyone who wants to build applications with OpenAI's GPT-3 β€οΈ 
    #         - Come by π€ [the forum](https://github.com/Shubhamsaboo/kairos_gpt3) if you'd like to ask questions, post an awesome app, or just say Hi!
    #     """)
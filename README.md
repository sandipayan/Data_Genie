# Data Genie 🧞‍

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com/)
[![Snowflake](https://img.shields.io/badge/-Snowflake-29BFFF?style=flat-square&logo=snowflake&logoColor=white)](https://www.snowflake.com/en/)
[![Supabase](https://img.shields.io/badge/-Supabase-00C04A?style=flat-square&logo=supabase&logoColor=white)](https://www.supabase.io/)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://snowchat.streamlit.app/)

**Data Genie**  is a chatbot designed to help you with Snowflake DWH. It is built using OpenAI's GPT-4 and Streamlit.
Go to the GitHub repo to learn more about the project.
#

## 🌟 Features

- Interactive and user-friendly interface
- Integration with Snowflake Data Warehouse
- Utilizes OpenAI's GPT-3.5-turbo-16k and text-embedding-ada-002
- Uses Supabase PG-vector Vector Database for storing and searching through vectors

## 🛠️ Installation

1. Clone this repository:
   git clone https://github.com/yourusername/snowchat.git

2. Install the required packages:
   cd snowchat
   pip install -r requirements.txt

3. Set up your `OPENAI_API_KEY`, `ACCOUNT`, `USER_NAME`, `PASSWORD`, `ROLE`, `DATABASE`, `SCHEMA`,  `WAREHOUSE`, `SUPABASE_URL` and `SUPABASE_SERVICE_KEY` in project directory `secrets.toml`.

4. Make you're schemas and store them in docs folder that matches you're database.

5. Create supabase extention, table and function from the supabase/scripts.sql.

6. Run `python ingest.py` to get convert to embeddings and store as an index file.

7. Run the Streamlit app to start chatting:
   streamlit run main.py

## 📚 Usage

1. Launch the app by visiting the URL provided by Streamlit.
2. Type your query in natural language or SQL format in the input box.
3. Press "Submit" to generate the response.
4. The chatbot will generate a response based on your query and display the result, including any relevant data or SQL code.

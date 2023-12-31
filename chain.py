from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import streamlit as st

template = """Considering the provided chat history and a subsequent question, rewrite the follow-up question to be an independent query. Alternatively, conclude the conversation if it appears to be complete.
Chat History:\"""
{chat_history}
\"""
Follow Up Input: \"""
{question}
\"""
Standalone question:"""

condense_question_prompt = PromptTemplate.from_template(template)

# Write the SQL code in markdown format.
# Additionally, offer a brief explanation about how you arrived at the SQL code.
# Based on the question provided, you must generate SQL code that is compatible with the Snowflake environment.
#but do not assume the existence of any not mentioned.

TEMPLATE = """ 
You're an AI assistant specializing in data analysis with Snowflake SQL. 
Based on the question provided, you must generate SQL code that is compatible with the Snowflake environment, but do not assume the existence of any not mentioned.
If the required column isn't explicitly stated in the context, find a most appropriate alternative using available information.
When a name is asked in the query its probably an ae_name or ZM_AE_NAME. Make all search case insensitive and wildcard.
Any string search should be case insensitive and wildcard.
Always consider sfdc_Account_id or Primary Key columns mentioned if multiple tables are to be joined. 
Always pick Industry value from  account_dim table. 
ZM_SFDC_ID is same as sfdc_account_id
never use these columns for filter: PROD_PAGE, PROD_PAGE_VIEWS

For checking contract renewal use contract_renewal_date_exit column. 


Question: {question}
{context}

Answer:

"""
QA_PROMPT = PromptTemplate(template=TEMPLATE, input_variables=["question", "context"])


def get_chain(vectorstore):
    """
    Get a chain for chatting with a vector database.
    """
    q_llm = OpenAI(
        temperature=0,
        openai_api_key=st.secrets["OPENAI_API_KEY"],
        model_name="gpt-3.5-turbo-16k",
        max_tokens=500,
    )

    llm = OpenAI(
        model_name="gpt-3.5-turbo-16k",
        temperature=0,
        openai_api_key=st.secrets["OPENAI_API_KEY"],
        max_tokens=1000,
    )

    question_generator = LLMChain(llm=q_llm, prompt=condense_question_prompt)

    doc_chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=QA_PROMPT)
    chain = ConversationalRetrievalChain(
        retriever=vectorstore.as_retriever(),
        combine_docs_chain=doc_chain,
        question_generator=question_generator,
    )
    return chain

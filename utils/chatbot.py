from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os
import dotenv

dotenv.load_dotenv()


def create_vectorstore(chunks):
    api_key = os.getenv('OPENAI_API_KEY')
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    return vectorstore

def create_conversation_chain(vectorstore):
    api_key = os.getenv('OPEN_AI_API')
    llm = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain
import os
import chainlit as cl
from langchain_openai.chat_models import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

chat = AzureChatOpenAI(
    azure_deployment="gpt-4o",
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

memory = ConversationBufferWindowMemory(k=8, return_messages=True)

def generate_response(user_message):
    template = "あなたは、ウミガメのスープのゲームマスターです。"
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(template),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}"),
    ])
    conversation = ConversationChain(llm=chat, memory=memory, prompt=prompt)
    return conversation.predict(input=user_message)

@cl.on_chat_start  
async def on_chat_start():
    await cl.Message(content="ウミガメのスープを始めます！メッセージを入力してください！").send()

@cl.on_message  
async def on_message(input_message):
    user_message = input_message.content
    print("user message: " + user_message)

    bot_response = generate_response(user_message)
    await cl.Message(content=bot_response).send()

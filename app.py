import os
from openai import AzureOpenAI
import chainlit as cl

# from langchain_core.messages import HumanMessage
# from langchain_core.runnables.history import RunnableWithMessageHistory

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)


# from langchain_community.chat_message_histories import SQLChatMessageHistory

# def get_session_history(session_id):
#     return SQLChatMessageHistory(session_id, "sqlite:///memory.db")


# runnable_with_history = RunnableWithMessageHistory(
#     client,
#     get_session_history,
# )

# runnable_with_history.invoke(
#     [HumanMessage(content="hi - im bob!")],
#     config={"configurable": {"session_id": "1"}},
# )

def generate_response(user_message):
    response = client.chat.completions.create(
       model="gpt-4o",
       messages=[
          {"role": "system", "content": "あなたは、ウミガメのスープのゲームマスターです。"},
          {"role": "user", "content": user_message}
       ]
    )
    return response.choices[0].message.content

# @cl.on_message
# async def main(message: cl.Message):
#     # Your custom logic goes here...

#     # Send a response back to the user
#     await cl.Message(
#         content=f"Received: {message.content}",
#     ).send()

@cl.on_chat_start  
async def on_chat_start():
    await cl.Message(content="ウミガメのスープを始めます！メッセージを入力してください！").send()

# メッセージが送信されたときに実行される関数
@cl.on_message  
async def on_message(input_message):
    user_message = input_message.content
    print("user message: " + user_message)

    bot_response = generate_response(user_message)
    await cl.Message(content=bot_response).send()


import openai
import os
import gradio as gr
openai.api_key = os.environ.get("OPENAI_API_KEY")


class Conversation:
    def __init__(self, prompt, num_of_round):
        self.prompt = prompt
        self.num_of_round = num_of_round
        self.messages = []
        self.messages.append({"role": "system", "content": self.prompt})
    
    def ask(self, question): 
        try:
            self.messages.append({"role": "user", "content": question})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                temperature=0.5,
                max_tokens=256,
                top_p=1,  
            )
        except Exception as e:
            print(e)
            return e
        message = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": message})
        if len(self.messages) > 3:  
            del self.messages[1:3] 
        return message

def add_text(history, text):  
    history = history + [(text, None)]
    return history, gr.update(value="", interactive=False)

def add_file(history, file):  
    history = history + [((file.name,), None)]  
    return history  
    
def bot(history, chatbot): 
    prompt = ". ".join([m["content"] for m in history if m["role"] == "user"])
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0
    )
    message = response["choices"][0]["text"]
    chatbot.add_message(content=message, role="assistant")

def answer(question, history=None):
    if history is None:
        history = []
    history.append(question)
    response = conv.ask(question)
    history.append(response)
    responses = [(u,b) for u,b in zip(history[::2], history[1::2])]
    return responses, history

def on_text_submit(chatbot, txt):
    prompt = ". ".join([m[0] for m in history if m[1] == "user"])
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0
    )
    message = response["choices"][0]["text"]
    chatbot.add(message, "assistant")

def on_file_upload(chatbot, btn):
    chatbot.add((btn.uploaded_file.name,), "user")  

with gr.Blocks(css="#chatbot{height:300px} .overflow-y-auto{height:500px}") as demo:
    chatbot = gr.Chatbot([], elem_id="chatbot").style(height=750)


prompt = """假如你是GPT-4,你可以回答用户提问的任何问题"""
conv = Conversation(prompt, 10)
# with gr.Blocks(css="#chatbot{height:300px} .overflow-y-auto{height:500px}") as demo:
#     chatbot = gr.Chatbot([], elem_id="chatbot").style(height=750)
#     state = gr.State()
    
#     with gr.Row():
#         with gr.Column(scale=0.85):
#             txt = gr.Textbox(
#                 show_label=False,
#                 placeholder="Enter text and press enter, or upload an image",    
#             ).style(container=False)
#         with gr.Column(scale=0.15, min_width=0):
#             btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])
            
#     txt_msg = txt.submit(answer, [txt, state], chatbot, state, queue=False).then(       
#         lambda x: chatbot.add(*x),  
#         None,   
#         [chatbot])
#     txt_msg.then(lambda: gr.update(interactive=True), None, [txt], queue=False)
#     file_msg = btn.upload(add_file, chatbot, btn, chatbot, btn, queue=False).then(       
#         lambda x: chatbot.add(*x),
#         None,   
#         [chatbot]  
#     )  
# demo.launch()

# with gr.Blocks(css="#chatbot{height:800px} .overflow-y-auto{height:500px}") as demo:
#     chatbot = gr.Chatbot([], elem_id="chatbot").style(height=750)
with gr.Blocks(css="#chatty{height:800px} .overflow-y-auto{height:500px}") as demo:
    chatty = gr.Chatbot([], name="Chatty", elem_id="chatbot").style(height=800, width=800)

    with gr.Row():
        with gr.Column(scale=0.85):
            txt = gr.Textbox(
                show_label=False,
                placeholder="Enter text and press enter, or upload an image",
            ).style(container=False)
        with gr.Column(scale=0.15, min_width=0):
            btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])

    txt_msg = txt.submit(add_text, [chatty, txt], [chatty, txt], queue=False).then(
        bot, chatty, chatty
    )
    txt_msg.then(lambda: gr.update(interactive=True), None, [txt], queue=False)
    file_msg = btn.upload(add_file, [chatty, btn], [chatty], queue=False).then(
        bot, chatty, chatty
    )
demo.launch()

# Chatty 🤖
OpenAI ChatCompletion+Gradio实现一个AI助手Chatty，用户可上传文件、视频、输入文本，实现对话、问题解答和文件摘要。                
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## 基于OpenAI的[ChatCompletion](https://platform.openai.com/docs/guides/gpt/chat-completions-api) API实现对话聊天
ChatCompletion API示例:
```
import openai
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```
如示例,需要传入的参数包括一个消息数组,每个元素包含`role`和`content`字段。 
- role 有三个选项:system代表系统,user代表用户,assistant代表AI助手的回复。
- 当`role`为`system`时,content中的内容表示给AI的提示,告诉AI如何回答用户的问题。例如,我们可以在`content`中写“你是一个只会用中文回答问题的助手”,这样即使用户问的问题是英文的,AI的回复也会是中文的。 
- 当`role`为`user`或`assistant`时,content中的内容表示用户和AI助手的对话。
我们考虑将历史对话一起发送给OpenAI的接口,这样AI助手能理解整个对话的上下文。
## 使用Gradio快速搭建聊天对话界面
界面样式如下:
![image](https://github.com/prime234/Chatty/assets/55311775/8e28abd0-d4d5-4678-af32-d8138996b4ed)

TODO: 待进一步功能开发，补充更详细内容，给出demo。 




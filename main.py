# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import openai
import webbrowser

# 输入你的 api_key
chat_gpt_key = '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'
# 将 Key 进行传入
openai.api_key = chat_gpt_key


def completion(prompt):
    response = openai.Completion.create(
        # text-davinci-003 是指它的模型
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None
    )
    message = response.choices[0].text
    return message


def ask(*args):
    prompt = entry.get().strip()  # 去掉输入的首尾空格
    if not prompt:  # 判断输入是否为空
        tk.messagebox.showerror("Error", "输入内容不能为空！")
    elif prompt == "清屏":
        text.delete("1.0", tk.END)  # 清空文本框内容
    elif prompt == "作者":
        webbrowser.open_new("https://subapi1.gardenparty.one/link/f1z87aYDziQ0M3rQ?sub=3")
    else:
        message = completion(prompt)
        text.insert(tk.END, "你问：" + prompt + "\n")
        text.insert(tk.END, "ChatGPT：" + message + "\n\n")
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("ChatGPT")
root.geometry("900x600")

label = tk.Label(root, text="请提问：", font=("宋体", 20), bg="pink")
label.pack(pady=10)

entry_frame = tk.Frame(root, bg="pink")
entry_frame.pack()

entry = tk.Entry(entry_frame, width=50, font=("宋体", 20))
entry.pack(side=tk.LEFT, padx=10)
entry.bind("<Return>", ask)

button = tk.Button(entry_frame, text="发送", command=ask, font=("宋体", 20), bg="pink")
button.pack(side=tk.LEFT, padx=10)

text = tk.Text(root, width=50, height=20, font=("宋体", 20))
text.pack(pady=10)

# 添加菜单栏
menu_bar = tk.Menu(root)

# 添加文件菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="关闭", command=root.quit)
menu_bar.add_cascade(label="文件", menu=file_menu)

# 添加帮助菜单
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="作者", command=lambda: webbrowser.open_new("https://subapi1.gardenparty.one/link/f1z87aYDziQ0M3rQ?sub=3"))
menu_bar.add_cascade(label="帮助", menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()

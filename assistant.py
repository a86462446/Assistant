import tkinter as tk
import openai
from tkinter.constants import *

openai.api_key = 'apikey'

def chatGPT(prompt):
    response= openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages= [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


def reply(ques, code):
    # 宣告prompt
    prompt= ques+ "\n"+ code

    # 清空輸入框
    textField.delete("1.0", tk.END)

    # 產生回覆
    response= chatGPT(prompt)

    # 輸入
    textField.insert(tk.END, response)


def save():
    # 儲存程式碼
    code= textField.get("1.0", tk.END)

    # 需輸入程式碼才能執行
    if code== "\n" or ("if __name__== \"__main__\":" not in code):
        warning.deiconify()

        # 視窗標題
        warning.title('警告')

        # 視窗大小
        warning.geometry('300x300')

        # 視窗放大縮小
        warning.resizable(False, False)

        # 視窗圖標
        warning.iconbitmap('icon.ico')

        warningButton.place(x= 150, y= 150, anchor= "center")

        # 在警告視窗中創建 Label 顯示文字
        label = tk.Label(warning, text='請輸入有效的程式碼。')
        label.place(x= 150, y= 110, anchor= "center")

        return

    # 清空輸入框
    textField.delete("1.0", tk.END)

    # 清除輸入按鈕
    inputButton.place_forget()

    # 宣告問題
    kit= "有需要安裝什麼插件嗎？"
    reduce= "幫我縮減程式碼，只需回覆我程式碼就好了"
    success= "幫我判斷此程式能否順利執行，還是有出現錯誤？"
    comment= "幫我為此程式產生中文註解"

    # 執行回覆
    kitButton= tk.Button(text= "套件安裝", command= lambda: reply(kit, code))
    reduceButton= tk.Button(text= "程式碼縮減", command= lambda: reply(reduce, code))
    successButton= tk.Button(text= "執行結果", command= lambda: reply(success, code))
    commentButton= tk.Button(text= "註解", command= lambda: reply(comment, code))

    # 顯示各功能按鈕
    kitButton.place(x= 300, y= 380, anchor= "center")
    reduceButton.place(x= 300, y= 430, anchor= "center")
    commentButton.place(x= 300, y= 480, anchor= "center")
    successButton.place(x= 300, y= 530, anchor= "center")

def ensure():
    warningButton.place_forget()
    warning.withdraw()

    # 清空輸入框
    textField.delete("1.0", tk.END)

def start():
    # 消除startButton
    startButton.place_forget()

    # 顯示輸入框
    textField.pack(side= "top")

    # 顯示輸入按鈕
    inputButton.place(x= 300, y= 440, anchor= "center")


if __name__== "__main__":
    # 視窗架構
    window = tk.Tk()

    # 視窗標題
    window.title('程式大師')

    # 視窗大小
    window.geometry('600x600')

    # 視窗放大縮小
    window.resizable(False, False)

    # 視窗圖標
    window.iconbitmap('icon.ico')

    # 物件宣告
    inputButton= tk.Button(text= "輸入", command= save)
    startButton= tk.Button(text= "開始使用", command= start)

    textField= tk.Text()

    # 顯示開始按鈕
    startButton.place(x= 300, y= 300, anchor= CENTER)

    warning= tk.Tk()
    warning.withdraw()
    warningButton= tk.Button(warning, text= "確定", command= ensure)

    # 視窗產生
    window.mainloop()
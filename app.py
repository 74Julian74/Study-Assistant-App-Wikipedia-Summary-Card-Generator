import tkinter as tk
from tkinter import messagebox
import wikipedia # type: ignore

# 設定 Wikipedia 語言
wikipedia.set_lang("zh")

# 建立主視窗
root = tk.Tk()
root.title("學習小幫手")
root.geometry("600x400")

# 標題
label = tk.Label(root, text="輸入你想學的主題", font=("Helvetica", 14))
label.pack(pady=10)

# 輸入欄位
entry = tk.Entry(root, width=50)
entry.pack()

# 顯示結果用的文字框
output = tk.Text(root, height=15, width=70)
output.pack(pady=10)

# 查詢函式
def search():
    keyword = entry.get()
    if not keyword:
        messagebox.showwarning("錯誤", "請輸入主題！")
        return

    try:
        summary = wikipedia.summary(keyword, sentences=3)
        output.delete(1.0, tk.END)
        output.insert(tk.END, summary)
    except wikipedia.exceptions.DisambiguationError as e:
        output.delete(1.0, tk.END)
        output.insert(tk.END, f"這個詞太模糊了，請再更具體一些：\n{e.options}")
    except wikipedia.exceptions.PageError:
        output.delete(1.0, tk.END)
        output.insert(tk.END, "查無此主題，請嘗試其他關鍵字。")

# 查詢按鈕
btn = tk.Button(root, text="查詢", command=search)
btn.pack(pady=5)

# 執行主迴圈
root.mainloop()

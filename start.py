import tkinter as tk
from tkinter import filedialog, messagebox
import os
import win32com.client as client
import getpass

def add_to_startup(program_path, shortcut_name="自動啟動程式"):
    """
    建立指定程式的啟動捷徑，並放入目前使用者的啟動資料夾。
    """
    try:
        # 取得目前使用者的啟動資料夾路徑
        startup_folder = os.path.join(
            os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
        )
        
        # 確認啟動資料夾是否存在，若無則建立
        if not os.path.exists(startup_folder):
            os.makedirs(startup_folder)

        # 建立捷徑物件
        shell = client.Dispatch("WScript.Shell")
        shortcut_path = os.path.join(startup_folder, f"{shortcut_name}.lnk")
        shortcut = shell.CreateShortcut(shortcut_path)

        # 設定捷徑屬性
        shortcut.TargetPath = program_path
        shortcut.WorkingDirectory = os.path.dirname(program_path)
        shortcut.Save()

        messagebox.showinfo("成功", f"'{shortcut_name}' 已成功加入開機啟動！\n捷徑位置：{shortcut_path}")

    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤：{e}\n請確認您選擇的是有效的程式檔案。")

class StartupApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("設定開機自動啟動")
        self.geometry("400x150")
        self.configure(bg="#f0f0f0")

        # 建立一個提示標籤
        self.label = tk.Label(
            self,
            text="點擊按鈕，選擇您想開機自動啟動的程式。",
            font=("Helvetica", 12),
            bg="#f0f0f0",
            fg="#555555"
        )
        self.label.pack(pady=20)
        
        # 建立一個選擇檔案的按鈕
        self.select_button = tk.Button(
            self,
            text="選擇程式",
            font=("Helvetica", 12, "bold"),
            command=self.select_file,
            bg="#4CAF50",
            fg="white",
            relief="raised",
            padx=10,
            pady=5
        )
        self.select_button.pack()

    def select_file(self):
        # 打開檔案選擇對話框
        file_path = filedialog.askopenfilename(
            title="選擇要設定自動啟動的程式",
            filetypes=(("執行檔", "*.exe"), ("所有檔案", "*.*"))
        )

        if file_path:
            # 從檔案路徑中取得捷徑名稱
            shortcut_name = os.path.splitext(os.path.basename(file_path))[0]
            
            # 呼叫設定啟動的函式
            add_to_startup(file_path, shortcut_name)
        else:
            # 如果使用者取消選擇
            messagebox.showinfo("提示", "您沒有選擇任何檔案。")

if __name__ == "__main__":
    app = StartupApp()
    app.mainloop()
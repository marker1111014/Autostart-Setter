# Autostart-Setter

 

一個簡單、直觀的桌面應用程式，讓您輕鬆設定任何 Windows 程式的開機自動啟動。

-----

## 💡 專案簡介

您是否厭倦了每次開機後都要手動開啟常用的軟體？**Autostart-Setter** 讓這一切變得簡單！

這個小工具提供一個使用者友善的視窗，您只需點擊按鈕，選擇您想要自動啟動的程式，它就會自動幫您將捷徑加入 Windows 的啟動資料夾。

**特色：**

  * **直觀易用**：簡潔的 GUI 介面，無需複雜操作。
  * **安全可靠**：程式會將捷徑加入目前使用者的啟動資料夾，不需要系統管理員權限。
  * **獨立執行**：打包成 `.exe` 檔案後，使用者無需安裝 Python 環境即可直接運行。

-----

## 🚀 如何使用

使用本程式非常簡單，您有兩種方式：

### 方法一：直接使用 `.exe` 檔案 (推薦)

1.  前往 [Releases](https://www.google.com/search?q=https://github.com/%E6%82%A8%E7%9A%84%E5%B8%B3%E8%99%9F/Autostart-Setter/releases) 頁面，下載最新版本的 `Autostart-Setter.exe` 檔案。
2.  雙擊執行該檔案。
3.  在彈出的視窗中，點擊 **「選擇程式」** 按鈕。
4.  在檔案總管中找到您想開機自動啟動的程式（例如：`chrome.exe` 或 `notepad.exe`），然後點擊「開啟」。

程式會自動建立捷徑，並在完成後顯示成功訊息。

### 方法二：從原始碼運行

1.  確保您的電腦已安裝 **Python 3.6** 或以上版本。
2.  複製此專案到您的本地電腦：
    ```bash
    git clone https://github.com/您的帳號/Autostart-Setter.git
    ```
3.  切換到專案目錄：
    ```bash
    cd Autostart-Setter
    ```
4.  安裝所需的函式庫：
    ```bash
    pip install pypiwin32
    ```
5.  運行程式：
    ```bash
    python startup_picker.py
    ```

-----

## 🛠️ 開發者資訊

  * **程式語言**：Python
  * **GUI 函式庫**：Tkinter (Python 內建)
  * **Windows API 函式庫**：`pypiwin32`
  * **打包工具**：PyInstaller

如果您對原始碼有興趣，歡迎隨時查看或提出 Pull Request。

-----

## 📄 授權條款

這個專案遵循 **MIT 授權條款**。詳情請參閱 `LICENSE` 檔案。

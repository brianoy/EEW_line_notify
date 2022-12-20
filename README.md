# EEW_line_notify
地震速報、速報軟件、line webhook推播、line webhook推送（配合地牛Wake Up!）
由於地牛wake up!只能觸發*cmd*和*bat*，如果想要推送到其他軟體就要call到python

# 使用說明
## 第一步 架設python環境(不示範)(請確保系統環境變數中有python路徑)

## 第二步 獲取line notify token
點擊：https://notify-bot.line.me/my/
### 登入後選擇發行權杖
<img src="https://user-images.githubusercontent.com/24865458/208755580-4528b3be-7822-4c0c-a9ca-95b10f9ffeb9.png" width="50%">
### 取一個喜歡的名字以及選擇聊天室後 複製權杖
<img src="https://user-images.githubusercontent.com/24865458/208755758-9a057691-c583-4012-bf63-9d48c711451f.png" width="50%">

## 第三步 下載zip解壓縮在想要的路徑

## 第四步 在地牛wake up!中選擇剛剛下載的earthquick.bat路徑
<img src="https://user-images.githubusercontent.com/24865458/208751019-a2ca4838-1839-4e55-9cf6-a49853e98d78.png" width="50%">

## 第五步 調整earthquick.bat中設定notify.py檔案的位置
<img src="https://user-images.githubusercontent.com/24865458/208752205-64f9032a-04c8-4af9-bfb2-abef3875c4b1.png" width="50%">

## 第六步 填入line notify 的 token

```XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX```

<img src="https://user-images.githubusercontent.com/24865458/208754014-784e5bfe-151e-46d2-ba62-eaa5f1ff1ba0.png" width="50%">



# EEW_line_notify
地震速報、速報軟件、line webhook推播、line webhook推送（配合地牛Wake Up!）

由於地牛wake up!只能觸發*cmd*和*bat*，如果想要推送到其他軟體就要call到python

```mermaid
      graph LR
      start[地震發生] --> input[地牛wakeup!被觸發]
      input -- 觸發*exe.cmd.bat. --> conditionA{看自己選擇\n傳入變數:強度時間}
      conditionA -- 分支:split\n傳入變數: 強度時間 --> conditionC{earthquick.bat}
      conditionC -- 觸發\n傳入變數: 強度時間 --> conditionD{discord_notify.py} -- webhook post--> send[discord傳訊息]
      send[discord傳訊息] --> stop[程式結束]
```


# 使用說明
## 第一步 架設python環境，請確保系統環境變數中有python路徑(PATH)
*(不示範)*
*推薦python版本: 3.12.2*

## 第二步 取得line notify token
取得連結：https://notify-bot.line.me/my/
### 登入後選擇發行權杖
<img src="https://user-images.githubusercontent.com/24865458/208755580-4528b3be-7822-4c0c-a9ca-95b10f9ffeb9.png" width="50%">

### 取一個名字、選擇聊天室，點擊複製權杖
*權杖只會出現過一次，請務必好好保管以免洩漏。如果不小心沒複製到，直接重新再新增一個權杖就好了*
<img src="https://user-images.githubusercontent.com/24865458/208755758-9a057691-c583-4012-bf63-9d48c711451f.png" width="50%">

## 第三步 下載zip解壓縮在想要的路徑
<img src="https://github.com/brianoy/EEW_line_notify/assets/24865458/ae1b92bf-d1e7-4e40-a6d6-18b882c21690" width="50%">

## 第四步 在地牛wake up!中選擇剛剛下載的earthquick.bat路徑
<img src="https://user-images.githubusercontent.com/24865458/208751019-a2ca4838-1839-4e55-9cf6-a49853e98d78.png" width="50%">

## 第五步 在line_notify.py中填入剛剛在line notify 申請的權杖
```XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX```

<img src="https://github.com/brianoy/EEW_line_notify/assets/24865458/a5bec1a2-00e1-488b-acc9-da80296dbc98" width="50%">

## 第六步 按自己的需求調整訊息傳送內容
<img src="https://github.com/brianoy/EEW_line_notify/assets/24865458/f4f8639e-a8fc-47cf-be41-d501b1fdb5fc" width="50%">


## 第七步 按下地牛wake up!中的測試按鍵
*建議先在自己的聊天室測試，免得嚇到朋友了*

<img src="https://github.com/brianoy/EEW_line_notify/assets/24865458/82ff5033-dc27-421b-82d2-10eccf5817ef" width="50%">
<img src="https://github.com/brianoy/EEW_line_notify/assets/24865458/f2059549-df99-4374-9258-e33c011c92b1" width="50%">


# 常見QA
1) 可不可以將bat和py檔案分在不同地方

> 不行，目前bat是用相對路徑寫的，請將兩個檔案維持在同一個資料夾

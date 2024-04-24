import requests
import sys
lineUrl = "https://notify-api.line.me/api/notify"
lineToken = "<你的權杖>"

try:
    magnitude = str(sys.argv[1]).replace("+","強").replace("-","弱")
    second = int(sys.argv[2])

    def lineWebhook(msg,token)->None:
        headers = { "Authorization": "Bearer " + token }
        data = { 'message': msg }
        requests.post(lineUrl,headers = headers, data = data)

    msg = "警告：XX地區預計震度" + str(magnitude) + "級地震\n預計到達時間:" + str(second) + "秒"
    
    lineWebhook(msg,lineToken)
    
except ModuleNotFoundError:
    print("=====錯誤:請確保request和sys module有被正確的安裝=====")
    
except IndexError:
    print("=====錯誤:請確保呼叫此程式時參數有正確的引數(規模和秒數)=====")


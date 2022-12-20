import requests
import sys
lineUrl = "https://notify-api.line.me/api/notify"
lineToken = "<line notify token>"

magnitude = str(sys.argv[1]).replace("+","強").replace("-","弱")
second = int(sys.argv[2])

def lineWebhook(msg,token)->None:
    headers = { "Authorization": "Bearer " + token }
    data = { 'message': msg }
    requests.post(lineUrl,headers = headers, data = data)

msg = "警告：地區預計震度" + magnitude + "級地震\n預計到達時間:" + second + "秒"

lineWebhook(msg,lineToken)



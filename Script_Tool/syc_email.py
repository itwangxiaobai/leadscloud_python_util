from sys import argv
import requests
import json
import time

"""
script, userId, userName, enterpriseId = argv
parameter = {"userId":{userId},"userName":"{userName}","enterpriseId":enterpriseId,"flag":"sended"}
rq = requests.put("http://test.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
data = rq.json()
print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
"""

prompt = '>>> '

print("Please Input 'userID', For Example>>>1400")
userId = input(prompt)
print("Please Input 'userName', For Example>>>yangdawei_10171")
userName = input(prompt)
print("Please Input 'enterpriseId', For Example>>>10171")
enterpriseId = input(prompt)
print(f"The Program is starting to syc {userId}--{enterpriseId}--{userName}'s email of outbox，and how much time is going to spend that's depends on how many emails in out box, Just wait...")
before_syc_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("current time is" + ' ' + before_syc_time)
parameter = {"userId":{userId},"userName":{userName},"enterpriseId":{enterpriseId},"flag":"sended"}
rq = requests.put("http://admin.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
data = rq.json()
print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
after_syc_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("current time is" + ' ' + after_syc_time)

input('Press Enter to exit program and then close this dialog....')




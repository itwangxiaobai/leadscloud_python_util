# -*- coding: utf-8 -*-
import threading
import requests
from time import ctime
import json



def syc_owen():
    """syc_owen"""

    print("Start synchronizing %s %s\n" % ("owen", ctime()))
    parameter = {"userId":"1263","userName":"13810078954","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_grace():
    """syc_grace"""

    print("Start synchronizing %s %s\n" % ("grace", ctime()))
    parameter = {"userId":"1294","userName":"13810327625","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_jsliang():
    """syc_jsliang"""
    
    print("Start synchronizing %s %s\n" % ("jsliang", ctime()))
    parameter = {"userId":"1223","userName":"18515934978","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_lucian():
    """syc_lucian"""
    print("Start synchronizing %s %s\n" % ("lucian", ctime()))
    parameter = {"userId":"1295","userName":"13911154792","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_jeanne():
    """syc_jeanne"""
    print("Start synchronizing %s %s\n" % ("jeanne", ctime()))
    parameter = {"userId":"1244","userName":"13810391489","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_leonard():
    """syc_leonard"""
    print("Start synchronizing %s %s\n" % ("leonard", ctime()))
    parameter = {"userId":"1278","userName":"18562278013","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_abby():
    """syc_abby"""
    print("Start synchronizing %s %s\n" % ("abby", ctime()))
    parameter = {"userId":"1272","userName":"18946126499","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_tilly():
    """syc_tilly"""
    print("Start synchronizing %s %s\n" % ("tilly", ctime()))
    parameter = {"userId":"1261","userName":"13810173051","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_chexinni():
    """syc_chexinni"""
    print("Start synchronizing %s %s\n" % ("chexinni", ctime()))
    parameter = {"userId":"1259","userName":"18363802567","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_kimi():
    """syc_kimi"""
    print("Start synchronizing %s %s\n" % ("kimi", ctime()))
    parameter = {"userId":"1446","userName":"17853556880","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_wangjun():
    """syc_wangjun"""
    print("Start synchronizing %s %s\n" % ("wangjun", ctime()))
    parameter = {"userId":"1297","userName":"13562503973","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_david():
    """syc_david"""
    print("Start synchronizing %s %s\n" % ("david", ctime()))
    parameter = {"userId":"1270","userName":"18853516269","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束")

def syc_steven():
    """syc_steven"""
    print("Start synchronizing %s %s\n" % ("steven", ctime()))
    parameter = {"userId":"1281","userName":"15210601805","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_Amy():
    """syc_Amy"""
    print("Start synchronizing %s %s\n" % ("Amy", ctime()))
    parameter = {"userId":"1283","userName":"13810589120","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_wendy():
    """syc_wendy"""
    print("Start synchronizing %s %s\n" % ("wendy", ctime()))
    parameter = {"userId":"1280","userName":"17854578765","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_Kayla():
    """syc_Kayla"""
    print("Start synchronizing %s %s\n" % ("Kayla", ctime()))
    parameter = {"userId":"1288","userName":"13810277804","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_wangjing():
    """同步own发件箱邮件"""
    print("Start synchronizing %s %s\n" % ("wangjing", ctime()))
    parameter = {"userId":"1443","userName":"15098587735","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")


def syc_cindy():
    """syc_cindy"""
    print("Start synchronizing %s %s\n" % ("cindy", ctime()))
    parameter = {"userId":"1285","userName":"13810326162","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_davidpan():
    """syc_davidpan"""
    print("Start synchronizing %s %s\n" % ("davidpan", ctime()))
    parameter = {"userId":"1447","userName":"13810377459","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_fabiana():
    """syc_fabiana"""
    print("Start synchronizing %s %s\n" % ("fabiana", ctime()))
    parameter = {"userId":"1248","userName":"13810123514","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_alice():
    """syc_alice"""
    print("Start synchronizing %s %s\n" % ("alice", ctime()))
    parameter = {"userId":"1284","userName":"13810384769","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_james():
    """syc_james"""
    print("Start synchronizing %s %s\n" % ("james", ctime()))
    parameter = {"userId":"1251","userName":"18853530636","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_helen():
    """syc_helen"""
    print("Start synchronizing %s %s\n" % ("helen", ctime()))
    parameter = {"userId":"1254","userName":"13810146431","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_yulia():
    """syc_yulia"""
    print("Start synchronizing %s %s\n" % ("yulia", ctime()))
    parameter = {"userId":"1246","userName":"13810330875","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束")

def syc_richard():
    """syc_richard"""
    print("Start synchronizing %s %s\n" % ("richard", ctime()))
    parameter = {"userId":"1262","userName":"13810268321","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_mila():
    """syc_mila"""
    print("Start synchronizing %s %s\n" % ("mila", ctime()))
    parameter = {"userId":"1243","userName":"13810384919","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_nina():
    """syc_nina"""
    print("Start synchronizing %s %s\n" % ("nina", ctime()))
    parameter = {"userId":"1282","userName":"13811692653","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_julie():
    """syc_julie"""
    print("Start synchronizing %s %s\n" % ("julie", ctime()))
    parameter = {"userId":"1296","userName":"18736093237","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_chenshiyuan():
    """syc_chenshiyuan"""
    print("Start synchronizing %s %s\n" % ("chenshiyuan", ctime()))
    parameter = {"userId":"1445","userName":"18562226988","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_pengshuai():
    """syc_pengshuai"""
    print("Start synchronizing %s %s\n" % ("pengshuai", ctime()))
    parameter = {"userId":"1450","userName":"18663858782","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_yolanda():
    """syc_yolanda"""
    print("Start synchronizing %s %s\n" % ("yolanda", ctime()))
    parameter = {"userId":"1252","userName":"13810401229","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")

def syc_francis():
    """syc_francis"""
    print("Start synchronizing %s %s\n" % ("francis", ctime()))
    parameter = {"userId":"1264","userName":"13810384609","enterpriseId":"10330","flag":"sended"}
    request_own = requests.put("https://admin-mail.leadscloud.com/mail/receiveSendedAndRubbishMail", data=parameter)
    data = request_own.json()
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False) )
    print("接口调用已经返回结果，本次同步结束\n")



syc_email_threads = []
owen_thread = threading.Thread(target=syc_owen)
syc_email_threads.append(owen_thread)

grace_thread = threading.Thread(target=syc_grace)
syc_email_threads.append(grace_thread)

jsliang_thread = threading.Thread(target=syc_jsliang)
syc_email_threads.append(jsliang_thread)

lucian_thread = threading.Thread(target=syc_lucian)
syc_email_threads.append(lucian_thread)

jeanne_thread = threading.Thread(target=syc_jeanne)
syc_email_threads.append(jeanne_thread)

leonard_thread = threading.Thread(target=syc_leonard)
syc_email_threads.append(leonard_thread)

abby_thread = threading.Thread(target=syc_abby)
syc_email_threads.append(abby_thread)

tilly_thread = threading.Thread(target=syc_tilly)
syc_email_threads.append(tilly_thread)

chexinni_thread = threading.Thread(target=syc_chexinni)
syc_email_threads.append(chexinni_thread)

kimi_thread = threading.Thread(target=syc_kimi)
syc_email_threads.append(kimi_thread)

wangjun_thread = threading.Thread(target=syc_wangjun)
syc_email_threads.append(wangjun_thread)

david_thread = threading.Thread(target=syc_david)
syc_email_threads.append(david_thread)

steven_thread = threading.Thread(target=syc_steven)
syc_email_threads.append(steven_thread)

Amy_thread = threading.Thread(target=syc_Amy)
syc_email_threads.append(Amy_thread)

wendy_thread = threading.Thread(target=syc_wendy)
syc_email_threads.append(wendy_thread)

Kayla_thread = threading.Thread(target=syc_Kayla)
syc_email_threads.append(Kayla_thread)

wangjing_thread = threading.Thread(target=syc_wangjing)
syc_email_threads.append(wangjing_thread)

cindy_thread = threading.Thread(target=syc_cindy)
syc_email_threads.append(cindy_thread)

davidpan_thread = threading.Thread(target=syc_davidpan)
syc_email_threads.append(davidpan_thread)

fabiana_thread = threading.Thread(target=syc_fabiana)
syc_email_threads.append(fabiana_thread)

alice_thread = threading.Thread(target=syc_alice)
syc_email_threads.append(alice_thread)

james_thread = threading.Thread(target=syc_james)
syc_email_threads.append(james_thread)

helen_thread = threading.Thread(target=syc_helen)
syc_email_threads.append(helen_thread)

yulia_thread = threading.Thread(target=syc_yulia)
syc_email_threads.append(yulia_thread)

richard_thread = threading.Thread(target=syc_richard)
syc_email_threads.append(richard_thread)

mila_thread = threading.Thread(target=syc_mila)
syc_email_threads.append(mila_thread)

nina_thread = threading.Thread(target=syc_nina)
syc_email_threads.append(nina_thread)

julie_thread = threading.Thread(target=syc_julie)
syc_email_threads.append(julie_thread)

chenshiyuan_thread = threading.Thread(target=syc_chenshiyuan)
syc_email_threads.append(chenshiyuan_thread)

pengshuai_thread = threading.Thread(target=syc_pengshuai)
syc_email_threads.append(pengshuai_thread)

yolanda_thread = threading.Thread(target=syc_yolanda)
syc_email_threads.append(yolanda_thread)

francis_thread = threading.Thread(target=syc_francis)
syc_email_threads.append(francis_thread)


if __name__ == '__main__':
    for threademail in syc_email_threads:
        threademail.start()
    for threademail in syc_email_threads:
        threademail.join()
    print("all invoking are finished")

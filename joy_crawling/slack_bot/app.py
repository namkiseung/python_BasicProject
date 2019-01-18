#-*- coding:utf-8 -*-
import json
from boannews_backend_api import * #보안기사 뉴스 가져오기
from flask import Flask, request, make_response, json
from slacker import Slacker
token = "[token]"
slack = Slacker(token)
app = Flask(__name__)
def get_answer():
    return "hihihihihi"
def get_news():
    news=""
    boannews_url_lists = [url_action, url_origin]
    for url_item in boannews_url_lists:
        slack.chat.post_message("#temp", str(get_obj_parserd(url_item).text));
    pass

#slack.chat.post_message("#temp", get_answer());
def event_handler(event_type, slack_event):
    if event_type == "app_mention":
        #슬랙앱을 호출한 위치 가져오기
        channel = slack_event["event"]["channel"]
        #사용자에게 응답할 텍스트 받아오자
        text = get_answer()
        #Slacker를 이용해 메시지를 해당채널로 보내자
        slack.chat.post_message(channel, text)
        print("channel: {}, text : {}".format(channel, text))
        return make_response("[+] This is app_mention", 200,  )
    message = "[%s] not found event_handler" % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})

@app.route('/slack', methods=['GET', 'POST'])
def hears():
    #slack api는 json으로 우리에게 보냄
    slack_event = json.loads(request.data)
    #우리서버가 정상인지 확인하기 위해 "challenge"에 대한 이벤트를 보내니까 이걸 처리하자.
    if "challenge" in slack_event:
        #그 challenge값을 그대로 슬랙에게 보내줘서 내가 정상이라고 말하자
        return make_response(slack_event["challenge"], 200,
                             {"content_type":"application/json"})
    #슬랙의 이벤트를 처리하자
    if "event" in slack_event:
        #event값이 존재하는 경우 type확인 우리는 app_mention으로 했다.
        event_type = slack_event["event"]["type"]
        #이벤트 헨들러 만들어서 type보내자 그러면 핸들이 가능
        return event_handler(event_type, slack_event)
    #이벤트 존재 안할떄는 오류를 띄우자(404)
    return make_response("not event at slack request by namki_bot", 404, {"X-Slack-No-Retry": 1})

@app.route('/', methods=['GET', 'POST']) #Routing Default
def index():    
    return "hello world"

if __name__ == '__main__':
    get_news()
    app.run(debug=True, host='0.0.0.0', port=1111)


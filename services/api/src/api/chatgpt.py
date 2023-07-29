from src import logger
import asyncio, requests
from aiohttp import ClientSession
from src.api.utils import exectimer
from threading import current_thread
from src.configs.colors import Colors 
from datetime import datetime, timezone,timedelta
from src.entities.chatgpt import ChatGPT, ChatGptSchema
from flask import Flask, request, jsonify, Blueprint, make_response, session
from dataclasses import make_dataclass, asdict
from enum import Enum
import json
# API-endpoint:  https://free.churchless.tech/v1/chat/completions
# API-key: BetterChatGPT
 # https://free.churchless.tech/v1/chat/completions
gptlogger = logger.create_logger('GptLogger')
better_chatgpt_api_endpoint = ' https://free.churchless.tech/v1/chat/completions'
api_key = 'BetterChatGPT'
headers = {'Content-Type':'application/json',
			'Authorization': f'Bearer {api_key}'}
model = "gpt-4"
chatgpt_blueprint = Blueprint('chatgpt', __name__)


messages = [{'role': "😀",'content': "😵"}]
data = {'model':model,'n':2,'messages':messages}

@chatgpt_blueprint.route('/api/gpt/ping',methods=['GET','POST'])
def pingpong():
	"""
		Endpoint to test health of gpt chat completions service
	"""
	response = 'P🔥SSED P😵NG '
	gptlogger.info(f'{Colors.LIGHT_GREEN}{200}-{response}{Colors.DEFAULT}')
	return jsonify('P🔥SSED P😵NG ')

@chatgpt_blueprint.route('/api/gpt/genchat',methods=['POST'])
@exectimer
def fetch_message():
	"""
		- Custom data models needed to process and serve request/response data
			text_response = make_dataclass('TextResponse',[('role',role),('sno',int,1),('text',str,''),('response',str,'')])
			text_response = make_dataclass('TextResponse',[('role',role),('sno',int,1),('text',str,''),('response',str,'')],namespace={'todict':lambda self:asdict(self,dict_factory=dict)})
			role = Enum('role','user assistant system',module=__name__,qualname=f'{__name__}.role')
			json_data = {'sno':1,'role':choice(role),'text':fake.text(100),'response':''}
			data = text_response(**json_data)


		Fetch a single message from message queue using aiohttp session 
		TODO track and save session messages history
		Endpoint receives request payload w format:
			{'sno':int,'role':str,'text':str,'resp':''}
		Convert request payload to required format:
			{
				"model":"gpt-3.5-turbo",
				"n":2,
				"messages":list[
							{"role":role,"content":"prompt str"},
							{"role":role,"content":"prompt str"},
							]
			}
		TODO 
			- from request.get_json()
				-> extract 'role','text'
				-> create message entry:
							{'role':role,'content':text}
				-> append to existing json data payload
			- (optional) from request.headers
				-> extract 'content-type','authorization api-key'
				-> OR use our own default headers
			- With updated headers & json payload data
				-> make post request to chat completinos endpoint
				-> wait for response from post request
			- With response from post request
				-> do response.json()
				-> use that result to create ChatGPT() object
			- From GPT() object
				-> extract response content:
						GPT().choices[0]['message']['content']
			- With response content
				-> recreate request format w updated response and role:
						{'sno':int,'role':'assistant','text':str,'response':content}
				-> return jsonify(response)
				-> DONE 😀
	"""
	role = Enum('role','user assistant system',module=__name__,qualname=f'{__name__}.role')
	text_response = make_dataclass('TextResponse',[('role',role),('sno',int,1),('text',str,''),('response',str,'')],namespace={'todict':lambda self:asdict(self,dict_factory=dict)})
	response = {'status':'failed'}
	try:
		# use default headers for now
		json_data = request.get_json()
		json_data = text_response(**json_data)
		message = {'role':role[json_data.role].name,
					'content':json_data.text}
		# if 'chathistory' in session: gptlogger.debug(f"current chathistory: {Colors.GREEN}{session['chathistory']}")
		session.update({'chathistory':{"model":model,"n":2,"messages":[message]}}) if 'chathistory' not in session else session['chathistory']['messages'].extend([message])
		session.modified = True
		json_payload = session['chathistory'] 
		gpt_response = requests.post(better_chatgpt_api_endpoint,headers=headers,json=json_payload)
		response_json =  gpt_response.json()
		gptlogger.debug(f'{Colors.YELLOW}response json: {response_json}{Colors.DEFAULT}')
		response_json = ChatGPT(response_json)
		response_content = response_json.choices[0]['message']['content']
		response_role = response_json.choices[0]['message']['role']
		response_message = {'role':role[response_role].name,'content':response_content}
		# json_payload['messages'].append(response_message)
		session['chathistory']['messages'].extend([response_message]) #json_payload
		session.modified = True
		json_data.response = response_content
		json_data.role = response_role
		response = json_data.todict()
		# gptlogger.debug(f'{Colors.LIGHT_PURPLE}{200}-{response}{Colors.DEFAULT}')
		if 'chathistory' in session: gptlogger.debug(f"{Colors.LIGHT_BLUE}fksession-ch - {json.dumps(session['chathistory'],indent=3)} {Colors.DEFAULT}")# else gptlogger.warning(f'fksession-ch - 😵')
		return jsonify(response)
	except Exception as e:
		gptlogger.error(f'{Colors.LIGHT_RED}ERROR - {type(e).__name__}{Colors.RED}{e}{Colors.DEFAULT}')
		return jsonify(response), 500
	raise NotImplementedError('TODO fetch a message from messages storage(mock)\
								 to feed ChatGpt for priming response 😵')

@chatgpt_blueprint.route('/api/session/test',methods=['GET','POST'])
def test_flask_session():
	role = Enum('role','user assistant system',module=__name__,qualname=f'{__name__}.role')
	text_response = make_dataclass('TextResponse',[('role',role),('sno',int,1),('text',str,''),('response',str,'')],namespace={'todict':lambda self:asdict(self,dict_factory=dict)})
	if request.method == 'POST':
		json_data = request.get_json()
		json_data = text_response(**json_data)
		message = {'role':role[json_data.role].name,
					'content':json_data.text}
		# session['persistent_data'] = 'testing persistence'
		session.update({'test_chathistory':{"model":model,"n":2,"messages":[message]}}) if 'test_chathistory' not in session else session['test_chathistory']['messages'].extend([message])
		session.modified = True
	response = session['test_chathistory'] if 'test_chathistory' in session else 'no chathistory yet - do post first'
	return jsonify(response)

@chatgpt_blueprint.route('/api/gpt/session/history',methods=['GET','POST'])
def get_session_history():
	response = {'message':'session has no saved test_chathistory'}
	if 'test_chathistory' in session:
		response = session['test_chathistory']
		return response
	return response

@chatgpt_blueprint.route('/api/gpt/completions/test', methods=['POST'])
@exectimer
def test_gpt_post():
	"""
		Endpoint to test requesting completions response
	"""
	response = {'status':'failed'}
	data =  {"model": model,
			"messages": [{"role": "user", "content": "Hello, how are you?"}]}
	json_data = request.get_json()
	try:
		gpt_response = requests.post(better_chatgpt_api_endpoint,headers=headers,json=json_data)
		response_json =  gpt_response.json()
		gptlogger.debug(f'{Colors.LIGHT_GREEN}response_json - {response_json}{Colors.DEFAULT}')
		gptobj = ChatGPT(response_json)
		gptlogger.debug(f'{Colors.LIGHT_GREEN}ChatGpt Object - {gptobj}{Colors.DEFAULT}')
		# gptobj.choices[0].index("content") + 11 # beginning of message content
		# gptobj.choices[0].index("'},") # ending of message content
		content = gptobj.choices[0]['message']['content']#, gptobj.choices[0].index("'},")
		# logger.debug("Message - {}".format(gptobj.choices[0][start:end]))
		gptlogger.debug("{}Message - \n{}{}".format(Colors.LIGHT_GREEN,content,Colors.DEFAULT))

		response['status'] = 'success'
		response['completion'] = gpt_response.json()
		response['response'] = content
		gptlogger.debug(f'{Colors.LIGHT_GREEN}response - {response}{Colors.DEFAULT}')
		# logger.debug(gpt)
		return jsonify(response), 200
	except requests.exceptions.HTTPError as e:
		gptlogger.error(f'{Colors.LIGHT_RED}ERROR - {e}{Colors.DEFAULT}')
		return jsonify(response), 500


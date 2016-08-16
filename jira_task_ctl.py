#!/usr/bin/env python

from jira import JIRA
import json

class Connect:
	def __init__(self,cfile='jira_connect.conf' ):
		cfg_file = open(cfile, 'r')
		self.connect_attr = cfg_file.readlines()
				
	def start(self):
		for attr in self.connect_attr:
			exec attr
		jira = JIRA(url, basic_auth=(username, password))
		return jira

class Consultar_status:
	def __init__(self, jira_issue_key):
		self.jira_server = Connect().start()
		self.s_jira_issue_key = str(jira_issue_key)

	def consultar(self):
		dict_jira_issue = json.loads(json.dumps(self.jira_server.issue(self.s_jira_issue_key).raw))
		return dict_jira_issue['fields']['status']['name']


class Change:
	def __init__(self, jira_issue_key):
		self.jira_server = Connect().start()
		s_jira_issue_key = str(jira_issue_key)
		self.issue = jira_server.issue(s_jira_issue_key)
			
	def to_done(self):
		
		self.jira_server.transitions_issue(self.issue, 'Done')
	
	def to_progress(self):
		self.jira_server.transitions_issue(self.issue, 'In Progress')
	
	def to_to_do(self):
		self.jira_server.transitions_issue(self.issue, 'To Do')

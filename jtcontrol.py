#!/usr/bin/env python
import jira_task_ctl
from sys import argv


get_status(issue_key){
	s_issue_key = str(issue_key)
	jira_issue = jira_task_ctl.Consultar_status(s_issue_key)
	issue_status = jira_issue.consultar()
	return issue_status
}

set_status(issue_key



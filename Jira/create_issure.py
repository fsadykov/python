from jira import JIRA
import google.auth
import re

option = {'server': 'https://acirrustech.atlassian.net/rest/api/2'}

jira = JIRA(options=option, auth=('sadykovfarkhod@gmail.com', '@zq#NFxr2UXZ'))

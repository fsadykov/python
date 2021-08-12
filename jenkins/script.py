import jenkins

server = jenkins.Jenkins('http://142.93.255.138:8080', username='farkhodsadykov', password='Redhat2018**')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

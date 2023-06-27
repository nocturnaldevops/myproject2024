import jenkins
server = jenkins.Jenkins('http://3.95.203.100:8080/', username='prashanth', password='prashanth')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
#server.create_job('Likhitha', jenkins.EMPTY_CONFIG_XML)
#jobs = server.get_jobs()
#print(jobs)
server.build_job('Likhitha')
jobs = server.get_jobs()
server.copy_job('Likhitha', 'likhitha_copy')
print(jobs)

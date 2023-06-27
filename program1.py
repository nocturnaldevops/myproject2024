import jenkins

server = jenkins.Jenkins('http://34.207.162.255:8080/', username='prashanth', password='prashanth')
#user = server.get_whoami()
#version = server.get_version()
#print('Hello %s from Jenkins %s' % (user['fullName'], version))
#server.create_job('project1', jenkins.EMPTY_CONFIG_XML)
#jobs = server.get_jobs()
#print(jobs)
server.build_job('project1')
#my_job = server.get_job_config('cool-job')
#print(my_job) # prints XML configuration
#server.delete_job('empty')


#server.delete_job('empty_copy')
#server.build_job('empty')
#server.disable_job('empty')
#server.copy_job('empty', 'empty_copy')
#server.enable_job('empty_copy')
#server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)


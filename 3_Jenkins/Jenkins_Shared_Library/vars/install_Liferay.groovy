def call (Map config = [:]){
	def file = new File(pwd+'/workspace/'+JOB_NAME+'/2_Ansible/host_vars/web_server.yaml')
	def new_web_serverConf = file.text.replace('web_server_ip_address',config.web_server_ip_address)
    	file.text = new_web_serverConf
	ansiblePlaybook become: true, 
		disableHostKeyChecking: true, 
		installation: 'Ansible',
		inventory: 'Ansible_for_Jenkins/hosts', 
		playbook: 'Ansible_for_Jenkins/InstallLifeRay.yml'
}

def call (Map config = [:]){
	def file = new File('${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml')
	def newConfig = file.text.replace('db_ip_address', '${config.db_ip_address}').replace('pgsql_db_name', '${config.pgsql_db_name}').replace('db_ssh_pass', '${config.db_ssh_pass}')
    	file.text = newConfig
	ansiblePlaybook disableHostKeyChecking: true, 
		installation: 'Ansible', 
		inventory: 'Ansible_for_Jenkins/hosts', 
		playbook: 'Ansible_for_Jenkins/InstallPostgres13.yml'
}

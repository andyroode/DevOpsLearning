def call (Map config = [:]){
	def file = new File(pwd+'/workspace/'+JOB_NAME+'/2_Ansible/host_vars/db_server.yaml')
	def new_db_serverConf = file.text.replace('db_ip_address',config.db_ip_address).
		replace('pgsql_db_name', config.pgsql_db_name).
		replace('db_ssh_pass', config.db_ssh_pass)
    	file.text = new_db_serverConf
	ansiblePlaybook disableHostKeyChecking: true, 
		installation: 'Ansible', 
		inventory: '2_Ansible/hosts', 
		playbook: '2_Ansible/InstallPostgres13.yml'
}

def call (Map config = [:]){
	sh "sed -i 's/db_ip_address/$config.db_ip_address/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
	sh "sed -i 's/pgsql_db_name/$config.pgsql_db_name/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
	ansiblePlaybook installation: 'Ansible', inventory: 'Ansible_for_Jenkins/hosts', playbook: 'Ansible_for_Jenkins/InstallPostgres13.yml', vaultCredentialsId: 'ansible_vault_pass'
}

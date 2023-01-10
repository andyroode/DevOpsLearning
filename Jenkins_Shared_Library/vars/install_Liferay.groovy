def call (Map config = [:]){
	sh "sed 's/web_server_ip_address/${config.web_server_ip_address}/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/web_server.yaml"
	sh "sed 's/web_server_ssh_user/${config.web_server_ssh_user}/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/web_server.yaml"
	sh "sed 's/db_ssh_pass/${config.db_ssh_pass}/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/web_server.yaml"
	sh "sed 's/db_sudo_pass/${config.db_sudo_pass}/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/web_server.yaml"
	ansiblePlaybook installation: 'Ansible', inventory: 'Ansible_for_Jenkins/hosts', playbook: 'Ansible_for_Jenkins/InstallLifeRay.yml'
}
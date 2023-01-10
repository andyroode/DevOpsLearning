def call (Map config = [:]){
	sh "sed -i 's/web_server_ip_address/$config.web_server_ip_address/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/web_server.yaml"
	sh "sed -i 's/liferay_ssh_user_pass/$config.liferay_ssh_user_pass/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/web_server.yaml"
	ansiblePlaybook installation: 'Ansible', inventory: 'Ansible_for_Jenkins/hosts', playbook: 'Ansible_for_Jenkins/InstallLifeRay.yml'
}

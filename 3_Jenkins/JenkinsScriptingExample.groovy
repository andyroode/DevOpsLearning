node {
    stage('Download Ansible repo') {
        git 'https://github.com/andyroode/DevOpsLearning.git'
        sh "ls -la"
    }
    stage('Install PostgreSQL-13') {
        sh "sed -i 's/db_ip_address/$db_ip_address/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
        sh "sed -i 's/pgsql_db_name/$pgsql_db_name/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
        sh "sed -i 's/db_ssh_pass/$db_ssh_pass/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
        ansiblePlaybook disableHostKeyChecking: true, installation: 'Ansible', inventory: 'Ansible_for_Jenkins/hosts', playbook: 'Ansible_for_Jenkins/InstallPostgres13.yml'
    }
    
}
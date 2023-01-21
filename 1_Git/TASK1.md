# TASK1

1. Завести аккаунт на gitlab/github
    * https://git.netcracker.com/anru0718

2. Создать новый удалённый репозиторий
    * https://git.netcracker.com/anru0718/devopslearn

3. Установить Git на локальную машину
    * git config --global user.name = "Andrei Rudchenko"
    * git config --global user.email "andy-roode@yandex.ru"
    * cat $USERPROFILE/.gitconfig
        + [user]
            name = Andrei Rudchenko
            email = andy-roode@yandex.ru

4. Инициализировать локальный репозиторий
    * git init
        + Initialized empty Git repository in C:/git/homework/.git/

5. Связать локальный репозиторий с удалённым
    * Делал коннект по SSH
        + git remote add origin git@git.netcracker.com:anru0718/devopslearn.git
        + cd ~/.ssh
        + ssh-keygen
            - Generating public/private rsa key pair.
            - Enter file in which to save the key (/c/Users/anru0718/.ssh/id_rsa):
            - /c/Users/anru0718/.ssh/id_rsa already exists.
            - Overwrite (y/n)? y
            - Enter passphrase (empty for no passphrase):
            - Enter same passphrase again:
            - Your identification has been saved in /c/Users/anru0718/.ssh/id_rsa
            - Your public key has been saved in /c/Users/anru0718/.ssh/id_rsa.pub
            - The key fingerprint is:
            - SHA256:ki6ZwWPYwW4o5mU39AOcjUWq1nTzVgteQDoYLgZboRs anru0718@WS-9701
        + cat id_rsa.pub
        + Копируем полученное значение в https://git.netcracker.com/-/profile/keys/
        + Авторизация по SSH: ssh -T git@git.netcracker.com
            - The authenticity of host 'git.netcracker.com (10.112.3.90)' can't be established.
            - ED25519 key fingerprint is SHA256:Fgsb+vsPn/3WbCB7tuxU7yhvMPeEKm/IpXel72kl2Zw.
            - This key is not known by any other names
            - Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
            - Warning: Permanently added 'git.netcracker.com' (ED25519) to the list of known hosts.
            - Welcome to GitLab, @anru0718!

6. Описать ранее проделанные шаги в виде TASK1.MD файла с указанием выполненных команд.
    * Смотреть выше.

7. Закоммитить файл в локальный репозиторий
    * git status
    * git add TASK1.md
    * git commit -m "TASK1.md commit"
    * git log
        + commit a8c75569da0f0a40f5464aac3928b829d8e9a576 (HEAD -> master)

8. Сделать push в удалённый репозиторий. Зайти на страницу репозитория GitLab/GitHub, убедиться в появлении изменений.
    * git push --set-upstream origin master
        + Здесь возникла трудность из-за initial коммита файла README.md при создании репозитория.
        + ! [rejected]        master -> master (fetch first)
        + error: failed to push some refs to 'git.netcracker.com:anru0718/devopslearn.git'
        + hint: Updates were rejected because the remote contains work that you do
        + hint: not have locally. This is usually caused by another repository pushing
        + hint: to the same ref. You may want to first integrate the remote changes
        + hint: (e.g., 'git pull ...') before pushing again.
        + hint: See the 'Note about fast-forwards' in 'git push --help' for details.
        + Данную проблему я обошёл, используя команду git pull origin master --allow-unrelated-histories
    * git pull origin master --allow-unrelated-histories
    * git status
        + Your branch is ahead of 'origin/master' by 2 commits.
    * git push
        + To git.netcracker.com:anru0718/devopslearn.git
        + 6b5a628..614faa6  master -> master

9. Дописать шаги 7-8 в файл TASK1.MD

# Задание успешно выполнено!:)

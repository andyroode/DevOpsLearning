# TASK2

1. Шаги 10-12 из TASK1.md описать в новом файле TASK2.md
    * git diff
        + Здесь мы видим изменения, добавленные в TASK1.md шагами 7-8.
    * git status
        + Changes not staged for commit:
        + modified:   TASK1.md
    * git add TASK1.md
    * git commit -m "Updated TASK1.md"
        + commit 0fb4a3ddbb194eb2617fe5e6e1f3afcaee4c0f9d (HEAD -> master, origin/master)
    * git push
        + https://git.netcracker.com/anru0718/devopslearn/-/commit/0fb4a3ddbb194eb2617fe5e6e1f3afcaee4c0f9d

2. Отвести бранч develop, в который залить файл TASK2.MD. Локально и удалённо.
    * git branch develop
    * git switch develop
    * git status
    * git add TASK2.md
    * git commit -m "Created branch develop and added TASK2.md"
    * git push --set-upstream origin develop

3. Добавить в конец файла TASK1.md строчку "Задание успешно выполнено!:)". Залить изменения локально и удалённо.
    * git status
        + modified:   TASK1.md
    * git add TASK1.md
    * git commit -m "Updated TASK1 with phrase, uploading to develop branch"
    * git push

4. Переключиться назад на основной бранч.
    * git switch master

5. Добавить в конец файла TASK1.MD строчку "Задания провалено!:(". Залить изменения локально и удалённо.
    * git status
        + modified:   TASK1.md
    * git add TASK1.md
    * git commit -m "Updated the TASK1.md with new row, added to master branch"
    * git push

6. Выполнить мерж из ветки develop в основную ветку. Разрешить конфликт в пользу основной ветки.
    * git merge develop
        + Auto-merging TASK1.md
        + CONFLICT (content): Merge conflict in TASK1.md
        + Automatic merge failed; fix conflicts and then commit the result. 
            - git status
            - Unmerged paths:
            - both modified:   TASK1.md
            - <<<<<<< HEAD
            - # Задание провалено!:(
            - =======
            - # Задание успешно выполнено!:)
            - >>>>>>> develop
            - Оставил в TASK1.md "Задание успешно выполнено!"
    * git add TASK1.md
    * git commit -m "Resolved the merge conflict from develop to master"
    * git push

7. Посмотреть лог проделанных изменений.
    * git log
        + commit 15b16397eb43385f476d26882f6da1690670fa80 (HEAD -> master, origin/master)
        + Merge: 7c4786a ddc6b18
        + Author: = <andy-roode@yandex.ru>
        + Date:   Wed Dec 7 20:03:31 2022 +0300

        +   Resolved the merge conflict from develop to master

        + commit 7c4786af6d253e5d867cdaafaea3cfc4fe2f8fe6
        + Author: = <andy-roode@yandex.ru>
        + Date:   Wed Dec 7 19:48:26 2022 +0300

        +   Updated the TASK1.md with new row, added to master branch

        + commit ddc6b18dd1914016435162b2734039361ff37311 (origin/develop, develop)
        + Author: = <andy-roode@yandex.ru>
        + Date:   Wed Dec 7 19:44:53 2022 +0300

        +   Updated TASK1 with phrase, uploading to develop branch
         
8. Описать проделанные упражнения в TASK2.md

9. Прислать ссылку на репозиторий.
    * https://git.netcracker.com/anru0718/devopslearn

# PS Я буду делать задание 3.
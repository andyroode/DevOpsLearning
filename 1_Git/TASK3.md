# TASK3

1. Изучить команду git stash
    * Stash переводится как Тайник. Таким образом эта команда и призвана "прятать" изменения.
    * Это необходимо для того, чтобы:
        - Избавиться от ненужных/неправильных изменений в коде (временно).
        - При переключении на ветку через git checkout вылетит ошибка, что нужно сначала закоммитить изменения. Команда git stash "спрячет" изменения и мы сможем перейти на другую ветку.
        - Если мы работаем на ветке мастер, и добавили изменения в Staging, то при переходе на ветку через git switch изменения так и останутся в Staging. А нам это не нужно, так как мы на другой ветке и этот коммит не касается текущей ветки.

2. Переключиться на бранч master.
    * git switch master

3. Изменить TASK2.md, дописав в него "PS Я буду делать задание 3".
    * git status
        - modified:   TASK2.md

4. Добавить изменения в Staging.
    * git add TASK2.md
        - Changes to be committed:
        - modified:   TASK2.md

5. Вызвать git stash
    * git stash
        - Saved working directory and index state WIP on master: 3b5122c Merge branch 'develop'

6. Вызвать git stash list и git status
    * git stash list
        - stash@{0}: WIP on master: 3b5122c Merge branch 'develop'
    * git status
        - Untracked files:
        - nothing added to commit but untracked files present (use "git add" to track)

7. Переключиться на ветку develop
    * git switch develop

8. Убедиться, что файл TASK3.md не содержит изменений.
    * git status
        - On branch develop
        - Your branch is up to date with 'origin/develop'.

        - Untracked files:
        - (use "git add <file>..." to include in what will be committed)
        - TASK3.md

        - nothing added to commit but untracked files present (use "git add" to track)

9. Добавить файл TASK3.md с описанием проделанной работы.

10. Закоммитить изменения
    * git add .
    * git commit -m "Adding TASK3 under develop branch"
    * git push

11. Переключиться на master.
    * git switch master

12. Вернуть stash изменения TASK2.md назад
    * git stash pop
        - Dropped refs/stash@{0} (3ea69283081dc65910d9ef144d36a421a7af0092)

13. Закоммитить изменения.
    * git add .
    * git commit -m "Returned the TASK2.md from stash"
    * git push

14. Смержить develop в master.
    * git merge develop
    * git push

15. Дописать в TASK3.md проделанные шаги.




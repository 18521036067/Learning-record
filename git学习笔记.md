# git入门

[参考官方文档](https://git-scm.com/book/zh/v1/Git-%E5%9F%BA%E7%A1%80)

## 1.本地仓库

查看git配置信息：git config --list

更改git作者名和email：`git config user.name` / `git config user.email `

1.git init

初始化

2.git add  *.py

开始跟踪文件或者将modified提交到暂存区

注意：.gitignore文件也需要跟踪

3.git status

查看当前目录文件状态

未跟踪(untracked)<-------->未修改(unmodified)<-------->已修改(modified)<-------->已暂存(staged)

4.git diff

查看已修改(尚未暂存)文件的修改

`--staged` (旧版为`--cached`) 查看已暂存文件的修改内容

5.git commit 

提交所有已暂存文件的快照

`-m` 不打开编辑器(默认vim)直接在同一行后跟参数写入提交说明 e.g: *$* git commit -m "First commit"

`-a`同时提交所有已暂存和已修改的文件快照(相当于对modified自动执行git add)

6.git rm

移除跟踪文件(并从目录删除文件)

如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项`-f`（译注：即 force 的首字母），以防误删除文件后丢失修改的内容。

`git rm --cached`从跟踪清单删除但不删除文件

7.git mv

要在 Git 中对文件改名，可以这么做：`git mv file_from file_to`

8.git log

查看提交历史。参数非常多，下面仅为常用参数

`-p`显示文件修改

`--stat`仅显示行数变化

`-2`显示最近2次更新

9.git commit --amend

重新上次提交(用于修改提交内容和提交说明)

```git
$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend
```

上面的三条命令最终只是产生一个提交，第二个提交命令修正了第一个的提交内容。

10.git reset

`git reset file`取消暂存(staged->modified)

11.git checkout 

`git checkout file`取消修改(回退modified的修改到unmodified)

12.总结

                                       ----文件修改---->                                    ----git add---->

未修改(unmodified)                                   已修改(modified)                            已暂存(staged)

                                   <----git checkout----                                <----git reset----

## 2.分支

`git branch`查看所有本地分支

`git branch -r`查看远程所有分支

`git branch -a`查看所有分支包括远程分支

### 2.1本地分支操作

1.git branch xxx

新建分支

2.git checkout xxx

切换当前分支

3.git checkout -b xxx

新建分支并切换，等同于：

```git
git branch xxx
git checkout xxx
```

4.git branch -d xxx删除分支

> 以上均为本地分支操作，新建分支后要将分支推送(需要权限)，删除分支后也是本地删除

### 2.2远程分支操作

clone远程仓库时，若不带参数默认clone所有远程分支，但本地只会创建一个默认的master分支跟踪远程origin/master分支。因此在clone后直接使用master就可以pull。

1.git branch 分支名 远程名/分支名

`git branch newbranch origin/newbranch`创建一个newbranch分支跟踪origin/newbranch分支，若newbranch缺省则自动创建名为origin/newbranch的同名分支来跟踪远程分支(注意是包含远程仓库名origin的同名分支)

2.git checkout -b 分支名 远程名/分支名

创建并切换分支来跟踪远程分支，其原理和本地的`git checkout -b xxx`类似

另外，新版本支持`git checkout --track origin/newbranch`自动创建无远程仓库名的同名分支来跟踪远程分支(无origin/前缀)

3.git push/pull 远程仓库名 本地分支 远程分支

将本地分支推送到远程分支上(如果本地分支不是远程分支的推进版本则需要先pull或者fetch+merge处理冲突)

如果是通过上述跟踪远程分支名建立的本地分支，直接push或者pull不带任何参数便可以对应远程分支

`git push 远程仓库名 本地分支名`在远程仓库建立新分支

`git push 远程仓库名 本地分支名 远程仓库名`==`git push 远程仓库名 本地分支名:远程分支名`

4.git push 远程仓库名 :远程分支名

删除远程分支(参考上一条，可以把它理解为：如果省略`[本地分支]`，那就等于是在说“在这里提取空白然后把它变成`[远程分支]`”。)

### 2.3变基

> 注意：**一旦分支中的提交对象发布到公共仓库，就千万不要对该分支进行变基操作。**
> 
> 既只能在本地分支变基操作并最终将变基结果推送到远程仓库，推送之后不可以对已推送commit进行任何变基操作

把一个分支中的修改整合到另一个分支的办法有两种：`merge`和`rebase`

## 3.版本回滚

此处为简单梳理。详细内容参考官方文档[重置揭秘](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E7%BD%AE%E6%8F%AD%E5%AF%86)章节，叙述非常形象具体。

1.git reset HEAD~

`HEAD^`==`HEAD~`,`HEAD^^`==`HEAD~2`

此系列命令共有三个模式选项

`git reset --soft HEAD~`

`git reset --mixed HEAD~`      缺省参数则默认--mixed

`git reset --hard HEAD~`        有数据丢失危险



> `--soft`仅HEAD指针回退到父结点，不改变Index区(staged)和工作区(modified)的内容，重新`commit`后回到原HEAD版本；
> 
> `--mixed`HEAD指针回退到父结点，并随后相应回退Index区内容(staged)，不改变工作区(modified)的内容，重新`add`后回到原HEAD版本；
> 
> `--soft`HEAD指针回退到父结点，随后相应回退Index区(staged)和工作区(modified)的内容，丢失全部内容，不可撤销，回不到HEAD版本；
> 
> 假设当前版本无已修改和已暂存文件。执行`--soft`后，当前版本(HEAD)回滚到上个版本，但是索引和工作区的内容依然存在，既HEAD和HEAD~版本之间做的修改都变为暂存，需要重新commit以从HEAD~版本fast forward到HEAD版本；
> 
> 若要继续回退，可以使用`git reset filename`或者`git reset .`取消某个文件或所有文件暂存，此时的状态相当于执行了`--mixed`；再使用`git checkout filename`或者`git checkout .`取消某个文件的修改(危险，会丢失内容)，此时相当于`--hard`。

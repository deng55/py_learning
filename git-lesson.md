# git

* git add readme.txt
* git commit -m "comment"
* git diff readme.txt

---

* git log  /  git log --pretty=oneline 
* git reset --hard HEAD^ 回退到上一个版本  同理 HEAD^^ 上上个版本
* 在当前窗口没有关闭的情况下  git reset --hard 87cd3c 可以回到最新版本
* 如果忘记了commit id 可以使用 git reflog 查看之前提交的记录

---

* `HEAD`指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令`git reset --hard commit_id`。
* 穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本。
* 要重返未来，用`git reflog`查看命令历史，以便确定要回到未来的哪个版本。 

---

**暂存区**   stage -master

撤销更改  

已编辑 git checkout -- fileName

 如果已提交到stage  git reset HEAD fileName

如果已经commit  第一步 回退版本  git reset --hard xxx

创建ssh key  `ssh-keygen -t rsa -C "youremail@example.com"`

` git remote add origin git@github.com:deng55/learngit.git`  deng55 是github的用户名

把本地的仓库关联到github，使用上面的命令

`git push -u origin master` 推送到远程库

由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送的远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令。

从现在起，只要本地作了提交，就可以通过命令：

```
$ git push origin master
```

git clone 有ssh 和http协议 ssh速度快

---

查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git checkout <name>`

创建+切换分支：`git checkout -b <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`





合并分支时，加上`--no-ff`参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而`fast forward`合并就看不出来曾经做过合并。



---

## bug 分支


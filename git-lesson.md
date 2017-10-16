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


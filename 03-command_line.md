# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1 cd .. - parent directory, 2 rm -rf - remove recursively, 3 rm - remove individual file, rmdir - remove individual directory (if empty), 4 mkdir - make new directory, 5 cp [destination] - copy file to destination, 6 touch - create a file, 7 find -name "*.X" - finds all files in directory/subdirs ending in ".X", 8 cat > file_name.txt - write input to file (use ctrl-D to submit), 9 apropos - finds commands, 10 info [command] - tells you what functions/commands do

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`
`ls -a`
`ls -l`
`ls -lh`
`ls -lah`
`ls -t`
`ls -Glp`

> > `ls`  list files/folders in current directory
`ls -a`  list all (including hidden) files/folders in current dir
`ls -l`  list files/folders long format
`ls -lh`  list files/folders slightly less long format
`ls -lah`  list all files/folders slightly less long format
`ls -t`  sort by newest (modified) first
`ls -Glp`  list files/folders without group names, long format, include / at end of subdirs.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls1 easy to see, -d only directories, -m could be useful to write > to a csv, -rm could be useful for same reason, -R displays subdirs as well

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs takes input from stdin and performs a command (argument, default echo) on it. So can be used in combo with | to pipe say `find -name "*.txt" | xargs rm` which will find all txt files in a directory and delete them.

 


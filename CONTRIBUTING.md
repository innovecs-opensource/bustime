You want to help? Great!

For developers
--------------

First you must clone this repository so that you can work on this project
locally.

    $ cd ~/
    $ git clone git@github.com:innovecs-opensource/bustime.git
    $ cd bustime
    $ git status
      > You should get a message that you are on master branch.

The master branch will be the pristine branch. If you want to add something or
modify in this project, then you must create a new feature branch. All work
by developers will be done in individual branches, and then merged to master.

    $ git checkout -b my_branch_name

Work on your code. When you are ready, add all of your changes, commit, and
push to GitHub.

    $ cd ~/bustime
    $ git add .
    $ git commit -m "A description for your commit."

Merging branches should be done in the form of a Pull Request. So, if you go
to [bustime](https://github.com/innovecs-opensource/bustime) repository on
GitHub, switch to your branch, you will be able to issue a pull request.

Pull requests are very important because it lets people to collaborate in code
development, and also notifies other developers of what changes are introduced.
Everyone who wants can comment on your changes. All communication regarding
a feature branch is node in one place.

Ideally, each pull request should have at least one reviewer. If possible,
assign as a reviewer a person that is competent in the area of code that your
pull request deals with. For example, for front-end changes a front-end
developer should be assigned. However, it is not always clear who should be
assigned for a particular pull request. In this case feel free to assign
[valera-rozuvan](https://github.com/valera-rozuvan).

Once all concerning developers are happy with a particular pull request, it can
be safely merged. There is a button at the bottom of each pull request page,
that is labeled "Merge".

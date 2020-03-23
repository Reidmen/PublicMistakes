# Command flow to process git repository

## Set default origin on github

`repository_name`: repository, `user_name`: github user...
* cd reposity_name/
* git remote rm origin
* git remote add origin https://github.com/user_name/repository_name.git

## Add, commit and push modifications to the origin (or branch)

* git add .
* git commit -m "commit message!"
* git push -u origin branch
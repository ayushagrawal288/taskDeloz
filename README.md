Github provides apis for accessing public repos, using these apis we can fetch any data regarding the public apis.
 
## Prerequisite  
You need to generate an personal access token from github link: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/  
And paste the token in both the files token variable in place of 'Your token'.
```
token = 'Your token'
replace
```
You have two tasks
* Create an api using any framework that you know or aware of, which can fetch top 20 public repos queried on "django" and sorted according to stars of that repo.  
* Sort the libraries fetched from 'requirements.txt' or 'requirements-dev.txt' according to the number of occurrences in the repos listed in the above result.

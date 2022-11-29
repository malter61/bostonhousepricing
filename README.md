# bostonhousepricing

### Software and Tools Requirements
1. [Github Account](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com)
3. [HerokuAccount](https://heroku.com)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment

'''
conda create -p venv python==3.7 -y
conda activate venv/ 

python3.7 -m venv .venv
source .venv/bin/activate
pip install wheel
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt

git config --global user.name "Mark Malter"
git config --global user.email "malter61@gmail.com"
'''

open postman and enter input values as json
validate json with json validator
hit "send" to get prediction

if error OSError: [Errno 48] Address already in use
type ps -a      this will gett all running processes
type kill -9 PID, where PID is the process number, e.g.,
kill -9 51181

go to heroku and create an app
connect to github and to your repo

click "Enable Automatic Deploys" if in production
deploy branch

Build docker file
create /.github/workflows directory
create main.yaml file in workflows dir


update yaml file with secrets

go to github 
click settings
click secrets
click actions
click new repository secret
type in HEROKU_API_KEY  and get the key from heroku under settings
type in HEROKU_EMAIL and type your email address
type in HEROKU_APP_NAME and type the name you gave the heroku app

=== Fetching app code........
=!= Your app does not include a heroku.yml build manifest. To deploy your app, either create a heroku.yml: https://devcenter.heroku.com/articles/build-docker-images-heroku-yml
Or switch back to buildpack-based deploys: https://devcenter.heroku.com/articles/container-registry-and-runtime#changing-deployment-method



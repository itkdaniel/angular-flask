
# Running Jenkins docker service

## Automated test integration with pytest

Run `docker-compose -f docker-compose-jenkins.yml up`

Open **http://localhost:8080/** in your browser to see the Unlock Jenkins page. Copy the password from 
`docker-compose exec -it jenkins cat var/jenkins_home/secrets/initialAdminPassword` 
and install suggested plugins. Create an admin user by filling in the details and keep the default URL. ‘Save and Finish’ and ‘Start Using Jenkins’.

Click on create new jobs to create a new freestyle project of any name. Under the General tab, you can mention the description for your project and specify the GitHub Project URL.

In Source Code Management tab, click on Git and add the repository URL. Enter the credentials by selecting Add->Jenkins and specifying the username and password of your Git account. This step will copy the repository **angular-flask** from the specified GitHub URL into /var/jenkins_home/workspace thereby creating the workspace inside our python-test-calculator directory.

Under Build tab, click on Add build step->Execute shell and copy the following:

```
  echo "Check current working directory"
  pwd
  echo "Starting all services"
  docker compose -f docker-compose.yml up -d
  docker compose exec api pytest -v src/test --junitxml=reports/result.xml
  echo "Copy result.xml into Jenkins container"
  rm -rf reports
  mkdir reports
  docker cp angular-flask-api-1:/api/reports/result.xml reports/
  echo "Cleanup"
  docker compose down
  /bin/sh scripts/docker-down.sh
```

In Post-Build Actions tab, we specify the location in workspace of the copied result.xml for publishing. Ensure that JUnit plugin is installed on Jenkins. Save the project configuration.

Click on Build Now in your project to see the magic.

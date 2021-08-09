# optimiserApp

This is an example on how to use the glpk solver in an application to be deployed in heroku. It runs the solver for a small instance of the knapsack problem

The file [Procfile](https://raw.githubusercontent.com/endorgobio/optimiserApp/master/Procfile) specifies the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, including Your app’s web server. [details](https://devcenter.heroku.com/articles/procfile)

The file [runtime](https://raw.githubusercontent.com/endorgobio/optimiserApp/master/runtime.txt) specifies the python version to be run.

The file [requirements.txt](https://raw.githubusercontent.com/endorgobio/optimiserApp/master/requirements.txt) provides the dependencies to be installed

GLPK solver was instaled via the use of an [Aptfile](https://raw.githubusercontent.com/endorgobio/optimiserApp/master/Aptfile). It requires to add a buildingpack (https://github.com/heroku/heroku-buildpack-apt)  whitin the settings menu. 
Details are given in this [link](https://devcenter.heroku.com/articles/buildpacks)

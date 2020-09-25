# Python on the Rstudio Server

## Preface
For some projects like Covid Twitter, there are sections of the codebase that use python for it's implementation. Below is a guide on how to run python applications and manage your dependencies using pip and virtualenv. 

## Prerequisite
On Rstudio navigate your way to the **terminal** tab. Navigate your way to your home directory. 
```bash
cd ~
```
##  1. Install virtualenv
```bash
python3 -m pip install --user virtualenv
```
virtualenv is a tool used to create isolated python environments. It will allow us to create a versioned set of dependencies per project. Since you do not have the permission to install dependencies globally, we will instead install all the dependencies we need for our projects in their own virtual enviornment

## 2.  Create a virtual enviornment for your project
```
python3 -m venv [your enviornment name here]
// ex: python3 -m venv DARL
```
This will create a virtual enviornment in your home directory and might take a while. You may place this virtual enviornment in any directory you want but it might be convinient to place all your enviornments in your home directory to keep track of them. Once that command has finished executing activate your enviornment by typing
```bash
source [your enviornment name here]/bin/activate
//ex: source DARL/bin/activate
```
Now you should see that in your terminal, the name of your virtual enviornment has appeared on the left. This will let you know which environment that you currently working in. 

In order to exit your virtual enviornment just type this command in your terminal
```bash
deactivate
```
*Note: * You will have to type this command and activate your enviornment everytime you connect to the rstudio server. You can activate a specific enviornment during log in using
```bash
echo 'source ~/[your enviornment name]/bin/activate' >> ~/.bashrc
// ex: echo 'source ~/DARL/bin/activate' >> ~/.bashrc
```

## 3. Upgrade pip
pip is python's default package manager and can be used to install, upgrade and remove packages for your virtual enviornment. The default version of pip available to your user on the Rstudio server is a bit old. In order to install the latest version of pip use
```bash
pip3 install --upgrade pip
```

Verify your installation by using
```bash
pip3 --version
// output should be version 20 or later
```

## 4. Install your packages
Now you can install whatever packages you need for your project. Ususally a python package will have a simple install command using pip([example](https://pypi.org/project/elasticsearch/ "example")). Install your packages using
```bash
pip3 install [package names separated by space]
// ex: pip3 install flask torch elasticsearch
```




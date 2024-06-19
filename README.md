# llm_summer2024

## Quick Compute Canada tutorial 

After logging into graham using:
```
ssh -Y graham@username.computecanada.ca 
```
you can use the command: 
```
ls
```
to list all the files and directories in your home folder. Doing so you are going to find three main [folders](https://docs.alliancecan.ca/wiki/Project_layout). Is this tutorial let's foccus on the `$SCRATCH` space and how to run a simple code.

After creating your [environment](https://docs.alliancecan.ca/wiki/Python#Creating_and_using_a_virtual_environment) in your `/home` directory (I really recomend you to create a folder called envs/environment and create your environment inside of it). Installing numpy using: 
```
pip install numpy --no-index
```
I need to upload my python file to the `$SCRATCH` space and then I can run my code. 

In order to access the scratch folder you do: 
```
cd scratch
```
once inside you can create a folder for separate codes/projects that you are working on. For example, I am going to create a `test` folder inside `$SCRATCH`: 
```
mkdir test
```
then I am going to enter `test` folder. Now I can either copy and paste the codes that I need inside this folder using text editors, cloning from a git repo or using VScode. 



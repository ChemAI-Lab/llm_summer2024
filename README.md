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
You need to upload the python file to the `$SCRATCH` space and then run the code. 

In order to access the scratch folder you do: 
```
cd scratch
```
once inside you can create a folder for separate codes/projects that you are working on. For example, I am going to create a `test` folder inside `$SCRATCH`: 
```
mkdir test
```
then I am going to enter `test` folder. Now I can either copy and paste the codes that I need inside this folder using text editors or cloning from a git repo. 

In this case I am going to demostrate using a python code called `basic_operations.py` that you can clone from this git repo. Once you've transfered the code to the `$SCRATCH` space you can run it by:
```
python basic_operations.py
```
remember you environment needs to be activate in order to that work. 

In this case we have a really dummy code that does not require a lot of memory or computer power, so its fine to run on the logging node. In the case you have a bigger code its necessary to run a [scheduler](https://docs.alliancecan.ca/wiki/What_is_a_scheduler%3F), in this case our scheduler is going to be called `sh_basic_operations.py` and you can run it using:
```
python sh_basic_operations.py
```

Look at the ST column in the output of `sq` to determine the status of your jobs. The two most common states are PD for pending and R for running. When the job has finished, it no longer appears in the `sq` output. 

If the code runs succesfully you should see a file `.log` like `out_Opt_times_First1_Second10.0.log` that you can open using a text editor or:
```
cat file.log
```
And you can check if you got any errors and, in this case, the print of our function. 

This is a really simple example, but the srtucture of the `sh` file and your python code (main file) it will be similar. 



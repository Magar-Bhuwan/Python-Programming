#Virtual Environment is a tool which helps to manage different dependencies for different projects 
# in a isolated manner.
# It creates a separate environment for each project, which contains its own set of libraries and dependencies.
# 
# Usage: 
#   python -m venv myenv
# Example: i have installed pip install pandas version 2.0 in my virtual environment
#          but i want to install pandas version 1.5 in another virtual environment
#          then i can use venv to manage different versions of pandas in different virtual environments

# To activate the virtual environment: 
#   myenv\Scripts\activate
#
# To deactivate the virtual environment: 
#   deactivate
# to create virtual environment
#  
#   python -m venv env --> to create virtual environment
#   env\Scripts\activate --> to activate

#   pip install virtualenv --> to install virtualenv globally
#    
#   pip install pandas==1.5.2   --> to install older version or user others version of pandas
#   pip freeze --> to see all the installed packages
#   pip install -r requirements.txt --> to install all the packages from the requirements.txt file
# to switch env --> env\Scripts\activate
# to switch off env --> deactivate



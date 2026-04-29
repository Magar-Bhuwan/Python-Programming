# Create two virtual environments, install few packages in first one. How do you create
# a virtual environment in the second one?

"""
# To create two virtual environments and install packages in the first one, you can follow these steps:
1. Open your terminal or command prompt.
2. Create the first virtual environment using the following command:
   -> python -m venv env1
3. Activate the first virtual environment:
   source env1/bin/activate  # On Windows: env1\Scripts\activate
4. Install packages in the first virtual environment:
   pip install package1 package2
5. Create the second virtual environment:
   python -m venv env2
6. Activate the second virtual environment:
   source env2/bin/activate  # On Windows: env2\Scripts\activate
Now you have two virtual environments, env1 and env2. You can switch between them 
by activating the respective environment. Each environment will have its own 
set of installed packages, allowing you to manage dependencies separately for different projects.

# To deactivate the current virtual environment, simply run:
-> deactivate
This will return you to the global Python environment. You can reactivate any of the 
virtual environments as needed.

# Note: Make sure to replace 'package1' and 'package2' with the actual names of the packages 
you want to install in the first virtual environment.

"""

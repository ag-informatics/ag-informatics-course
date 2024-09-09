If you haven't installed python natively before, you'll need to first install Python (and it's associated package manager 'pip'). [Follow the instructions here](https://www.python.org/downloads/).


### Install Django
A package manager is a tool that keeps a running list of all the packages associated with a particular language on your computer. You can use it to install, update, and remove different types of packages, or libraries. In the past, we had used Anaconda, a package manager with a nice user interface. This module, we'll use a command line based Python package manaer called ['pip'](https://pip.pypa.io/en/stable/).

  1. Open your terminal and run the following command.
    
    Mac: `python -m pip install Django`. More information available here: https://docs.djangoproject.com/en/4.1/topics/install/

    Windows: `py -m pip install Django`. More information available here: https://docs.djangoproject.com/en/4.1/howto/windows/

> NOTE: For the rest of this lab, if you are on a Mac, you can use the `python` commands as written. If you are on a Windows machine you will use the command `py` instead.

  2. Verify that django 4.1 is installed
    `python -m django --version`

> Example: if you are on a Mac, the previous command is run as-is. On a Windows machine, you'd run `py -m django --version`
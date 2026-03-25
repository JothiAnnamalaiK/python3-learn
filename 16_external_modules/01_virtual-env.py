"""
To install virtualenv package:
    > python3 -m pip install virtualenv

To create venv inside a project or folder.  Go to the path and do:
    > python3 -m venv my_first_py_env

To activate the packages:
If windows: > ./my_first_py_env/Scripts/Activate.ps1  (change forward slash to backward slash)
If mac:     > source my_first_py_env/bin/activate

After activate you could see like this in terminal with venv name...
    (my_first_py_env) VTA-DT0405:16_external_modules vt324$

To deactivate venv:
    > deactivate

To install packages in that venv:
    > python3 -m pip install pandas
    > python3 -m pip install requests
    > python3 -m pip install numpy==1.20.0 #with version num

To install older version package inside venv:, run this before installing packages
    > python -m pip install --upgrade pip setuptools wheel

To upgrade packages:
    > pip install --upgrade requests

To remove packages:
    > pip uninstall requests

To view packages installed with thier version:
    > pip freeze

To create a txt file to help other devs, needs to be installed: (create file like package.json)\
    > pip freeze > requirements.txt

To install all the packages from requirements.txt:
    > pip install -r requirements.txt

To view the list of package installed:
    > pip list
"""

import moviepy

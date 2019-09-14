# Excel to database
This project tries to read excel data and save it to a database. When excel data is saved in database an status would be created to show what happend to each row of the excel file. this status encompasses three different values: added, updated and failed.
Futhermore, if the excel header differ from fields of the database table (model) a translation can be passed to the database writer.
Validating data and modifying fields is another property of this project. Using inheritance the absract methods of the DatabaseReader and DatabaseWriter can be implemented to implement model specific validations and modifications. 


## Getting Started

# Enviroment setup
First install requirments and create a virtual environment for the project
using codes below:
```
sudo apt-get install python3-pip python3-dev
sudo pip3.6 install virtualenvwrapper
echo "export VIRTUALENVWRAPPER_PYTHON=`which python3.6`" >> ~/.bashrc
echo "alias v.activate=\"source $(which virtualenvwrapper.sh)\"" >> ~/.bashrc
source ~/.bashrc
v.activate
mkvirtualenv --python=$(which python3.6) --no-site-packages excel_to_database
```

Clone the project with the following link:
```
git clone git@github.com:mkhfring/excel_to_database.git
```
Then in the virtual env created in the previous step run commands below:

```
pip install -e .
pip install -r requirements.txt
```

### Prerequisites

requirements for the project are listed in requirements.txt



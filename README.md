# SeleniumFrameworkPython

## Installation & Prerequisites
1. Instal python [documentation](https://www.python.org/downloads/)
2. Install pytest [documentation](https://docs.pytest.org/en/7.1.x/getting-started.html)

   - Add path in Enviroment Variables-System variables "AppData\Roaming\Python\Python312\Scripts"
4. Install openpyxl [documentation](https://pypi.org/project/openpyxl/)
5. Install pytest-html [documentation](https://pypi.org/project/pytest-html/)
6. Install PyCharm [documentation](https://www.jetbrains.com/help/pycharm/installation-guide.html)
  
## Framework Setup
To set up the framework, you can either fork or clone the repository from [here](https://github.com/markogavrilovic032/SeleniumFrameworkPyhton.git) or download the ZIP file and set it up in your local workspace.

## Running steps:
Open the terminal in the folder **tests** and run the command **py.test --browser_name chrome --html=../reports/reports.html -v --junitxml="../reports/result.xml"**
   
Test can be run in three browsers:
  - chrome
  - firefox

Example command for running tests in chrome browser
**py.test --browser_name chrome --html=../reports/reports.html -v --junitxml="../reports/result.xml**
Example command for running tests in firefox browser
**py.test --browser_name firefox --html=../reports/reports.html -v --junitxml="../reports/result.xml**

## Test repors
After the execution of tests results.html report is generated in the "reports" folder. 
results.xml report contains screenshots of tests that failed.

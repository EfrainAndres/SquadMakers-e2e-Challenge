# SquadMakers-e2e-Challenge

What is the challenge?
URL https://www.saucedemo.com/
The challenge will be based on doing the proposed requirements gathering and automating
and automate those E2E tests on the given web.
To do this you will need to create an online repository in the preferred service
of your choice (Gitlab, Github...) where you will upload the code resulting from the
resulting from the test will be uploaded. 


As this will be done in Python and Selenium, before you begin
you should make sure that you have it installed and accessible for programming.
programming.


The test consists of documenting and automating the features in
the web: https://www.saucedemo.com/

## Installation
- The code has been tested on Python 3.9.4 and Windows 11
- `Pip` is required
- `Behave`, `Selenium` libraries were used

1. Clone repository:
```
git clone https://github.com/EfrainAndres/SquadMakers-e2e-Challenge.git
```

2. Create Virtual Enviroment
- The idea is create this virtual enviroment, in the same folder (SquadMakers-e2e-Challenge):
```
python -m venv venv
```
- Then we should activate the virtual enviroment:
```
myenv\Scripts\activate
```
Install the dependencies:
```
pip install -r requirements.txt
```

Running the tests:
- We can run the tests with the next commands:
```
behave
```

- We can run the tests and generate the html report
```
behave -f html -o report/behave-report.html
```

![image](https://user-images.githubusercontent.com/20568951/208354238-7c241df3-d721-4a5b-baad-439fbe4fa633.png)

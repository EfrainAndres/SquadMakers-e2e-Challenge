# SquadMakers-e2e-Challenge

¿En que consiste el reto?
URL https://www.saucedemo.com/
El reto se basará en hacer la toma de requerimientos
propuestos y automatizar esas pruebas E2E en la web dada.
Para ello se necesitará crear un repositorio online en el servicio
que se prefiera (Gitlab, Github...) donde se subirá el código
resultante de la prueba. 


Como se realizará en Python y Selenium, antes de empezar
deberá asegurarse de que lo tiene instalado y accesible para
programar.


La prueba consiste en documentar y automatizar las features en
la web: https://www.saucedemo.com/

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

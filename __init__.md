# ` $ date `
<span style='color:#fff; font-family: Dejavu Sans Mono; font-size: 1.1em;'>- Path: /home/marcosranes/Desktop/Python_OOP</span>
```
sáb 06 nov 2021 22:10:12 -03
```
### ` $ ln -s draft-README.md __init__.md `

## What is `__init__(self)`?

`__init__` is a method to initialize the object, also known as the constructor of a class.\
Self parameter in turn refers to the object of an instance. Without it (self), the parameters wouldn't be stored in the stack variables and/or would be discarded when the init method went out of the class scope. Once out of its scope, self has to be replaced by the object of instance. (i.e. self.side, thus square.side); square, in turn, is the instance object name.
```python
class Square:
    def __init__(self, side=1):
        self.side = side
```
###  Reusing an existent class and instancing an object
```python
from samples.square import Square

square = Square()
print(square.side)
```
###
#Having a look at the structure
## ` $ tree ../Python_OOP `
<span style='color:#fff; font-family: Dejavu Sans Mono; font-size: 1.1em;'>- Path: /home/marcosranes/Desktop/Python_OOP</span>
```
../Python_OOP
├── draft-README.md
├── __init__.md -> draft-README.md
├── LICENSE
├── README.md
└── samples
    ├── __init__.py
    └── square.py

1 directory, 6 files
```

## ` $ cat samples/square.py `
<span style='color:#fff; font-family: Dejavu Sans Mono; font-size: 1.1em;'>- Path: /home/marcosranes/Desktop/Python_OOP</span>
```
class Square:
    def __init__(self, side=1):
        self.side = side

    def area_calculate(self):
        return pow(self.side, 2)


square = Square(5)
print(square.side, square.area_calculate())
```
### See the output when running the above code
```shell
/home/marcosranes/Desktop/Python_OOP/.venv/bin/python /home/marcosranes/Desktop/Python_OOP/samples/square.py
5 25

Process finished with exit code 0
```

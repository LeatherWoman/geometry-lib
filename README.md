# Geometry Library

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/LeatherWoman/geometry-lib/actions/workflows/python-package.yml/badge.svg)](https://github.com/LeatherWoman/geometry-lib/actions)
[![Code Coverage](https://codecov.io/gh/LeatherWoman/geometry-lib/branch/main/graph/badge.svg)](https://codecov.io/gh/LeatherWoman/geometry-lib)

Библиотека для вычисления площадей геометрических фигур с поддержкой различных операций.

## 📦 Установка

Установите библиотеку через pip:

```bash
pip install git+https://github.com/LeatherWoman/geometry-lib.git
Или для разработки:

git clone https://github.com/LeatherWoman/geometry-lib.git
cd geometry-lib
pip install -e .[test,dev]

## Возможности

Вычисление площади круга по радиусу

Вычисление площади треугольника по трём сторонам

Проверка треугольника на прямоугольность

Полиморфная работа с фигурами

Легкое добавление новых фигур

## Использование

Базовый пример

from geometry_lib import Circle, Triangle

circle = Circle(5)
print(f"Площадь круга: {circle.area:.2f}")

triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.area:.2f}")
print(f"Прямоугольный: {triangle.is_right_angled()}")

Использование фабрики

from geometry_lib import ShapeFactory, calculate_area

shapes = [
    ShapeFactory.create(5),          # Круг
    ShapeFactory.create(3, 4, 5),    # Треугольник
    ShapeFactory.create(4, 5)        # Прямоугольник
]

for shape in shapes:
    print(f"Тип: {type(shape).__name__}")
    print(f"Площадь: {calculate_area(shape):.2f}")

## 🧪 Тестирование

Запуск тестов:

pytest -v

Проверка стиля кода:

flake8 geometry_lib
black --check geometry_lib
mypy geometry_lib

## Как добавить новую фигуру

Создайте новый класс в папке geometry_lib/shapes/

Унаследуйтесь от Shape

Реализуйте обязательные методы:

from typing_extensions import override
from .base import Shape

class NewShape(Shape):
    def __init__(self, *args):
        # Инициализация
        
    @property
    @override
    def area(self) -> float:
        # Вычисление площади
        
    @override
    def is_right_angled(self) -> bool:
        # Проверка на прямоугольность

## Лицензия

MIT License. Подробнее в файле LICENSE.

## Контакты

Автор: LeatherWoman
Email: kostya_chernevich@mail.ru
GitHub: https://github.com/LeatherWoman
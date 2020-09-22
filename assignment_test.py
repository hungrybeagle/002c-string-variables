#! python3

import task1, task2, task3, task4, task5, task6

def test1():
  assert task1.result == "dog barked"

def test3():
  assert hasattr(task3, 'result') == False

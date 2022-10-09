# issue-03

* Для запуска из консоли используется команда

```python
python -m unittest -v issue-03.py
```

Результаты запуска находятся в файле result.txt

**Полный код записи в файл result.txt:**
```python
echo 'Result of running command: python -m unittest -v issue-03.py' > result.txt
echo '' >> result.txt
python -m unittest -v issue-03.py 2>> result.txt
```
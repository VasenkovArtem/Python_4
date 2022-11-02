# issue-05

* Для запуска из консоли используется команда

```python
python -m pytest -v test_what_is_year_now.py --cov=what_is_year_now --cov-report html
```

Результаты запуска находятся в файле result.txt. Отчёт о покрытии кода тестами представлен в директории с html файлами

**Полный код записи в файл result.txt:**
```python
echo 'Result of running command: python -m pytest -v test_what_is_year_now.py --cov=what_is_year_now --cov-report html' > result.txt
echo '' >> result.txt
python -m pytest -v test_what_is_year_now.py --cov=what_is_year_now --cov-report html >> result.txt
```
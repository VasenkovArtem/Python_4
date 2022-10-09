# issue-01

* Для запуска из консоли без флагов используется команда

```python
python -m doctest -v issue-01.py
```

* Для запуска из консоли с флагом NORMALIZE_WHITESPACE используется команда

```python
python -m doctest -o NORMALIZE_WHITESPACE -v issue-01.py
```
Результаты запуска находятся в файле result.txt
* При запуске команды без флага NORMALIZE_WHITESPACE 5-ый тест проваливается, так как в нём находится лишний пробел
* При запуске команды с флагом NORMALIZE_WHITESPACE все тесты проходят успешно

В тестировании использованы #doctest: +SKIP (пример из документации) и #doctest: +IGNORE_EXCEPTION_DETAIL (неверная детализация ошибки)

**Полный код записи в файл result.txt:**
```python
echo 'Result of running command without flag: python -m doctest -v issue-01.py' > result.txt
echo '' >> result.txt
python -m doctest -v issue-01.py >> result.txt
echo '' >> result.txt
echo '' >> result.txt
echo '--------------------------------------------------' >> result.txt
echo '' >> result.txt
python -m doctest -o NORMALIZE_WHITESPACE -v issue-01.py >> result.txt
```
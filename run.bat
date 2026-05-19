@echo off
echo Kurulum basliyor...
python -m pip install -r requirements.txt
echo.
echo Sunucu baslatiliyor... Lutfen tarayicinizda http://localhost:8000 adresine gidin.
echo.
python -m uvicorn main:app --reload
pause

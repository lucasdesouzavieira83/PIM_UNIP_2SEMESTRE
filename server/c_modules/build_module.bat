@echo off
REM build_module.bat - compila o modulo C para Windows (MinGW-w64)
cd /d "%~dp0"
if exist sort_search.dll del sort_search.dll
gcc -shared -o sort_search.dll -fPIC sort_search.c
if errorlevel 1 (
  echo Erro ao compilar. Verifique se MinGW-w64 (gcc) esta no PATH.
  pause
  exit /b 1
)
echo Compilacao concluida: sort_search.dll
pause

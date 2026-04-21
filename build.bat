@echo off
echo Building Hill Walks site...
cd docs
sphinx-build -b html . ..\_build\html
cd ..
if %ERRORLEVEL% EQU 0 (
    echo.
    echo Build successful!
    echo Output: _build\html\index.html
    pause
) else (
    echo.
    echo Build failed!
    pause
)

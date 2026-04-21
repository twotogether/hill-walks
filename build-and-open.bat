@echo off
echo Building Hill Walks site...
cd docs
sphinx-build -b html . ..\_build\html
cd ..
if %ERRORLEVEL% EQU 0 (
    echo Build successful! Opening in browser...
    start _build\html\index.html
) else (
    echo Build failed!
    pause
)

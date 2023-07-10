@echo off
setlocal enabledelayedexpansion

set SublimePath="C:\Program Files\Sublime Text 3\sublime_text.exe"  

set FileToOpen=%~1

set "CurrentDirectory=%cd%"

for /r "%CurrentDirectory%" %%I in (%FileToOpen%) do (
   set "FullPath=%%~fI"
   if exist %SublimePath% (
      start "" %SublimePath% "!FullPath!"
      exit /b
   )
)

echo Sublime Text is not installed or the file could not be found.
echo Please verify the installation path in the batch file and ensure the file exists.
endlocal

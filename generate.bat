@echo off
setlocal enabledelayedexpansion

set "debug=0"
if "%1"=="debug" (
	set /a debug=1
)

rem If debug is true; disable echo off
if "%debug%"=="1" echo on

rem Change these if you want
set "ParentFolder=%CD%\software"
set "DestFolder=%cd%\output"

rem Get count of subfolders in parent folder
set DirCount=0
for /d %%A in ("%ParentFolder%\*") do set/a DirCount+=1

rem Generate a random number from 1 up to %DirCount%
set/a RandomNumber=%random%%%DirCount+1
set/a fileCount = 3
set/a min = 1
set/a catCount = 4
set/a RandomFile=(%random% %% (fileCount - min)) + min
rem pick one random folder
set DirNumber=1
rem :fileCopy
if exist "%ParentFolder%\cat%FileCount%\%RandomFile%.exe" (
	goto existSameName
) else (
	goto notExistName
goto compress

:existSameName
	copy "%ParentFolder%\cat%FileCount%\%RandomFile%.exe" "%DestFolder%\%RandomFile%_%RandomNumber%.exe"

:notExistName
copy "%ParentFolder%\cat%FileCount%\%RandomFile%.exe" "%DestFolder%"

:compress
if exist "%DestFolder%" (
	echo Here is your mystery box! > %DestFolder%\hi.txt
            tools\7z a -t7z "%DestFolder%.7z" "%DestFolder%\"
        ) else (
            echo Warning: Destination folder not found.
        )
)
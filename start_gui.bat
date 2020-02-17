@echo Loading DIRT-X File Processor GUI (please wait) ...
@echo off

SET _propy=""

IF EXIST "%LOCALAPPDATA%\Continuum\anaconda3\Scripts\" (
	SET conda="%LOCALAPPDATA%\Continuum\anaconda3\Scripts\conda.exe"
)

IF EXIST "%LOCALAPPDATA%\Continuum\anaconda3\envs\geo-python\" (
	SET _propy="%LOCALAPPDATA%\Continuum\anaconda3\envs\geo-python\python.exe"
)

IF %conda%=="" (
	goto err_conda
)

IF %_propy%=="" (
	goto err_geopy
)


@echo on
call conda init cmd.exe
call conda activate geo-python
call %_propy% "%cd%\launch_gui.py"

exit

:err_conda
	@echo off
	@echo: 
	@echo ERROR: Cannot find Anaconda. Make sure Python Anaconda is installed in the local user folder.
	pause
	exit


:err_geopy
	@echo off
	@echo:
	@echo ERROR: Cannot find geo-python environment. Make sure to follow the installation instructions for creating the conda environment in your local user folder.
	pause
	exit
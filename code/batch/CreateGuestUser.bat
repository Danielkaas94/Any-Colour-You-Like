@REM Create Guest User in Windows 10

@REM Run CMD as Admin

net user Guest /add /active:yes

@REM Password for Guest:
net user Guest *
@REM Write your Password


@REM Disable Guest Account in Windows 10 using CMD
net user Guest /active:no
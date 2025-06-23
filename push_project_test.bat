rem �������K�̉񓚃v���W�F�N�g���ASDP�`�[���̃��|�W�g����push���邽�߂̃o�b�`�t�@�C���i���쌟�ؗp�j�ł�
@echo off
setlocal enabledelayedexpansion

rem ���L�̃R�}���h��"UserName"/"MailAddress"/"ProjectName"�̉ӏ��̓��|�W�g���I�[�i�[�̂��̂ɕύX���Ă����Ă�������
rem �u"�v�i�_�u���N�I�[�e�[�V�����j�͂����܂܋L�����đ��v�ł�
git config --global user.name "Tomoya Nakagoshi"
git config --global user.email "tnakagoshi@knowledge-ex.jp"
set PROJECT_NAME=tnakagoshi

for /f "tokens=*" %%i in ('git config --global user.name') do set VAR1=%%i
for /f "tokens=*" %%i in ('git config --global user.email') do set VAR2=%%i

echo Git���[�U��       : %VAR1%
echo Git���[���A�h���X : %VAR2%
echo �v���W�F�N�g��    : %PROJECT_NAME%

if "%VAR1%" == "UserName" (
  echo *** initremotes.bat��4�s�ڂ̃��[�U���𐳂����ύX���Ă���Ď��s���Ă�������
  exit /b
)

if "%VAR2%" == "MailAddress" (
  echo *** initremotes.bat��5�s�ڂ̃��[���A�h���X�𐳂����ύX���Ă���Ď��s���Ă�������
  exit /b
)

if "%PROJECT_NAME%" == "ProjectName" (
  echo *** initremotes.bat��6�s�ڂ̃v���W�F�N�g���𐳂����ύX���Ă���Ď��s���Ă�������
  exit /b
)

echo ��L�A�J�E���g�Ń��|�W�g���쐬�����s���܂��B���Ȃ���΁AEnter�L�[���������Ă��������B
pause 

set "letters=A B C D E F G H"

for %%L in (%letters%) do (
  git clone https://github.com/%PROJECT_NAME%/sdp-%%Lteam-fy25.git
  mkdir sdp-%%Lteam-fy25\suppliesproject
  xcopy /E /I /Y suppliesproject sdp-%%Lteam-fy25\suppliesproject
  cd sdp-%%Lteam-fy25
  git add .
  git commit -m "suppliesproject"
  git branch -M main
  git push -u origin main
  cd ..
  rmdir /S /Q sdp-%%Lteam-fy25
)

echo Finished!

rem 総合演習の回答プロジェクトを、SDPチームのリポジトリにpushするためのバッチファイル（動作検証用）です
@echo off
setlocal enabledelayedexpansion

rem 下記のコマンドの"UserName"/"MailAddress"/"ProjectName"の箇所はリポジトリオーナーのものに変更しておいてください
rem 「"」（ダブルクオーテーション）はつけたまま記入して大丈夫です
git config --global user.name "Tomoya Nakagoshi"
git config --global user.email "tnakagoshi@knowledge-ex.jp"
set PROJECT_NAME=tnakagoshi

for /f "tokens=*" %%i in ('git config --global user.name') do set VAR1=%%i
for /f "tokens=*" %%i in ('git config --global user.email') do set VAR2=%%i

echo Gitユーザ名       : %VAR1%
echo Gitメールアドレス : %VAR2%
echo プロジェクト名    : %PROJECT_NAME%

if "%VAR1%" == "UserName" (
  echo *** initremotes.batの4行目のユーザ名を正しく変更してから再実行してください
  exit /b
)

if "%VAR2%" == "MailAddress" (
  echo *** initremotes.batの5行目のメールアドレスを正しく変更してから再実行してください
  exit /b
)

if "%PROJECT_NAME%" == "ProjectName" (
  echo *** initremotes.batの6行目のプロジェクト名を正しく変更してから再実行してください
  exit /b
)

echo 上記アカウントでリポジトリ作成を実行します。問題なければ、Enterキーを押下してください。
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

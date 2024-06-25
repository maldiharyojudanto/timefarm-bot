# timefarm-bot
timefarm bot auto claim/farming multiple account https://t.me/TimeFarmCryptoBot

<img width="705" alt="2024-06-21 00_17_28-main py - tapbot - Visual Studio Code" src="https://github.com/maldiharyojudanto/timefarm-bot/assets/76139419/c12ba345-27a9-4320-80e9-3eb7d464f0e7">

## Features
- Auto create token (login by query_id)
- Auto start/claim farming
- Auto upgrade
- Auto complete tasks
- Auto claim refferal balance
- Auto refresh token

## Requirement
- Python 3.8+

## How to run
1. Clone/download this repository
2. > pip install -r requirements.txt
3. > python main.py

## How to get query_id?
1. Open telegram web/desktop
2. Go to Settings - Advanced - Experimental settings - Enable webview inspecting
3. Open bot https://t.me/TimeFarmCryptoBot
4. Press F12 or right click then select inspect element
5. Go to Application tab - Session storage - Select tg-tap-miniapp/timefarm - Select '__telegram__initParams' (copy value start with ```query_id=```)
6. Separate query_id with the newline (for multiple account)

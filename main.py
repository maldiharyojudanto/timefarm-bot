import httpx
import asyncio
import json
import time
import os
import datetime
from colorama import Fore, Style, init
from dotenv import load_dotenv
import ast

init()
load_dotenv()

async def getToken(session, query):
    url = "https://tg-bot-tap.laborx.io/api/v1/auth/validate-init/v2"

    payload = json.dumps({
        "initData": f"{query}",
        "platform": "tdesktop"
    })
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://timefarm.app',
        'priority': 'u=1, i',
        'referer': 'https://timefarm.app/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getToken, try again ... {e}")

async def getInfoUser(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/farming/info"

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.get(url, headers=headers)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getInfoUser, try again ... {e}")

async def getListTask(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/tasks"

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.get(url, headers=headers)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getListTask, try again ... {e}")

async def getReffInfo(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/referral/link"

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.get(url, headers=headers)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getReffInfo, try again ... {e}")

async def startFarming(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/farming/start"
    
    payload = json.dumps({})

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            elif resp.status_code == 403: # farming already start
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to startFarming, try again ... {e}")

async def finishFarming(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/farming/finish"

    payload = json.dumps({})
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            elif resp.status_code == 403: # farming already start
                # print(resp.json())
                return resp.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to finishFarming, try again ... {e}")

async def startTask(session, token, idtask):
    url = f"https://tg-bot-tap.laborx.io/api/v1/tasks/{idtask}/submissions"

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers)

            if resp.status_code == 200:
                # print(resp.status_code)
                # print(resp.json())
                return resp.json()
            elif resp.status_code == 400:
                # print(resp.json())
                return resp.json() # already submitted
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to startTask, try again ... {e}")
        except json.decoder.JSONDecodeError as e:
            # print(f"{e}")
            continue

async def claimTask(session, token, idtask):
    url = f"https://tg-bot-tap.laborx.io/api/v1/tasks/{idtask}/claims"

    payload = json.dumps({})

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            elif resp.status_code == 400:
                # print(resp.json())
                return resp.json() # already submitted
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimTask, try again ... {e}")
        except json.decoder.JSONDecodeError as e:
            # print(f"{e}")
            continue

async def claimReff(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/balance/referral/claim"

    payload = json.dumps({})

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            elif resp.status_code == 403:
                # print(resp.json())
                return resp.json() # nothing to claim
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimReff, try again ... {e}")
        except json.decoder.JSONDecodeError as e:
            # print(f"{e}")
            continue

async def upgradeLevel(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/me/level/upgrade"

    payload = json.dumps({})

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'https://tg-tap-miniapp.laborx.io',
        'priority': 'u=1, i',
        'referer': 'https://tg-tap-miniapp.laborx.io/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            resp = await session.post(url, headers=headers, data=payload)

            if resp.status_code == 200:
                # print(resp.json())
                return resp.json()
            elif resp.status_code == 403:
                # print(resp.json())
                return resp.json() # "message": "Max level reached", message': 'Not enough balance',
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to upgradeLevel, try again ... {e}")
        except json.decoder.JSONDecodeError as e:
            # print(f"{e}")
            continue

async def runGetToken():
    try:
        with open('query.txt', 'r') as qf:
            querys = qf.readlines()
            async with httpx.AsyncClient() as session:
                for i in range(len(querys)):
                    # print(querys[i].strip())
                    query = querys[i].strip()

                    get_token = await getToken(session, query)
                    levelnow = get_token['info']['level']
                    token = get_token['token']
                    level = get_token['levelDescriptions']

                    querys[i] = f"{levelnow}|{token}|{level}\n"

                    with open('tokens.txt', 'w+') as tf:
                        tf.writelines(querys)
        print("Create token success!")
    except FileNotFoundError:
        qf = open('query.txt', 'w')
        print("Fill the query.txt first!")
        qf.write("query1\nquery2\ndst...")
        qf.close()
        exit()

def countLength(n):
    num = str(n)
    return len(num)

async def runAll(levelnow, token, index, upgradelist):
    async with httpx.AsyncClient() as session:
        info = await getInfoUser(session, token)
        list_task = await getListTask(session, token)
        reff_info = await getReffInfo(session, token)

        balance = float(info['balance'])
        farming_duration = int(info['farmingDurationInSec']/60/60)
        farming_reward = info['farmingReward']
        total_reff = reff_info['userCount']

        if total_reff > 0:
            status_reff = f"{Fore.GREEN}{total_reff}{Style.RESET_ALL}"
        else:
            status_reff = total_reff

        start_farm = await startFarming(session, token) #if message/error in startFarming: farming started
        claim_farm = await finishFarming(session, token)

        status_farm = "-"
        if 'error' in start_farm:
            status_farm = f"{Fore.YELLOW}Farming{Style.RESET_ALL}"
        else:
            status_farm = f"{Fore.GREEN}Farming started{Style.RESET_ALL}"

        if os.getenv("AUTO_TASKS") == "true" or os.getenv("AUTO_TASKS") == "yes" or os.getenv("AUTO_TASKS") == "y":
            status_task = f"{Fore.GREEN}On{Style.RESET_ALL}"
            for i in list_task:
                idtask = i['id']
                await startTask(session, token, idtask)
            
            for i in list_task:
                idtask = i['id']
                await claimTask(session, token, idtask)
            
            status_task = f"{Fore.GREEN}All task completed{Style.RESET_ALL}"
        else:
            status_task = "Off"

        if os.getenv("AUTO_CLAIM_REFF") == "true" or os.getenv("AUTO_CLAIM_REFF") == "yes" or os.getenv("AUTO_CLAIM_REFF") == "y":
            status_autoclaimreff = f"{Fore.GREEN}On{Style.RESET_ALL}"
            claimreff_res = await claimReff(session, token)
            if 'error' in claimreff_res:
                status_autoclaimreff = f"{Fore.YELLOW}{claimreff_res['error']['message']}{Style.RESET_ALL}"
            else:
                status_autoclaimreff = f"{Fore.GREEN}Success{Style.RESET_ALL}"
        else:
            status_autoclaimreff = "Off"

        if os.getenv("AUTO_UPGRADE") == "true":
            status_upgrade = f"{Fore.GREEN}On{Style.RESET_ALL}"
            for i in upgradelist:
                if 'price' in i:
                    if i['price'] != -1 and i['level'] > levelnow and balance > i['price']:
                        await upgradeLevel(session, token)
                    else:
                        pass
        else:
            status_upgrade = "Off"
        
        lengcount = countLength(index)

        if lengcount == 1:
            print(f"[Account 0{index}] | Level : {levelnow} | Balance : {Fore.GREEN}{int(balance)}{Style.RESET_ALL} | Reward : {farming_reward}/{farming_duration} hours | Status : {status_farm} | Tasks : {status_task} | Auto upgrade : {status_upgrade} | Referral : {status_reff} ")
        else:
            print(f"[Account {index}] | Level : {levelnow} | Balance : {Fore.GREEN}{int(balance)}{Style.RESET_ALL} | Reward : {farming_reward}/{farming_duration} hours | Status : {status_farm} | Tasks : {status_task} | Auto upgrade : {status_upgrade} | Referral : {status_reff} ")

async def main():
    # query = ""

    os.system("cls" if os.name == "nt" else "clear") # remove the printed 

    print("Create token started")
    await runGetToken()

    sekarang = time.time()
    nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))

    while sekarang < nanti:
        print("""
 _   _                   __                        _           _   
| |_(_)_ __ ___   ___   / _| __ _ _ __ _ __ ___   | |__   ___ | |_ 
| __| | '_ ` _ \ / _ \ | |_ / _` | '__| '_ ` _ \  | '_ \ / _ \| __|
| |_| | | | | | |  __/ |  _| (_| | |  | | | | | | | |_) | (_) | |_ 
 \__|_|_| |_| |_|\___| |_|  \__,_|_|  |_| |_| |_| |_.__/ \___/ \__|                                       
              """)
        start = time.time()
        schedules = []
        with open('tokens.txt', 'r') as tf:
            tokens = tf.readlines()
            for i in range(len(tokens)):
                # print(tokens[i].strip())
                token_auth = tokens[i].strip().split("|")
                # print(token_auth[0])
                upgradelist = ast.literal_eval(token_auth[2])
                schedules.append(asyncio.create_task(runAll(token_auth[0], token_auth[1], i+1, upgradelist)))

        # gather to run concurently
        await asyncio.gather(*schedules) # BOOOMMMM TO RUN

        print("")
        finish = time.time()-start
        #################### CHANGE THE REFRESH HERE ####################
        claim_remaining = int(os.getenv("REFRESH_CLAIM")) # set to 2 menit or 120 seconds
        refresh_token_at = datetime.datetime.fromtimestamp(nanti).strftime("%H:%M:%S")
        ###############################################################

        while claim_remaining:
            hour, secs = divmod(claim_remaining, 60) 
            timer = '{:02d}'.format(secs) 
            print(f"Execution time : {Fore.YELLOW}{round(finish, 2)}{Style.RESET_ALL} seconds | Refresh tokens after : {Fore.YELLOW}{refresh_token_at}{Style.RESET_ALL} | Refresh after : {Fore.YELLOW}{timer}{Style.RESET_ALL} seconds", end="\r")
            time.sleep(1) 
            claim_remaining -= 1
    
        sekarang = time.time() + int(os.getenv("REFRESH_CLAIM"))
        if sekarang >= nanti:
            print("")
            print("Refresh tokens started!")
            await runGetToken()
            time.sleep(2)
            nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))
            
        os.system("cls" if os.name == "nt" else "clear") # remove the printed 

if __name__ == "__main__":
    # Set the policy to prevent "Event loop is closed" error on Windows - https://github.com/encode/httpx/issues/914
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

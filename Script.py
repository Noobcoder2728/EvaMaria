class script(object):
    START_TXT = """ʜᴇʟʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}>{}</a>, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ 😍"""
    HELP_TXT = """Hᴇʏ {}
𝐻𝑒𝑟𝑒 𝑖𝑠 𝑇ℎ𝑒 𝐻𝑒𝑙𝑝 𝐹𝑜𝑟 𝑀𝑦 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠."""
    ABOUT_TXT = """★ 𝑀𝑦 𝑁𝑎𝑚𝑒: {}
★ 𝐿𝑖𝑏𝑟𝑎𝑟𝑦 : Pʏʀᴏɢʀᴀᴍ
★ 𝐿𝑎𝑛𝑔𝑢𝑎𝑔𝑒 : Pʏᴛʜᴏɴ 3
★ 𝐷𝑎𝑡𝑎𝑏𝑎𝑠𝑒 : ᴍᴏɴɢᴏ DB
★ 𝑠𝑒𝑟𝑣𝑒𝑟 : Hᴇʀᴏᴋᴜ
★ 𝐵𝑢𝑖𝑙𝑑 𝑆𝑡𝑎𝑡𝑢𝑠 : v1.0.1 [ Bᴇᴛᴀ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
► Beast is a close source project. 
► Contact devs only for reporting bugs.  

<b>ᴅᴇᴠᴇʟᴏᴘᴇʀ​:</b>
► <a href=https://t.me/Im_Tamilan_bot>Im Tamilan</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. 𝐁𝐄𝐀𝐒𝐓 should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

► 𝐁𝐄𝐀𝐒𝐓 Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. 𝐁𝐄𝐀𝐒𝐓 supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MovieSearchTG_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ ᴛᴏᴛᴀʟ ꜰɪʟᴇs: <code>{}</code>
➥ ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
➥ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
➥ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code> 
➥ ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

# Momiji
The only Discord bot you'll ever need. Built using discord.py and uses sqlite3 database.

Momiji is a fake AI Discord bot that actually learns from the messages it can see and responds you with the knowledge it obtained from that channel, when it is triggered. Basically, if a channel has a personality, Momiji would be it. How cancerous Momiji is in a given channel really depends on the messages sent in that channel.

---

![](https://i.imgur.com/v0kgBww.png)

---

# By the way I tend to make database related changes which can break the bot after updating if you don't adjust the database accordingly
I am sorry, but this happens when you want to add new features and accounting for this is a waste of time on my end.

---

## Stuff to note

+ Momiji's main functionality is taking a random message that has been said by someone else and replying with it once someone triggers Momiji. When Momiji first joins a server, it has no collection of chat logs. It's highly recommended import messages from the channel immediately so Momiji can get to working as intended. To import messages from every channel the bot sees, type `;init`. This will import old messages. This may take a very very long time depending on how many messages there are to import. Newer messages are automatically stored.
+ To prevent leaking information between channels, Momiji will pick a message that has been said in that current channel before.
+ I recommend blacklisting some offensive words with this command `;blacklist <whatever you want to blacklist>`.
+ See configuration.md for how to configure it. Though it's out of date. I think the `;help` command is a lot more useful.

---

## Data usage

For Momiji to work, it collects chat logs. It is essential for operation. While this can be done in other ways, I opted for this because some current and future functionality won't work without this. Also, collecting lots makes moderation and dealing with abusive staff a lot easier. In my hosted instance of this bot, any data collected through this bot stays on my server, used within the scope of the bot it self and for moderation purposes, and is not given to anyone else. If you are self hosting, don't give the data you collect to anyone.

---

Also, credits to whoever made `pinged.gif`, I don't know who made it, sorry, or I would have put his name here. Therefore, license of this repository applies everything in here except `pinged.gif`.

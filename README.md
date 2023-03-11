Telegram Wiper
==============

A simple Python script to wipe a user's messages out from some chat.

The easiest way to run the script is to use a Docker image:

```shell
docker run -it --rm --env-file .env kozalo/tg-wipe
```

However, before doing that you need to get your own *API_ID* and *API_HASH* on https://my.telegram.org/apps and put them
into the `.env` file in the working directory by replacing placeholders there.

The script will ask you about your Telegram credentials and give you a numbered list of all of your chats. Select the
number and messages will disappear.

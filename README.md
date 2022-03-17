# PdfUploader
This is the pdf uploader bot

# Installation

You need Python3 (3.6 works fine, 3.5 will crash randomly).

Install dependencies by running this command:

    pip install -r requirements.txt

(If you want faster downloading-uploading, then install `cryptg` and its dependencies)

Warning: If you get a `File size too large message`, check the version of Telethon library you are using. Old versions have got a 1.5Gb file size limit.


Obtain your own api id: https://core.telegram.org/api/obtaining_api_id

# Usage

Rename file `.envs` to `.env` and add required values into it or
add these values to your config variable sections in cloud platform:

| Environment Variable     | Command Line argument | Description                                                  
|--------------------------|:-----------------------:|---------------------------------------------------------------|
| `api_hash`                 | `--api-hash`          | api_id from https://core.telegram.org/api/obtaining_api_id| 
| `api_id`                   | `--api-id`            | api_hash from https://core.telegram.org/api/obtaining_api_id  |
| `bot_chat_id`              | `--bot_chat_id`       | Destination bots for downloaded files                | 
| `bot_chat_id2`             | `--bot_chat_id`       | Destination bots for downloaded files                |
| `my_channel_id`            | `--channel_id`        | Your Channel id 1   |      Get from @userbot         | 
| `my_channel_id2`           | `--channel_id`        | Your Cahnnel id 2  |      Get from @userbot         |
| `other_channel_id`         | `--channel_id`        | Other scrapped Channel id  | Get from @userbot       |
| `pd_chat_id`               | `--your chat_id`      | Get from @botfather |                              |

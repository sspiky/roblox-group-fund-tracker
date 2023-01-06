# roblox group fund tracker
adds up the robux in your groups and sends a discord embed to a desired channel, useful if you sell robux via group funds or whatever

uses requests bc idc about saving an extra 4 ms

made this for my friend for usage @ .gg/flop

## Requirements
- requests
- discord.py

## Usage
- put your group ids in the groups list
- place a valid .ROBLOSECURITY in the headers after `.ROBLOSECURITY=`
- put your bot token in the `bot.run()` at the bottom
- change channel id on the `bot.get_channel(123456789123456789)` line
- change footer of embed or remove it completely if you want
- change sleep time if you want - default is `1 hour / 3600 seconds`

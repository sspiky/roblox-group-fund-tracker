# roblox group fund tracker
adds up the robux in your groups and updates a discord embed in a desired channel every hour

uses requests bc idc about saving an extra 4 ms

made this for my friend for usage @ .gg/flop, useful if you sell robux via group funds or whatever
## Example
![alt text](https://i.imgur.com/UMBZlDm.png)

## Requirements
- requests
- discord.py

## Usage
- put your group ids in the groups list
- place a valid .ROBLOSECURITY in the headers after `.ROBLOSECURITY=`
- put your bot token in the `bot.run()` at the bottom
- change channel id on the `bot.get_channel(123456789123456789)` line

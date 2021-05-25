## Koinos Testnet Faucet Discord Bot

### How To Install

Create a new virtual environment

`sudo apt install python3-venv`

`python3 -m venv ~/venv/discord_bot`

Activate the virtual environment:

`source ~/venv/discord_bot/bin/activate`

Install prereqs in virtual environment:

`pip install -r requirements.txt`

Copy the example config, then set desired parameters:

`cp example_config.yaml config.yaml`


### How To Run

Activate the virtual environment:

`source ~/venv/discord_bot/bin/activate`

Run the script:

`python discord_bot.py`

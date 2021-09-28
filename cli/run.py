from cli import auth
import cli
from cfg.cfg import get_value
from handler import tokenException
from helper import wizard
import asyncio

def start():
    try:
        if get_value('token') != "token_here":
            cli.loop.create_task(auth.client.run(get_value('token')))
        else:
            # Call setup wizard
            sloop = asyncio.get_event_loop()
            sloop.run_until_complete(wizard.setup_bot())
            sloop.close()
    except Exception as e:
        tokenException.tokenError(str(e))
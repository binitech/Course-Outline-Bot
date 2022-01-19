import glob
from pathlib import Path

from aiogram.utils import executor

from Bot.utils import load_plugins
import logging
from Bot import dp

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Bot Started Successfully!")

if __name__ == "__main__":
    executor.start_polling(dp)

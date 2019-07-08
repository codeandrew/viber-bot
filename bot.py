from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
    name="WC DevOps",
    auth_token="49f3efc15b27d706-c93a2e0b25a905f4-2047e2a0840eb7f1",
    avatar="https://cdn4.iconfinder.com/data/icons/devops/128/build-devops-automation-recycle_code-refresh_settings-preferences-512.png"
)

viber = Api(bot_configuration)

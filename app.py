from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

app = Flask(__name__)
bot_configuration = BotConfiguration(
    name="WC DevOps",
    auth_token="49f3efc15b27d706-c93a2e0b25a905f4-2047e2a0840eb7f1",
    avatar="https://cdn4.iconfinder.com/data/icons/devops/128/build-devops-automation-recycle_code-refresh_settings-preferences-512.png"
)

viber = Api(bot_configuration)

logger = logging.getLogger()

@app.route('/viber/incoming', methods=['GET'])
def index():
    return "Test"

@app.route('/viber/incoming', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        # lets echo back
        viber.send_messages(viber_request.sender.id, [
            TextMessage(text=str(viber_request))
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(viber_request, status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

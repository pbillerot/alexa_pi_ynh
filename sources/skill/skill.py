# -*- coding: utf-8 -*-

# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.interfaces.audioplayer import (
  PlayDirective, PlayBehavior, AudioItem, Stream, AudioItemMetadata,
  StopDirective, ClearQueueDirective, ClearBehavior)
from ask_sdk_model.ui import StandardCard, Image

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

import requests
import configparser
import os
currentDir = os.path.dirname(os.path.realpath(__file__))

config = configparser.ConfigParser()

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class SongFouleSentimentaleConeIntentHandler(AbstractRequestHandler):
  def can_handle(self, handler_input):
    return is_intent_name("SongFouleSentimentaleConeIntent")(handler_input)

    def handle(self, handler_input):
      try:
        config.read(currentDir + "/data/songs.ini")
        speech_text = config.get("FouleSentimentale", "c1").replace("\n", ", ")
      except:
        speech_text = "FouleSentimentale couplet 1 non trouvé"

      handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Parole", speech_text)).set_should_end_session(
        False)
      return handler_input.response_builder.response
sb.add_request_handler(SongFouleSentimentaleConeIntentHandler())

class SongFouleSentimentaleRoneIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("SongFouleSentimentaleRoneIntent")(handler_input)

    def handle(self, handler_input):
        try:
            config.read(currentDir + "/data/songs.ini")
            speech_text = config.get("FouleSentimentale", "r1").replace("\n", ", ")
        except:
            speech_text = "FouleSentimentale refrain 1 non trouvé"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Parole", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response
sb.add_request_handler(SongFouleSentimentaleRoneIntentHandler())

class SongRiveGaucheConeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("SongRiveGaucheConeIntent")(handler_input)

    def handle(self, handler_input):
        try:
            config.read(currentDir + "/data/songs.ini")
            speech_text = config.get("RiveGauche", "c1").replace("\n", ", ")
        except:
            speech_text = "RiveGauche couplet 1 non trouvé"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Parole", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response
sb.add_request_handler(SongRiveGaucheConeIntentHandler())

class SongRiveGaucheRoneIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("SongRiveGaucheRoneIntent")(handler_input)

    def handle(self, handler_input):
        try:
            config.read(currentDir + "/data/songs.ini")
            speech_text = config.get("RiveGauche", "r1").replace("\n", ", ")
        except:
            speech_text = "RiveGauche refrain 1 non trouvé"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Parole", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response
sb.add_request_handler(SongRiveGaucheRoneIntentHandler())

class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        print("HelloWorldIntent")
        speech_text = "Bonjour, de la part de Karl!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response
sb.add_request_handler(HelloWorldIntentHandler())

class MeteoIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("MeteoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("MeteoIntent")
        speech_text = "Il fait beau!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response
sb.add_request_handler(MeteoIntentHandler())

class TempoCentIntentHandler(AbstractRequestHandler):
    """Handler for Tempo 100 Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("TempoCentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("TempoCentIntent")
        speech_text = "OK j'envoie la Tempo 100!"

        requests.get(url="http://0.0.0.0:5000/player/play/drums_100.wav")

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response

sb.add_request_handler(TempoCentIntentHandler())

class TempoCentDixIntentHandler(AbstractRequestHandler):
    """Handler for Tempo 110 Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("TempoCentDixIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("TempoCentDixIntent")
        speech_text = "OK j'envoie la Tempo 110!"

        requests.get(url="http://0.0.0.0:8000/alexa/player/play/drums_110.wav")

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response
sb.add_request_handler(TempoCentDixIntentHandler())

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("LaunchRequest")
        speech_text = "Karl à ton écoute"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("HelpIntent")
        speech_text = "Tu peux me dire bonjour!"

        handler_input.response_builder.speak(speech_text).ask(
            speech_text).set_card(SimpleCard(
                "Hello World", speech_text))
        return handler_input.response_builder.response

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("CancelOrStopIntent")
        speech_text = "Bye!"

        requests.get(url="http://0.0.0.0:8000/alexa/player/stop")

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text))
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print("SessionEndedRequest")
        # requests.get(url="http://0.0.0.0:8000/alexa/player/stop")
        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        print("CatchAllException")
        logger.error(exception, exc_info=True)

        speech = "Désolé, ya un bug dans le programme de Barbichu !!"
        handler_input.response_builder.speak(speech).ask(speech)
        # requests.get(url="http://0.0.0.0:8000/alexa/player/stop")
        return handler_input.response_builder.response

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()
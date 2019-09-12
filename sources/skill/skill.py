# -*- coding: utf-8 -*-
"""
  https://alexa-skills-kit-python-sdk.readthedocs.io/en/latest/legacy.html
  https://developer.amazon.com/fr/docs/alexa-skills-kit-sdk-for-python/overview.html
  
"""

# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name, get_slot, get_slot_value
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.interfaces.audioplayer import (
  PlayDirective, PlayBehavior, AudioItem, Stream, AudioItemMetadata,
  StopDirective, ClearQueueDirective, ClearBehavior)
from ask_sdk_model.ui import StandardCard, Image

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

import requests
import configparser
import os, pprint
currentDir = os.path.dirname(os.path.realpath(__file__))

config = configparser.ConfigParser()

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

function get_slot_id(slot){
    let value = slot.value;
    let resolution = (slot.resolutions && slot.resolutions.resolutionsPerAuthority 
      && slot.resolutions.resolutionsPerAuthority.length > 0) 
      ? slot.resolutions.resolutionsPerAuthority[0] : null;
    if(resolution && resolution.status.code == 'ER_SUCCESS_MATCH'){
        let resolutionValue = resolution.values[0].value;
        value = resolutionValue.id ? resolutionValue.id : resolutionValue.name;
    }
    return value;
}

class ParoleIntentHandler(AbstractRequestHandler):
  def can_handle(self, handler_input):
    return is_intent_name("ParoleIntent")(handler_input)

  def handle(self, handler_input):
    slots = handler_input.request_envelope.request.intent.slots
    slot_morceau = None
    slot_couplet = None
    slot_refrain = None
    morceau = "Morceau"
    couplet = "Couplet"
    refrain = "Refrain"
    if morceau in slots:
      slot_morceau = get_slot_id(slots[morceau])
    if couplet in slots:
      slot_couplet = get_slot_id(slots[couplet])
    if refrain in slots:
      slot_refrain = get_slot_id(slots[refrain])

    speech_text = "Paroles non trouvées"
    try:
      if slot_morceau is not None:
        config.read(currentDir + "/data/songs.ini")
        if slot_couplet is not None:
          speech_text = config.get(slot_morceau, slot_couplet).replace("\n", ", ")
        if slot_refrain is not None:
          speech_text = config.get(slot_morceau, slot_refrain).replace("\n", ", ")
    except:
      speech_text = "Erreur recherche "

    print(f"morceau: {slot_morceau} couplet:{slot_couplet} refrain:{slot_refrain}")
    
    handler_input.response_builder.speak(speech_text).set_should_end_session(False)
    return handler_input.response_builder.response
sb.add_request_handler(ParoleIntentHandler())

class HelloWorldIntentHandler(AbstractRequestHandler):
  """Handler for Hello World Intent."""
  def can_handle(self, handler_input):
    return is_intent_name("HelloWorldIntent")(handler_input)

  def handle(self, handler_input):
    print("Hello World")
    speech_text = "Bonjour, de la part de Karl!"
    handler_input.response_builder.speak(speech_text).set_should_end_session(False)
    return handler_input.response_builder.response
sb.add_request_handler(HelloWorldIntentHandler())

class TempoCentIntentHandler(AbstractRequestHandler):
  """Handler for Tempo 100 Intent."""
  def can_handle(self, handler_input):
    return is_intent_name("TempoCentIntent")(handler_input)

  def handle(self, handler_input):
    print("TempoCent")
    speech_text = "OK j'envoie la Tempo 100!"

    requests.get(url="http://0.0.0.0:5000/player/play/drums_100.wav")

    handler_input.response_builder.speak(speech_text).set_should_end_session(False)
    return handler_input.response_builder.response

sb.add_request_handler(TempoCentIntentHandler())

class TempoCentDixIntentHandler(AbstractRequestHandler):
  """Handler for Tempo 110 Intent."""
  def can_handle(self, handler_input):
    return is_intent_name("TempoCentDixIntent")(handler_input)

  def handle(self, handler_input):
    print("TempoCentDix")
    speech_text = "OK j'envoie la Tempo 110!"

    requests.get(url="http://0.0.0.0:8000/alexa/player/play/drums_110.wav")

    handler_input.response_builder.speak(speech_text).set_should_end_session(False)
    return handler_input.response_builder.response
sb.add_request_handler(TempoCentDixIntentHandler())

class LaunchRequestHandler(AbstractRequestHandler):
  """Handler for Skill Launch."""
  def can_handle(self, handler_input):
    return is_request_type("LaunchRequest")(handler_input)

  def handle(self, handler_input):
    print("LaunchRequest Karl à ton écoute")
    speech_text = "Karl à ton écoute"

    handler_input.response_builder.speak(speech_text).set_should_end_session(False)
    return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
  """Handler for Help Intent."""
  def can_handle(self, handler_input):
    return is_intent_name("AMAZON.HelpIntent")(handler_input)

  def handle(self, handler_input):
    print("HelpIntent")
    speech_text = "Tu peux me dire bonjour!"

    handler_input.response_builder.speak(speech_text).set_should_end_session(False)
    return handler_input.response_builder.response

class CancelOrStopIntentHandler(AbstractRequestHandler):
  """Single handler for Cancel and Stop Intent."""
  def can_handle(self, handler_input):
    return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
            is_intent_name("AMAZON.StopIntent")(handler_input))

  def handle(self, handler_input):
    print("CancelOrStopIntent")
    speech_text = "Bye!"
    # requests.get(url="http://0.0.0.0:8000/alexa/player/stop")
    handler_input.response_builder.speak(speech_text).set_should_end_session(True)
    return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
  """Handler for Session End."""
  def can_handle(self, handler_input):
    return is_request_type("SessionEndedRequest")(handler_input)

  def handle(self, handler_input):
    print("SessionEndedRequest")
    # requests.get(url="http://0.0.0.0:8000/alexa/player/stop")
    return handler_input.response_builder.response

class CatchAllExceptionHandler(AbstractExceptionHandler):
  """Catch all exception handler, log exception and
  respond with custom message.
  """
  def can_handle(self, handler_input, exception):
    return True

  def handle(self, handler_input, exception):
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
import logging
from django.http import HttpResponse
from django.shortcuts import render  # noqa

logger = logging.getLogger(__name__)


#  Create your views here.
def index(request):
    from django.conf import settings

    print(settings.BASE_DIR)  # MY_PATH/proy_gestor/proy_gestor
    
    logger.error(f"Demo logging INFO | {settings.CONFIG_LOAD}", extra={"opcion_1": "anything", "variable_a": "abc"})
    logger.warning(f"Demo logging WARNING | {settings.CONFIG_LOAD}", extra={"opcion_2": "anything", "variable_b": "bbccd"})

    return HttpResponse("Bienvenidos al app base")


#  Create your views here.
def loggerDefault(request):
    
    logging.debug("I am ignored | this is a DEBUG")
    logging.info("I am a breadcrumb | this is a INFO")
    logging.warning("An exception | this is WARNING", extra=dict(bar=43, foo=66))
    logging.error("I am an event | this is ERROR", extra=dict(bar=43))
    logging.exception("An exception happened")
    
    return HttpResponse("Se disparo logging por default")

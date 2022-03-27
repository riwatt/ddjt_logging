"""ddjt_logging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import HttpResponse
import datetime

import logging
import sys

logger = logging.getLogger('this.is.my.logger')


def current_datetime(request):
    now = datetime.datetime.now()
    print("%s --- start ----" % now, file=sys.stderr)
    logger.debug("%s debug here", now)
    logger.info("%s info here", now)
    logger.warning("%s warning here", now)
    logger.error("%s error here", now)
    logger.critical("%s critical here", now)
    print("%s ---  end  ----" % now, file=sys.stderr)
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


urlpatterns = [
    path('', current_datetime),
]

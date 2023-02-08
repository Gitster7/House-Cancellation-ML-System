"""
WSGI config for HouseCancellation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HouseCancellation.settings')

application = get_wsgi_application()

# ML registry
import inspect
from ml.registry import MLRegistry
from ml.cancel_classifier import Classifier

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = Classifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="cancel_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Omkar Vatsa",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(Classifier))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))

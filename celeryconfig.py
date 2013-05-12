import os


## Broker settings
BROKER_URL = "amqp://%s:%s@pzcluster-0" % (os.environ["RABBITMQ_USERNAME"], os.environ["RABBITMQ_PASSWORD"])


# List of modules to import when celery starts.
CELERY_IMPORTS = ("tasks", )

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = "amqp"

CELERY_ANNOTATIONS = {"tasks.make_pi": {"rate_limit": "1/s"}}

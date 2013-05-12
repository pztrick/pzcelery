from celery import Celery, current_task
import os

rabbitmq_username = os.environ["RABBITMQ_USERNAME"]
rabbitmq_password = os.environ["RABBITMQ_PASSWORD"]
celery = Celery('tasks', backend='amqp', broker="amqp://%s:%s@pzcluster-0" % (rabbitmq_username, rabbitmq_password))


@celery.task
def make_pi(number_of_digits):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    ret = ''
    length = 0
    while length < number_of_digits:
        if 4 * q + r - t < m * t:
            ret += str(m)
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2
        length = len(ret)
    return dict(hostname=current_task.request.hostname, result=ret[:1] + '.' + ret[1:])

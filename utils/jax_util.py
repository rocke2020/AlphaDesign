import jax
from .log_util import logger

def check_gpu_count():
    """ Returns: 0 means no gpu """
    if jax.default_backend() == 'gpu':
        return jax.local_device_count()
    else:
        logger.info('no gpu, use CPU!')
        return 0


def get_gpu_device_id(gpu_device_id:str):
    """ if int(gpu_device_id) >= gpu_count, that's too large, use gpu_device_id = '0' """
    gpu_count = check_gpu_count()
    if int(gpu_device_id) >= gpu_count:
        gpu_device_id = '0'
    logger.info('gpu_device_id %s', gpu_device_id)
    return gpu_device_id
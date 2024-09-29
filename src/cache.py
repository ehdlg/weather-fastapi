from redis import Redis

from constants import REDIS_HOST, REDIS_PORT, REDIS_PWD

r = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PWD)


def get_cache(url):
    cached_data = r.get(url)

    return cached_data


def set_cache(url, data):
    # 12h
    return r.set(url, data, ex=12 * 60 * 60)

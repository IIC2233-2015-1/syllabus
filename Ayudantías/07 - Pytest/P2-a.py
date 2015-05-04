__author__ = 'patricio_lopez'


def random_ip():
        from random import randint
        return ".".join([str(randint(0, 255)) for x in range(0, 4)])


def test_random_ip():
    ip = random_ip()
    ip_parts = ip.split('.')
    assert len(ip_parts) == 4

    for numero in ip_parts:
        assert 0 <= int(numero) <= 255

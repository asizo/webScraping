import random
import os


def interval() -> int:
    """
    페이지 이동 간에 인터벌 시간 리턴
    :return:
    """
    [minSec, maxSec] = list(os.environ.get('PAGE_MOVE_INTERVAL').split(', '))
    return int(random.randrange(int(minSec), int(maxSec)))
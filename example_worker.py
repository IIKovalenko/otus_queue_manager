import queue_manager as qm

from example import get_queue_manager


if __name__ == '__main__':
    queue_client = get_queue_manager()
    queue_client.start_worker()

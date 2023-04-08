import argparse, os
from datetime import datetime


DATE_TIME = "%Y_%m_%d %H:%M:%S"


class ArgparseUtil(object):
    """
    参数解析工具类
    """
    def __init__(self):
        """ Basic args """
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--seed", default=2, type=int)
        self.parser.add_argument('--gpu_device_id', default=0, type=str, help='the GPU NO.')

    def batch_runner(self):
        """ task args """
        self.parser.add_argument("--reverse", type=int, default=0, help="0 is false, 1 is true")
        self.parser.add_argument("--parts_num", type=int, default=1, help="NB: starts from 1")
        self.parser.add_argument("--total_parts", type=int, default=2, help="input file total parts num")
        args = self.parser.parse_args()
        return args


def save_args(args, output_dir='.', with_time_at_filename=False):
    os.makedirs(output_dir, exist_ok=True)

    t0 = datetime.now().strftime(DATE_TIME)
    if with_time_at_filename:
        out_file = os.path.join(output_dir, f"args-{t0}.txt")
    else:
        out_file = os.path.join(output_dir, f"args.txt")
    with open(out_file, "w", encoding='utf-8') as f:
        f.write(f'{t0}\n')
        for arg, value in vars(args).items():
            f.write(f"{arg}: {value}\n")


def log_args(args, logger):
    for arg, value in vars(args).items():
        logger.info(f"{arg}: {value}")

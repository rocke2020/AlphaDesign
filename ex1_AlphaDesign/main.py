import nni
import os
import sys
sys.path.append(os.path.abspath('.'))
from ex1_AlphaDesign.parser import create_parser
import random
import numpy as np
import torch
from utils.log_util import logger


def SetSeed(seed,det=True):
    """function used to set a random seed
    Arguments:
        seed {int} -- seed number, will set to torch, random and numpy
    """
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    np.random.seed(seed)
    if det:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


if __name__ == '__main__':
    """ python main.py --method AlphaDesign --data_name UP000000437_7955_DANRE_v2 --ex_name AlphaDesign_DANRE """
    args = create_parser().parse_args()

    config = args.__dict__
    # tuner_params = nni.get_next_parameter()
    # config.update(tuner_params)
    if not args.joint_data: 
        if args.limit_length == 1:
            prefix = 'SL'
        else:
            prefix = 'SF'
    else:
        if args.limit_length == 1:
            prefix = 'JL'
        else:
            prefix = 'JF'
    if args.search:
        config['ex_name'] = prefix+'_'+ args.method+'_'+args.data_name#+'_{}'.format(args.epoch_e)
    logger.info(args)

    SetSeed(args.seed)
    
    from ex1_AlphaDesign.engine_ADesign import Exp
    exp = Exp(args)
    logger.info('>>>>>>>start training >>>>>>>>>>>>>>>>>>>>>>>>>>')
    exp.train(args)
    
    # logger.info('>>>>>>>testing <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # exp.model.load_state_dict(torch.load(os.path.join(exp.path, 'checkpoint.pth')))

    # with torch.no_grad():
    #     num_correct = exp.evaluate(exp.test_loader, 'test')
    # logger.info("Final | perplexity: {0:.7f}\n".format(num_correct))
    # logger.info("Final | perplexity: {0:.7f}\n".format(num_correct))

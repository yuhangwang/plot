from plot.canvas import create
from plot.parameter import update
import os


def test():
    here = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(here, 'config', 'in1.yaml')
    answer = create(update(config_file))
    assert len(answer['canvas']['axes']) == answer['global']['figure']['rows']
    assert len(answer['canvas']['axes'][0]) == answer['global']['figure']['columns']
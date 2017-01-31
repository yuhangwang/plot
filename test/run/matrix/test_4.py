import os
import plot


def test():
    here = os.path.dirname(os.path.realpath(__file__))
    config = os.path.join(here, 'config', 'in4.yaml')
    preview = True
    answer = plot.run(config, preview)
    assert answer is True

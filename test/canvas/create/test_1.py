from plot.canvas import create

def test():
    here = os.path.dirname(os.path.realpath(__file__))
    config = os.path.join(here, 'config', 'in1.yaml')
    preview = True
    answer = create(config, preview)
    assert answer is True
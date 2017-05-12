from plot.tk.dictTK import wrap_value


def test():
    d1 = {'text': [{'content': 'text 101'}], 'which panel': [0, 0]}
    solution = {
        'text': [{'content': {'v': 'text 101'}}],
        'which panel': {'v': [0, 0]}
    }
    assert wrap_value(d1) == solution

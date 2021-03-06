import plot.io.input.postprocessing.assort_plots_by_type as M


def test():
    p = {
        "data": [
            {"plot_type": "line"},
            {"plot_type": "matrix"},
        ],
        "internal": {
            "user": {
                "plots": {
                    "line": [],
                    "matrix": []
                }
            }
        }

    }
    answer = M.assort_plots_by_type(p)
    assert answer['internal']['user']['plots']['line'] == [0]
    assert answer['internal']['user']['plots']['matrix'] == [1]

"""
Extract legend handle/label lists
"""
from typging import List


def extract_legend_handles_labels(handle_label_pairs):
    # type: (List) -> List
    """Extract legend handles/labels

    Extract legend handles/labels and
    filter out those with None values.

    Args:
        handle_label_pairs (list): list of pairs
            of handles and labels
    Returns:
        two lists: handle list and label list
    """
    def tail(xs): return xs[1:]

    def aux(pairs, handles, labels):
        # type: (List, List, List) -> List
        if len(pairs) == 0:
            return (handles, labels)
        else:
            k, v = paris[0]
            if (k is not None) and (v is not None):
                return aux(
                    tail(pairs),
                    handles + [k],
                    values + [v])
            else:
                return aux(tail(pairs), handles, values)
    return aux(handle_label_pairs, [] [])

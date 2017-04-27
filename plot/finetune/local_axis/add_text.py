"""
Add text annotation to each panel
"""
import matplotlib


def add_text(params: dict) -> dict:
    for panel_id, p in params['local'].items():
        for t in p['text']:
            if t['content'] is not None:
                obj_axis = params['internal']['canvas']['axes'][panel_id]
                matplotlib.pyplot.figtext(
                    t["x"],
                    t["y"],
                    t["content"],
                    axes=obj_axis,
                    alpha=t["opacity"],
                    fontsize=t["font"]["size"],
                    color=t["font"]["color"],
                    rotation=t["rotation"],
                    backgroundcolor=t["background"]["color"],
                    horizontalalignment=t["alignment"]["horizontal"],
                    verticalalignment=t["alignment"]["vertical"],
                    )
    return params

from brand_shoes import jordans, nikes, vans, yeezys, pradas
from credentials import var_global


def print_shoes():
    """
    To call each function brand to print its shoes
    """
    if var_global.pick == 1:
        jordans.display_jordans()

    elif var_global.pick == 2:
        nikes.display_nikes()

    elif var_global.pick == 3:
        yeezys.display_yeezys()

    elif var_global.pick == 4:
        vans.display_vans()

    elif var_global.pick == 5:
        pradas.display_pradas()

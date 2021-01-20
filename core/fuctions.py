from pandastable.core import Table
import pandas as pd


class MyTable(Table):
    """
      # https://readthedocs.org/projects/pandastable/downloads/pdf/latest/
      Custom table class inherits from Table.
      You can then override required methods
     """

    def __init__(self, parent=None, **kwargs):
        Table.__init__(self, parent, **kwargs)
        return


def show_aux_table(frame, df, **kwds):
    """muestra la tabla de escolaridades registradas y su numero de alumnos"""
    pt = MyTable(frame, dataframe=df, **kwds)
    pt.show()
    return pt


def make_table(frame, path, **kwds):
    """crea una tabla simple"""

    df = pd.read_json(path)
    pt = MyTable(frame, dataframe=df, **kwds)
    pt.show()
    return pt
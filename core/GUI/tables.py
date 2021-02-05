from pandastable.core import Table


class MyTable(Table):

    def __init__(self, parent=None, **kwargs):
        Table.__init__(self, parent, **kwargs)
        return


def make_table(frame, table, **kwds):
    pt = MyTable(frame, dataframe=table, **kwds)
    pt.autoResizeColumns()
    pt.expandColumns()
    pt.show()
    return pt

from ..ast.base import Base, _make_name, ASTCacheKey

from .. import operations
from .bv import BV


class Array(Base):
    """
    Base class that represent the AST of an Array object and implements all the operation useful to create and modify the AST.
    """

    __slots__ = ()

    def __getitem__(self, index):
        if type(index) is BV:
            return ArrayIndex(index, self)
        else:
            raise ValueError("Only bitvectors are allowed for array indexing")

def ArrayS(name, dom, rng):
    if type(name) is bytes:
        name = name.decode()
    if type(name) is not str:
        raise TypeError("Name value for Array must be a str, got %r" % type(name))

    name = _make_name(name, -1)

    return Array('Array', (name, dom, rng), variables={name}, symbolic=True)



ArrayIndex = operations.op('ArrIndex', (BV, Array), BV, calc_length=operations.arrindex_length_calc)
Store = operations.op('ArrStore', (Array, BV, BV), Array)

Array.Index = staticmethod(ArrayIndex)
Array.Store = staticmethod(Store)

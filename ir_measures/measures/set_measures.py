from ir_measures import measures
from .base import Measure, ParamInfo


class _SetP(measures.Measure):
    """
    The Set Precision (SetP); i.e., the number of relevant docs divided by the total number retrieved
    """
    __name__ = 'SetP'
    NAME = __name__
    SUPPORTED_PARAMS = {
        'rel': measures.ParamInfo(dtype=int, default=1, desc='minimum relevance score to be considered relevant (inclusive)')
    }

SetP = _SetP()
measures.register(SetP)


class _SetR(measures.Measure):
    """
    The Set Recall (SetR); i.e., the number of relevant docs divided by the total number of relevant documents
    """
    __name__ = 'SetR'
    NAME = __name__
    SUPPORTED_PARAMS = {
        'rel': measures.ParamInfo(dtype=int, default=1, desc='minimum relevance score to be considered relevant (inclusive)')
    }

SetR = _SetR()
measures.register(SetR)

class _SetF(measures.Measure):
    """
    The Set F measure (SetF); i.e., the harmonic mean of SetP and SetR
    """
    __name__ = 'SetF'
    NAME = __name__
    SUPPORTED_PARAMS = {
        'rel': measures.ParamInfo(dtype=int, default=1, desc='minimum relevance score to be considered relevant (inclusive)'),
        'beta': measures.ParamInfo(dtype=float, default=1., desc='relative importance of R to P in the harmonic mean'),
    }

SetF = _SetF()
measures.register(SetF)

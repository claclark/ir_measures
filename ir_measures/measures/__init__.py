registry = {}
def register(measure, aliases=[], name=None):
    if name is None:
        name = measure.__name__
    assert name not in registry
    registry[name] = measure
    for alias in aliases:
        assert alias not in registry
        registry[alias] = measure
    return registry

from .base import Measure, ParamInfo, MultiMeasures, MeanAgg, SumAgg
from .ap import AP, MAP, _AP
from .bpref import Bpref, BPref, _Bpref
from .err import ERR, _ERR
from .infap import infAP, _infAP
from .iprec import IPrec, _IPrec
from .judged import Judged, _Judged
from .ndcg import nDCG, NDCG, _nDCG
from .numq import NumQ, _NumQ
from .numrel import NumRel, _NumRel
from .numret import NumRet, NumRelRet, _NumRet
from .p import P, _P
from .r import R, _R
from .rbp import RBP, _RBP
from .rprec import Rprec, RPrec, _Rprec
from .rr import RR, MRR, _RR
from .set_measures import SetP, _SetP, SetR, _SetR, SetF, _SetF
from .success import Success, _Success

# enable from "ir_measures.measures import *" --- on purpuse, do not include _-prefixed versions,
# as these are intended for internal use
__all__ = list(registry.keys())

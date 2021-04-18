from ir_measures import measures
from .base import BaseMeasure, ParamInfo


class _P(measures.BaseMeasure):
	"""
	Basic measure for that computes the percentage of documents in the top cutoff results
	that are labeled as relevant. cutoff is a required parameter, and can be provided as
	P@cutoff.
	"""
    __name__ = 'P'
    SUPPORTED_PARAMS = {
        'cutoff': measures.ParamInfo(dtype=int, required=True, desc='ranking cutoff threshold'),
        'rel': measures.ParamInfo(dtype=int, default=1, desc='minimum relevance score to be considered relevant (inclusive)')
    }


P = _P()
measures.register(P)

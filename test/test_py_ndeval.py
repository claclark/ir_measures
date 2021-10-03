import unittest
import itertools
import ir_measures


class TestPytrecEval(unittest.TestCase):

    def test_ERR_IA(self):
        qrels = list(ir_measures.util.parse_trec_qrels('''
0 0 D0 0
0 0 D1 1
0 0 D2 1
0 1 D2 1
0 1 D3 2
0 0 D4 0
1 0 D0 1
1 0 D3 2
1 1 D5 2
'''))
        run = list(ir_measures.util.parse_trec_run('''
0 0 D0 1 0.8 run
0 0 D2 2 0.7 run
0 0 D1 3 0.3 run
0 0 D3 4 0.4 run
0 0 D4 5 0.1 run
1 0 D1 1 0.8 run
1 0 D3 2 0.7 run
1 0 D4 3 0.3 run
1 0 D2 4 0.4 run
'''))
        provider = ir_measures.providers.PyNdEvalProvider()
        measure = ir_measures.ERR_IA@20
        result = list(provider.iter_calc([measure], qrels, run))
        self.assertEqual(result[0].query_id, "0")
        self.assertAlmostEqual(result[0].value, 0.4659, places=4)
        self.assertEqual(result[1].query_id, "1")
        self.assertAlmostEqual(result[1].value, 0.1803, places=4)
        self.assertAlmostEqual(provider.calc_aggregate([measure], qrels, run)[measure], 0.3231, places=4)



if __name__ == '__main__':
    unittest.main()
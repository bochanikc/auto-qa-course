import tasks

class TestTasks:
    result = tasks.Solution()

    def test_mid_of_sum_devided(self):
        assert self.result.mid_of_sum_devided(-5, 12) == 4.5
    
    def test_percent_of_GC(self):
        assert self.result.percent_of_GC('acggtgttat') == 40.0
    
    def test_code_DNC(self):
        assert self.result.code_DNC('abasdasfsfsdafsdfdssdsddssdfdFSGFJGsdygeuywgdfaedcGDETFTFEUYGDFCc') == '1a1b1a1s1d1a1s1f1s1f1s1d1a1f1s1d1f1d2s1d1s2d2s1d1f1d1F1S1G1F1J1G1s1d1y1g1e1u1y1w1g1d1f1a1e1d1c1G1D1E1T1F1T1F1E1U1Y1G1D1F1C1c'
    
    def test_digits_count_more_one(self):
        assert self.result.return_sequence(7) == '1 2 2 3 3 3 4 '

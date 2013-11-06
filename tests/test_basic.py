import sqer

class FakeRecord(object):
    def __init__(self, sequence, name=''):
        self.sequence = sequence
        self.name = name

def test_sum_bp():
	r = FakeRecord('ATGC')
	count = sqer.sum_bp(r)
	assert count == 4, count

def test_sum_bp_records():
    rl = [ FakeRecord("A"), FakeRecord("G") ]
    assert sqer.sum_bp_records(rl) == 2

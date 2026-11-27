from src.instrument import Instrument

DMM = Instrument('DMM-100', 'dmm', 'V', 0.0, 100.0, 0.01, 0.002)


def test_covers_range():
    assert DMM.covers(0.0, 50.0)
    assert not DMM.covers(0.0, 150.0)


def test_uncertainty():
    expected = 28.0 * 0.0001 + 0.002
    assert abs(DMM.uncertainty_at(28.0) - expected) < 1e-9

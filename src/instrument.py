from dataclasses import dataclass


@dataclass(frozen=True)
class Instrument:
    name: str
    kind: str
    unit: str
    range_min: float
    range_max: float
    acc_pct_reading: float
    acc_offset: float
    role: str = 'measure'

    def covers(self, low: float, high: float) -> bool:
        return self.range_min <= low and high <= self.range_max

    def uncertainty_at(self, value: float) -> float:
        return abs(value) * self.acc_pct_reading / 100.0 + self.acc_offset

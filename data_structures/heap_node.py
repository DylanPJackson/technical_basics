import functools


@functools.total_ordering
class HeapNode:
    """
    Presently used as part of min-heap in Djikstra's.
    """
    def __init__(self, label: str, val: int):
        self.label = label
        self.val = val

    def _is_valid_operand(self, other):
        return hasattr(other, "label") and hasattr(other, "val")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.val == other.val

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.val < other.val

    def __gt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.val > other.val

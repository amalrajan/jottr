from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class ResponseModel:
    status: str
    message: str
    data: dict
    timestamp: str = None

    def __post_init__(self):
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return asdict(self)

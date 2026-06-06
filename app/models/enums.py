import enum

class UserRole(str, enum.Enum):
    admin = "admin"
    domain_expert = "domain expert"
    candidate = "candidate"

class Difficulty(str, enum.Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class TestStatus(str, enum.Enum):
    draft = "draft"
    published = "published"

class AttemptStatus(str, enum.Enum):
    in_progress = "in_progress"
    submitted = "submitted"
class Episode:
    def __init__(self, id: str, title: str, topic: str, episode_number: int, planned_date: str, status: str, guests: list):
        self.id = id
        self.title = title
        self.topic = topic
        self.episode_number = episode_number
        self.planned_date = planned_date  # ISO format
        self.status = status  # Draft | Scripted | Published
        self.guests = guests  # List of Guest IDs

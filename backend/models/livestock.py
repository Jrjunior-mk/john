class Livestock:
    def __init__(self, id, name, type, description, feed_requirement, water_requirement, maturity_age):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.feed_requirement = feed_requirement
        self.water_requirement = water_requirement
        self.maturity_age = maturity_age
        self.created_at = '2026-02-13 09:12:14'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'feed_requirement': self.feed_requirement,
            'water_requirement': self.water_requirement,
            'maturity_age': self.maturity_age,
            'created_at': self.created_at
        }
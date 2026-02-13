class Crop:
    def __init__(self, id, name, description, growing_season, maturity_days, water_requirement, soil_type, created_at):
        self.id = id
        self.name = name
        self.description = description
        self.growing_season = growing_season
        self.maturity_days = maturity_days
        self.water_requirement = water_requirement
        self.soil_type = soil_type
        self.created_at = created_at
        self.diseases = []  # List of disease objects
        self.prevention_methods = []  # List of prevention method objects

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'growing_season': self.growing_season,
            'maturity_days': self.maturity_days,
            'water_requirement': self.water_requirement,
            'soil_type': self.soil_type,
            'created_at': self.created_at,
            'diseases': [disease.to_dict() for disease in self.diseases],
            'prevention_methods': [method.to_dict() for method in self.prevention_methods],
        }

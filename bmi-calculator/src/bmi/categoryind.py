from enum import Enum
# Enum class
class CategoryInd(Enum):
    CAT1 = 'Underweight,Malnutrition risk'
    CAT2 = 'Normal weight,Low risk'
    CAT3 = 'Overweight,Enhanced risk'
    CAT4 = 'Moderately obese,Medium risk'
    CAT5 = 'Severely obese,High risk'
    CAT6 = 'Very severely obese,Very high risk'

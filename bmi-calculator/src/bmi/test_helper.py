import unittest
import helper
from categoryind import CategoryInd

class TestHelper(unittest.TestCase):
    def test_calculate_bmi(self):
        mass_kg = 75
        height_m = 1.75    
        assert helper.calculate_bmi(mass_kg,height_m) == 24.5


    def test_fetch_bmi_category_indicator(self):      
        assert helper.fetch_bmi_category_indicator(18.4) == CategoryInd.CAT1  
        assert helper.fetch_bmi_category_indicator(18.5) == CategoryInd.CAT2
        assert helper.fetch_bmi_category_indicator(18.44) == CategoryInd.CAT1  
        assert helper.fetch_bmi_category_indicator(18.46) == CategoryInd.CAT2
        assert helper.fetch_bmi_category_indicator(25) == CategoryInd.CAT3  
        assert helper.fetch_bmi_category_indicator(30.15) == CategoryInd.CAT4
        assert helper.fetch_bmi_category_indicator(35) == CategoryInd.CAT5  
        assert helper.fetch_bmi_category_indicator(40) == CategoryInd.CAT6
        assert helper.fetch_bmi_category_indicator(29.91) == CategoryInd.CAT3  
        assert helper.fetch_bmi_category_indicator(34.9) == CategoryInd.CAT4
        assert helper.fetch_bmi_category_indicator(39.9) == CategoryInd.CAT5  
        assert helper.fetch_bmi_category_indicator(99) == CategoryInd.CAT6

if __name__ == "__main__":
    unittest.main()
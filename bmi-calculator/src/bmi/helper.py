from categoryind import CategoryInd
 
def calculate_bmi(mass_kg:float, height_m:float):
    """
        The function calculates BMI based on input mass and height.
  
        Parameters:
            mass_kg (float): mass of person in kg
            height_m (float): height of person in m
          
        Returns:
            float: BMI value rounded to 1 decimal place
       """
    return round(mass_kg/pow(height_m,2),1)

def load_person_details(input_json:dict):    
    # Load the data from input argument
    return eval(input_json[0])

def append_bmi_values(person_data:dict):
    """
        The function generates the updated person data after appending the bmi, category and health risk values.
  
        Parameters:
            person_data (dict): dict containing the input json data
          
        Returns:
            dict: Dict which contains additional details of BMI. category and health risk appeneded to the input
       """ 
    
    # Iterate through person data
    for person in person_data:
        
        #Validate Input data
        if person["HeightCm"] == 0 or (type(person["HeightCm"]) != int or type(person["HeightCm"]) == float) or (type(person["WeightKg"]) != int or type(person["WeightKg"]) == float):
            print("Input height is incorrect for the object : "+ str(person))
            continue

        #Calculate BMI
        bmi = calculate_bmi(person["WeightKg"],(person["HeightCm"]/100))

        #Update the person data with BMI details
        person.update(build_bmi_response(bmi))
        
        #Calculate category and health risk based on BMI
        category_ind = fetch_bmi_category_indicator(bmi)
        
        #Update the person data with category and health risk details
        person.update(build_category_ind_response(category_ind.value))

    return person_data

def build_bmi_response(bmi:str):
    """
        The function generates the response for bmi value in key value format so that it can be appended to the dict.
  
        Parameters:
            bmi (str): value containing bmi 
          
        Returns:
            dict: Dict which contains detail of BMI rounded to 2 decimal places.
       """ 
    return {"Bmi":round(float(bmi),2)}

def build_category_ind_response(category_ind:str):  
    """
        The function generates the response for bmi category health risk value in key value format so that it can be appended to the dict.
  
        Parameters:
            category_ind (str): value containing bmi category health risk value
          
        Returns:
            dict: Dict which contains detail of BMI category and health risk.
       """ 
    category_risk_list = category_ind.split(",")
    return {"Category":category_risk_list[0],"HealthRisk":category_risk_list[1]}

def fetch_bmi_category_indicator(bmi:float):
    """
        The function finds the bmi category based on input bmi value.
  
        Parameters:
            bmi_value (float): value containing bmi
          
        Returns:
            enum: CategoryInd Enum which contains detail of BMI category and health risk.
        """
    # Observation : As there is no condition for value between 18.4 and 18.5
    #  if we have 2 decimal places; the BMI value has been rounded to 1 decimal place
    bmi_value = round(bmi,1)
    if bmi_value <= 18.4:
        return CategoryInd.CAT1
    elif bmi_value>=18.5 and bmi_value<=24.9: 
        return CategoryInd.CAT2
    elif bmi_value>=25 and bmi_value<=29.9:
        return CategoryInd.CAT3
    elif bmi_value>=30 and bmi_value<=34.9:
        return CategoryInd.CAT4
    elif bmi_value>=35 and bmi_value<=39.9:
        return CategoryInd.CAT5
    elif bmi_value>=40:
        return CategoryInd.CAT6

def find_people_count_on_category(person_data:dict, category:str):
    """
        The function finds count of people based on category.
  
        Parameters:
            person_data (dict): The dict containing the details of the person data.
            category (str): String containing the category data
          
        Returns:
            int: A number which contains the total count of person in the category.
        """
    count = 0
    for person in person_data:
        person.setdefault('Category', 'Not Present')
        if person["Category"] == category:
            count = count+1
    return count


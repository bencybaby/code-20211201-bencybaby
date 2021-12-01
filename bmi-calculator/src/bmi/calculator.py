import sys
import helper

def main():

    # Read the JSON data as argument. If argument is not present, it throws an error
    if len(sys.argv)>1:
        # Added this method so that we can keep the flexibility of adding new arguments in future if we want to
        data = helper.load_person_details(sys.argv[1:])
    else:
        print("Mandatory Parameter not present")
        exit()

    # Fetch the bmi values for the input data set and generate the updated data
    bmi_updated_data = helper.append_bmi_values(data)

    # Find count of people who are overweight
    count = helper.find_people_count_on_category(bmi_updated_data, "Overweight")
    
    # Print overweight count
    print(count)


if __name__ == "__main__":
    # calling main function
    main()

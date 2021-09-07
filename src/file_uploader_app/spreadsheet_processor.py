import re

class RealEstateSpreadsheetProcessor:
    def __init__(self):
        self.non_decimal_regular_exp = re.compile(r"[^\d.]+")
    
    def process_file(self, list_of_lists):
        processed_list_of_dicts = []
        for row in list_of_lists:
            row_dict = {}
            city, state, zip_code = self._convert_address_to_address_parts(row[0])
            row_dict["Address"] = row[0]
            row_dict["City"] = city
            row_dict["State"] = state
            row_dict["Zip Code"] = zip_code
            row_dict["Date"] = row[1]
            row_dict["Amount"] = self._convert_amount_to_currency(row[2], row[3])
            row_dict["Notes"] = row[4]
            processed_list_of_dicts.append(row_dict)
        
        return processed_list_of_dicts
    
    def _convert_amount_to_currency(self, entry, string_amount):
        string_amount_clean = self.non_decimal_regular_exp.sub("", string_amount)
        amount = "$" + string_amount_clean
        if entry == 'Debit':
            amount = "-" + amount
        
        return amount

    def _convert_address_to_address_parts(self, address):
        if address.find(",") == -1:
            return "City", "State", "Zip Code"
        first_comma = address.find(",") + 1
        second_comma = address.find(",", first_comma) + 1
        third_comma = address.find(",", second_comma) + 1
        city = address[first_comma:second_comma-1]
        state = address[second_comma:third_comma-1]
        zip_code = address[third_comma:]

        return city.strip(), state.strip(), zip_code.strip()
    

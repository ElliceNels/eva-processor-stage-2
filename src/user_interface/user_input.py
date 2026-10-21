from datetime import datetime
class UserInput:

    @staticmethod
    def receive_country():
        input_value = UserInput._receive_user_input()
        cleaned_input = UserInput._clean_input(input_value)
        return cleaned_input
    
    @staticmethod
    def receive_year():
        validated_year = None 
        while validated_year is None:
            input_value = UserInput._receive_user_input()
            cleaned_input = UserInput._clean_input(input_value)
            validated_year = UserInput._validate_year_input(cleaned_input)
        return validated_year
        
    @staticmethod
    def _receive_user_input():
        user_input = input()
        return user_input

    @staticmethod
    def _clean_input(inp):
        return inp.strip().lower()

    @staticmethod
    def _validate_year_input(inp):
        try:
            year = int(inp)
            current_year = datetime.now().year
            # Assume that the year should be a positive integer and not in the future
            if year > current_year or year < 0:
                return None
            else:
                return year
        except ValueError:
            return None

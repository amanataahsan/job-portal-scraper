import string

def parse_classification(input_string: str):
    translation_table = str.maketrans("", "", string.punctuation)
    formatted_string = input_string.translate(translation_table)
    result_string =  "-".join(formatted_string.split()).lower()

    return result_string
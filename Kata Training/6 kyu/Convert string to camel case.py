import re


def to_camel_case(text):
    text_list = re.split('-|_', text)
    result_text = text_list[0]
    for word in range(1, len(text_list)):
        result_text += text_list[word].capitalize()
    return result_text

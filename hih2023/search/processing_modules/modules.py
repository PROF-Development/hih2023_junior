import json
import difflib


def get_matches(name: str, check_name: str):
    arr_name: list = name.split()
    arr_check_name: list = check_name.split()
    matches_count = 0
    for j in range(0, len(arr_check_name)):
        matches = False
        for i in range(0, len(arr_name)):
            matches_percent: float = float(difflib.SequenceMatcher(a=arr_name[i].lower(), b=arr_check_name[j].lower()).ratio())
            if matches_percent >= 0.80:
                matches = True
                break
        if matches:
            matches_count += 1

    if len(arr_check_name) != 0 and matches_count / len(arr_check_name) >= 0.5:
        return True
    else:
        return False


def find_matches_keywords(current_data_keywords, searching_document_keywords):
    for i in range(0, len(searching_document_keywords)):
        for j in range(0, len(current_data_keywords)):
            if difflib.SequenceMatcher(a=searching_document_keywords[i].lower(), b=current_data_keywords[j].lower()).ratio() >= 0.8:
                return True
    return False


def search_documents(searching_document: dict) -> dict:
    found_documents = {}
    with open("./data/data.json", "r", encoding="utf-8") as file:
        data: dict = json.load(file)

    for number_of_document in data.keys():
        current_data: dict = data[number_of_document]

        if current_data["document_name"] == searching_document["document_name"]:
            found_documents[number_of_document] = current_data
            break
        if get_matches(current_data["document_name"], searching_document["document_name"]):
            found_documents[number_of_document] = current_data

        for element_of_document in current_data.keys():
            if searching_document.get(element_of_document) is not None:
                if current_data[element_of_document] == searching_document[element_of_document]:
                    # TODO: Нужно продумать боллее логичную систему отбора данных по критериям
                    found_documents[number_of_document] = current_data
                    break
                if element_of_document == "key_words":
                    searching_data_keywords: list = searching_document[element_of_document].split()
                    current_data_keywords: list = current_data[element_of_document].split(", ")

                    if find_matches_keywords(current_data_keywords, searching_data_keywords):
                        found_documents[number_of_document] = current_data

    return found_documents


def get_documents(searching_document: dict) -> dict:
    return search_documents(searching_document)

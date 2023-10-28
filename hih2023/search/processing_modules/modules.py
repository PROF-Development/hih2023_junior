import json
import difflib


def get_matches(name: str, check_name: str):
    arr_name: list = name.split()
    arr_check_name: list = check_name.split()
    matches_count = 0
    for j in range(0, len(arr_check_name)):
        matches = False
        for i in range(0, len(arr_name)):
            matches_percent: float = float(difflib.SequenceMatcher(a=arr_name[i], b=arr_check_name[j]).ratio())
            if matches_percent >= 0.80:
                matches = True
                break
        if matches:
            matches_count += 1

    if matches_count / len(arr_check_name) >= 0.5:
        return True
    else:
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

    return found_documents


def get_documents(searching_document: dict) -> dict:
    return search_documents(searching_document)

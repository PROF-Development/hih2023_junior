import json


def search_documents(searching_document: dict) -> dict:
    found_documents = {}
    with open("./data/data.json", "r", encoding="utf-8") as file:
        data: dict = json.load(file)

    for number_of_document in data.keys():
        current_data: dict = data[number_of_document]
        for element_of_document in current_data.keys():
            if searching_document.get(element_of_document) is not None:
                if current_data[element_of_document] == searching_document[element_of_document]:
                    # TODO: Нужно продумать боллее логичную систему отбора данных по критериям
                    found_documents[number_of_document] = current_data
                    break

    return found_documents


def get_documents(searching_document: dict) -> dict:
    return search_documents(searching_document)

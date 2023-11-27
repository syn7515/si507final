import xml.etree.ElementTree as ET
import json
import requests
import xmltodict
import pprint

GAMEGEEK = "https://boardgamegeek.com/xmlapi2/"


def xml_api_to_dict(url):
    """
    Fetches XML data from an API and converts it into a dictionary.

    Args:
    url (str): The URL of the XML API endpoint.

    Returns:
    dict: A dictionary representation of the API's XML response.
    """
    response = requests.get(url)
    data = xmltodict.parse(response.content)

    return data


def write_json(filepath, data, encoding="utf-8", ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.
        encoding (str): name of encoding used to encode the file.
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON.

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    url = GAMEGEEK + "thing?id=1023"
    dict_data = xml_api_to_dict(url)

    write_json("sampleData.json", [dict_data])


if __name__ == "__main__":
    main()

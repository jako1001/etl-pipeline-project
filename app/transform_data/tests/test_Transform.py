import pandas as pd
import re


def test_csv_to_dataframe() -> None:
    test_df = pd.DataFrame(
        [
            {
                "first_name": "Joanie",
                "last_name": "Kirsop",
                "email": "jkirsop0@vkontakte.ru",
                "phone_number": "560-141-8153",
                "address": "4 Sloan Place",
            }
        ]
    )

    df = pd.read_csv("./app/transform_data/tests/test.csv")

    assert test_df.equals(df)


def test_unstructured_email_and_number_to_dataframe() -> None:
    test_email = ["meldritt3@so-net.ne.jp"]
    test_phone_number = ["628-519-9481"]

    with open("./app/transform_data/tests/test.txt") as f:
        text = f.read()

        email = re.findall(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", text
        )
        phone_number = re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)

    assert test_email == email
    assert test_phone_number == phone_number

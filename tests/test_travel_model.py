import pytest
from pydantic import ValidationError
from models.travel_model import TravelInfoRequest, TravelInfoResponse


# TravelInfoRequest

def test_travel_info_request_requires_all_fields():
    with pytest.raises(ValidationError):
        TravelInfoRequest(country_from="France")


def test_request_consists_all_fields():
    request = TravelInfoRequest(
        country_from="France",
        country_to="Germany",
        is_capital=True,
        is_weather=True,
        is_currency=False
    )

    assert request.country_from == "France" #check if field country_from is set correctly
    assert request.country_to == 'Germany'
    assert request.is_capital is True
    assert request.is_currency is False
    assert request.is_weather is True


# TravelInfoResponse

# The decorator tells Pytest:
# "Run the following function multiple times,
# each time with a new pair of values."

@pytest.mark.parametrize(
    "field, invalid_value",
    [
        ("currency_code_from", "EUR" * 100),
        ("currency_code_to", ""),
        ("currency_code_from", 123),
        ("currency_code_to", True),
        ("currency_name_from", True),
        ("currency_name_to", 1500),
        ("exchange_rate", "bla"),
    ]
)
def test_response_invalid_fields(field, invalid_value):
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            country_from="France",
            country_to="Germany",
            **{field: invalid_value}
        )


def test_response_without_required_fields():
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            capital_to=None,
            currency_code_from=None,
            currency_code_to=None,
            weather=None,
            currency_name_from=None,
            currency_name_to=None
        )


@pytest.mark.parametrize(
    "field, valid_value",
    [
        ("currency_code_from", "EUR"),
        ("currency_code_to", "USD"),
        ("currency_name_from", "Euro"),
        ("currency_name_to", "US Dollar"),
        ("exchange_rate", 1.25),
    ]
)
def test_response_valid_fields(field, valid_value):
    response = TravelInfoResponse(
        country_from="France",
        country_to="Germany",
        **{field: valid_value}
    )

    assert getattr(response, field) == valid_value #«Возьми у объекта response атрибут, имя которого находится в переменной field».

import pytest
from pydantic import ValidationError

from models.travel_model import TravelInfoRequest, TravelInfoResponse

# TODO: Add tests for TravelInfoRequest and TravelInfoResponse

def test_travel_info_request_requires_all_fields():
    with pytest.raises(ValidationError):
        TravelInfoRequest(country_from="France")

def test_request_consists_all_fields():
    TravelInfoRequest(country_from="France", country_to="France",is_capital=True, is_weather=True,is_currency=False)



def test_response_field_length_currency_code_from():
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            country_from="France",
            country_to="Germany",
            currency_code_from="EUR"*100
        )
def test_response_field_length_currency_code_to():
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            country_from="France",
            country_to="Germany",
            currency_code_to=""
        )



def test_response_without_required_fields():
    with pytest.raises(ValidationError):
        TravelInfoResponse(capital_to=None, currency_code_from=None,currency_code_to=None,weather=None,currency_name_from=None,currency_name_to=None)


def test_response_currency_code_from_is_str():
    TravelInfoResponse(
        country_from="France",
        country_to="Germany",
        currency_code_from="EUR")

def test_response_currency_code_from_is_str2():
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            country_from="France",
            country_to="Germany",
            currency_code_from=123
        )



def test_response_currency_code_to_is_str():
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            country_from="France",
            country_to="Germany",
            currency_code_to=True)


def test_response_currency_name_from_is_str():
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            country_from="France",
            country_to="Germany",
            currency_name_from=True)



def test_response_currency_name_to_is_str():
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            country_from="France",
            country_to="Germany",
            currency_name_to=1500)


def test_response_exchange_rate_is_float():
    with pytest.raises(ValidationError):
        TravelInfoResponse(
            country_from="France",
            country_to="Germany",
            exchange_rate='bla')
























import pytest

from hseling_api_direct_speech.process import process_data


test_data = [
    ([], []),
]


@pytest.mark.parametrize("input_data, expected_result", test_data)
def test_process_data(input_data, expected_result):
    processed_data = input_data
    assert processed_data == expected_result


def test_process_data_bad_values():
    with pytest.raises(AttributeError):
        assert [contents for _, contents in process_data({"test": 1})]

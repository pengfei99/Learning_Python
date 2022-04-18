import pytest

from learning_python.Lesson01_Basics.Section01_Basic_syntax.src.test_demo.test_with_fixture.display import \
    format_data_for_display


@pytest.mark.test_fixture
def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

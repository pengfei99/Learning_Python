import pytest

from learning_python.Lesson01_Basics.Section01_Basic_syntax.src.test_demo.test_with_fixture.export_csv import \
    format_data_for_excel


@pytest.mark.test_fixture
def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == ["given,family,title",
                                                          "Alfonsa,Ruiz,Senior Software Engineer",
                                                          "Sayid,Khan,Project Manager"]

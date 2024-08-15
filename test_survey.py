from survey import AnonymousSurvey
def test_store_single_response():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses       #测试类

import pytest
from survey import AnonymousSurvey
@pytest.fixture                                 #放在函数前面的装饰器 用于修改后面的函数代码的行为  这个为夹具
def language_survey():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey                      

def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses       #当测试函数的一个形参与应用了装饰器@pytest.fixture 的函数（夹具）同名时，将自动运行夹具，并将夹具返回的值传递给测试函数。

def test_store_three_responses(language_survey):
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
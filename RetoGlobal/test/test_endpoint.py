import requests
import pytest

from prog import check
filetef="../prog/JSONstructure.txt"
comprobar=check.check()
comprobar.addJsonStruct(filetef)


#class Test_endpoint(object):
    
def test_check_structure():
    req=requests.get('http://api.github.com/orgs/pytest-dev')
    assert comprobar.dic.keys()==req.json().keys()
    
def test_check_content():
    req=requests.get('http://api.github.com/orgs/pytest-dev')
    comp=[["login","pytest-dev"],["id",8897583],["public_repos",45],["public_gists",0],["followers",0]]
    for elem in comp:
        comprobar.dic[elem[0]]=elem[1]
        assert comprobar.dic[elem[0]]==req.json()[elem[0]]
        
@pytest.mark.parametrize("test_input,expected",[
    (requests.get('http://api.github.com/orgs/pytest-dev').status_code, 200),
    (requests.get('http://api.github.com/orgs/pytest').status_code, 404),
    (requests.get('http://api.github.com/orgs/').status_code,404),
])
def test_check_status(test_input,expected):
    #req=requests.get('http://api.github.com/orgs/{0}'.format(test_input))
    #assert req.status_code == expected
    assert check_status(test_input)== expected

def check_status(test_input):
    return test_input
                 

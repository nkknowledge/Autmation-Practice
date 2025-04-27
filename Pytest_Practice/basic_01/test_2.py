import pytest



class TestClass:

    @pytest.fixture()  #decorator
    def setup(self):
        print("launching the browser")    #Execute beforeevery test methods
        print("open the application")
        yield
        print("Close the browser")  #Execute after every test methods


    def test_login(self, setup):
        print("this is the Method1")

    def test_search(self, setup):
        print("this is the Method2")

    def test_Advancedsearch(self, setup):
        print("this is the Method3")
from Day18.Assessment_Q1.Q1 import LoginPage

def test_fill_form(setup):
    loginobj = LoginPage(setup)
    loginobj.enter_firstname("Ram")
    loginobj.enter_lastname("s")
    loginobj.enter_jobtitle("Software Engineer")
    loginobj.select_education("high-school")
    loginobj.select_sex("male")
    loginobj.select_experience("5-9")
    loginobj.select_date("02/15/2026")
    loginobj.click_submit()

    assert "thanks" in setup.current_url
    print("Form submitted successfully")

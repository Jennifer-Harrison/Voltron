# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Scenario1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://uat.orthofi.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_scenario1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("automation.testing.tc@orthofi.com")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Password1!")
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        # Create Patient
        driver.find_element_by_link_text("Patients").click()
        driver.find_element_by_css_selector("a.btn.add").click()
        driver.find_element_by_id("FirstName").clear()
        driver.find_element_by_id("FirstName").send_keys("Patient")
        driver.find_element_by_id("LastName").clear()
        driver.find_element_by_id("LastName").send_keys("Automation")
        driver.find_element_by_id("DateOfBirth").clear()
        driver.find_element_by_id("DateOfBirth").send_keys("01012001")
        driver.find_element_by_id("Guardian_UserProfile_FirstName").clear()
        driver.find_element_by_id("Guardian_UserProfile_FirstName").send_keys("Parent1")
        driver.find_element_by_id("Guardian_UserProfile_LastName").clear()
        driver.find_element_by_id("Guardian_UserProfile_LastName").send_keys("Automation")
        driver.find_element_by_id("Guardian_CellPhone").clear()
        driver.find_element_by_id("Guardian_CellPhone").send_keys("3039999999")
        driver.find_element_by_id("Guardian_UserProfile_UserName").clear()
        driver.find_element_by_id("Guardian_UserProfile_UserName").send_keys("parent1.automation@orthofi.com")
        # Insert Exam Type Here
        driver.find_element_by_id("Exam_ExamDate").click()
        driver.find_element_by_id("Exam_ExamTime").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_css_selector("button.btn.submit").click()
        driver.find_element_by_link_text("Dashboard").click()
        driver.find_element_by_name("ExamFilterType").click()
        self.assertEqual("Automation, Patient", driver.find_element_by_link_text("Automation, Patient").text)
        driver.find_element_by_link_text("Complete Forms").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-closethick").click()
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Password1!")
        driver.find_element_by_id("ConfirmPassword").clear()
        driver.find_element_by_id("ConfirmPassword").send_keys("Password1!")
        driver.find_element_by_id("SecurityQuestion").clear()
        driver.find_element_by_id("SecurityQuestion").send_keys("Question")
        driver.find_element_by_id("SecurityAnswer").clear()
        driver.find_element_by_id("SecurityAnswer").send_keys("Answer")
        driver.find_element_by_id("TOS").click()
        driver.find_element_by_css_selector("button.btn.submit").click()
        # Patient Contact Info Form
        try: self.assertEqual("01/01/2001", driver.find_element_by_id("Patient_DateOfBirth").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("Patient_Sex").click()
        driver.find_element_by_id("Patient_Address1").clear()
        driver.find_element_by_id("Patient_Address1").send_keys("99999 Tester Lane")
        driver.find_element_by_id("Patient_PostalCode").clear()
        driver.find_element_by_id("Patient_PostalCode").send_keys("80234")
        driver.find_element_by_id("Patient_City").clear()
        driver.find_element_by_id("Patient_City").send_keys("Denver")
        Select(driver.find_element_by_id("Patient_StateTerritory_Abbreviation")).select_by_visible_text("Colorado")
        driver.find_element_by_css_selector("option[value=\"CO\"]").click()
        driver.find_element_by_id("Guardian_DateOfBirth").clear()
        driver.find_element_by_id("Guardian_DateOfBirth").send_keys("02021972")
        driver.find_element_by_id("Guardian_Sex").click()
        driver.find_element_by_id("SameAsPatient").click()
        try: self.assertEqual("99999 Tester Lane", driver.find_element_by_id("Guardian_Address1").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("80234", driver.find_element_by_id("Guardian_PostalCode").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Denver", driver.find_element_by_id("Guardian_City").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(//input[@id='Guardian_MaritalStatus'])[2]").click()
        driver.find_element_by_xpath("(//input[@id='Guardian_RelationshipToPatient'])[2]").click()
        try: self.assertEqual("(303)999-9999", driver.find_element_by_id("Guardian_CellPhone").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("(//input[@id='PrimaryContactIsFinanciallyResponsible'])[2]").click()
        driver.find_element_by_id("TreatmentReason").clear()
        driver.find_element_by_id("TreatmentReason").send_keys("Jacked Teeth")
        driver.find_element_by_id("DentistIsNotListed").click()
        driver.find_element_by_id("ReferringDentistOther").clear()
        driver.find_element_by_id("ReferringDentistOther").send_keys("Dr No")
        # Adjust Sliders!!!
        driver.find_element_by_css_selector("button.btn.submit").click()
        # Patient Medical History Form
        try: self.assertEqual("Dr No", driver.find_element_by_id("CurrentDentist").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("LastAppointmentId")).select_by_visible_text("Less than 6 months")
        driver.find_element_by_id("CurrentPhysicalHealth").click()
        driver.find_element_by_id("CurrentlyUnderPhysicianCare").click()
        # Select Medical Conditions!!!
        driver.find_element_by_id("ConfirmedMedicalHistory").click()
        driver.find_element_by_name("Submit").click()
        # Patient Insurance Form
        driver.find_element_by_xpath("//form[@id='frmCreate']/fieldset/div[3]/div/div/div/ul/li[2]").click()
        driver.find_element_by_css_selector("button.btn.submit").click()
        # Patient Flexible Financing Form
        driver.find_element_by_xpath("//form[@id='frmFlexibleFinancing']/div[4]/div/div/div[2]/span").click()
        driver.find_element_by_id("ShareAccount").click()
        driver.find_element_by_id("FinancialContact_UserProfile_FirstName").clear()
        driver.find_element_by_id("FinancialContact_UserProfile_FirstName").send_keys("Parent2")
        driver.find_element_by_id("FinancialContact_UserProfile_LastName").clear()
        driver.find_element_by_id("FinancialContact_UserProfile_LastName").send_keys("Automation")
        driver.find_element_by_id("FinancialContact_DateOfBirth").clear()
        driver.find_element_by_id("FinancialContact_DateOfBirth").send_keys("03031973")
        driver.find_element_by_xpath("(//input[@id='FinancialContact_Sex'])[2]").click()
        driver.find_element_by_id("AddressSameAsPatient").click()
        driver.find_element_by_id("FinancialContact_CellPhone").clear()
        driver.find_element_by_id("FinancialContact_CellPhone").send_keys("3038888888")
        driver.find_element_by_xpath("(//input[@id='FinancialContact_DoesOwn'])[2]").click()
        Select(driver.find_element_by_id("FinancialContact_TimeAtAddressId")).select_by_visible_text("Longer than 24 months")
        Select(driver.find_element_by_id("FinancialContact_EmploymentStatusId")).select_by_visible_text("Retired")
        driver.find_element_by_id("btnRealSubmit").click()
        driver.find_element_by_css_selector("button.btn.submit").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-closethick").click()
        # TC Login
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("automation.testing.tc@orthofi.com")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Password1!")
        driver.find_element_by_css_selector("button.btn.submit").click()
        driver.find_element_by_link_text("Dashboard").click()
        driver.find_element_by_name("ExamFilterType").click()
        driver.find_element_by_link_text("Action").click()
        # Select Tx Recommended
        driver.find_element_by_id("TreatmentType").click()
        driver.find_element_by_xpath("(//input[@name='Dentition'])[2]").click()
        driver.find_element_by_name("Severity").click()
        driver.find_element_by_id("cb_673").click()
        driver.find_element_by_id("tll_673").clear()
        driver.find_element_by_id("tll_673").send_keys("12")
        driver.find_element_by_id("tlh_673").clear()
        driver.find_element_by_id("tlh_673").send_keys("18")
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_xpath("(//input[@id='TreatmentType'])[2]").click()
        driver.find_element_by_xpath("(//input[@name='Dentition'])[2]").click()
        driver.find_element_by_name("Severity").click()
        driver.find_element_by_id("cb_673").click()
        driver.find_element_by_id("tll_673").clear()
        driver.find_element_by_id("tll_673").send_keys("12")
        driver.find_element_by_id("tlh_673").clear()
        driver.find_element_by_id("tlh_673").send_keys("18")
        driver.find_element_by_id("btnSubmit").click()
        # Medical Credit Check Authorization
        driver.find_element_by_id("SSN").clear()
        driver.find_element_by_id("SSN").send_keys("999999999")
        driver.find_element_by_id("btnSubmit").click()
        # Payment Slider
        driver.find_element_by_id("btnFinish").click()
        # Contract Details
        driver.find_element_by_id("btnChangeDueDay").click()
        driver.find_element_by_id("DocumentTerms_1__Term_TermInitials").clear()
        driver.find_element_by_id("DocumentTerms_1__Term_TermInitials").send_keys("PA")
        driver.find_element_by_id("DocumentTerms_2__Term_TermInitials").clear()
        driver.find_element_by_id("DocumentTerms_2__Term_TermInitials").send_keys("PA")
        driver.find_element_by_id("DocumentTerms_3__Term_TermInitials").clear()
        driver.find_element_by_id("DocumentTerms_3__Term_TermInitials").send_keys("PA")
        driver.find_element_by_id("DocumentTerms_5__Term_TermInitials").clear()
        driver.find_element_by_id("DocumentTerms_5__Term_TermInitials").send_keys("PA")
        driver.find_element_by_xpath("//div[@id='wrap']/div/div/div[2]/div/form/button").click()
        driver.find_element_by_id("StaffPin").clear()
        driver.find_element_by_id("StaffPin").send_keys("Password1!")
        driver.find_element_by_id("txtPin").clear()
        driver.find_element_by_id("txtPin").send_keys("Password1!")
        # Retail Installment Services Contract
        driver.find_element_by_id("Signature").clear()
        driver.find_element_by_id("Signature").send_keys("Parent2 Automation")
        driver.find_element_by_id("SignerIsRP").click()
        driver.find_element_by_id("WitnessSignature").clear()
        driver.find_element_by_id("WitnessSignature").send_keys("Automation Tester")
        driver.find_element_by_xpath("//div[@id='wrap']/div/div/div[2]/div/form/button").click()
        # Make a Payment 
        driver.find_element_by_id("CreditCardNumber").clear()
        driver.find_element_by_id("CreditCardNumber").send_keys("4111111111111111")
        # Select Expiration Date
        driver.find_element_by_id("CCV").clear()
        driver.find_element_by_id("CCV").send_keys("126")
        driver.find_element_by_link_text("Print Service Contract").click()
        driver.find_element_by_link_text("Continue").click()
        driver.find_element_by_link_text("Jennifer Harrison").click()
        driver.find_element_by_link_text("Log Off").click()
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("parent1.automation@orthofi.com")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Password1!")
        driver.find_element_by_css_selector("button.btn.submit").click()
        driver.find_element_by_link_text("Action").click()
        driver.find_element_by_link_text("View Payment Plan").click()
        driver.find_element_by_link_text("Pay Off or Make Payment").click()
        # Click Add New Method from Pay From
        # Select Payment Type: Credit Card, Credit Card Type: Discover
        driver.find_element_by_id("CreditCardNumber").clear()
        driver.find_element_by_id("CreditCardNumber").send_keys("6011000993026909")
        # Select Expiration Date
        driver.find_element_by_id("CCV").clear()
        driver.find_element_by_id("CCV").send_keys("123")
        driver.find_element_by_css_selector("button.btn.submit").click()
        driver.find_element_by_link_text("Continue").click()
        driver.find_element_by_link_text("Parent1 Automation").click()
        driver.find_element_by_link_text("Log Off").click()
        driver.find_element_by_id("Password").clear()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

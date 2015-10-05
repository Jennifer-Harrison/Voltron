# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Scenario2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://uat.orthofi.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_scenario2(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        # Login as TC
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("automation.testing.tc@orthofi.com")
        driver.find_element_by_id("txtPin").clear()
        driver.find_element_by_id("txtPin").send_keys("Password1!")
        driver.find_element_by_css_selector("button.btn.btn-default").click()
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
        driver.find_element_by_id("Guardian_UserProfile_UserName").clear()
        driver.find_element_by_id("Guardian_UserProfile_UserName").send_keys("parent1.automation@orthofi.com")
        driver.find_element_by_id("Guardian_CellPhone").clear()
        driver.find_element_by_id("Guardian_CellPhone").send_keys("3039999999")
        # Select Exam Type: Recall Ready
        driver.find_element_by_id("Exam_ExamDate").click()
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_id("Exam_ExamTime").click()
        driver.find_element_by_css_selector("fieldset.form-group.patient-exam").click()
        driver.find_element_by_css_selector("button.btn.submit").click()
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
        # Contact Info Form
        driver.find_element_by_xpath("(//input[@id='Patient_Sex'])[2]").click()
        driver.find_element_by_id("Patient_Address1").clear()
        driver.find_element_by_id("Patient_Address1").send_keys("9999 Tester")
        driver.find_element_by_id("Patient_Address1").clear()
        driver.find_element_by_id("Patient_Address1").send_keys("99999 Tester Lane")
        driver.find_element_by_id("Patient_PostalCode").clear()
        driver.find_element_by_id("Patient_PostalCode").send_keys("80234")
        driver.find_element_by_id("Patient_City").clear()
        driver.find_element_by_id("Patient_City").send_keys("Denver")
        Select(driver.find_element_by_id("Patient_StateTerritory_Abbreviation")).select_by_visible_text("Colorado")
        driver.find_element_by_id("Guardian_DateOfBirth").clear()
        driver.find_element_by_id("Guardian_DateOfBirth").send_keys("01011971")
        driver.find_element_by_xpath("(//input[@id='Guardian_Sex'])[2]").click()
        driver.find_element_by_id("SameAsPatient").click()
        driver.find_element_by_xpath("(//input[@id='Guardian_MaritalStatus'])[2]").click()
        driver.find_element_by_id("Guardian_RelationshipToPatient").click()
        driver.find_element_by_id("sizcache06928782177332579").click()
        driver.find_element_by_id("PrimaryContactIsFinanciallyResponsible").click()
        driver.find_element_by_id("TreatmentReason").clear()
        driver.find_element_by_id("TreatmentReason").send_keys("Jacked Teeth")
        driver.find_element_by_id("DentistIsNotListed").click()
        driver.find_element_by_id("ReferringDentistOther").clear()
        driver.find_element_by_id("ReferringDentistOther").send_keys("Dr No")
        # Select Treatment Sliders!!!
        driver.find_element_by_css_selector("button.btn.submit").click()
        # Medical History Form
        Select(driver.find_element_by_id("LastAppointmentId")).select_by_visible_text("Less than 6 months")
        driver.find_element_by_id("CurrentPhysicalHealth").click()
        driver.find_element_by_id("IsOnBirthControl").click()
        driver.find_element_by_xpath("(//input[@id='IsPregnant'])[2]").click()
        driver.find_element_by_id("CurrentlyUnderPhysicianCare").click()
        # Select Medical Conditions
        driver.find_element_by_id("ConfirmedMedicalHistory").click()
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_xpath("//form[@id='frmCreate']/fieldset/div[3]/div/div/div/ul/li[2]").click()
        driver.find_element_by_css_selector("button.btn.submit").click()
        # Flexible Financing Form
        driver.find_element_by_xpath("(//input[@id='FinancialContact_DoesOwn'])[2]").click()
        Select(driver.find_element_by_id("FinancialContact_TimeAtAddressId")).select_by_visible_text("Between 12 months and 18 months")
        Select(driver.find_element_by_id("FinancialContact_TimeAtPreviousAddressId")).select_by_visible_text("Between 12 months and 18 months")
        Select(driver.find_element_by_id("FinancialContact_EmploymentStatusId")).select_by_visible_text("Employed")
        Select(driver.find_element_by_id("FinancialContact_TimeAtEmployerId")).select_by_visible_text("Between 6 months and 12 months")
        driver.find_element_by_id("FinancialContact_Employer").clear()
        driver.find_element_by_id("FinancialContact_Employer").send_keys("Automation")
        driver.find_element_by_id("FinancialContact_Occupation").clear()
        driver.find_element_by_id("FinancialContact_Occupation").send_keys("Tester")
        Select(driver.find_element_by_id("FinancialContact_TimeAtPreviousEmployerId")).select_by_visible_text("Between 12 months and 18 months")
        driver.find_element_by_id("FinancialContact_PreviousEmployer").clear()
        driver.find_element_by_id("FinancialContact_PreviousEmployer").send_keys("Testing")
        driver.find_element_by_id("FinancialContact_PreviousOccupation").clear()
        driver.find_element_by_id("FinancialContact_PreviousOccupation").send_keys("Automating")
        driver.find_element_by_id("SsnHolder").clear()
        driver.find_element_by_id("SsnHolder").send_keys("999999999")
        driver.find_element_by_id("btnFakeSubmit").click()
        driver.find_element_by_id("btnRealSubmit").click()
        driver.find_element_by_css_selector("button.btn.submit").click()
        # Login as TC
        driver.find_element_by_link_text("close").click()
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("automation.testing.tc@orthofi.com")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Password1!")
        driver.find_element_by_css_selector("button.btn.submit").click()
        driver.find_element_by_link_text("Dashboard").click()
        driver.find_element_by_id("txtPin").clear()
        driver.find_element_by_id("txtPin").send_keys("Password1!")
        driver.find_element_by_name("ExamFilterType").click()
        driver.find_element_by_link_text("Action").click()
        # Select Tx Recommended
        driver.find_element_by_id("TreatmentType").click()
        driver.find_element_by_id("sizcache019733730145310224").click()
        driver.find_element_by_name("Dentition").click()
        driver.find_element_by_name("Severity").click()
        driver.find_element_by_id("sizcache019733730145310224").click()
        driver.find_element_by_id("cb_674").click()
        driver.find_element_by_id("tll_674").clear()
        driver.find_element_by_id("tll_674").send_keys("12")
        driver.find_element_by_id("tlh_674").clear()
        driver.find_element_by_id("tlh_674").send_keys("18")
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_xpath("(//input[@id='TreatmentType'])[2]").click()
        driver.find_element_by_name("Dentition").click()
        driver.find_element_by_name("Severity").click()
        driver.find_element_by_id("cb_674").click()
        driver.find_element_by_id("tll_674").clear()
        driver.find_element_by_id("tll_674").send_keys("12")
        driver.find_element_by_id("tlh_674").clear()
        driver.find_element_by_id("tlh_674").send_keys("18")
        self.assertEqual("on", driver.find_element_by_id("txAddCost_659").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@value=''])[16]").clear()
        driver.find_element_by_xpath("(//input[@value=''])[16]").send_keys("Referral")
        driver.find_element_by_xpath("(//input[@value=''])[17]").clear()
        driver.find_element_by_xpath("(//input[@value=''])[17]").send_keys("500.00")
        self.assertEqual("on", driver.find_element_by_id("txCourtesy_-1").get_attribute("value"))
        driver.find_element_by_id("btnSubmit").click()
        # Payment Slider
        driver.find_element_by_id("txtPin").clear()
        driver.find_element_by_id("txtPin").send_keys("Password1!")
        driver.find_element_by_id("mainSliderWrapper").click()
        driver.find_element_by_id("btnFinish").click()
        driver.find_element_by_id("DocumentTerms_1__Term_TermInitials").clear()
        driver.find_element_by_id("DocumentTerms_1__Term_TermInitials").send_keys("PA")
        driver.find_element_by_id("DocumentTerms_2__Term_TermInitials").clear()
        driver.find_element_by_id("DocumentTerms_2__Term_TermInitials").send_keys("PA")
        driver.find_element_by_id("DocumentTerms_3__Term_TermInitials").clear()
        driver.find_element_by_id("DocumentTerms_3__Term_TermInitials").send_keys("PA")
        driver.find_element_by_id("DocumentTerms_5__Term_TermInitials").clear()
        driver.find_element_by_id("DocumentTerms_5__Term_TermInitials").send_keys("PA")
        driver.find_element_by_xpath("//div[@id='wrap']/div/div/div[2]/div/form/button").click()
        driver.find_element_by_id("Signature").clear()
        driver.find_element_by_id("Signature").send_keys("Parent1 Automation")
        driver.find_element_by_id("SignerIsRP").click()
        driver.find_element_by_id("WitnessSignature").clear()
        driver.find_element_by_id("WitnessSignature").send_keys("Automation Tester")
        driver.find_element_by_id("StaffPin").clear()
        driver.find_element_by_id("StaffPin").send_keys("Password1!")
        driver.find_element_by_id("RoutingNumber").clear()
        driver.find_element_by_id("RoutingNumber").send_keys("056008849")
        driver.find_element_by_id("AccountNumber").clear()
        driver.find_element_by_id("AccountNumber").send_keys("12345678901234")
        driver.find_element_by_id("ConfirmAccountNumber").clear()
        driver.find_element_by_id("ConfirmAccountNumber").send_keys("12345678901234")
        driver.find_element_by_css_selector("button.btn.submit").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_link_text("Continue").click()
        driver.find_element_by_link_text("Action").click()
        driver.find_element_by_link_text("View Payment Plan").click()
        driver.find_element_by_link_text("Pay Now").click()
        driver.find_element_by_id("select2-chosen-1").click()
        driver.find_element_by_link_text("Continue").click()
        driver.find_element_by_link_text("Action").click()
        driver.find_element_by_link_text("View Payment Plan").click()
        driver.find_element_by_link_text("Add Payment Method").click()
        driver.find_element_by_id("select2-result-label-22").click()
        driver.find_element_by_id("CreditCardNumber").clear()
        driver.find_element_by_id("CreditCardNumber").send_keys("4111111111111111")
        driver.find_element_by_id("select2-chosen-4").click()
        driver.find_element_by_id("CCV").clear()
        driver.find_element_by_id("CCV").send_keys("123")
        driver.find_element_by_css_selector("button.btn.submit").click()
        driver.find_element_by_xpath("//ul[@id='awwsliders']/div[2]/div[2]/a").click()
        self.assertEqual("Visa Card account ending in 1111\n \n\n 50% Applied to Monthly Payment", driver.find_element_by_xpath("//ul[@id='awwsliders']/div[4]").text)
        driver.find_element_by_link_text("Remove").click()
        # ERROR: Caught exception [unknown command []]
    
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

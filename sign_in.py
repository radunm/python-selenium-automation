"""
Amazon logo,                       by XPath, "//i[contains(@class,'logo')]"
Email field,                       search by ID, “ap_email”
Continue button,                   search by ID, “continue”
Need help link,                    by XPath, "//span[@class='a-expander-prompt']"
Forgot your password link,         search by ID, “auth-fpp-link-bottom”
Other issues with Sign-In link,    search by ID, “ap-other-signin-issues-link”
Create your Amazon account button, search by ID, “createAccountSubmit”
*Conditions of use link,           by XPath, "//div[@id='legalTextRow']//a[contains(@href, 'condition_of_use')]"
*Privacy Notice link,              by XPath, "//div[@id='legalTextRow']//a[contains(@href, 'privacy_notice')]"

"""

"""
Find the most optimal locators for Create Account (Registration) page elements:

Amazon logo                        by CSS, ".a-icon-logo"
Create account label               by CSS, "h1"
Your name field                    by ID, "ap_customer_name"
Email field                        by ID, "ap_email"
Password field                     by ID, "ap_password"
At least 6 character label         by CSS, ".auth-inlined-information-message .a-alert-content"
Re-enter password field            by ID, "ap_password_check"
Create your Amazon account button  by ID, "continue"
Conditions of use link             by XPath, "//a[contains(@href, 'condition_of_use')]"
Privacy Notice link                by XPath, "//div[@id='legalTextRow']//a[contains(@href, 'privacy_notice')]"
Sign in link                       by CSS, ".a-link-emphasis"
"""

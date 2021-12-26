Goal is to write an automated test using Selenium IDE (for any browser) that will test a customer registration process.
Script should test https://dev3.freento.com/ and does such steps:
Open Home Page.
Click “Create an Account” link.
Fill customer registration form. 
Each test run must generate a unique email in such format test+<some random number>@test.com (ex. test+5@test.com)
Submit a form.
Check if the final page has the following success message on it: “Thank you for registering with Main Website Store.”

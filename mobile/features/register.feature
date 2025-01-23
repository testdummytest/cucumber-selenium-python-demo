
@register
Feature: Register

   @registration
   Scenario Outline: C01-Register form firstname and lastname field
      Given User open browser and navigates to the <Link> page
      When User enters <firstName>
      When User validate the firstName error msg <firstNameError>
      When User is enter <lastName>
      When User is validate the lastName error msg <lastNameError>

      Examples:
      | Link                                    | firstName | firstNameError     | lastName | lastNameError     | 
      | https://signup.testewallet.com/register | ftest123  | Invalid First Name | ltest123 | Invalid Last Name |


   @registration
   Scenario Outline: C02-Register form Email field
      Given User open browser and navigates to the <Link> page
      When User now enter the <Email>
      When User want to validate the Email error msg <emailError>

      Examples:
      | Link                                    | Email       | emailError    |
      | https://signup.testewallet.com/register | testhgmail  | Invalid Email |


   @registration
   Scenario Outline: C03-Register form phoneNumber field
      Given User open browser and navigates to the <Link> page
      When User want to enters a <phoneNumber>
      When User is validates phoneNumber error msg <phoneError>

      Examples:
      | Link                                    | phoneNumber | phoneError      |
      | https://signup.testewallet.com/register | 123         | Invalid Number  |


   @registration
   Scenario Outline: C04-Register form country field
      Given User open browser and navigates to the <Link> page
      When User validate country field <countryError>

      Examples:
      | Link                                    | countryError        |
      | https://signup.testewallet.com/register | Country is required |


   @registration
   Scenario Outline: C05-Register form check register button is default enabled
      Given User open browser and navigates to the <Link> page
      When User see register button is default enabled

      Examples:
      | Link                                    |
      | https://signup.testewallet.com/register |
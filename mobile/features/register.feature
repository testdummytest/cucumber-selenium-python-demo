
@register
Feature: Register

   @testhere
   Scenario Outline: C01-Register form firstname and lastname field
      Given User open browser and navigates to the <link> page
      When User enters <firstname>
      When User validate the firstname error msg <fnameerror>
      When User is enter <lastname>
      When User is validate the lastname error msg <lnameerror>

      Examples:
      | link                                    | firstname | fnameerror         | lastname | lnameerror        | 
      | https://signup.testewallet.com/register | ftest123  | Invalid First Name | ltest123 | Invalid Last Name |


   # @testhere
   Scenario Outline: C02-Register form email field
      Given User open browser and navigates to the <link> page
      When User now enter the <email>
      When User want to validate the email error msg <emailerror>

      Examples:
      | link                                    | email       | emailerror    |
      | https://signup.testewallet.com/register | testhgmail  | Invalid Email |


   # @testhere
   Scenario Outline: C03-Register form phonenumber field
      Given User open browser and navigates to the <link> page
      When User want to enters a <phonenumber>
      When User is validates phonenumber error msg <phoneerror>

      Examples:
      | link                                    | phonenumber | phoneerror           |
      | https://signup.testewallet.com/register | 123         | Invalid Phone Number |


   # @testhere
   Scenario Outline: C04-Register form country field
      Given User open browser and navigates to the <link> page
      When User validate country field <countryerror>

      Examples:
      | link                                    | countryerror        |
      | https://signup.testewallet.com/register | Country is required |


   # @testhere
   Scenario Outline: C05-Register form check register button is default enabled
      Given User open browser and navigates to the <link> page
      When User see register button is default enabled

      Examples:
      | link                                    |
      | https://signup.testewallet.com/register |
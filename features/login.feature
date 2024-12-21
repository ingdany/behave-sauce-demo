Feature: New Login View

    Scenario: Validate new user is able to view after clicking on new Registration
        Given User navigates to the Login Page "https://www.saucedemo.com/v1/index.html"
        When  User types user "standard_user" and password "secret_sauce"
        And Clicks the Login Button
        Then  User should be able to view "Products" page
Scenario Outline: Add new user
  Given a user list
  Given a user
  When I add the user the list
  Then the new user list is equal to the old list with the added user

Scenario Outline: Delete a user
  Given a non-empty user list
  Given a random user from the list
  When I delete the user from the list
  Then the new user list is equal to the old list without the deleted user

Scenario Outline: Edit a user
  Given a non-empty user list
  Given a random user from the list
  When I edit the user from the list
  Then the new user list is equal to the old list without the edit user



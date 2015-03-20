Feature: Rocking with lettuce and django

	Scenario: Index page from staticpages
		Given I access the url "/staticpages"
		Then I see the title "INDEX"

	Scenario: Home page
		Given I access the url "/staticpages/home"
		Then I see the title "HOME"
	
	Scenario: Help page
		Given I access the url "/staticpages/help"
		Then I see the title "HELP"
	
	Scenario: About page
		Given I access the url "/staticpages/about"
		Then I see the title "ABOUT"

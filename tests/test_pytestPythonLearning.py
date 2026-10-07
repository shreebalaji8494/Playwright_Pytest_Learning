import pytest


@pytest.fixture(scope="session") # scope="session" means this fixture will be created once per test session, and the same instance will be used for all tests in the session.
#Scope can also be set to "function" (default), "class", or "module" depending on how long you want the fixture to last.
#If Scope is set to "function", the fixture will be created and destroyed for each test function. 
#If set to "class", it will be created once per test class.
#if set to "module", it will be created once per test module.
def setup_teardown():
    """Fixture to set up and tear down resources for the test session."""
    # Setup code: This runs before any tests are executed.
    print("Setting up resources for the test session.")
    # You can initialize shared resources here, like database connections, test data, etc.

    yield  # This is where the testing happens.This keyword allows the fixture to pause here and run the tests, then resume for teardown.

    # Teardown code: This runs after all tests have completed.
    print("Tearing down resources for the test session.")
    # Clean up shared resources here, like closing database connections, deleting test data, etc.
@pytest.mark.skip
#This test is marked to be skipped, meaning it will not be executed when the test suite runs.
def test_example(setup_teardown):
    """Example test that uses the setup_teardown fixture."""
    print("Running a test that uses the setup_teardown fixture.")

@pytest.mark.smoke
#This test is marked as a smoke test, indicating that it is a basic test to check.
#Similarly we can use @pytest.mark.regression to mark a test as a regression test, which is a more comprehensive test that checks for bugs or issues in the application.
#Also we can use @pytest.mark.sanity to mark a test as a sanity test, which is a quick check to ensure that the application is functioning as expected after a change or update.
#Also we can use @pytest.mark.performance to mark a test as a performance test, which checks the application's performance under load or stress.
#It is important to note that these markers are just labels and do not affect the execution of the tests. They can be used to filter tests when running the test suite, 
#for example, by using the -m option with pytest to run only smoke tests or regression tests.
def test_another_example(setup_teardown):
    """Another example test that uses the setup_teardown fixture."""
    print("Running another test that uses the setup_teardown fixture.")    
       
import unittest
import random
import server

class ServerFileTestCase(unittest.TestCase):

    def test_job_variables(self):
        """Tests the JOB_VARIABLES dictionary is properly initialized from the JOB_TITLES list.
        For example, if the JOB_TITLES list consists of ['Software Engineer'], the JOB_VARIABLES 
        dictionary should be {"software-engineer": "Software Engineer"}.
        """

        for key, value in server.JOB_VARIABLES.items():
            self.assertIn(value, server.JOB_TITLES)
            self.assertEqual(key.split("-"), value.lower().split())


class WebsiteIntegrationTestCase(unittest.TestCase):
    """Tests for our company site."""

    def setUp(self):
        """Sets up a client for testing the website."""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        """Test that the homepage loads correctly and extends from the base."""

        result = self.client.get("/")
        self.assertIn("Reputable Company", result.data)

    def test_jobs_on_homepage(self):
        """Test that the homepage accurately displays whether we are hiring, and for which jobs."""

        result = self.client.get("/")
        if not server.JOB_TITLES:
            self.assertIn("not hiring", result.data)
        else:
            self.assertIn("welcoming applications", result.data)
            for job in server.JOB_TITLES:
                self.assertIn(job, result.data)

    def test_plural_formatting(self):
        """Test that the text on the website displays the job list in reasonably correct English."""

        result = self.client.get("/")
        respaced_text = ' '.join(result.data.split())

        if len(server.JOB_TITLES) == 1:
            self.assertIn("for %ss." % server.JOB_TITLES[0], respaced_text)
        elif len(server.JOB_TITLES) == 2:
            self.assertIn("for %ss and %ss." % tuple(server.JOB_TITLES), respaced_text)
        elif len(server.JOB_TITLES) > 2:
            self.assertIn("s, %ss, and %ss." % tuple(server.JOB_TITLES[-2:]), respaced_text)


    def test_jobs_in_form(self):
        """Test that the jobs are all displayed in the form."""

        result = self.client.get("/application")
        for job_key in server.JOB_VARIABLES:
            job_value = server.JOB_VARIABLES[job_key]
            self.assertIn("value=\""+job_key+"\"", result.data)
            self.assertIn(job_value, result.data)

    def test_application_form_basic(self):
        """The application received page should reflect all the values in the form."""

        if server.JOB_VARIABLES:
            sample_job_title = random.choice(server.JOB_VARIABLES.keys())

            result = self.client.post("/application/success", 
                                    data={"first-name": "Amelia",
                                        "last-name": "Bedelia",
                                        "job-title": sample_job_title,
                                        "min-salary": "10055"})
            self.assertIn("Thank you, Amelia Bedelia", result.data)
            self.assertIn("applying to be a %s" % server.JOB_VARIABLES[sample_job_title], result.data)
            self.assertIn("$10,055.00", result.data)

    def test_application_form_no_salary(self):
        """The minimum salary field is optional; website should default to $0.00 if it is left blank."""

        if server.JOB_VARIABLES:
            sample_job_title = random.choice(server.JOB_VARIABLES.keys())

        result = self.client.post("/application/success",
                            data={"first-name": "Amelia C.",
                            "last-name" : "Bedelia",
                            "job-title" : sample_job_title})
        self.assertIn("$0.00", result.data)



if __name__ == "__main__":
    unittest.main()
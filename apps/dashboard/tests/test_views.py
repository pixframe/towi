from django.test import TestCase


class TestHomeView(TestCase):
    def test_home(self):
        resp = self.client.get('/inicio/')
        self.assertEqual(resp.status_code, 200)


class TestHomeLaboratorio(TestCase):
    def test_home_laboratorio(self):
        resp = self.client.get('/ccl/')
        self.assertEqual(resp.status_code, 200)


class TestTools(TestCase):
    def test_tools_ccl(self):
        resp = self.client.get('/ccl/tools/')
        self.assertEqual(resp.status_code, 200)


class TestReseachers(TestCase):
    def test_researchers(self):
        resp = self.client.get('/ccl/researchers/')
        self.assertEqual(resp.status_code, 200)


class TestProjects(TestCase):
    def test_projects(self):
        resp = self.client.get('/ccl/projects/')
        self.assertEqual(resp.status_code, 200)


class TestResources(TestCase):
    def test_resources(self):
        resp = self.client.get('/ccl/resources/')
        self.assertEqual(resp.status_code, 200)


class TestParticipate(TestCase):
    def test_participate(self):
        resp = self.client.get('/ccl/participate/')
        self.assertEqual(resp.status_code, 200)

        #Page Not Found
        resp = self.client.get('/ccl/participatee/')
        self.assertEqual(resp.status_code, 404)

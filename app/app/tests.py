from django.test import SimpleTestCase


from app import calc


class calculator(SimpleTestCase):
    def test_sum(self):
        ans = calc.add(5, 0)
        self.assertEqual(ans, 5)

    def prompt(self, name):
        self.name = name
        i = calc.introduce(name)
        print(i)

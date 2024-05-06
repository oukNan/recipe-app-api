"""
Model user email and password
"""

class ModelTests(TestCase):
  def test_create_user_with_email_successful(self):
    email = 'test@example.co
    password = 'testpass123'
    user = get_user_model().objects.create_user(
      email = email,
      password = password,
    )

self.assertEqual(user.email, email)
self.assertTrue(user.check_password(password))





    

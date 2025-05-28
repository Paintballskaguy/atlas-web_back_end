#!/usr/bin/env python3
""" User module
"""
import hashlib
from models.base import Base


class User(Base):
    """ User class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a User instance """
        super().__init__(*args, **kwargs)
        self.email = self.normalize_email(kwargs.get('email'))
        self._password = kwargs.get('_password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    def normalize_email(self, email):
        """Normalize email for consistent storage"""
        if email and isinstance(email, str):
            return email.strip().lower()
        return email

    @property
    def password(self) -> str:
        """ Getter of the password """
        return self._password

    @password.setter
    def password(self, pwd: str):
        """ Setter of a new password: encrypt in SHA256 """
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd: str) -> bool:
        """ Validate a password """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        pwd_e = pwd.encode()
        return hashlib.sha256(pwd_e).hexdigest().lower() == self.password

    def display_name(self) -> str:
        """ Display User name based on email/first_name/last_name
        """
        if self.email is None and self.first_name is None \
                and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        if self.last_name is None:
            return "{}".format(self.first_name)
        if self.first_name is None:
            return "{}".format(self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)

    @classmethod
    def search(cls, attributes: dict) -> list:
        """Search for users matching attributes"""
        if not attributes or not isinstance(attributes, dict):
            return []

        try:
            all_users = cls.all()
            if not all_users:
                return []

            matching_users = []
            for user in all_users:
                try:
                    # Special handling for email
                    if 'email' in attributes:
                        # Normalize both emails for comparison
                        db_email = (user.email or "").strip().lower()
                        search_email = (attributes['email'] or "").strip().lower()

                        if db_email != search_email:
                            continue
                    else:
                        # For other attributes
                        match = True
                        for key, value in attributes.items():
                            if getattr(user, key, None) != value:
                                match = False
                                break
                        if not match:
                            continue

                    matching_users.append(user)
                except Exception:
                    continue

            return matching_users
        except Exception:
            return []

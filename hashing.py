from passlib.context import CryptContext

# Create a CryptContext instance for bcrypt hashing
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:
        """
        Hashes a password using bcrypt.
        """
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
        """
        Verifies a plain password against a hashed password using bcrypt.
        Returns True if the plain password matches the hashed one, False otherwise.
        """
        return pwd_cxt.verify(plain_password, hashed_password)

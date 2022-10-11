instructions = [
    'DROP TABLE IF EXISTS email;',
    """
        CREATE TABLE email (
            id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """]


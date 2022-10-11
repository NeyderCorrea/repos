instructions = [
    'DROP TABLE IF EXISTS email;',
    """
        CREATE TABLE email (
            id SERIAL PRIMARY KEY NOT NULL,
            email TEXT UNIQUE NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """]


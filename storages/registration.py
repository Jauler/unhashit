

class Registration:

    def __init__(self, email, algorithm, hash_value):
        self.email = email
        self.algorithm = algorithm
        self.hash_value = hash_value;

    def GetEmail(self):
        return self.email

    def GetAlgorithm(self):
        return self.algorithm

    def GetValue(self):
        return self.hash_value

    def Write(self, db):
        db.ExecuteSQL("INSERT INTO registrations (email, algorithm, hash) VALUES (%s, %s, %s)", (self.email, self.algorithm, self.hash_value))
        db.Commit()

    def Delete(self, db):
        db.ExecuteSQL("DELETE FROM registrations WHERE email=%s AND algorithm=%s AND hash=%s", (self.email, self.algorithm, self.hash_value))
        db.Commit()

    @staticmethod
    def Read(db, algorithm, hash):
        results = db.ExecuteSQL("SELECT email, algorithm, hash FROM registrations WHERE algorithm=%s AND hash=%s", (algorithm, hash))
        registrations = []
        for result in results:
            registrations.append(Registration(result[0], result[1], result[2]))

        return registrations;


class ClientNotFoundError(Exception):
    """Exception levée lorsque l'employé n'est pas trouvé."""
    def __init__(self, message="Le client avec ce code n'existe pas."):
        self.message = message
        super().__init__(self.message)

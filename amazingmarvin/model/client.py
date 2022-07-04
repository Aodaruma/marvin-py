
class RawClient(object):
    """
    amazing marvin client but 1 on 1 interface
    """
    def __init__(self, API_token :str):
        """
        init
        """
        self._token = API_token

class Client(RawClient):
    """
    amazing marvin client
    """
    
    def __init__(self, API_token :str):
        """
        init
        """
        super().__init__(API_token)

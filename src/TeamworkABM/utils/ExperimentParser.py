
class ExperimentParser:
    """
        Parses experiment data from provided experiment folder and id.
    """

    __algorith_version = "1.0.0"
    
    def __init__(self, folder: str, id: str):
        """
        Parameters
        ----------
        folder : str
            Top level folder where the experiment is stored.
        id : str
            The id or name of the experiment
        """
        self.__folder = folder
        self.__id = id

    def createTimeline(self) -> str:
        
        return ""
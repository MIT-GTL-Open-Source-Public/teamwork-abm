
class ExperimentParser:
    """
        Parses experiment data from provided experiment folder and id.

        Methods
        -------
        createTimeline(time_increment_s=10)
            Starts process to create timeline and store in a local or remote database
    """

    __algorith_version = "1.0.0"

    def __init__(self, folder: str, id: str, results_database: str):
        """
            Parameters
            ----------
            folder : str
                Top level folder where the experiment is stored.
            id : str
                The id or name of the experiment
            results_database: str
                Pointer to a local or remote database where results are to be stored
        """
        self.__folder = folder
        self.__id = id

    def createTimeline(self, time_increment_s=10) -> str:
        """Starts process to create timeline and store results in a local database
            Returns
            -------
            str
                a GUID representing process id that can be used to query status of 
                job    
        """
        return ""

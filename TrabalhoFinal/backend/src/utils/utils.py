class Utils:
    """
    métodos de ajuda
    """
    
    @classmethod
    def obj_to_json(cls, obj: object):
        data = vars(obj)

        if data.get("id") is None:
            data.pop("id", None)
        return data

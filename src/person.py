"""
src.person
"""
class Person:
    """
    Person Class
    """

    def __init__(self, first_name, last_name):
        """
        Constructs a person

        Args:
            first_name (str): the first name
            last_name (str): the last name
        
        Examples:
            >>> person = Person('Jieun', 'Lee')

        """
        self.first_name = first_name
        self.last_name = last_name
    
    def get_first_name(self):
        """
        Returns the first name

        Returns:
            the first name
        """
        return self.first_name
    
    def set_first_name(self, first_name):
        """
        Sets the first name

        Args:
            first_name (str): the first name
        """
        self.first_name = first_name
    
    def print_full_name(self):
        """
        Prints the full name

        Examples:
            >>> person.print_full_name()
            Jieun Lee

        """
        print ('{} {}'.format(self.first_name, self.last_name))
    
    def get_person_as_dict(self):
        """
        Returns the person in a Json format

        Returns:
            the person in a Jason format
        
        .. code-block:: none
            {
                'first_name': 'Jieun',
                'last_name': 'Lee'
            }

        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name
        }
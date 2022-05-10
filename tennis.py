class TableTennisClub:
    """
        A class representing a table tennis club.
        Keeps track of general club information and a roster of members.
    """
    def __init__(self, room_num):
        """
            Create a new TableTennisClub object.

            Parameters:
                - room_num: The room number where the club meets
        """

        self.room_num = room_num
        # Set up a list to store members
        self.members = []
    
    def add_member(self, member):
        """
            Add a member the club.
        """
        self.members.append(member)
    
    def __str__(self):
        """
            Convert the TableTennisClub to a string representation.
            This prints a complete roster of everyone in the club.
        """
        output = f"{self.room_num} Table Tennis Club Roster\n"
        output += '------------------------------\n'
        for m in self.members:
            output += str(m) + "\n"
        return output

class TableTennisPlayer:
    """
        A class representing a table tennis player.
        Keeps track of their name and whether they own a table.
    """
    def __init__(self, name, has_table):
        """
            Create a new TableTennisPlayer object.

            Parameters:
                - name: The player's name
                - has_table: A Boolean value indicating whether the player owns 
                             a table tennis table.
        """
        self.name = name
        self.has_table = has_table

    def __str__(self):
        """
            Convert the TableTennisPlayer to a string representation.
            This prints all known information about the player.
        """
        output = f"Name: {self.name}\tHas table: {self.has_table}"
        return output

class RatedPlayer(TableTennisPlayer):
    """
        A class representing a table tennis player who plays in competitions
        Keeps track of their name and whether they own a table, plus their
        score in the competitions.
    """
    def __init__(self, name, has_table, score):
        """
            Create a new RatedPlayer object.

            Parameters:
                - name: The player's name.
                - has_table: A Boolean value indicating whether the player owns 
                             a table tennis table.
                - score: The player's score in competitive table tennis competitions.
        """

        # Use super() to invoke __init__() in the parent TableTennisPlayer class.
        # This saves us the trouble of having to save name and has_table ourselves.
        super().__init__(name, has_table)

        # Set the score
        self.score = score

    def __str__(self):
        """
            Convert the RatedPlayer to a string representation.
            This prints all known information about the player.
        """

        # Use super() to invoke __str__() on the parent TableTennisPlayer class.
        # This creates a string already formatted like it should be - all we
        # have to do is add extra information about the player's score.
        output = super().__str__()
        output += "\tScore: " + str(self.score)
        return output


# Create a club meeting in Ingersoll 113.
club = TableTennisClub(113)

# Add a variety of members: some regular players, some RatedPlayers.
# This demonstrates polymorphism: the TableTennisClub is able to
# interact with both of them, even though they do different things.
club.add_member(TableTennisPlayer("Matt", True))
club.add_member(TableTennisPlayer("Bob", False))
club.add_member(RatedPlayer("Alice", True, 1022))
club.add_member(TableTennisPlayer("Steve", False))

print(club)

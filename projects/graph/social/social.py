import random

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        else:
            return None

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(i)

        # Create friendships
        friendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                friendships.append((userID, friendID))
        random.shuffle(friendships)
        total = numUsers * avgFriendships
        friendships = friendships[:total]
        for friendship in friendships:
            self.addFriendship(friendship[0], friendship[1])
    
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        q.enqueue(userID)
        connected = { userID: [userID] }

        while q.size > 0:
            current = q.dequeue()
            for user in self.friendships[current]:
                if user not in connected:
                    q.enqueue(user)
                    connected[user] = list(connected[current])
                    connected[user].append(user)
        return connected


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
